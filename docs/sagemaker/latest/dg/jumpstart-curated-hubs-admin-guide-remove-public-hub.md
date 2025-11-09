# Remove access

to the SageMaker **Public models** hub

In addition to adding a private curated hub to JumpStart in Studio, you
can also remove access to the SageMaker **Public models** hub
for your users. The SageMaker **Public models** hub has access
to all available JumpStart foundation models.

If you remove access to the SageMaker **Public models** hub
and a user has access to only one private hub, then the user is taken directly into
that private hub when they choose **JumpStart** in the left
navigation pane in Studio. If a user has access to multiple private hubs, then
the user is taken to a **Hubs** menu page when they choose
**JumpStart** in the left navigation pane in
Studio.

Remove access to the SageMaker **Public models** hub for your
users with the following inline policy:

###### Note

You can specify any additional Amazon S3 buckets that you want your hub to access in the policy
below. Be sure to replace `REGION` with
the Region of your hub.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "s3:*",
 "Effect": "Deny",
 "NotResource": [
 "arn:aws:s3:::jumpstart-cache-prod-us-east-1/*.ipynb",
 "arn:aws:s3:::jumpstart-cache-prod-us-east-1/*eula*",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ]
 },
 {
 "Action": "sagemaker:*",
 "Effect": "Deny",
 "Resource": [
 "arn:aws:sagemaker:us-east-1:aws:hub/SageMakerPublicHub",
 "arn:aws:sagemaker:us-east-1:aws:hub-content/SageMakerPublicHub/*/*"
 ]
 }
 ]
}`

```
