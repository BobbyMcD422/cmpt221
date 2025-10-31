"""app.py: render and route to webpages"""

import os, bcrypt, logging
from dotenv import load_dotenv # type: ignore
from flask import Flask, render_template, request, redirect, url_for
from db.query import get_all, insert, get_one
from db.server import init_database
from db.schema import Users

# Setup for Logger
logging.basicConfig( 
    filename="logs/log.txt", level=logging.INFO, filemode="a", format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

# load environment variables from .env
load_dotenv()

# database connection - values set in .env
db_name = os.getenv('db_name')
db_owner = os.getenv('db_owner')
db_pass = os.getenv('db_pass')
db_url = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

def create_app():
    """Create Flask application and connect to your DB"""
    # create flask app
    app = Flask(__name__, 
                template_folder=os.path.join(os.getcwd(), 'templates'), 
                static_folder=os.path.join(os.getcwd(), 'static'))
    
    # connect to db
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    
    # Initialize database
    with app.app_context():
        if not init_database():
            print("Failed to initialize database. Exiting.")
            exit(1)

    # ===============================================================
    # routes
    # ===============================================================

    # create a webpage based off of the html in templates/index.html
    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        """Sign up page: enables users to sign up"""
        
        # Server Side Input Validation
        error: str = None
        is_valid: bool = False

        if request.method == 'POST':
            
            FirstName=request.form["FirstName"]
            LastName=request.form["LastName"]
            PhoneNumber=request.form["PhoneNumber"]

            if FirstName.isalpha() and LastName.isalpha() and PhoneNumber.isnumeric() and len(PhoneNumber) == 10:
                print(f"Inputs {FirstName}, {LastName}, and {PhoneNumber} are valid.")
                is_valid = True
            elif not FirstName.isalpha():
                print(f"Input: {FirstName} is Invalde")
                #error = error_msg

            if is_valid:

                user_data: dict = {}

                for key, value in request.form.items():
                    user_data[key] = value.strip()
                
                # converting password to array of bytes
                bytes = user_data['Password'].encode('utf-8')

                # generating the salt
                salt = bcrypt.gensalt()

                # Hashing the password
                user_data['Password'] = bcrypt.hashpw(bytes, salt)

                try:
                    user = Users(FirstName=user_data['FirstName'],
                            LastName=user_data['LastName'],
                            Email=user_data['Email'],
                            PhoneNumber=user_data['PhoneNumber'],
                            Password=user_data['Password'])
                    insert(user)
                except Exception as e:
                    logging.error(f"An error has occurred: {e}")
                    return redirect(url_for('error'), errors=str(e))
                finally:
                    return redirect(url_for('index'))

        return render_template('signup.html')
    
    @app.route('/error')
    def error():
        """Doc later"""
        errors = request.args.get('errors', 'Unknown error')
        return render_template('error', errors=errors)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """Log in page: enables users to log in"""

        if request.method == 'POST':
            try:
                # Get SQLAlchemy Object And See If The Email + Pass Combo Exists 
                attempted_user = get_one(Users, Email=request.form["Email"].lower())
                
                if attempted_user.Password == request.form["Password"]:
                    return redirect(url_for('success'))
                else:
                    print("Wrong Password")
                return redirect(url_for('login'))
            except Exception as e:
                logging.error(f"An error has occurred: {e}")
                print("No Account With Such Email (most likely)")
                return redirect(url_for('login'))

        return render_template('login.html')

    @app.route('/users')
    def users():
        """Users page: displays all users in the Users table"""
        all_users = get_all(Users)
        
        return render_template('users.html', users=all_users)

    @app.route('/success')
    def success():
        """Success page: displayed upon successful login"""

        return render_template('success.html')

    return app

if __name__ == "__main__":
    app = create_app()
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)