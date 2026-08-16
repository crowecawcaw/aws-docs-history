# Example policy: Send events to a custom bus in a different account in Amazon EventBridge

The following example policy grants the account 111122223333 permission to
publish events to the `central-event-bus` in account 123456789012, but
only for events with a source value set to `com.exampleCorp.webStore` and a
`detail-type` set to `newOrderCreated`.

You attach this resource-based policy to the `central-event-bus` in the
bus-owner account (123456789012), which is the account that receives the events.
The publishing account (111122223333) is the IAM principal that the policy grants
access to, so replace the example account IDs with your own bus-owner and publishing account
IDs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "WebStoreCrossAccountPublish",
 "Effect": "Allow",
 "Action": [
 "events:PutEvents"
 ],
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:root"
 },
 "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/central-event-bus",
 "Condition": {
 "ForAllValues:StringEquals": {
 "events:source": "com.exampleCorp.webStore",
 "events:detail-type": "newOrderCreated"
 }
 }
 }
 ]
}`

```
