# -- coding: utf-8 --
#! /usr/bin/env python
"""
Archivo base del proyecto
"""
_author_ = "Chamito"
_copyright_ = "Copyright 2019"
_credits_ = ["Chamito"]

from flask import jsonify
from flask_httpauth import HTTPTokenAuth

from app.models import User


auth_token = HTTPTokenAuth()


@auth_token.verify_token
def verify_token(token):
    """
    """
    user = User.verify_auth_token(token)
    return user is not None


@auth_token.error_handler
def bad_token():
    """
    """
    response = jsonify({'status': 401, 'error': 'unauthorized',
                        'message': 'por favor enviar el token de autenticacion'})
    response.status_code = 401
    return response