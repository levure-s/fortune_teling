from flask import Flask, render_template, request, logging, Response, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('HISEN.config')

db = SQLAlchemy(app)

import HISEN.script
