

# Handling errors
<a name="errors"></a>

 The API returns errors with an HTTP status code and a JSON body. The body contains a `message`. 

## Error reference
<a name="errors-reference"></a>


**Errors returned by the AWS Events API**  

| Status | Meaning | What to do | 
| --- | --- | --- | 
| `400` | The API could not accept the request as sent. A field is missing, too long, or malformed. The API also returns this for a `nextToken` it did not issue. | Do not retry. Fix the request. The message says which field. | 
| `401` | The operation needs a signed-in attendee, but you sent no valid token. The `WWW-Authenticate` header says where to sign in. An event that requires registration has no public catalog. For that event, `ListSessions` and `GetSession` return `401` to an anonymous caller. | Sign in, or refresh the token, then retry once. See [Keeping the attendee signed in](auth-refreshing.md). | 
| `403` | Two different causes, told apart by the body. With a JSON body, the caller is signed in but not registered for this event. That includes reading the catalog of an event that requires registration, so an unregistered caller gets `403` from `ListSessions` and `GetSession` too. With no body, the refusal came from the edge rather than the API, and requests from your address are being refused. | For a registration problem, do not retry. Register for the event first, because signing in again will not help. For an edge refusal, slow down, then retry. | 
| `404` | The event, session, or personal time entry does not exist. For a removal, it is already gone. | Do not retry. For removals, treat it as already done. | 
| `409` | The operation is not currently available. The request itself was valid. | Do not retry immediately. See [When an operation is closed](#errors-operation-closed). | 
| `429` | The caller has used up this operation's quota for the current minute. | Wait for `Retry-After` seconds, then retry. See [Quotas and throttling](quotas.md). | 
| `500` | The service hit an internal error. It could not process the request. | Retry a read with backoff. Before retrying a write, reconcile from `GetSchedule`. See [Retrying a write safely](#errors-retrying-writes). If it persists, report it using the *Feedback* link on this page. | 
| `503` | The service is temporarily unavailable. | Retry a read with backoff. For a write, see [Retrying a write safely](#errors-retrying-writes). | 

## When an operation is closed
<a name="errors-operation-closed"></a>

 An operation can close for a time while the rest of the API keeps working. A closed operation returns `409` to every caller. The request itself was not the problem. The same request will not succeed until the operation opens. 

 Reservations might be closed until reserved seating opens for an event. Browsing and favoriting keep working. 

## Retrying a write safely
<a name="errors-retrying-writes"></a>

 The API has no idempotency key. Re-sending a create makes a new one. This matters for the two bulk operations and for `CreatePersonalTime`. If you never learned the outcome of one of those — a timeout, a dropped connection, a `500` or a `503` — do not simply re-send it. Read [GetSchedule](rest-op-getschedule.md) and compare it with what you intended. Send only what is still missing. 

 The single removals are different. Canceling a reservation or removing a favorite that is already gone returns `404`, so a retry whose response you never saw is safe: treat `404` as already done. 

 A `429` and a `409` are also safe to retry later, because neither performed the write. 