from flask import jsonify
from app.exceptions import ValidationError
from . import api


def bad_request(message):
    """
    错误请求
    """
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    """
    非法请求
    """
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    """
    禁用请求
    """
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    """
    API 中 ValidationError 异常的处理程序
    """
    return bad_request(e.args[0])
