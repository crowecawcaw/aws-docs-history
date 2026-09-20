

# ListEvents
<a name="rest-op-listevents"></a>

Lists AWS events. By default, it returns running and upcoming events. Set `includePast=true` to also include events that have ended. No sign-in is needed. Use the `eventId` in each entry for `{eventId}` in the other paths in this chapter.

```
GET /v1/events
```

```
curl "https://api.awsevents.com/v1/events?includePast=true"
```