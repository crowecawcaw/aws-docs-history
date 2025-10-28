# elasticache-supported-engine-version

Checks if ElastiCache clusters are running a version greater or equal to the recommended engine version. The rule is NON_COMPLIANT if the 'EngineVersion' for an ElastiCache cluster is less than the specified recommended version for its given engine.

**Identifier:** ELASTICACHE_SUPPORTED_ENGINE_VERSION

**Resource Types:** AWS::ElastiCache::CacheCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

latestMemcachedVersion
Type: String

The latest recommended engine version for Memcached. Valid values are in semantic versioning (SemVer) format with 3-component number for major, minor, and patch versions (for example, 1.6.6, not 1.6).

latestRedisVersion
Type: String

The latest recommended engine version for Redis. Valid values are in semantic versioning (SemVer) format with 3-component number for major, minor, and patch versions (for example, 7.0.5, not 7.0).

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
