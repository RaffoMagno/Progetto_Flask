from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #inizialliziamo sqlAlchemy

class ListaSpesa(db.Model): #tabella
    id = db.Column(db.Integer, primary_key=True) #id elemento, unico
    elemento = db.Column(db.String(100), nullable=False) #elemento, non nullo