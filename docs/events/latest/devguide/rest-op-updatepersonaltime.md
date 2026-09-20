

# UpdatePersonalTime
<a name="rest-op-updatepersonaltime"></a>

Replaces a personal time entry that you already created. You must sign in.

**Note**  
This replaces the entry. It does not merge. Resend every field, even the ones you are not changing. For the field list, see [Personal time fields](rest-op-createpersonaltime.md#rest-personal-time-fields). If you omit `location`, it is cleared. The entry keeps its `personalTimeId`.

```
PUT /v1/events/{eventId}/personal-time/{personalTimeId}
```

```
curl -X PUT \
  https://api.awsevents.com/v1/events/reinvent2026/personal-time/$PERSONAL_TIME_ID \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Booth duty",
    "description": "Staffing the partner booth",
    "startDateTime": "2026-12-01T19:30:00",
    "endDateTime": "2026-12-01T21:30:00",
    "location": "Expo hall"
  }'
```