

# DisassociateFavorite
<a name="rest-op-disassociatefavorite"></a>

Removes one session from your favorites. Give the session ID in the path. If it is not there, the call returns `404`. You must sign in.

```
DELETE /v1/events/{eventId}/favorites/{sessionId}
```

```
curl -X DELETE \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  https://api.awsevents.com/v1/events/reinvent2026/favorites/$SESSION_ID
```