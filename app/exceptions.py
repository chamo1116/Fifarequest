# -- coding: utf-8 --
#! /usr/bin/env python
"""
Archivo base del proyecto
"""
_author_ = "Chamito"
_credits_ = ["Chamito"]


class ValidationError(ValueError):
    """
    """
    pass


class InternalServerError(ValueError):
    """
    """
    pass


class BadRequest(ValueError):
    """
    """
    pass


class HTTP_404(ValueError):
    """
    """
    pass