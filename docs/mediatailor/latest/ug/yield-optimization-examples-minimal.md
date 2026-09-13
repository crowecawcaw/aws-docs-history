

# Example 1: Minimal template (CTV app)
<a name="yield-optimization-examples-minimal"></a>

The simplest valid template. Good starting point for testing. Uses session variables for device identification so it works for real viewers.

```
{
  "app": {
    "bundle": "com.example.myapp",
    "storeurl": "https://play.google.com/store/apps/details?id=com.example.myapp",
    "name": "My Streaming App",
    "content": {
      "language": "en"
    }
  },
  "device": {
    "ua": "{{session.user_agent}}",
    "ip": "{{session.client_ip}}",
    "devicetype": 3
  },
  "imp": [
    {
      "video": {
        "mimes": ["video/mp4"],
        "protocols": [2, 3, 5, 6],
        "w": 1920,
        "h": 1080,
        "ext": {
          "slotId": "your_aps_slot_id_here"
        }
      },
      "bidfloor": 5.0
    }
  ]
}
```

The default floor is $5 CPM. If you are not receiving bids during testing, try lowering this value (for example, `1.0` or `0.01`) to increase the pool of eligible advertisers.

**Player parameters required:** None. `device.ua` and `device.ip` are populated automatically from the viewer's session.

**When to use:** Initial testing and validation that your Publisher ID and APS integration are working. Suitable for production since `device.ua` and `device.ip` reflect the actual viewer automatically through session variables.