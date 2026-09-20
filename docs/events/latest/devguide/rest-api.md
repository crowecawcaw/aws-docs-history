

# Using the REST API
<a name="rest-api"></a>

 All requests go to `https://api.awsevents.com`. Every path is versioned and begins with `/v1`. Requests and responses are JSON. 

 Reading a registration event's catalog, and every operation on your own schedule, needs a bearer token from an attendee registered for that event. For more information, see [Authentication](authentication.md). Examples use `reinvent2026`, which requires registration, and shell variables for the IDs and token you supply. 

**Note**  
 The full OpenAPI description of these operations is served at `https://api.awsevents.com/v1/openapi.json`. 

**Topics**
+ [ListEvents](rest-op-listevents.md)
+ [GetEvent](rest-op-getevent.md)
+ [ListSessions](rest-op-listsessions.md)
+ [GetSession](rest-op-getsession.md)
+ [GetSchedule](rest-op-getschedule.md)
+ [ReserveSessions](rest-op-reservesessions.md)
+ [CancelReservation](rest-op-cancelreservation.md)
+ [AssociateFavorites](rest-op-associatefavorites.md)
+ [DisassociateFavorite](rest-op-disassociatefavorite.md)
+ [CreatePersonalTime](rest-op-createpersonaltime.md)
+ [UpdatePersonalTime](rest-op-updatepersonaltime.md)
+ [DeletePersonalTime](rest-op-deletepersonaltime.md)