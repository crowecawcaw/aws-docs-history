# Resource-based policy

examples for AWS Glue

This section contains example resource-based policies, including policies that grant
cross-account access.

The examples use the AWS Command Line Interface (AWS CLI) to interact with AWS Glue service
API operations. You can perform the same operations on the AWS Glue console
or using one of the AWS SDKs.

###### Important

By changing an AWS Glue resource policy, you might accidentally revoke
permissions for existing AWS Glue users in your account and cause
unexpected disruptions. Try these examples only in development or test accounts, and
ensure that they don't break any existing workflows before you make the
changes.

###### Topics

- [Considerations for using resource-based policies with AWS Glue](#security_iam_resource-based-policy-examples-considerations "#security_iam_resource-based-policy-examples-considerations")
- [Use a resource
  policy to control access in the same account](#glue-policy-resource-policies-example-same-account "#glue-policy-resource-policies-example-same-account")

## Considerations for using resource-based policies with AWS Glue

###### Note

Both IAM policies and an AWS Glue resource policy take a few
seconds to propagate. After you attach a new policy, you might notice that the old
policy is still in effect until the new policy has propagated through the
system.

You use a policy document written in JSON format to create or modify a resource
policy. The policy syntax is the same as for an identity-based IAM policy (see
[IAM JSON policy
reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")), with the following exceptions:

- A `"Principal"` or `"NotPrincipal"` block is required
  for each policy statement.
- The `"Principal"` or `"NotPrincipal"` must identify
  valid existing principals. Wildcard patterns (like
  `arn:aws:iam::`account-id`:user/*`)
  are not allowed.
- The `"Resource"` block in the policy requires all resource ARNs
  to match the following regular expression syntax (where the first
  `%s` is the `region`, and the second
  `%s` is the `account-id`):

```
*arn:aws:glue:%s:%s:(\*|[a-zA-Z\*]+\/?.*)
```

For example, both
`arn:aws:glue:us-west-2:`account-id`:*`
and
`arn:aws:glue:us-west-2:`account-id`:database/default`
are allowed, but `*` is not allowed.

- Unlike identity-based policies, an AWS Glue resource policy must
  only contain Amazon Resource Names (ARNs) of resources that belong to the
  catalog that the policy is attached to. Such ARNs always start with
  `arn:aws:glue:`.
- A policy cannot cause the identity that creates it to be locked out of
  further policy creation or modification.
- A resource-policy JSON document cannot exceed 10 KB in size.

## Use a resource

policy to control access in the same account

In this example, an admin user in Account A creates a resource policy that grants
IAM user `Alice` in Account A full access to the catalog. Alice has no
IAM policy attached.

To do this, the admin user runs the following AWS CLI command.

```
# Run as admin of Account A
$ aws glue put-resource-policy --profile `administrator-name` --region us-west-2 --policy-in-json '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Principal": {
        "AWS": [
          "arn:aws:iam::`account-A-id`:user/Alice"
        ]
      },
      "Effect": "Allow",
      "Action": [
        "glue:*"
      ],
      "Resource": [
        "arn:aws:glue:us-west-2:`account-A-id`:*"
      ]
    }
  ]
}'
```

Instead of entering the JSON policy document as a part of your AWS CLI command, you
can save a policy document in a file and reference the file path in the AWS CLI
command, prefixed by `file://`. The following is an example of how you
might do that.

```
$ echo '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Principal": {
        "AWS": [
          "arn:aws:iam::`account-A-id`:user/Alice"
        ]
      },
      "Effect": "Allow",
      "Action": [
        "glue:*"
      ],
      "Resource": [
        "arn:aws:glue:us-west-2:`account-A-id`:*"
      ]
    }
  ]
}' > /temp/policy.json

$ aws glue put-resource-policy --profile admin1 \
    --region us-west-2 --policy-in-json file:///temp/policy.json

```

After this resource policy has propagated, Alice can access all
AWS Glue resources in Account A, as follows.

```
# Run as user Alice
$ aws glue create-database --profile alice --region us-west-2 --database-input '{
    "Name": "new_database",
    "Description": "A new database created by Alice",
    "LocationUri": "s3://amzn-s3-demo-bucket"
}'

$ aws glue get-table --profile alice --region us-west-2 --database-name "default" --table-name "tbl1"}
```

In response to Alice's `get-table` call, the AWS Glue
service returns the following.

```
{
  "Table": {
    "Name": "tbl1",
    "PartitionKeys": [],
    "StorageDescriptor": {
        ......
    },
    ......
  }
}
```
