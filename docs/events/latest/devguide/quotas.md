

# Quotas and throttling
<a name="quotas"></a>

 Each operation in the following table has its own quota on how many requests you can make per minute. 

## Per-attendee quotas
<a name="quotas-limits"></a>


**Requests per minute, by operation**  

| Operation | Quota per minute | 
| --- | --- | 
| GetSession | 120 | 
| ListSessions | 60 | 
| GetSchedule | 60 | 
| ReserveSessions | 30 sessions | 
| CancelReservation | 30 | 
| AssociateFavorites | 30 sessions | 
| DisassociateFavorite | 30 | 
| CreatePersonalTime | 30 | 
| UpdatePersonalTime | 30 | 
| DeletePersonalTime | 30 | 

**Note**  
 `ReserveSessions` and `AssociateFavorites` count each session named in the request, not each request. A batch is no cheaper than one request per session. It only saves round trips. 

## Handling throttling
<a name="quotas-throttled"></a>

 When you exceed a quota, the API returns `429` with a `Retry-After` header giving the seconds to wait, which is the time left in the current minute before the quota resets. Wait that long before retrying. If a batch is larger than the quota you have left, make it smaller and retry right away, because a refused request spends none of the quota. 