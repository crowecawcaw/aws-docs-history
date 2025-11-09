# Example: WorkSpaces Applications Elastic fleets session script

Amazon S3 bucket policy cross-service confused deputy prevention

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
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::`your-bucket-name`/`your-session-script-path`",
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
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::`bucket`/`AppStream2`/*",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:appstream:us-east-1:111122223333:fleet/`yourFleetName`"
 }
 }
 }
 ]
}`

```
