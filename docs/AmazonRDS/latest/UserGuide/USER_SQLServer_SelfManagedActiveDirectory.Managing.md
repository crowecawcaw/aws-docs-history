

# Managing a DB instance in a self-managed Active Directory Domain
<a name="USER_SQLServer_SelfManagedActiveDirectory.Managing"></a>

 You can use the console, AWS CLI, or the Amazon RDS API to manage your DB instance and its relationship with your self-managed AD domain. For example, you can move the DB instance into, out of, or between domains. 

 For example, using the Amazon RDS API, you can do the following: 
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
+ To list self-managed AD domain membership for each DB instance, use the [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/DescribeDBInstances.html) API operation.