"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "api/v1/marketnavigation": {
        "url": "api/v1/marketnavigation",
        "params": {},
        "response": {
            "nodes": [
                {
                    "id": "hierarchy_v1.commons_group",
                    "name": "commons_group"
                },
                {
                    "id": "hierarchy_v1.commodities_group",
                    "name": "commodities_group"
                },
                {
                    "id": "hierarchy_v1.oil_markets_group",
                    "name": "oil_markets_group"
                }
            ]
        }
    },
    "api/v1/marketnavigation/{nodeId}?limit=500": {
        "url": "api/v1/marketnavigation/{nodeId}?limit=500",
        "params": {},
        "response": {
          "nodes": [
            {
              "id": "hierarchy_v1.commons.most_traded",
              "name": "Most Traded"
            },
            {
              "id": "hierarchy_v1.commons.recently_traded",
              "name": "Recently Traded"
            },
            {
              "id": "hierarchy_v1.commons.new",
              "name": "New"
            },
            {
              "id": "hierarchy_v1.commons.top_gainers",
              "name": "Top Risers"
            },
            {
              "id": "hierarchy_v1.commons.top_losers",
              "name": "Top Fallers"
            },
            {
              "id": "hierarchy_v1.commons.most_volatile",
              "name": "Most Volatile"
            },
            {
              "id": "hierarchy_v1.commons.weekend_trading",
              "name": "Weekend Trading"
            }
          ]
        }
    }
 }