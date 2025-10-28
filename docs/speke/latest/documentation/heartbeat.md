# SPEKE API v1 - Heartbeat

_Request Syntax Example_

The following URL is an example and does not indicate a fixed format:

```
GET https://speke-compatible-server/speke/v1.0/heartbeat
```

_Request Response_

| HTTP CODE       | Payload Name  | Occurs | Description                       |
| --------------- | ------------- | ------ | --------------------------------- |
| `200 (Success)` | statusMessage | 1..1   | Message that describes the status |
