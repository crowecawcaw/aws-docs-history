

# What is the AWS Events API?
<a name="what-is-events-api"></a>

**Note**  
Reserved seating for AWS re:Invent opens on October 6, 2026, and opens through this API on October 8, 2026. Until then, reserving and canceling return `409`. Reading the catalog and marking favorites work as normal.

 AWS re:Invent, AWS Summits, and other AWS conferences publish session catalogs listing talks, workshops, and labs. 

 With this API you can list events, read a session catalog, and manage your own schedule: reserve sessions, mark favorites, and add personal time. 

 You sign in on your own machine. There is no hosted option. An application you distribute runs on each attendee's machine and signs that person in. The API always acts for the attendee who is signed in. 

 You can use the API two ways. Both offer the same features. 
+  A *REST API*, for applications and scripts. For more information, see [Using the REST API](rest-api.md). 
+  A *Model Context Protocol (MCP) server*, for AI assistants and agents. An MCP client finds the available tools and calls them for you. You can ask an assistant to find sessions or build a schedule. Unlike the REST API, the MCP server requires sign-in for every call, even catalog reads. For more information, see [Using the MCP server](mcp-server.md). 

## Which events you can read, and when you need to sign in
<a name="what-is-access"></a>

 Whether an event's session catalog is public depends on whether that event requires registration. That same requirement decides whether there is a schedule to manage. 
+  *Events that do not require registration*: the session catalog is public. Anyone can read it with no credentials. These events have no schedule to manage. 
+  *Events that require registration*: the session catalog is not public. Reading it needs an attendee who has signed in and is registered for that event. Those attendees can also read and change their own schedule: make and cancel reservations, add and remove favorites, and manage personal time. 

 `ListEvents` and `GetEvent` need no credentials for any event. An event that requires registration still appears in the list even when its sessions are not readable. 

## What the API does not do
<a name="what-is-not-included"></a>
+ It does not register you for an event. It does not return a registration link. Register through the event's own registration site first.
+ It does not expose other attendees, or any data belonging to them.
+  It does not guarantee a reservation. A request can be refused for one session while succeeding for others. For more information, see [Reading the result](rest-op-reservesessions.md#rest-reservations). 
+  It does not search or filter the catalog. You retrieve an event's sessions and filter them in your own application. 