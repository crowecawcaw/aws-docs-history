

# GetSchedule
<a name="rest-op-getschedule"></a>

Gets your own schedule for an event. This includes the sessions you reserved, your favorites, and your personal time entries. You must sign in.

It is the source of truth for your own data. Read it back after any change. This confirms the result and returns IDs the write operations do not.

```
GET /v1/events/{eventId}/schedule
```

```
curl -H "Authorization: Bearer $ACCESS_TOKEN" \
  https://api.awsevents.com/v1/events/reinvent2026/schedule
```