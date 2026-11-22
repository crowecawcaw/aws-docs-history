

# GetSchedule

Gets your own schedule for an event. This includes the sessions you reserved, your favorites, your personal time entries, and the sessions you are invited to. You must sign in.

Invited sessions may not be in the session catalog, so each one is returned whole, in the shape described in [What a session contains](rest-op-listsessions.md#rest-session-shape). The event manages them, so you cannot reserve, cancel, favorite, or unfavorite an invited session. [CancelReservation](rest-op-cancelreservation.md) and [DisassociateFavorite](rest-op-disassociatefavorite.md) return `400` for one, and [ReserveSessions](rest-op-reservesessions.md) and [AssociateFavorites](rest-op-associatefavorites.md) report it as a failure.

It is the source of truth for your own data. Read it back after any change. This confirms the result and returns IDs the write operations do not.

```http
GET /v1/events/{eventId}/schedule
```

```bash
curl -H "Authorization: Bearer $ACCESS_TOKEN" \
  https://api.awsevents.com/v1/events/reinvent2026/schedule
```