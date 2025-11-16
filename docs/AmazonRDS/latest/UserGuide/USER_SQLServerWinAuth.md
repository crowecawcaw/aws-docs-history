# Managing a DB instance in a

Domain

You can use the console, AWS CLI, or the Amazon RDS API to manage your DB instance and its
relationship with your domain. For example, you can move the DB instance into, out of,
or between domains.

For example, using the Amazon RDS API, you can do the following:

- To reattempt a domain join for a failed membership, use the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") API
  operation and specify the current membership's directory ID.
- To update the IAM role name for membership, use the `ModifyDBInstance` API operation and
  specify the current membership's directory ID and the new IAM role.
- To remove a DB instance from a domain, use the `ModifyDBInstance` API operation and specify
  `none` as the domain parameter.
- To move a DB instance from one domain to another, use the `ModifyDBInstance` API operation
  and specify the domain identifier of the new domain as the domain parameter.
- To list membership for each DB instance, use the [DescribeDBInstances](../APIReference/DescribeDBInstances.md "../APIReference/DescribeDBInstances.md") API operation.

## Understanding Domain

membership

After you create or modify your DB instance, the instance becomes a member of the
domain. The AWS console indicates the status of the domain membership for the DB
instance. The status of the DB instance can be one of the following:

- **joined** – The instance is a member of the domain.
- **joining** – The instance is in the process of becoming a member of the
  domain.
- **pending-join** – The instance membership is pending.
- **pending-maintenance-join** – AWS will attempt to make the instance a member of
  the domain during the next scheduled maintenance window.
- **pending-removal** – The removal of the instance from the domain is
  pending.
- **pending-maintenance-removal** – AWS will attempt to remove the instance from
  the domain during the next scheduled maintenance window.
- **failed** – A configuration problem has prevented the instance from joining the
  domain. Check and fix your configuration before reissuing the instance modify command.
- **removing** – The instance is being removed from the domain.

A request to become a member of a domain can fail because of a network connectivity issue or an incorrect IAM role. For example,
you might create a DB instance or modify an existing instance and have the attempt fail for the DB instance to become a
member of a domain. In this case, either reissue the command to create or modify the DB instance or modify the newly created
instance to join the domain.
