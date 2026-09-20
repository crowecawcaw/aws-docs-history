

# AssociateFavorites
<a name="rest-op-associatefavorites"></a>

Marks one or more sessions as favorites, 1 to 10 of them and all distinct. A favorite records interest only. It does not reserve the session. The result is per session, exactly as for [ReserveSessions](rest-op-reservesessions.md). Read the failures, and do not treat a repeat as a safe retry. You must sign in.

```
POST /v1/events/{eventId}/favorites
```

```
curl -X POST https://api.awsevents.com/v1/events/reinvent2026/favorites \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"sessionIds": ["'$SESSION_ID'"]}'
```