# Managing a DB instance in a self-managed Active Directory

Domain

You can use the console, AWS CLI, or the Amazon RDS API to manage your DB instance and its
relationship with your self-managed AD domain. For example, you can move the DB instance into, out of,
or between domains.

For example, using the Amazon RDS API, you can do the following:

- To reattempt a self-managed domain join for a failed membership, use the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") API
  operation and specify the same set of parameters:
  - `--domain-fqdn`
  - `--domain-dns-ips`
  - `--domain-ou`
  - `--domain-auth-secret-arn`

- To remove a DB instance from a self-managed domain, use the `ModifyDBInstance` API operation
  and specify `--disable-domain` for the domain parameter.
- To move a DB instance from one self-managed domain to another, use the `ModifyDBInstance` API operation
  and specify the domain parameters for the new domain:
  - `--domain-fqdn`
  - `--domain-dns-ips`
  - `--domain-ou`
  - `--domain-auth-secret-arn`

- To list self-managed AD domain membership for each DB instance, use the [DescribeDBInstances](../APIReference/DescribeDBInstances.md "../APIReference/DescribeDBInstances.md") API operation.
