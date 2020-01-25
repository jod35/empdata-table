class Config:
    #SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI='mysql://jon:nathanoj35@localhost/employee_data'
    #SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='secreto!@#$%^&&*'
    DEBUG=True
