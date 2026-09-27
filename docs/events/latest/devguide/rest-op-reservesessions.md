

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

The response reports each session independently, as succeeded or failed. Each failure names the session and a reason code, such as the session being full, clashing with something already on your schedule, or already being on it. A clash also names what it clashes with. Treat a code you do not recognize as a refusal you cannot act on, because codes are added over time.

**Important**  
A `200` does not mean everything succeeded. Always read the failures. A session that was already reserved counts as a failure too, so re-sending the same request is not a safe retry.