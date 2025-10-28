# Data security in Amazon ElastiCache

To help keep your data secure, Amazon ElastiCache and Amazon EC2 provide mechanisms to guard against
unauthorized access of your data on the server.

Amazon ElastiCache for Memcached provides encryption features for data on caches running Memcached versions 1.6.12 or later.

Amazon ElastiCache with Valkey and Redis OSS provides encryption features for data on caches running Valkey 7.2 or later, and Redis OSS versions 3.2.6 (scheduled for EOL, see
[Redis OSS versions end of life schedule](engine-versions.md#deprecated-engine-versions "engine-versions.md#deprecated-engine-versions")), 4.0.10 or later.
Amazon ElastiCache also supports authenticating users with either IAM or Valkey and Redis OSS AUTH, and authorizing user operations using Role-Based Access Control (RBAC).

- In-transit encryption encrypts your data whenever it is moving from one place to another,
  such as between nodes in your cluster or between your cache and your application.
- At-rest encryption encrypts your on-disk data during sync and backup operations.
  ElastiCache supports authenticating users using IAM and the Valkey and Redis OSS AUTH command, and authorizing user operations using Role-Based Access Control (RBAC).

![Image: ElastiCache for Valkey and Redis OSS Security Diagram](images/ElastiCache-Redis-Secure-Compliant.png)
_ElastiCache for Valkey and Redis OSS Security Diagram_

###### Topics

- [ElastiCache in-transit encryption (TLS)](in-transit-encryption.md "in-transit-encryption.md")
- [At-Rest Encryption in ElastiCache](at-rest-encryption.md "at-rest-encryption.md")
- [Authentication and Authorization](auth-redis.md "auth-redis.md")
