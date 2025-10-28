# Use CalledVia context keys for Athena

When a [principal](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal") makes a [request](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-request "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-request")
to AWS, AWS gathers the request information into a _request context_
that evaluates and authorizes the request. You can use the `Condition` element of
a JSON policy to compare keys in the request context with key values that you specify in
your policy. _Global condition context keys_ are condition
keys with an `aws:` prefix.

## About the

aws:CalledVia context key

You can use the [aws:CalledVia](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia") global condition context key to compare
the services in the policy with the services that made requests on behalf of the IAM
principal (user or role). When a principal makes a request to an AWS service, that
service might use the principal's credentials to make subsequent requests to other
services. The `aws:CalledVia` key contains an ordered list of each service in
the chain that made requests on the principal's behalf.

By specifying a service principal name for the `aws:CalledVia` context key,
you can make the context key AWS service-specific. For example, you can use the
`aws:CalledVia` condition key to limit requests to only those made from
Athena. To use the `aws:CalledVia` condition key in a policy with Athena, you
specify the Athena service principal name `athena.amazonaws.com`, as in the
following example.

```
 ...
    "Condition": {
        "ForAnyValue:StringEquals": {
            "**aws:CalledVia**": "**athena.amazonaws.com**"
        }
    }
...
```

You can use the `aws:CalledVia` context key to ensure that callers only
have access to a resource (like a Lambda function) if they call the resource from
Athena.

###### Note

The `aws:CalledVia` context key is not compatible with the trusted
identity propagation feature.

## Add a CalledVia context key for access to Lambda functions

Athena requires the caller to have `lambda:InvokeFunction` permissions in
order to invoke the Lambda function associated with the query. The following statement
specifies that the user can invoke Lambda functions only from Athena.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor3",
 "Effect": "Allow",
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:us-east-1:`111122223333`:function:`OneAthenaLambdaFunction`",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "athena.amazonaws.com"
 }
 }
 }
 ]
}`

```

The following example shows the addition of the previous statement to a policy that
allows a user to run and read a federated query. Principals who are allowed to perform
these actions can run queries that specify Athena catalogs associated with a federated
data source. However, the principal cannot access the associated Lambda function unless
the function is invoked through Athena.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "athena:GetWorkGroup",
 "s3:PutObject",
 "s3:GetObject",
 "athena:StartQueryExecution",
 "s3:AbortMultipartUpload",
 "athena:StopQueryExecution",
 "athena:GetQueryExecution",
 "athena:GetQueryResults",
 "s3:ListMultipartUploadParts"
 ],
 "Resource": [
 "arn:aws:athena:*:`111122223333`:workgroup/`WorkGroupName`",
 "arn:aws:s3:::`MyQueryResultsBucket`/*",
 "arn:aws:s3:::`MyLambdaSpillBucket`/`MyLambdaSpillPrefix`*"
 ]
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": "athena:ListWorkGroups",
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor2",
 "Effect": "Allow",
 "Action":
 [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`MyLambdaSpillBucket`"
 },
 {
 "Sid": "VisualEditor3",
 "Effect": "Allow",
 "Action": "lambda:InvokeFunction",
 "Resource": [
 "arn:aws:lambda:*:`111122223333`:function:`OneAthenaLambdaFunction`",
 "arn:aws:lambda:*:`111122223333`:function:`AnotherAthenaLambdaFunction`"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "athena.amazonaws.com"
 }
 }
 }
 ]
}`

```

For more information about `CalledVia` condition keys, see [AWS global
condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.
