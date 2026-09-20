

# ListSessions
<a name="rest-op-listsessions"></a>

Lists an event's sessions, a page at a time. The service sets the page size. Pass `nextToken` to continue. Every page reports `totalCount`, the number of sessions in the catalog, so you can size a walk from the first page. Set `includeAbstracts=false` to omit each session's `abstract`, the largest field, when you only need enough to choose between sessions. An optional `locale` query parameter takes a language tag. If it is unavailable or omitted, the catalog is served in `en-US`. The response reports what was actually served. No sign-in is needed, unless the event requires registration.

```
GET /v1/events/{eventId}/sessions
```

```
curl https://api.awsevents.com/v1/events/reinvent2026/sessions
```

To fetch the next page, pass the `nextToken` from the previous response:

```
curl "https://api.awsevents.com/v1/events/reinvent2026/sessions?nextToken=$NEXT_TOKEN"
```

## What a session contains
<a name="rest-session-shape"></a>

`ListSessions` and `GetSession` return the same session shape. A session carries a `sessionId`, a title, an abstract, and a short session code; its type and level, and taxonomy lists such as tracks, topics, industries, roles, and services; its start, end, room, and venue, and whether it runs all day; whether it can be reserved, and when it can, a coarse indication of how full it is; and the names of the speakers presenting it.

A field is present only when the event provides it. Treat any single field as optional, and read defensively.

## Paginating sessions
<a name="rest-pagination"></a>

**Note**  
Page sizes can vary, and a short page does not mean the last page. Stop when `nextToken` is absent, never when a page looks short. A client that stops early silently misses sessions.