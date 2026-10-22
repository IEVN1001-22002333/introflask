from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import config

maestros_bp=Blueprint('maestros',__name__,)