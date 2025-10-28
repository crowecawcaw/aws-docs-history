# Using AWS Management Console Private Access with AWS Organizations

service control policies

If your AWS organization is using a service control policy (SCP) that allows specific
services, you must add `signin:*` to the allowed actions. This permission is
needed because signing in to the AWS Management Console over a Private Access VPC endpoint performs an
IAM authorization that the SCP blocks without the permission. As an example, the following
service control policy allows the Amazon EC2 and CloudWatch services to be used in the organization,
including when they are accessed using an AWS Management Console Private Access endpoint.

```
{
  "Effect": "Allow",
  "Action": [
    "signin:*",
    "ec2:*",
    "cloudwatch:*",
    ... Other services allowed
  },
  "Resource": "*"
}
```

For more information about SCPs, see [Service control
policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
