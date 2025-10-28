# Example policy: Send events to the

default bus in a different account in Amazon EventBridge

The following example policy grants the account 111122223333 permission to
publish events to the default event bus in the account 123456789012.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "sid1",
 "Effect": "Allow",
 "Principal": {"AWS":"arn:aws:iam::111112222333:root"},
 "Action": "events:PutEvents",
 "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/default"
 }
 ]
 }`

```
