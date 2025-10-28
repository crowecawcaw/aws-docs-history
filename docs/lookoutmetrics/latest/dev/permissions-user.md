Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Identity-based IAM policies for Lookout for Metrics

To grant users in your account access to Lookout for Metrics, you use identity-based policies in AWS Identity and Access Management (IAM).
Identity-based policies can apply directly to users, or to groups and roles that are associated with a
user. You can also grant users in another account permission to assume a role in your account and access your Lookout for Metrics
resources.

The following IAM policy allows a user to access all Lookout for Metrics API actions, and to pass [service roles](permissions-service.md "permissions-service.md") to Lookout for Metrics.

###### Example User policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lookoutmetrics:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "lookoutmetrics.amazonaws.com"
 }
 }
 }
 ]
}`

```

The preceding policy does not allow a user to create IAM roles. For a user with these permissions to create a
dataset or alert, an administrator must create the service role that grants Lookout for Metrics permission to access datasources
and alert channels. For more information, see [Service roles for Amazon Lookout for Metrics](permissions-service.md "permissions-service.md").

In addition to Lookout for Metrics, a user needs permission to view resources in services that they use as a detector's
datasource or as alert channels. When you work with a detector in the Lookout for Metrics console, the console uses your
permissions to simplify the configuration process.

You can grant full access to each service or limit the scope of permissions by resource name. The following
example shows a policy that provides read-only access to a subset of resources in Lookout for Metrics. The `Resources`
key for applicable actions limits access to resources whose names start with `intern-`.

If you [tag your resources](detectors-tags.md "detectors-tags.md"), you can also use condition keys to limit access
to a resource based on the presence or value of a tag. For permissions purposes, detectors, datasets and alerts are
independent resources. If you grant or deny permission to a detector, the permission does not automatically apply to
the detector's dataset or alerts.

The resources and conditions supported for use in policies vary among API actions. For more information, see
[Actions, resources, and condition keys for
Amazon Lookout for Metrics](../../../service-authorization/latest/reference/list_amazonlookoutformetrics.md "../../../service-authorization/latest/reference/list_amazonlookoutformetrics.md") in the Service Authorization Reference.
