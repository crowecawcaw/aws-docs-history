

# CancelReservation
<a name="rest-op-cancelreservation"></a>

Cancels one of your reservations, by session ID. If you have none for that session, the call returns `404`. So a `404` on a retry means it was already gone. You must sign in.

```
DELETE /v1/events/{eventId}/reservations/{sessionId}
```

```
curl -X DELETE -H "Authorization: Bearer $ACCESS_TOKEN" \
  https://api.awsevents.com/v1/events/$EVENT_ID/reservations/$SESSION_ID
```