

# GetEvent

Gets one event, with the same fields as a list entry. Not filtered by date, so a link to an event keeps working after it ends. No sign-in is needed.

```http
GET /v1/events/{eventId}
```

```bash
curl https://api.awsevents.com/v1/events/reinvent2026
```