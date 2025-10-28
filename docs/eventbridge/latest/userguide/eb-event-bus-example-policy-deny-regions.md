# Example policy: Deny sending events

from specific Regions in Amazon EventBridge

The following example policy attached to an event bus named `CrossRegionBus` in
account 123456789012 grants permission for the event bus to receive events from the
account 111122223333, but not events that are generated in the US West (Oregon)
Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "1AllowAnyEventsFromAccount111112222333",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111112222333:root"
 },
 "Action": "events:PutEvents",
 "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/CrossRegionBus"
 },
 {
 "Sid": "2DenyAllCrossRegionUSWest2Events",
 "Effect": "Deny",
 "Principal": {
 "AWS": "*"
 },
 "Action": "events:PutEvents",
 "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/CrossRegionBus",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:events:us-west-2:*:*"
 ]
 }
 }
 }
 ]
}`

```
