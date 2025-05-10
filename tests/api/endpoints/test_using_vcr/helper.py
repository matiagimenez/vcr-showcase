

from typing import Any
import json

from fastapi import Request


def sanitize_response(response: dict[str, Any]) -> dict[str, Any]:
    """
    Remove sensitive information from the response.
    """
    response_headers = response.get("headers", {})
    response_headers.pop("Set-Cookie", None)
    body = response.get("body", {}).get("string", {})
    if isinstance(body, bytes):
        body = body.decode("utf-8")

    try:
        body_json = json.loads(body)
    except json.JSONDecodeError:
        return response

    if isinstance(body_json, list):
        return response

    if not body_json.get("accessToken") and not body_json.get("refreshToken"):
        return response

    body_json["accessToken"] = "[REDACTED]"
    body_json["refreshToken"] = "[REDACTED]"
    response["body"]["string"] = json.dumps(body_json).encode("utf-8")

    return response


def sanitize_request(request: Request) -> Request:
    """
    Remove sensitive information from the request.
    """
    if request.path != "/api/users/login":
        return request

    try:
        # Decode the request body if it's in JSON format
        body = json.loads(request._body)
        if not body.get("password"):
            return request
            # Replace the password with a placeholder

        body["password"] = "[REDACTED]"
        request._body = json.dumps(body)
    except json.JSONDecodeError:
        return request
    return request
