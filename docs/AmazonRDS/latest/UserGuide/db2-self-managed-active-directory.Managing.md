

# Managing a DB instance in a self-managed Active Directory domain
<a name="db2-self-managed-active-directory.Managing"></a>

You can use the AWS Management Console, AWS CLI, or the Amazon RDS API to manage your DB instance and its relationship with your self-managed AD domain. For example, you can move the DB instance into, out of, or between domains.

Using the Amazon RDS API, you can:
+ To reattempt a self-managed domain join for a failed membership, use the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) API operation and specify the same set of parameters:
  + `--domain-fqdn`
  + `--domain-dns-ips`
  + `--domain-ou`
  + `--domain-auth-secret-arn`
+ To remove a DB instance from a self-managed domain, use the `ModifyDBInstance` API operation and specify `--disable-domain` for the domain parameter.
+ To move a DB instance from one self-managed domain to another, use the `ModifyDBInstance` API operation and specify the domain parameters for the new domain:
  + `--domain-fqdn`
  + `--domain-dns-ips`
  + `--domain-ou`
  + `--domain-auth-secret-arn`
+ To list self-managed AD domain membership for each DB instance, use the [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) API operation.

## Understanding self-managed Active Directory domain membership
<a name="db2-self-managed-active-directory.Understanding"></a>

After you create or modify your DB instance while specifying AD details, the instance becomes a member of the self-managed AD domain. The AWS console indicates the status of the self-managed Active Directory domain membership for the DB instance. The status of the DB instance can be one of the following:
+ **joined** – The instance is a member of the AD domain.
+ **joining** – The instance is in the process of becoming a member of the AD domain.
+ **pending-join** – The instance membership is pending.
+ **pending-maintenance-join** – AWS attempts to make the instance a member of the AD domain during the next scheduled maintenance window.
+ **pending-removal** – The removal of the instance from the AD domain is pending.
+ **pending-maintenance-removal** – AWS attempts to remove the instance from the AD domain during the next scheduled maintenance window.
+ **failed** – A configuration problem has prevented the instance from joining the AD domain. Check and fix your configuration before reissuing the instance modify command.
+ **removing** – The instance is being removed from the self-managed AD domain.

**Important**  
A request to become a member of a self-managed AD domain can fail because of a network connectivity issue. For example, you might create a DB instance or modify an existing instance and have the attempt fail for the DB instance to become a member of a self-managed AD domain. In this case, either reissue the command to create or modify the DB instance or modify the newly created instance to join the self-managed AD domain.