# Example: AppStream 2.0 service role cross-service

confused deputy prevention

AppStream 2.0 assumes a service role using a variety of resource ARNs, which leads to a
complicated conditional statement. We recommend using a wildcard resource type to
prevent any unexpected AppStream 2.0 resources failures.

###### Example `aws:SourceAccount` Conditional:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "appstream.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`your AWS account ID`"
 }
 }
 }
 ]
}`

```

###### Example `aws:SourceArn` Conditional:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "appstream.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:appstream:`us-east-1`:`111122223333`:*"
 }
 }
 }
 ]
}`

```
