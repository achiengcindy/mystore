 # mystore
 
## Resources

### Implemented bootstrap 4 
navigation get bootstrap at:
[bootstrap navigation] (https://v4-alpha.getbootstrap.com/examples/jumbotron/)

### crispy forms
[link to crispy form doc!] (http://django-crispy-forms.readthedocs.io/en/d-0/install.html)

### stripe
[link stripe js!] (https://js.stripe.com/v3)
[link stripe configuration!] (https://stripe.com/docs/stripe-js/elements/quickstart)


## Git
###Creating branch
git branch to see available branches
git checkout to switch branches
### Configuring wait in sublime text editor
export EDITOR='subl -w new-window'
Close the text editor command
### Resolving merge conflicts
1. git checkout master


### Djnago-allauth resources
[Djnago-allauth resources!] (https://django-allauth.readthedocs.io/en/latest/installation.html)


#### sample code settings.py
    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = "/"

    ACCOUNT_AUTHENTICATION_METHOD = "username_email"
    ACCOUNT_CONFIRM_EMAIL_ON_GET =False
    ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL =LOGIN_URL
    ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
    ACCOUNT_EMAIL_REQUIRED = False
    ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3
    ACCOUNT_EMAIL_VERIFICATION = "None"
    ACCOUNT_EMAIL_SUBJECT_PREFIX = 'My Subject'
    ACCOUNT_DEFAULT_HTTP_PROTOCOL ="http"

    #ACCOUNT_LOGIN_ATTEMPTS_LIMIT =5
     
    #ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =False
    ACCOUNT_LOGOUT_ON_GET =False
    ACCOUNT_LOGOUT_REDIRECT_URL = "/"

    ACCOUNT_SIGNUP_FORM_CLASS = None
    ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True 
    ACCOUNT_UNIQUE_EMAIL = True 
    ACCOUNT_USER_MODEL_USERNAME_FIELD ="username"
    ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE =False

    ACCOUNT_USERNAME_MIN_LENGTH =5
    ACCOUNT_USERNAME_BLACKLIST =[]
    ACCOUNT_USERNAME_REQUIRED = True   
    ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =False
    ACCOUNT_USER_MODEL_EMAIL_FIELD ="email"
#### Implementing Stipe paymenyt
[stripe resources!] (https://django-allauth.readthedocs.io/en/latest/installation.html)

