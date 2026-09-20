

# CreatePersonalTime
<a name="rest-op-createpersonaltime"></a>

Adds a block of time that is your own, rather than a session — travel, a meeting, a break. You must sign in.

```
POST /v1/events/{eventId}/personal-time
```

```
curl -X POST https://api.awsevents.com/v1/events/reinvent2026/personal-time \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Booth duty",
    "description": "Staffing the partner booth",
    "startDateTime": "2026-12-01T19:00:00",
    "endDateTime": "2026-12-01T21:00:00",
    "location": "Expo hall"
  }'
```

**Note**  
Create returns no body. To obtain the new entry's ID, read it back from [GetSchedule](rest-op-getschedule.md).

## Personal time fields
<a name="rest-personal-time-fields"></a>

The following table describes the fields on a personal time entry.


**Personal time fields**  

| Field | Required | Notes | 
| --- | --- | --- | 
| `title` | Yes | 1–128 characters. | 
| `description` | Yes | 1–250 characters. | 
| `startDateTime` | Yes | UTC, formatted `YYYY-MM-DDTHH:mm:ss`, with no offset or trailing `Z`. | 
| `endDateTime` | Yes | Same format. The duration from start to end must be a whole number of 5-minute increments. | 
| `location` | No | Up to 255 characters. | 