

# Getting started
<a name="getting-started"></a>

 Listing events needs no credentials. Whether you can go on to read an event's sessions depends on that event. 

## List events without signing in
<a name="getting-started-anonymous"></a>

 Every event currently running or upcoming: 

```
curl https://api.awsevents.com/v1/events
```

 To include events that have already ended, add `includePast=true`. 

 Each entry reports whether that event requires registration. For an event that does not, read its sessions the same way, a page at a time: 

```
curl https://api.awsevents.com/v1/events/$EVENT_ID/sessions
```

 Pages can come back short. Only an absent `nextToken` means the end. See [Paginating sessions](rest-op-listsessions.md#rest-pagination). 

**Note**  
 An event that requires registration has no public catalog: its sessions return `401` to an anonymous caller. The event itself still appears in `ListEvents`. 

## Sign in to read a registration event and manage your schedule
<a name="getting-started-authenticated"></a>

 For an event that requires registration, both its session catalog and your own schedule need an access token. You sign in with your AWS Builder ID. For more information, see [Authentication](authentication.md). In outline, the process is: 

1. Register for the event through its registration site, if you have not already.

1. Sign in with your Builder ID. Obtain an access token.

1.  Send the token as a bearer token on each request: 

   ```
   curl -H "Authorization: Bearer $ACCESS_TOKEN" \
     https://api.awsevents.com/v1/events/reinvent2026/schedule
   ```

 If the token is valid but you are not registered for that event, the response is `403` rather than `401`. Signing in again will not fix it. For more information, see [Access token and event registration](auth-two-requirements.md). 

## Or connect an AI assistant
<a name="getting-started-mcp"></a>

 If you would rather work through an AI assistant than write requests, point an MCP client at the server. It will discover the available tools itself. For more information, see [Using the MCP server](mcp-server.md). 