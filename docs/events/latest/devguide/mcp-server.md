

# Using the MCP server
<a name="mcp-server"></a>

 The MCP server offers the same operations as the REST API, as tools that an AI assistant can call. 

## Connecting a client
<a name="mcp-connecting"></a>

 The server endpoint is `https://api.awsevents.com/mcp`, over streamable HTTP. Point a client at that URL. Where a client lets you set a client ID, use `7vmom55m1qstvq8i71ph127bfq`, which is shared by all callers. 

 The server requires sign-in, and the client handles that flow for you. On the first call it receives a challenge naming where to sign in, opens that page in a browser, and stores the resulting token. The sign-in itself is the flow described in [Authentication](authentication.md). 

**Kiro**

 Add the server to your MCP configuration file: 

```
{
  "mcpServers": {
    "awsevents": {
      "url": "https://api.awsevents.com/mcp",
      "oauth": {
        "clientId": "7vmom55m1qstvq8i71ph127bfq",
        "redirectUri": "http://127.0.0.1:8976",
        "oauthScopes": ["openid", "email", "events/access"]
      }
    }
  }
}
```

 End `redirectUri` at the port, as shown. Kiro reads the port from the last colon onward and adds the `/oauth/callback` path itself. Give it a value with a path and it cannot read the port, so it falls back to a random one and sign-in fails with `redirect_mismatch`. Reload the window after editing the file. 

**Claude Code**

```
claude mcp add --transport http --scope user awsevents \
  https://api.awsevents.com/mcp \
  --callback-port 8484 --client-id 7vmom55m1qstvq8i71ph127bfq
```

**Important**  
 Use the preceding callback values, and always set the port. Both clients pick a random port otherwise, and a random port cannot sign in. The API matches a callback in full, port and path included, with no wildcards, and one it does not recognize fails without reporting the callback as the cause. 

**Note**  
 The client stores your token on the machine it runs on, and not every client protects it well. Deleting a client's configuration does not invalidate the token it already holds. An MCP client has no redirect chain to sign you out with, so to sign out fully, revoke the token as described in [Signing an attendee out](auth-signing-out.md), then end the Builder ID session at `https://profile.aws.amazon.com`. 

 To confirm the connection, ask the assistant to list events. 

## Available tools
<a name="mcp-tools"></a>

 Each tool maps to one REST operation. The server itself requires sign-in, so every tool call is made as a signed-in attendee, including the catalog tools that need no credentials on the REST API. Reading the catalog of an event that requires registration, and anything that touches a schedule, additionally requires that the attendee be registered for that event. 


**MCP tools**  

| Tool | Description | 
| --- | --- | 
| ListEvents | Lists AWS events that are running or upcoming, such as AWS re:Invent. | 
| GetEvent | Gets one event by ID. | 
| ListSessions | Lists an event's sessions, a page at a time. | 
| GetSession | Gets one session within an event. | 
| GetSchedule | Gets your own schedule for an event. | 
| ReserveSessions | Reserves one or more sessions. | 
| CancelReservation | Cancels one of your reservations. | 
| AssociateFavorites | Marks one or more sessions as favorites. | 
| DisassociateFavorite | Removes one session from favorites. | 
| CreatePersonalTime | Adds a personal time entry. | 
| UpdatePersonalTime | Replaces a personal time entry. | 
| DeletePersonalTime | Removes a personal time entry. | 

## What to expect from an assistant
<a name="mcp-behavior"></a>
+  Per-operation quotas apply as on the REST API, and an operation can be closed even when its tool is listed. For more information, see [Quotas and throttling](quotas.md) and [When an operation is closed](errors.md#errors-operation-closed). 
+  Reserving and favoriting succeed per session, not per request, so an assistant can report "done" when some sessions failed. Ask it to confirm from `GetSchedule`. 