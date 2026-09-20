

# GetSession
<a name="rest-op-getsession"></a>

Gets one session in an event. The session has the same shape as a list entry. See [What a session contains](rest-op-listsessions.md#rest-session-shape). Session IDs come from `ListSessions`. No sign-in is needed, unless the event requires registration.

```
GET /v1/events/{eventId}/sessions/{sessionId}
```

```
curl https://api.awsevents.com/v1/events/reinvent2026/sessions/$SESSION_ID
```