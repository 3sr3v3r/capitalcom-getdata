"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "api/v1/prices/{epic}": {
        "url": "api/v1/prices/{epic}",
        "instrument": "EURUSD",
        "params": {
           "resolution": "MINUTE",
            "max": 500,
           "from": "2023-04-25T08:00:00",
           "to": "2023-04-26T08:00:00",
        },
        "response": {
          "prices": [
            {
              "snapshotTime": "2022-04-06T15:18:00",
              "snapshotTimeUTC": "2022-04-06T13:18:00",
              "openPrice": {
                "bid": 24.356,
                "ask": 24.376
              },
              "closePrice": {
                "bid": 24.378,
                "ask": 24.398
              },
              "highPrice": {
                "bid": 24.378,
                "ask": 24.398
              },
              "lowPrice": {
                "bid": 24.355,
                "ask": 24.375
              },
              "lastTradedVolume": 187
            },
            {
              "snapshotTime": "2022-04-06T15:19:00",
              "snapshotTimeUTC": "2022-04-06T13:19:00",
              "openPrice": {
                "bid": 24.379,
                "ask": 24.399
              },
              "closePrice": {
                "bid": 24.379,
                "ask": 24.399
              },
              "highPrice": {
                "bid": 24.389,
                "ask": 24.409
              },
              "lowPrice": {
                "bid": 24.373,
                "ask": 24.393
              },
              "lastTradedVolume": 168
            },
            {
              "snapshotTime": "2022-04-06T15:20:00",
              "snapshotTimeUTC": "2022-04-06T13:20:00",
              "openPrice": {
                "bid": 24.378,
                "ask": 24.398
              },
              "closePrice": {
                "bid": 24.4,
                "ask": 24.42
              },
              "highPrice": {
                "bid": 24.4,
                "ask": 24.42
              },
              "lowPrice": {
                "bid": 24.375,
                "ask": 24.395
              },
              "lastTradedVolume": 183
            },
            {
              "snapshotTime": "2022-04-06T15:21:00",
              "snapshotTimeUTC": "2022-04-06T13:21:00",
              "openPrice": {
                "bid": 24.399,
                "ask": 24.419
              },
              "closePrice": {
                "bid": 24.395,
                "ask": 24.415
              },
              "highPrice": {
                "bid": 24.405,
                "ask": 24.425
              },
              "lowPrice": {
                "bid": 24.388,
                "ask": 24.408
              },
              "lastTradedVolume": 196
            },
            {
              "snapshotTime": "2022-04-06T15:22:00",
              "snapshotTimeUTC": "2022-04-06T13:22:00",
              "openPrice": {
                "bid": 24.394,
                "ask": 24.414
              },
              "closePrice": {
                "bid": 24.399,
                "ask": 24.419
              },
              "highPrice": {
                "bid": 24.4,
                "ask": 24.42
              },
              "lowPrice": {
                "bid": 24.383,
                "ask": 24.403
              },
              "lastTradedVolume": 171
            },
            {
              "snapshotTime": "2022-04-06T15:23:00",
              "snapshotTimeUTC": "2022-04-06T13:23:00",
              "openPrice": {
                "bid": 24.398,
                "ask": 24.418
              },
              "closePrice": {
                "bid": 24.381,
                "ask": 24.401
              },
              "highPrice": {
                "bid": 24.405,
                "ask": 24.425
              },
              "lowPrice": {
                "bid": 24.38,
                "ask": 24.4
              },
              "lastTradedVolume": 161
            },
            {
              "snapshotTime": "2022-04-06T15:24:00",
              "snapshotTimeUTC": "2022-04-06T13:24:00",
              "openPrice": {
                "bid": 24.38,
                "ask": 24.4
              },
              "closePrice": {
                "bid": 24.387,
                "ask": 24.407
              },
              "highPrice": {
                "bid": 24.399,
                "ask": 24.419
              },
              "lowPrice": {
                "bid": 24.38,
                "ask": 24.4
              },
              "lastTradedVolume": 155
            },
            {
              "snapshotTime": "2022-04-06T15:25:00",
              "snapshotTimeUTC": "2022-04-06T13:25:00",
              "openPrice": {
                "bid": 24.388,
                "ask": 24.408
              },
              "closePrice": {
                "bid": 24.389,
                "ask": 24.409
              },
              "highPrice": {
                "bid": 24.393,
                "ask": 24.413
              },
              "lowPrice": {
                "bid": 24.384,
                "ask": 24.404
              },
              "lastTradedVolume": 118
            },
            {
              "snapshotTime": "2022-04-06T15:26:00",
              "snapshotTimeUTC": "2022-04-06T13:26:00",
              "openPrice": {
                "bid": 24.389,
                "ask": 24.409
              },
              "closePrice": {
                "bid": 24.373,
                "ask": 24.393
              },
              "highPrice": {
                "bid": 24.39,
                "ask": 24.41
              },
              "lowPrice": {
                "bid": 24.37,
                "ask": 24.39
              },
              "lastTradedVolume": 143
            },
            {
              "snapshotTime": "2022-04-06T15:27:00",
              "snapshotTimeUTC": "2022-04-06T13:27:00",
              "openPrice": {
                "bid": 24.372,
                "ask": 24.392
              },
              "closePrice": {
                "bid": 24.375,
                "ask": 24.395
              },
              "highPrice": {
                "bid": 24.376,
                "ask": 24.396
              },
              "lowPrice": {
                "bid": 24.371,
                "ask": 24.391
              },
              "lastTradedVolume": 44
            }
          ],
          "instrumentType": "COMMODITIES"
        }
    }
}
