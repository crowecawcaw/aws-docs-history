# Custom action Lambda execution block sample policy

The following is a sample policy to attach if you add execution blocks to a Region switch plan for Lambda functions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:GetFunction",
 "lambda:InvokeFunction"
 ],
 "Resource": [
 "arn:aws:lambda:us-east-1:123456789012:function:app-recovery-primary",
 "arn:aws:lambda:us-west-2:123456789012:function:app-recovery-secondary"
 ]
 }
 ]
}`

```
