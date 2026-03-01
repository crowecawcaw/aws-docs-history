# Example: WorkSpaces Applications service role cross-service confused deputy prevention

WorkSpaces Applications assumes a service role using a variety of resource ARNs, which leads to a
complicated conditional statement. We recommend using a wildcard resource type to
prevent any unexpected WorkSpaces Applications resources failures.

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
