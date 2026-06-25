# middleware.py
import json
import logging
import time
logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:

   def __init__(self, get_response):
       self.get_response = get_response

   def __call__(self, request):

       start_time = time.time()

       logger.info(
           f"REQUEST | Method={request.method} | "
           f"Path={request.path} | "
           f"IP={request.META.get('REMOTE_ADDR')}"
       )

       response = self.get_response(request)

       duration = round(time.time() - start_time, 3)

       logger.info(
           f"RESPONSE | Status={response.status_code} | "
           f"Duration={duration}s"
       )

       return response

# middleware.py

class RequestResponseLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()

        # Request Body
        try:
            request_body = (
                request.body.decode("utf-8")
                if request.body
                else None
            )
        except Exception:
            request_body = "Unable to read request body"

        logger.info(
            {
                "type": "REQUEST",
                "method": request.method,
                "path": request.path,
                "ip": request.META.get("REMOTE_ADDR"),
                "headers": dict(request.headers),
                "body": request_body,
            }
        )

        response = self.get_response(request)

        duration = round(time.time() - start_time, 3)

        # Response Body
        try:
            response_body = response.content.decode("utf-8")
        except Exception:
            response_body = "Unable to read response body"

        logger.info(
            {
                "type": "RESPONSE",
                "status_code": response.status_code,
                "duration": f"{duration}s",
                "body": response_body,
            }
        )

        return response