

# Remediating exposures for GCP Cloud SQL instances

AWS Security Hub can generate exposure findings for GCP Cloud SQL instances.

On the Security Hub console, the GCP Cloud SQL instance involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the `GetFindingsV2` operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Google Cloud resources. 

**Contents**
+ [Misconfiguration traits for GCP Cloud SQL instances](#gcp-sql-misconfiguration)
  + [The Cloud SQL instance has public network access enabled](#public-network-access-enabled)
  + [The Cloud SQL instance has automated backups disabled](#automated-backups-disabled)
  + [The Cloud SQL instance has deletion protection disabled](#deletion-protection-disabled)
  + [The Cloud SQL instance has IAM database authentication disabled](#iam-database-authentication-disabled)

## Misconfiguration traits for GCP Cloud SQL instances
<a name="gcp-sql-misconfiguration"></a>

Here are misconfiguration traits for GCP Cloud SQL instances and suggested remediation steps.

### The Cloud SQL instance has public network access enabled
<a name="public-network-access-enabled"></a><a name="sql-server-public-network-access"></a>

 The Cloud SQL instance has a public IP address. A public IP address exposes the database endpoint to the internet, so authorized networks and database credentials become the main barriers to unauthorized access. Following standard security principles, use private IP for your Cloud SQL instances, and turn off public IP. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Move to private IP and turn off public IP**  
 Configure the instance to use private IP, and then turn off public IP. Adding private IP to an existing instance restarts it. Before you turn off public IP, move clients that use the public address to private IP. For more information, see [Configure private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access) and [Configure public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) on the Google Cloud website. 

**Limit authorized networks as an interim measure**  
 While you move the instance to private IP, limit its authorized networks to the specific address ranges that need access. This reduces exposure, but the trait remains until you turn off public IP. For more information, see [Configure public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) on the Google Cloud website. 

### The Cloud SQL instance has automated backups disabled
<a name="automated-backups-disabled"></a>

 The Cloud SQL instance has automated backups turned off. Without automated backups, you might not be able to restore data after an accidental deletion, a failed migration, or a ransomware attack. Following data protection best practices, turn on automated backups for your Cloud SQL instances. 

**Remediation: Turn on automated backups**  
 Turn on automated backups for the instance, and schedule the backup window for a low-traffic period. We also recommend turning on point-in-time recovery. For more information, see [Manage standard backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-standard-backups) on the Google Cloud website. 

### The Cloud SQL instance has deletion protection disabled
<a name="deletion-protection-disabled"></a>

 Deletion protection prevents accidental deletion of a Cloud SQL instance. When it's off, anyone with permission to delete instances can delete the instance and all its data in one operation, even by mistake. Following data protection best practices, turn on deletion protection for your Cloud SQL instances. 

**Remediation: Turn on deletion protection**  
 Turn on deletion protection for the instance. Automation that deletes and re-creates instances, such as in test environments, fails while deletion protection is on. For more information, see [Prevent deletion of an instance](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection) on the Google Cloud website. 

### The Cloud SQL instance has IAM database authentication disabled
<a name="iam-database-authentication-disabled"></a>

 Identity and Access Management (IAM) database authentication lets IAM principals sign in to the database with an access token instead of a password. When it's off, only built-in database users with static passwords can sign in, and you can't revoke their access through IAM. Following standard security principles, turn on IAM database authentication for your Cloud SQL instances. 

**Remediation: Turn on IAM database authentication**  
 Set the instance's IAM authentication database flag to `on`, and then add IAM users or groups to the instance. Built-in database users can still sign in with passwords, so remove any that you no longer need. For more information, see [IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication) for MySQL and [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication) for PostgreSQL on the Google Cloud website. 