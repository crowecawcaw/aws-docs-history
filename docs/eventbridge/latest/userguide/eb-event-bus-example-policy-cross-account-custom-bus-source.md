# Example policy:

Send events to a custom bus in a different account in Amazon EventBridge

The following example policy grants the account 111122223333 permission to
publish events to the `central-event-bus` in account 123456789012, but
only for events with a source value set to `com.exampleCorp.webStore` and a
`detail-type` set to `newOrderCreated`.

JSON

```


```
