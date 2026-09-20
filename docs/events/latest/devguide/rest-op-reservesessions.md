

# ReserveSessions
<a name="rest-op-reservesessions"></a>

Reserves one or more sessions for you. Send the session IDs in the request body. One request carries 1 to 10 session IDs. They must be distinct. You must sign in.

```
POST /v1/events/{eventId}/reservations
```

```
curl -X POST https://api.awsevents.com/v1/events/reinvent2026/reservations \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"sessionIds": ["'$SESSION_ID'"]}'
```

## Reading the result
<a name="rest-reservations"></a>

The response reports each session independently, as succeeded or failed. Each failure names the session and the reason: the session is full, its time conflicts with something already on your schedule, or you already have it.

**Important**  
A `200` does not mean everything succeeded. Always read the failures. A session that was already reserved counts as a failure too, so re-sending the same request is not a safe retry.