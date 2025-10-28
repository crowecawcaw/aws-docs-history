# Example policy: Send events to an event bus in the same account in Amazon EventBridge

The following example policy attached to an event bus named `CustomBus1` allows the event bus to receive events
from the same account and Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "events:PutEvents"
 ],
 "Resource": [
 "arn:aws:events:us-east-1:`111122223333`:event-bus/CustomBus1"
 ]
 }
 ]
}`

```
