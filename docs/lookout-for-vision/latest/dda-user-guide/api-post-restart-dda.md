Defect Detection App is in preview release and is subject to change.

# POST

/restart-dda

Initiates the restart of the Defect Detection Station App. The restart might take a few minutes to
complete. During restart the response from [GET /dda-component-status](api-get-dda-component-status.md "api-get-dda-component-status.md") is `UNHEALTHY`. The
response is `HEALTHY` after the Station App has successfully restarted.

For more information, see [Managing station health](dda-managing-system-health.md "dda-managing-system-health.md").

## Endpoint

```
POST /restart-dda
```

## Request

parameters

None

## Response

None.
