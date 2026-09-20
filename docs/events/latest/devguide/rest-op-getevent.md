

# GetEvent
<a name="rest-op-getevent"></a>

Gets one event, with the same fields as a list entry. Not filtered by date, so a link to an event keeps working after it ends. No sign-in is needed.

```
GET /v1/events/{eventId}
```

```
curl https://api.awsevents.com/v1/events/reinvent2026
```