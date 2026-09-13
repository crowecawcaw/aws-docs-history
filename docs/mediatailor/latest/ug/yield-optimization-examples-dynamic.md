

# Example 2: Dynamic template with player parameters
<a name="yield-optimization-examples-dynamic"></a>

Uses player parameters for app and device identification. Suitable for production multi-device deployments.

```
{
  "app": {
    "id": "{{player_params.app_id}}",
    "bundle": "com.example.myapp",
    "storeurl": "https://play.google.com/store/apps/details?id=com.example.myapp",
    "name": "{{player_params.app_name}}",
    "domain": "{{player_params.domain}}",
    "content": {
      "genre": "{{asset.genre}}",
      "contentrating": "{{asset.content_rating}}",
      "language": "{{player_params.language}}"
    }
  },
  "device": {
    "ua": "{{session.user_agent}}",
    "ip": "{{session.client_ip}}",
    "devicetype": 3,
    "ifa": "{{player_params.device_ifa}}",
    "os": "{{player_params.os}}",
    "osv": "{{player_params.osv}}",
    "model": "{{player_params.model}}",
    "make": "{{player_params.make}}",
    "language": "{{player_params.language}}",
    "w": 1920,
    "h": 1080
  },
  "imp": [
    {
      "video": {
        "mimes": ["video/mp4", "video/webm"],
        "protocols": [2, 3, 5, 6],
        "w": 1920,
        "h": 1080,
        "startdelay": -1,
        "plcmt": 1,
        "ext": {
          "slotId": "{{player_params.slot_id}}"
        }
      },
      "bidfloor": 2.0,
      "secure": 1
    }
  ],
  "user": {
    "consent": "{{player_params.consent}}"
  },
  "regs": {
    "coppa": 0,
    "gdpr": "{{player_params.gdpr}}",
    "us_privacy": "{{player_params.us_privacy}}",
    "gpp": "{{player_params.gpp_consent}}",
    "gpp_sid": "{{player_params.gpp_sid}}"
  }
}
```

**Player parameters recommended:**
+ `playerParams.app_id`, `playerParams.app_name`, `playerParams.domain`
+ `playerParams.device_ifa`, `playerParams.os`, `playerParams.osv`, `playerParams.model`, `playerParams.make`
+ `playerParams.language`, `playerParams.slot_id`
+ `playerParams.consent`, `playerParams.us_privacy`, `playerParams.gdpr`, `playerParams.gpp_consent`, `playerParams.gpp_sid`

**Session initialization example (POST body):**

```
POST https://<mediatailor-endpoint>/v1/session/<config-hash>/<origin-id>/master.m3u8

{
  "playerParams": {
    "app_id": "558775_example",
    "app_name": "My Streaming App",
    "domain": "myapp.com",
    "slot_id": "608109df-2378-4bc5-8da5-24bc355f01a4",
    "os": "Tizen",
    "osv": "5.5",
    "make": "Samsung",
    "model": "Tizen TV",
    "device_ifa": "00000000-0000-0000-0000-000000000000",
    "language": "en",
    "consent": "1",
    "us_privacy": "1YNY",
    "gdpr": "0",
    "gpp_consent": "DBABLA~BVQqAAAAAgA",
    "gpp_sid": "[7]"
  }
}
```