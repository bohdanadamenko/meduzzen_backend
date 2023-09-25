from django.shortcuts import render
from django.http import JsonResponse
import logging


logger = logging.getLogger(__name__)


def health_check(request):
    """Responds with application status."""
    logger.info('Someone load "/" page.')
    return JsonResponse({
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    })
