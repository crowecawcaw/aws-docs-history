# Configuring Amazon OpenSearch Service domain security

To use the plugin with OpenSearch Service, the user or role that's accessing your domain must have `PassRole`
permissions for the [IAM service role for OpenSearch Service](service-role-managed.md "service-role-managed.md") you just created. Also, the user or
role must have permission to perform the `es:ESHttpGet` and `es:ESHttpPut` actions.

For information about configuring access to OpenSearch Service, see [Security in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/security.md "../../../opensearch-service/latest/developerguide/security.md") in the
_Amazon OpenSearch Service Developer Guide_. For policy examples, see [Policy examples for OpenSearch Service user or role](#opensearch-domain-user-policy-examples "#opensearch-domain-user-policy-examples").

## Policy examples for OpenSearch Service user or role

The following IAM policy example grants a user or role `PassRole` permissions for the IAM service role
that you created for OpenSearch Service in [Configuring permissions when resources are in the same
account](service-role-managed.md "service-role-managed.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/opensearchservice.amazonaws.com/AWSServiceRoleForAmazonOpenSearchService"
 }
 ]
}`

```

The following IAM policy grants the minimum permissions to create pipelines and search queries with
OpenSearch Service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "es:ESHttpGet",
 "es:ESHttpPut"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:ResourceTag/environment": [
 "production"
 ]
 }
 }
 }
 ]
}`

```
