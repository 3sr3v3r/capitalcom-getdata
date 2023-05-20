"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "api/v1/session/encryptionKey": {
        "url": "api/v1/session/encryptionKey",
        "params": {},
        "response": {
            "encryptionKey":"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAraOXvUjVAH82bBXuTLCG8SlLWO+RbEHQ/oisV1HyI/944Wz0C/LQfoRiRdN3MGdv5QMtX8kdKRlYpEbIQdWY0IHYKDi1SQ3WbOJ+C5CR4Qp2ynIju51A6fHzkjF+9TD0ExANxXylbKm183Ggmm8MhSxfDzmKWNFL+8qNwFROM6W5qHDBC5hzwSawtZJ/QqaJQI1LGv8b1OIkwqltOmB2MZPVbenqUPRNJ18ksbsDHfhxlDXl4qmi2n7kGccrFDzhLJVKQWxmlt1C7f2vYI9+Aar6+qLpBmkJBupR4WSzJ/HcJ67EZlJXJbB6RQo9oBKsFeTOTBTsAphmWZsxsIE9tQIDAQAB",
            "timeStamp":1682249548580
        }
    },
    "api/v1/session": {
        "url": "api/v1/session",
        "body": {"encryptedPassword": "true", "identifier": "'+ accountID + '", "password": "'+ password+'"},
        "response": {
                "clientId": "12345678",
                "accountId": "12345678901234567",
                "timezoneOffset": 3,
                "locale": "en",
                "currency": "USD",
                "streamEndpoint": "wss://api-streaming-capital.backend-capital.com/"
        }
    },
    "api/v1/ping": {
        "url": "api/v1/ping",
        "params": {},
        "response": {
                "status": "OK"
        }
    }
 }