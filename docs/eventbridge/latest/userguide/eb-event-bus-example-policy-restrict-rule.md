# Example policy: Send events

from specific rules to an Amazon EventBridge bus in a different Region

The following example policy grants the account 111122223333 permission to send
events that match a rule named `SendToUSE1AnotherAccount` in the
Middle East (Bahrain) and US West (Oregon) Regions to an event bus named
`CrossRegionBus` in the US East (N. Virginia) in account 123456789012. The
example policy is added to the event bus named `CrossRegionBus` in account 123456789012. The policy allows events only if they match a rule specified for the
event bus in account 111122223333. The `Condition` statement restricts
events to only events that match the rules with the specified rule ARN.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSpecificRulesAsCrossRegionSource",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111112222333:root"
 },
 "Action": "events:PutEvents",
 "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/CrossRegionBus",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:events:us-west-2:111112222333:rule/CrossRegionBus/SendToUSE1AnotherAccount",
 "arn:aws:events:me-south-1:111112222333:rule/CrossRegionBus/SendToUSE1AnotherAccount"
 ]
 }
 }
 }
 ]
}`

```
