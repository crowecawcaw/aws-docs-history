Defect Detection App is in preview release and is subject to change.

# GET /dda-component-status

Gets the current health status of the station. If the station is unhealthy, you can call
to get
more information.

## Endpoint

```
GET /dda-component-status
```

## Request

parameters

None

## Response

The current status of the station. `HEALTHY` if the station
is healthy, otherwise `UNHEALTHY`.

Format: String
