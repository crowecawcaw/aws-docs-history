# Configure the IAM permissions required to

create multi-Region keyspaces and tables

To successfully create multi-Region keyspaces and tables, the IAM principal needs to
be able to create a service-linked role. This service-linked role is a unique type of
IAM role that is predefined by Amazon Keyspaces. It includes all the permissions that Amazon Keyspaces
requires to perform actions on your behalf. For more information about the
service-linked role, see [Using roles for Amazon Keyspaces Multi-Region Replication](using-service-linked-roles-multi-region-replication.md "using-service-linked-roles-multi-region-replication.md").

To create the service-linked role required by multi-Region replication, the policy for the IAM
principal requires the following elements:

- `iam:CreateServiceLinkedRole` – The **action** the principal can perform.
- `arn:aws:iam::*:role/aws-service-role/replication.cassandra.amazonaws.com/AWSServiceRoleForKeyspacesReplication`
  – The **resource** that the action can be
  performed on.
- `iam:AWSServiceName": "replication.cassandra.amazonaws.com`
  – The only AWS service that this role can be attached to is Amazon Keyspaces.
  The following is an example of the policy that grants the minimum required permissions
  to a principal to create multi-Region keyspaces and tables.

```
{
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/replication.cassandra.amazonaws.com/AWSServiceRoleForKeyspacesReplication",
            "Condition": {"StringLike": {"iam:AWSServiceName": "replication.cassandra.amazonaws.com"}}
}
```

For additional IAM permissions for multi-Region keyspaces and tables, see the
[Actions, resources, and condition keys for Amazon Keyspaces (for Apache Cassandra)](../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md "../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md") in the _Service Authorization Reference_.
