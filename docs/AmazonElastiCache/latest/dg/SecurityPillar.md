# Amazon ElastiCache Well-Architected Lens Security Pillar

The security pillar focuses on protecting information and systems. Key topics include
confidentiality and integrity of data, identifying and managing who can do what with
privilege-based management, protecting systems, and establishing controls to detect
security events.

###### Topics

- [SEC 1: What steps are you taking in controlling authorized access to ElastiCache data?](#SecurityPillarSEC1 "#SecurityPillarSEC1")
- [SEC 2: Do your applications require additional authorization to ElastiCache over and above networking-based controls?](#SecurityPillarSEC2 "#SecurityPillarSEC2")
- [SEC 3: Is there a risk that commands can be executed inadvertently, causing data loss or failure?](#SecurityPillarSEC3 "#SecurityPillarSEC3")
- [SEC 4: How do you ensure data encryption at rest with ElastiCache](#SecurityPillarSEC4 "#SecurityPillarSEC4")
- [SEC 5: How do you encrypt in-transit data with ElastiCache?](#SecurityPillarSEC5 "#SecurityPillarSEC5")
- [SEC 6: How do you restrict access to control plane resources?](#SecurityPillarSEC6 "#SecurityPillarSEC6")
- [SEC 7: How do you detect and respond to security events?](#SecurityPillarSEC7 "#SecurityPillarSEC7")

## SEC 1: What steps are you taking in controlling authorized access to ElastiCache data?

**Question-level introduction:** All ElastiCache
clusters are designed to be accessed from Amazon Elastic Compute Cloud instances in a VPC, serverless
functions (AWS Lambda), or containers (Amazon Elastic Container Service). The most
encountered scenario is to access an ElastiCache cluster from an Amazon Elastic Compute Cloud instance
within the same Amazon Virtual Private Cloud (Amazon Virtual Private Cloud). Before you can connect to
a cluster from an Amazon EC2 instance, you must authorize the Amazon EC2 instance to access
the cluster. To access an ElastiCache cluster running in a VPC, it is necessary to grant
network ingress to the cluster.

**Question-level benefit:** Network ingress into the
cluster is controlled via VPC security groups. A security group acts as a virtual
firewall for your Amazon EC2 instances to control incoming and outgoing traffic. Inbound
rules control the incoming traffic to your instance, and outbound rules control the
outgoing traffic from your instance. In the case of ElastiCache, when launching a
cluster, it requires associating a security group. This ensures that inbound and
outbound traffic rules are in place for all nodes that make up the cluster.
Additionally, ElastiCache is configured to deploy on private subnets exclusively
such that they are only accessible from via the VPC’s private networking.

- **[Required]** The security group associated
  with your cluster controls network ingress and access to the cluster. By
  default, a security group will not have any inbound rules defined and,
  therefore, no ingress path to ElastiCache. To enable this, configure an
  inbound rule on the security group specifying source IP address/range, TCP
  type traffic and the port for your ElastiCache cluster (default port 6379
  for ElastiCache for Valkey and Redis OSS for example). While it is possible to allow a very
  broad set of ingress sources, like all resources within a VPC (0.0.0.0/0),
  it is advised to be as granular as possible in defining the inbound rules
  such as authorizing only inbound access to Valkey or Redis OSS clients running on Amazon
  Amazon EC2 instances associated with a specific security group.

**[Resources]:**

    + [Subnets and subnet groups](SubnetGroups.md "SubnetGroups.md")
    + [Accessing your cluster or replication group](accessing-elasticache.md "accessing-elasticache.md")
    + [Control traffic to resources using security
     groups](../../../vpc/latest/userguide/vpc-security-groups.md#DefaultSecurityGroupdefault%20security%20group "../../../vpc/latest/userguide/vpc-security-groups.md#DefaultSecurityGroupdefault%20security%20group")
    + [Amazon Elastic Compute Cloud security groups for Linux instances](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#creating-your-own-security-groups "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#creating-your-own-security-groups")

- **[Required]** AWS Identity and Access Management policies can be
  assigned to AWS Lambda functions allowing them to access ElastiCache data. To
  enable this feature, create an IAM execution role with the
  `AWSLambdaVPCAccessExecutionRole` permission, then assign the
  role to the AWS Lambda function.

**[Resources]:** Configuring a Lambda function
to access Amazon ElastiCache in an Amazon VPC: [Tutorial:
Configuring a Lambda function to access Amazon ElastiCache in an Amazon
VPC](../../../lambda/latest/dg/services-elasticache-tutorial.md "../../../lambda/latest/dg/services-elasticache-tutorial.md")

## SEC 2: Do your applications require additional authorization to ElastiCache over and above networking-based controls?

**Question-level introduction:** In scenarios where
it is necessary to restrict or control access to clusters at
an individual client level, it is recommended to authenticate via the AUTH command.
ElastiCache authentication tokens, with optional
user and user group management, enable ElastiCache to require a password
before allowing clients to run commands and access keys, thereby improving data
plane security.

**Question-level benefit:** To help keep your data
secure, ElastiCache provides mechanisms to safeguard against unauthorized
access of your data. This includes enforcing Role-Based Access Control (RBAC) AUTH,
or AUTH token (password) be used by clients to connect to ElastiCache before
performing authorized commands.

- **[Best]** For ElastiCache version 6.x and
  higher for Redis OSS, and ElastiCache version 7.2 and higher for Valkey, define authentication and authorization controls by defining user
  groups, users, and access strings. Assign users to user groups, then assign
  user groups to clusters. To utilize RBAC, it must be selected upon cluster
  creation, and in-transit encryption must be enabled. Ensure you are using a
  Valkey or Redis OSS client that supports TLS to be able to leverage RBAC.

**[Resources]:**

    + [Applying RBAC to a Replication Group for ElastiCache](Clusters.md#rbac-using "Clusters.md#rbac-using")
    + [Specifying Permissions Using an Access String](Clusters.md#Access-string "Clusters.md#Access-string")
    + [ACL](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/")
    + [Supported ElastiCache versions](VersionManagement.md#supported-engine-versions "VersionManagement.md#supported-engine-versions")

- **[Best]** For ElastiCache versions
  prior to 6.x for Redis OSS, in addition to setting strong token/password and maintaining a
  strict password policy for AUTH, it is best practice
  to rotate the password/token. ElastiCache can manage up to two (2)
  authentication tokens at any given time. You can also modify the cluster to
  explicitly require the use of authentication tokens.

**[Resources]:** [Modifying the AUTH token on an existing ElastiCache
cluster](auth.md#auth-modifyng-token "auth.md#auth-modifyng-token")

## SEC 3: Is there a risk that commands can be executed inadvertently, causing data loss or failure?

**Question-level introduction:** There are a number
of Valkey or Redis OSS commands that can have adverse impacts on operations if executed by mistake
or by malicious actors. These commands can have un-intended consequences from a
performance and data safety perspective. For example a developer may routinely call
the FLUSHALL command in a dev environment, and due to a mistake may inadvertently
attempt to call this command on a production system, resulting in accidental data
loss.

**Question-level benefit:** Beginning with
ElastiCache version 5.0.3 for Redis OSS, you have the ability to rename certain
commands that might be disruptive to your workload. Renaming the commands can help
prevent them from being inadvertently executed on the cluster.

- **[Required]**

**[Resources]:**

    + [ElastiCache version 5.0.3 for Redis OSS (deprecated, use version
     5.0.6)](engine-versions.md#redis-version-5-0.3 "engine-versions.md#redis-version-5-0.3")
    + [ElastiCache version 5.0.3 for Redis OSS parameter changes](ParameterGroups.md#ParameterGroups.Redis.5-0-3 "ParameterGroups.md#ParameterGroups.Redis.5-0-3")
    + [Redis OSS security](https://redis.io/docs/management/security/ "https://redis.io/docs/management/security/")

## SEC 4: How do you ensure data encryption at rest with ElastiCache

**Question-level introduction:** While ElastiCache is an in-memory data store, it is possible to encrypt any data that may be
persisted (on storage) as part of standard operations of the cluster. This includes
both scheduled and manual backups written to Amazon S3, as well as data saved to
disk storage as a result of sync and swap operations. Instance types in the M6g and
R6g families also feature always-on, in-memory encryption.

**Question-level benefit:** ElastiCache
provides optional encryption at-rest to increase data security.

- **[Required]** At-rest encryption can be
  enabled on an ElastiCache cluster (replication group) only when it is
  created. An existing cluster cannot be modified to begin encrypting data
  at-rest. By default, ElastiCache will provide and manage the keys used in
  at-rest encryption.

**[Resources]:**

    + [At-Rest Encryption Constraints](at-rest-encryption.md#at-rest-encryption-constraints "at-rest-encryption.md#at-rest-encryption-constraints")
    + [Enabling At-Rest Encryption](at-rest-encryption.md#at-rest-encryption-enable "at-rest-encryption.md#at-rest-encryption-enable")

- **[Best]** Leverage Amazon EC2 instance types that
  encrypt data while it is in memory (such as M6g or R6g). Where possible,
  consider managing your own keys for at-rest encryption. For more stringent
  data security environments, AWS Key Management Service (KMS) can be used to self-manage
  Customer Master Keys (CMK). Through ElastiCache integration with AWS Key Management Service,
  you are able to create, own, and manage the keys used for encryption of data
  at rest for your ElastiCache cluster.

**[Resources]:**

    + [Using customer managed keys from AWS Key Management Service](at-rest-encryption.md#using-customer-managed-keys-for-elasticache-security "at-rest-encryption.md#using-customer-managed-keys-for-elasticache-security")
    + [AWS Key
     Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
    + [AWS
     KMS concepts](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys")

## SEC 5: How do you encrypt in-transit data with ElastiCache?

**Question-level introduction:** It is a common
requirement to mitigate against data being compromised while in transit. This
represents data within components of a distributed system, as well as between
application clients and cluster nodes. ElastiCache supports this
requirement by allowing for encrypting data in-transit between clients and cluster,
and between cluster nodes themselves. Instance types in the M6g and R6g families
also feature always-on, in-memory encryption.

**Question-level benefit:** Amazon ElastiCache in-transit
encryption is an optional feature that allows you to increase the security of your
data at its most vulnerable points, when it is in-transit from one location to
another.

- **[Required]** In-transit encryption can only
  be enabled on a cluster (replication group) upon
  creation. Please note that, due to the additional processing required for
  encrypting/decrypting data, implementing in-transit encryption will have
  some performance impact. To understand the impact, it is recommended to
  benchmark your workload before and after enabling
  encryption-in-transit.

**[Resources]:**

    + [In-transit encryption overview](in-transit-encryption.md#in-transit-encryption-overview "in-transit-encryption.md#in-transit-encryption-overview")

## SEC 6: How do you restrict access to control plane resources?

**Question-level introduction:** IAM policies and ARN
enable fine grained access controls for ElastiCache for Valkey and Redis OSS, allowing for tighter
control to manage the creation, modification and deletion of
clusters.

**Question-level benefit:** Management of Amazon
ElastiCache resources, such as replication groups, nodes, etc. can be constrained to
AWS accounts that have specific permissions based on IAM policies, improving
security and reliability of resources.

- **[Required]** Manage access to Amazon
  ElastiCache resources by assigning specific AWS Identity and Access Managementpolicies to AWS
  users, allowing finer control over which accounts can perform what actions
  on clusters.

**[Resources]:**

    + [Overview
     of managing access permissions to your ElastiCache
     resources](IAM.md "IAM.md")
    + [Using identity-based policies (IAM policies) for Amazon
     ElastiCache](IAM.md "IAM.md")

## SEC 7: How do you detect and respond to security events?

**Question-level introduction:** ElastiCache, when
deployed with RBAC enabled, exports CloudWatch metrics to notify users of security
events. These metrics help identify failed attempts to authenticate, access keys, or
run commands that connecting RBAC users are not authorized for.

Additionally, AWS products and services resources help secure your overall workload by
automating deployments and logging all actions and modifications for later
review/audit.

**Question-level benefit:** By monitoring events, you
enable your organization to respond according to your requirements, policies, and
procedures. Automating the monitoring and responses to these security events hardens
your overall security posture.

- **[Required]** Familiarize yourself with the
  CloudWatch Metrics published that pertain to RBAC authentication and
  authorization failures.

      + AuthenticationFailures = Failed attempts to authenticate to
       Valkey or Redis OSS
      + KeyAuthorizationFailures = Failed attempts by users to access keys
       without permission
      + CommandAuthorizationFailures = Failed attempts by users to run
       commands without permission

  **[Resources]:**

      + [Metrics for Valkey or Redis OSS](CacheMetrics.md "CacheMetrics.md")

- **[Best]** It is recommended to setup alerts
  and notifications on these metrics and respond as necessary.

**[Resources]:**

    + [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")

- **[Best]** Use the Valkey or Redis OSS ACL LOG command to
  gather further details

**[Resources]:**

    + [ACL LOG](https://valkey.io/commands/acl-log/ "https://valkey.io/commands/acl-log/")

- **[Best]** Familiarize yourself with the
  AWS products and services capabilities as it pertains to monitoring, logging, and
  analyzing ElastiCache deployments and events

**[Resources]:**

    + [Logging Amazon ElastiCache API calls with AWS
     CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
    + [elasticache-redis-cluster-automatic-backup-check](../../../config/latest/developerguide/elasticache-redis-cluster-automatic-backup-check.md "../../../config/latest/developerguide/elasticache-redis-cluster-automatic-backup-check.md")
    + [Monitoring use with CloudWatch Metrics](CacheMetrics.md "CacheMetrics.md")
