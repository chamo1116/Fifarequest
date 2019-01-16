# -- coding: utf-8 --
#! /usr/bin/env python
"""
Archivo base del proyecto
"""
_author_ = "Chamito"
_credits_ = ["Chamito"]

from flask import jsonify
from app.api.v1 import api
from app.exceptions import (
    ValidationError,
    InternalServerError,
    BadRequest,
    HTTP_404
)


@api.errorhandler(ValidationError)
def validation_error(err):
    """
    """
    response = jsonify({'status': 400, 'error': 'bad request',
                        'message': str(err.args[0])})
    response.status_code = 400
    return response


@api.errorhandler(InternalServerError)
def internal_server_error(err):
    """
    """
    response = jsonify({'status': 500, 'error': 'internal server error',
                        'message': str(err.args[0])})
    response.status_code = 500
    return response


@api.errorhandler(BadRequest)
def bad_request(err):
    """
    """
    response = jsonify({'status': 400, 'error': 'bad request',
                        'message': str(err.args[0])})
    response.status_code = 400
    return response


@api.errorhandler(HTTP_404)
def http_404(err):
    """
    """
    response = jsonify({'status': 404, 'error': 'not found',
                        'message': str(err.args[0])})
    response.status_code = 404
    return response