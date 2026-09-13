

# Example 3: Full-featured template (production-ready)
<a name="yield-optimization-examples-full"></a>

Comprehensive template with all APS-recommended fields, regulatory compliance, content targeting, and extended identifiers.

```
{
  "app": {
    "id": "{{player_params.app_id}}",
    "bundle": "com.example.streamingapp",
    "storeurl": "https://www.amazon.com/dp/B0EXAMPLE",
    "name": "Example Streaming",
    "domain": "streaming.example.com",
    "cat": ["IAB1-1"],
    "content": {
      "genre": "{{asset.genre}}",
      "contentrating": "{{asset.content_rating}}",
      "language": "en",
      "len": 3600
    }
  },
  "device": {
    "ua": "{{session.user_agent}}",
    "ip": "{{session.client_ip}}",
    "devicetype": 3,
    "dnt": "{{player_params.dnt}}",
    "ifa": "{{player_params.ifa}}",
    "os": "{{player_params.os}}",
    "osv": "{{player_params.osv}}",
    "model": "{{player_params.model}}",
    "make": "{{player_params.make}}",
    "language": "en",
    "w": 1920,
    "h": 1080,
    "connectiontype": 2
  },
  "imp": [
    {
      "video": {
        "mimes": ["video/mp4", "video/webm"],
        "protocols": [1, 2, 3, 4, 5, 6, 7, 8],
        "w": 1920,
        "h": 1080,
        "startdelay": -1,
        "podid": "1",
        "plcmt": 1,
        "linearity": 1,
        "playbackmethod": [1],
        "ext": {
          "slotId": "608109df-a1b2-c3d4-e5f6-789012345678"
        }
      },
      "bidfloor": 3.0,
      "bidfloorcur": "USD",
      "secure": 1,
      "ssai": 1
    }
  ],
  "user": {
    "id": "{{player_params.user_id}}",
    "eids": [
      {
        "source": "liveramp.com",
        "uids": [
          {
            "id": "{{player_params.envelope}}",
            "atype": 3
          }
        ]
      }
    ],
    "consent": "{{player_params.consent}}"
  },
  "regs": {
    "coppa": 0,
    "gdpr": "{{player_params.gdpr}}",
    "us_privacy": "{{player_params.us_privacy}}",
    "gpp": "{{player_params.gpp_consent}}",
    "gpp_sid": "{{player_params.gpp_sid}}"
  },
  "bcat": ["IAB25", "IAB26"],
  "badv": ["competitor.com"]
}
```