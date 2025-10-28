# Example policy: Send events only

from a specific Region to a different Region in Amazon EventBridge

The following example policy grants account 111122223333 permission to send all
events that are generated in the Middle East (Bahrain) and US West (Oregon) Regions to the
event bus named `CrossRegionBus` in account 123456789012 in the
US East (N. Virginia) Region. Account 111122223333 doesn't have permission to send
events that are generated in any other Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCrossRegionEventsFromUSWest2AndMESouth1",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111112222333:root"
 },
 "Action": "events:PutEvents",
 "Resource": "arn:aws:events:us-east-1:123456789012:event-bus/CrossRegionBus",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:events:us-west-2:*:*",
 "arn:aws:events:me-south-1:*:*"
 ]
 }
 }
 }
 ]
}`

```
