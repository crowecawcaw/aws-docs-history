Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Tag resources in Amazon Redshift

In AWS, tags are user-defined labels that consist of key-value pairs. Amazon Redshift supports
tagging to provide metadata about resources at a glance, and to categorize your billing
reports based on cost allocation. To use tags for cost allocation, you must first activate
those tags in the AWS Billing and Cost Management service. For more information about setting up and using tags for
billing purposes, see [Use cost allocation
tags for custom billing reports](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") and [Setting up your monthly cost
allocation report](../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md "../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md").

Tags are not required for resources in Amazon Redshift, but they help provide context. You might
want to tag resources with metadata about cost centers, project names, and other pertinent
information related to the resource. For example, suppose you want to track which resources
belong to a test environment and a production environment. You could create a key named
`environment` and provide the value `test` or
`production` to identify the resources used in each environment. If you use
tagging in other AWS services or have standard categories for your business, we recommend
that you create the same key-value pairs for resources in Amazon Redshift for consistency.

Tags are retained for resources after you resize a cluster, and after you restore a
snapshot of a cluster within the same region. However, tags are not retained if you copy a
snapshot to another region, so you must recreate the tags in the new region. If you delete a
resource, any associated tags are deleted.

Each resource has one _tag set_, which is a collection of one or more
tags assigned to the resource. Each resource can have up to 50 tags per tag set. You can add
tags when you create a resource and after a resource has been created. You can add tags to
the following resource types in Amazon Redshift:

- CIDR/IP
- Cluster
- Cluster security group
- Cluster security group ingress rule
- Amazon EC2 security group
- Hardware security module (HSM) connection
- HSM client certificate
- Parameter group
- Snapshot
- Subnet group
- Integration (zero-ETL integration)
  To use tagging from the Amazon Redshift console, your user can attach the AWS managed policy
  `AmazonRedshiftFullAccess`. For an example IAM policy with limited tagging
  permissions that you can attach to an Amazon Redshift console user, see [Example 7: Allow a
  user to tag resources with the Amazon Redshift console](redshift-iam-access-control-identity-based.md#redshift-policy-example-allow-tagging-with-console "redshift-iam-access-control-identity-based.md#redshift-policy-example-allow-tagging-with-console"). For more information
  about tagging, see [What is AWS Resource
  Groups?](../../../ARG/latest/userguide/welcome.md "../../../ARG/latest/userguide/welcome.md").

## Tagging requirements

Tags have the following requirements:

- Keys can't be prefixed with `aws:`.
- Keys must be unique per tag set.
- A key must be between 1 and 128 allowed characters.
- A value must be between 0 and 256 allowed characters.
- Values do not need to be unique per tag set.
- Allowed characters for keys and values are Unicode letters, digits, white
  space, and any of the following symbols: \_ . : / = + - @.
- Keys and values are case sensitive.
