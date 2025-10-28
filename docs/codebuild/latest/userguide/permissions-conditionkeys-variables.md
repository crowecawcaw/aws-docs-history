# Use CodeBuild condition keys as IAM service role variables to control build access

With the CodeBuild build ARN, you can restrict build resource access by using context keys to
scope down resource access in your CodeBuild service role. For CodeBuild, the keys that can be used
to control build access behavior are `codebuild:buildArn` and
`codebuild:projectArn`. With the build project ARN, you can verify whether a
call to your resource came from a specific build project. To verify this, use the
`codebuild:buildArn` or `codebuild:projectArn` condition keys in
an IAM identity-based policy.

To use the `codebuild:buildArn` or `codebuild:projectArn` condition
keys in your policy, include it as a condition with any of the ARN condition operators. The
value of the key must be an IAM variable that resolves to a valid ARN. In the example policy
below, the only access allowed will be to the build project with the project ARN for the
`${codebuild:projectArn}` IAM variable.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::bucket-name/${codebuild:projectArn}/*"
 }
 ]
}`

```
