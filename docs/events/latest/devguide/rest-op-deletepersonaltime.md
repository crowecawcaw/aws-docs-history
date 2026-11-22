

# DeletePersonalTime

Removes a personal time entry. Give its ID in the path. IDs come from [GetSchedule](rest-op-getschedule.md). You must sign in.

```http
DELETE /v1/events/{eventId}/personal-time/{personalTimeId}
```

```bash
curl -X DELETE \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  https://api.awsevents.com/v1/events/reinvent2026/personal-time/$PERSONAL_TIME_ID
```