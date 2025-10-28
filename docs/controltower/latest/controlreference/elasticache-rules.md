# Amazon ElastiCache controls

###### Topics

- [[CT.ELASTICACHE.PR.1] Require an Amazon ElastiCache (Redis OSS) cluster to have automatic backups activated](#ct-elasticache-pr-1-description "#ct-elasticache-pr-1-description")
- [[CT.ELASTICACHE.PR.2] Require an Amazon ElastiCache (Redis OSS) cluster to have automatic minor version upgrades activated](#ct-elasticache-pr-2-description "#ct-elasticache-pr-2-description")
- [[CT.ELASTICACHE.PR.3] Require an Amazon ElastiCache (Redis OSS) replication group to have automatic failover activated](#ct-elasticache-pr-3-description "#ct-elasticache-pr-3-description")
- [[CT.ELASTICACHE.PR.4] Require an Amazon ElastiCache (Redis OSS) replication group to have encryption at rest activated](#ct-elasticache-pr-4-description "#ct-elasticache-pr-4-description")
- [[CT.ELASTICACHE.PR.5] Require an Amazon ElastiCache (Redis OSS) replication group to have encryption in transit activated](#ct-elasticache-pr-5-description "#ct-elasticache-pr-5-description")
- [[CT.ELASTICACHE.PR.6] Require an Amazon ElastiCache cache cluster to use a custom subnet group](#ct-elasticache-pr-6-description "#ct-elasticache-pr-6-description")
- [[CT.ELASTICACHE.PR.7] Require an Amazon ElastiCache replication group of earlier Redis OSS versions to have Redis OSS AUTH activated](#ct-elasticache-pr-7-description "#ct-elasticache-pr-7-description")
- [[CT.ELASTICACHE.PR.8] Require an Amazon ElastiCache replication group of later Redis OSS versions to have RBAC authentication activated](#ct-elasticache-pr-8-description "#ct-elasticache-pr-8-description")

## [CT.ELASTICACHE.PR.1] Require an Amazon ElastiCache (Redis OSS) cluster to have automatic backups activated

This control checks whether an Amazon ElastiCache (Redis OSS) cluster has automatic backups enabled.

- **Control objective:** Improve resiliency
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::ElastiCache::CacheCluster`
- **AWS CloudFormation guard rule:**
  [CT.ELASTICACHE.PR.1 rule specification](#ct-elasticache-pr-1-rule "#ct-elasticache-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.ELASTICACHE.PR.1 rule specification](#ct-elasticache-pr-1-rule "#ct-elasticache-pr-1-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.ELASTICACHE.PR.1 example templates](#ct-elasticache-pr-1-templates "#ct-elasticache-pr-1-templates")

**Explanation**

When automatic backups are enabled, Amazon ElastiCache creates a backup of the cluster on a daily basis. There is no impact on the cluster, and the change is immediate. Automatic backups can help guard against data loss. In the event of a failure, you can create a new cluster, and restore your data from the most recent backup.

###### Usage considerations

- This control applies only to Amazon ElastiCache cache clusters with an engine type of `redis`

### Remediation for rule failure

Set the value of the `SnapshotRetentionLimit` parameter to an integer value greater than 0.

The examples that follow show how to implement this remediation.

#### Amazon ElastiCache Cache Cluster - Example

An Amazon ElastiCache cache cluster configured with automatic backups enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "CacheCluster": {
        "Type": "AWS::ElastiCache::CacheCluster",
        "Properties": {
            "Engine": "redis",
            "NumCacheNodes": 1,
            "CacheNodeType": "cache.t3.micro",
            "VpcSecurityGroupIds": [
                {
                    "Ref": "SecurityGroup"
                }
            ],
            "CacheSubnetGroupName": {
                "Ref": "SubnetGroup"
            },
            "SnapshotRetentionLimit": 5
        }
    }
}

```

**YAML example**

```

CacheCluster:
  Type: AWS::ElastiCache::CacheCluster
  Properties:
    Engine: redis
    NumCacheNodes: 1
    CacheNodeType: cache.t3.micro
    VpcSecurityGroupIds:
      - !Ref 'SecurityGroup'
    CacheSubnetGroupName: !Ref 'SubnetGroup'
    SnapshotRetentionLimit: 5


```

### CT.ELASTICACHE.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   elasticache_redis_cluster_auto_backup_check
#
# Description:
#   This control checks whether an Amazon ElastiCache (Redis OSS) cluster has automatic backups enabled.
#
# Reports on:
#   AWS::ElastiCache::CacheCluster
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any ElastiCache cache cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache CacheCluster resource
#       And: 'Engine' has not been provided or has been provided and is not set to 'redis'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cache cluster resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'SnapshotRetentionLimit' has not been provided
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cache cluster resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'SnapshotRetentionLimit' has been provided and set to a non-integer value or an integer value of 0
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cache cluster resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'SnapshotRetentionLimit' has been provided and set to an integer value greater than 0
#      Then: PASS

#
# Constants
#
let ELASTICACHE_CACHE_CLUSTER_TYPE = "AWS::ElastiCache::CacheCluster"
let REDIS_ENGINE_TYPE = "redis"
let INPUT_DOCUMENT = this

#
# Assignments
#
let elasticache_clusters = Resources.*[ Type == %ELASTICACHE_CACHE_CLUSTER_TYPE ]

#
# Primary Rules
#
rule elasticache_redis_cluster_auto_backup_check when is_cfn_template(%INPUT_DOCUMENT)
                                                      %elasticache_clusters not empty {
    check(%elasticache_clusters.Properties)
        <<
        [CT.ELASTICACHE.PR.1]: Require an Amazon ElastiCache (Redis OSS) cluster to have automatic backups activated
        [FIX]: Set the value of the 'SnapshotRetentionLimit' parameter to an integer value greater than 0.
        >>
}

rule elasticache_redis_cluster_auto_backup_check when is_cfn_hook(%INPUT_DOCUMENT, %ELASTICACHE_CACHE_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%ELASTICACHE_CACHE_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.ELASTICACHE.PR.1]: Require an Amazon ElastiCache (Redis OSS) cluster to have automatic backups activated
        [FIX]: Set the value of the 'SnapshotRetentionLimit' parameter to an integer value greater than 0.
        >>
}

#
# Parameterized Rules
#
rule check(elasticache_cache_cluster) {
    %elasticache_cache_cluster [
        # Scenario 2
        Engine exists
        Engine == %REDIS_ENGINE_TYPE
    ] {
        # Scenarios 3, 4 and 5
        SnapshotRetentionLimit exists
        SnapshotRetentionLimit > 0
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.ELASTICACHE.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: test
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Cache Subnet Group
      SubnetIds:
      - Ref: Subnet
  CacheCluster:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      Engine: redis
      NumCacheNodes: 1
      CacheNodeType: cache.t3.micro
      VpcSecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      SnapshotRetentionLimit: 5


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: test
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Cache Subnet Group
      SubnetIds:
      - Ref: Subnet
  CacheCluster:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      Engine: redis
      NumCacheNodes: 1
      CacheNodeType: cache.t3.micro
      VpcSecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      SnapshotRetentionLimit: 0


```

## [CT.ELASTICACHE.PR.2] Require an Amazon ElastiCache (Redis OSS) cluster to have automatic minor version upgrades activated

This control checks whether an Amazon ElastiCache (Redis OSS) cluster has automatic minor version upgrades enabled.

- **Control objective:** Manage vulnerabilities
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::ElastiCache::CacheCluster`
- **AWS CloudFormation guard rule:**
  [CT.ELASTICACHE.PR.2 rule specification](#ct-elasticache-pr-2-rule "#ct-elasticache-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.ELASTICACHE.PR.2 rule specification](#ct-elasticache-pr-2-rule "#ct-elasticache-pr-2-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:

[CT.ELASTICACHE.PR.2 example templates](#ct-elasticache-pr-2-templates "#ct-elasticache-pr-2-templates")

**Explanation**

By enabling automatic minor version upgrades, you ensure that the latest minor version updates to Amazon ElastiCache cache clusters are installed.
These upgrades may include security patches and bug fixes. Keeping up to date with patch installation is an important step in securing
systems.

###### Usage considerations

- This control applies only to Amazon ElastiCache cache clusters with an engine type of `redis` and an engine version of
  6.0 or later.

### Remediation for rule failure

Set the value of the `AutoMinorVersionUpgrade` parameter to true.

The examples that follow show how to implement this remediation.

#### Amazon ElastiCache Cache Cluster - Example

An Amazon ElastiCache cache cluster configured with automatic minor version upgrades enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "ElastCacheCacheCluster": {
        "Type": "AWS::ElastiCache::CacheCluster",
        "Properties": {
            "CacheNodeType": "cache.t3.micro",
            "NumCacheNodes": "1",
            "VpcSecurityGroupIds": [
                {
                    "Fn::GetAtt": [
                        "SecurityGroup",
                        "GroupId"
                    ]
                }
            ],
            "Engine": "redis",
            "EngineVersion": 6.0,
            "AutoMinorVersionUpgrade": true
        }
    }
}

```

**YAML example**

```

ElastCacheCacheCluster:
  Type: AWS::ElastiCache::CacheCluster
  Properties:
    CacheNodeType: cache.t3.micro
    NumCacheNodes: '1'
    VpcSecurityGroupIds:
      - !GetAtt 'SecurityGroup.GroupId'
    Engine: redis
    EngineVersion: 6.0
    AutoMinorVersionUpgrade: true


```

### CT.ELASTICACHE.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   elasticache_auto_minor_version_upgrade_check
#
# Description:
#   This control checks whether an Amazon ElastiCache (Redis OSS) cluster has automatic minor version upgrades enabled.
#
# Reports on:
#   AWS::ElastiCache::CacheCluster
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any ElastiCache cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cluster resource
#       And: 'Engine' has not been provided or has been provided and is not set to 'redis'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cluster resource
#       And: 'Engine' has been provided and is set to 'redis'
#       And: 'EngineVersion' has been provided and set to a version less than 6
#      Then: SKIP
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cluster resource
#       And: 'Engine' has been provided and is set to 'redis'
#       And: 'EngineVersion' has not been provided or 'EngineVersion' has been provided and set
#            to a version greater than or equal to 6
#       And: 'AutoMinorVersionUpgrade' has not been provided
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cluster resource
#       And: 'Engine' has been provided and is set to 'redis'
#       And: 'EngineVersion' has not been provided or 'EngineVersion' has been provided and set
#            to a version greater than or equal to 6
#       And: 'AutoMinorVersionUpgrade' has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cluster resource
#       And: 'Engine' has been provided and is set to 'redis'
#       And: 'EngineVersion' has not been provided or 'EngineVersion' has been provided and set
#            to a version greater than or equal to 6
#       And: 'AutoMinorVersionUpgrade' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let ELASTICACHE_CLUSTER_TYPE = "AWS::ElastiCache::CacheCluster"
let INPUT_DOCUMENT = this
let REDIS_ENGINE_TYPE = "redis"
let UNSUPPORTED_REDIS_ENGINE_VERSIONS_FOR_AUTO_UPGRADE = [
    /^2\./,
    /^3\./,
    /^4\./,
    /^5\./
]

#
# Assignments
#
let elasticache_clusters = Resources.*[ Type == %ELASTICACHE_CLUSTER_TYPE ]

#
# Primary Rules
#
rule elasticache_auto_minor_version_upgrade_check when is_cfn_template(%INPUT_DOCUMENT)
                                                       %elasticache_clusters not empty {
    check(%elasticache_clusters.Properties)
        <<
        [CT.ELASTICACHE.PR.2]: Require an Amazon ElastiCache (Redis OSS) cluster to have automatic minor version upgrades activated
        [FIX]: Set the value of the 'AutoMinorVersionUpgrade' parameter to true.
        >>
}

rule elasticache_auto_minor_version_upgrade_check when is_cfn_hook(%INPUT_DOCUMENT, %ELASTICACHE_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%ELASTICACHE_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.ELASTICACHE.PR.2]: Require an Amazon ElastiCache (Redis OSS) cluster to have automatic minor version upgrades activated
        [FIX]: Set the value of the 'AutoMinorVersionUpgrade' parameter to true.
        >>
}

#
# Parameterized Rules
#
rule check(elasticache_clusters) {
    %elasticache_clusters [
        # Scenario 2
        Engine exists
        Engine == %REDIS_ENGINE_TYPE

        # Scenario 3
        EngineVersion not exists or
        EngineVersion not in %UNSUPPORTED_REDIS_ENGINE_VERSIONS_FOR_AUTO_UPGRADE
    ] {
        # Scenario 4, 5 and 6
        AutoMinorVersionUpgrade exists
        AutoMinorVersionUpgrade == true
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.ELASTICACHE.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 11211
        ToPort: 11211
        CidrIp: 10.0.0.0/24
  ElastCacheCacheCluster:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      CacheNodeType: cache.t3.micro
      NumCacheNodes: '1'
      VpcSecurityGroupIds:
      - Fn::GetAtt:
        - SecurityGroup
        - GroupId
      Engine: redis
      AutoMinorVersionUpgrade: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 11211
        ToPort: 11211
        CidrIp: 10.0.0.0/24
  ElastCacheCacheCluster:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      CacheNodeType: cache.t3.micro
      NumCacheNodes: '1'
      VpcSecurityGroupIds:
      - Fn::GetAtt:
        - SecurityGroup
        - GroupId
      Engine: redis
      AutoMinorVersionUpgrade: false


```

## [CT.ELASTICACHE.PR.3] Require an Amazon ElastiCache (Redis OSS) replication group to have automatic failover activated

This control checks whether an Amazon ElastiCache (Redis OSS) replication group has automatic failover enabled.

- **Control objective:** Improve resiliency
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::ElastiCache::ReplicationGroup`
- **AWS CloudFormation guard rule:**
  [CT.ELASTICACHE.PR.3 rule specification](#ct-elasticache-pr-3-rule "#ct-elasticache-pr-3-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.ELASTICACHE.PR.3 rule specification](#ct-elasticache-pr-3-rule "#ct-elasticache-pr-3-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.ELASTICACHE.PR.3 example templates](#ct-elasticache-pr-3-templates "#ct-elasticache-pr-3-templates")

**Explanation**

When automatic failover is enabled for a replication group, the role of primary node will fail over to one of the read replicas, automatically. This failover and replica promotion ensure that you can resume writing to the new primary as soon as promotion is complete, thereby reducing overall downtime in case of failure.

### Remediation for rule failure

Set the value of the `AutomaticFailoverEnabled` parameter to true.

The examples that follow show how to implement this remediation.

#### Amazon ElastiCache Replication Group - Example

An Amazon ElastiCache replication group configured with automatic failover enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "ReplicationGroup": {
        "Type": "AWS::ElastiCache::ReplicationGroup",
        "Properties": {
            "ReplicationGroupDescription": "Sample replication group",
            "CacheNodeType": "cache.t3.micro",
            "SecurityGroupIds": [
                {
                    "Ref": "SecurityGroup"
                }
            ],
            "CacheSubnetGroupName": {
                "Ref": "SubnetGroup"
            },
            "NumCacheClusters": 2,
            "Engine": "redis",
            "AutomaticFailoverEnabled": true
        }
    }
}

```

**YAML example**

```

ReplicationGroup:
  Type: AWS::ElastiCache::ReplicationGroup
  Properties:
    ReplicationGroupDescription: Sample replication group
    CacheNodeType: cache.t3.micro
    SecurityGroupIds:
      - !Ref 'SecurityGroup'
    CacheSubnetGroupName: !Ref 'SubnetGroup'
    NumCacheClusters: 2
    Engine: redis
    AutomaticFailoverEnabled: true


```

### CT.ELASTICACHE.PR.3 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   elasticache_repl_grp_backup_enabled_check
#
# Description:
#   This control checks whether an Amazon ElastiCache (Redis OSS) replication group has automatic failover enabled.
#
# Reports on:
#   AWS::ElastiCache::ReplicationGroup
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any ElastiCache replication group resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache replication group resource
#       And: 'Engine' has not been provided or has been provided and is not set to 'redis'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache replication group resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'AutomaticFailoverEnabled' has not been provided
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache replication group resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'AutomaticFailoverEnabled' has been provided and is set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache replication group resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'AutomaticFailoverEnabled' has been provided and is set to a value of bool(true)
#      Then: PASS

#
# Constants
#
let ELASTICACHE_REPLICATION_GROUP_TYPE = "AWS::ElastiCache::ReplicationGroup"
let REDIS_ENGINE_TYPE = "redis"
let INPUT_DOCUMENT = this

#
# Assignments
#
let elasticache_replication_groups = Resources.*[ Type == %ELASTICACHE_REPLICATION_GROUP_TYPE ]

#
# Primary Rules
#
rule elasticache_repl_grp_auto_failover_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                                           %elasticache_replication_groups not empty {
    check(%elasticache_replication_groups.Properties)
        <<
        [CT.ELASTICACHE.PR.3]: Require an Amazon ElastiCache (Redis OSS) replication group to have automatic failover activated
        [FIX]: Set the value of the 'AutomaticFailoverEnabled' parameter to true.
        >>
}

rule elasticache_repl_grp_auto_failover_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %ELASTICACHE_REPLICATION_GROUP_TYPE) {
    check(%INPUT_DOCUMENT.%ELASTICACHE_REPLICATION_GROUP_TYPE.resourceProperties)
        <<
        [CT.ELASTICACHE.PR.3]: Require an Amazon ElastiCache (Redis OSS) replication group to have automatic failover activated
        [FIX]: Set the value of the 'AutomaticFailoverEnabled' parameter to true.
        >>
}

#
# Parameterized Rules
#
rule check(elasticache_replication_group) {
    %elasticache_replication_group [
        # Scenario 2
        Engine exists
        Engine == %REDIS_ENGINE_TYPE
    ] {
        # Scenarios 3, 4 and 5
        AutomaticFailoverEnabled exists
        AutomaticFailoverEnabled == true
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.ELASTICACHE.PR.3 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Example subnet group
      SubnetIds:
      - Ref: Subnet
  ReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription:
        Fn::Sub: ${AWS::StackName}-example
      CacheNodeType: cache.t3.micro
      SecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      NumCacheClusters: 2
      Engine: redis
      AutomaticFailoverEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Example subnet group
      SubnetIds:
      - Ref: Subnet
  ReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription:
        Fn::Sub: ${AWS::StackName}-example
      CacheNodeType: cache.t3.micro
      SecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      NumCacheClusters: 2
      Engine: redis
      AutomaticFailoverEnabled: false


```

## [CT.ELASTICACHE.PR.4] Require an Amazon ElastiCache (Redis OSS) replication group to have encryption at rest activated

This control checks whether an Amazon ElastiCache (Redis OSS) replication group has the encryption-at-rest setting enabled.

- **Control objective:** Encrypt data at rest
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::ElastiCache::ReplicationGroup`
- **AWS CloudFormation guard rule:**
  [CT.ELASTICACHE.PR.4 rule specification](#ct-elasticache-pr-4-rule "#ct-elasticache-pr-4-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.ELASTICACHE.PR.4 rule specification](#ct-elasticache-pr-4-rule "#ct-elasticache-pr-4-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.ELASTICACHE.PR.4 example templates](#ct-elasticache-pr-4-templates "#ct-elasticache-pr-4-templates")

**Explanation**

Encryption of data at rest is a recommended best practice that adds a layer of access management around your data. In case of any compromise to your Amazon ElastiCache replica nodes, this encryption-at-rest setting ensures that your data is protected from unintended access.

###### Usage considerations

- This control requires the use of encryption at rest, which is supported only for replication groups with Redis OSS engine versions of 3.2.6 or above.

### Remediation for rule failure

Set the value of the `AtRestEncryptionEnabled` parameter to true.

The examples that follow show how to implement this remediation.

#### Amazon ElastiCache Replication Group - Example

Amazon ElastiCache replication group configured with encryption at rest enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "ElastiCacheReplicationGroup": {
        "Type": "AWS::ElastiCache::ReplicationGroup",
        "Properties": {
            "CacheSubnetGroupName": {
                "Ref": "SubnetGroup"
            },
            "CacheNodeType": "cache.t3.medium",
            "NumCacheClusters": 2,
            "Engine": "redis",
            "ReplicationGroupDescription": "Sample replication group",
            "AtRestEncryptionEnabled": true
        }
    }
}

```

**YAML example**

```

ElastiCacheReplicationGroup:
  Type: AWS::ElastiCache::ReplicationGroup
  Properties:
    CacheSubnetGroupName: !Ref 'SubnetGroup'
    CacheNodeType: cache.t3.medium
    NumCacheClusters: 2
    Engine: redis
    ReplicationGroupDescription: Sample replication group
    AtRestEncryptionEnabled: true


```

### CT.ELASTICACHE.PR.4 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   elasticache_repl_grp_encrypted_at_rest_check
#
# Description:
#   This control checks whether an Amazon ElastiCache replication group has the encryption-at-rest setting enabled.
#
# Reports on:
#   AWS::ElastiCache::ReplicationGroup
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#  Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any ElastiCache ReplicationGroup resources
#      Then: SKIP
#  Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache ReplicationGroup resource
#       And: 'Engine' has not been provided or has been provided and is not set to 'redis'
#      Then: SKIP
#  Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache ReplicationGroup resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'AtRestEncryptionEnabled' has not been provided
#      Then: FAIL
#  Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache ReplicationGroup resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'AtRestEncryptionEnabled' has been provided and is set to a value other than bool(true)
#      Then: FAIL
#  Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache ReplicationGroup resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'AtRestEncryptionEnabled' has been provided and is set to a value of bool(true)
#      Then: PASS

#
# Constants
#
let ELASTICACHE_REPLICATION_GROUP_TYPE = "AWS::ElastiCache::ReplicationGroup"
let INPUT_DOCUMENT = this

#
# Assignments
#
let elasticache_replication_groups = Resources.*[ Type == %ELASTICACHE_REPLICATION_GROUP_TYPE ]

#
# Primary Rules
#
rule elasticache_repl_grp_encrypted_at_rest_check when is_cfn_template(%INPUT_DOCUMENT)
                                                       %elasticache_replication_groups not empty {
    check(%elasticache_replication_groups.Properties)
        <<
        [CT.ELASTICACHE.PR.4]: Require an Amazon ElastiCache replication group to have encryption at rest activated
        [FIX]: Set the value of the 'AtRestEncryptionEnabled' parameter to true.
        >>
}

rule elasticache_repl_grp_encrypted_at_rest_check when is_cfn_hook(%INPUT_DOCUMENT, %ELASTICACHE_REPLICATION_GROUP_TYPE) {
    check(%INPUT_DOCUMENT.%ELASTICACHE_REPLICATION_GROUP_TYPE.resourceProperties)
        <<
        [CT.ELASTICACHE.PR.4]: Require an Amazon ElastiCache replication group to have encryption at rest activated
        [FIX]: Set the value of the 'AtRestEncryptionEnabled' parameter to true.
        >>
}

#
# Parameterized Rules
#
rule check(elasticache_replication_group) {
    %elasticache_replication_group [
        # Scenario 2
        filter_elasticache_replication_group(this)
    ] {
        # Scenario 3
        AtRestEncryptionEnabled exists

        # Scenarios 4 and 5
        AtRestEncryptionEnabled == true
    }
}

rule filter_elasticache_replication_group(elasticache_replication_group) {
    %elasticache_replication_group {
        Engine exists
        Engine == "redis"
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.ELASTICACHE.PR.4 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Example subnet group
      SubnetIds:
      - Ref: Subnet
  ElastiCacheReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      CacheSubnetGroupName:
        Ref: SubnetGroup
      CacheNodeType: cache.t3.medium
      NumCacheClusters: 2
      Engine: redis
      ReplicationGroupDescription: Example replication group
      AtRestEncryptionEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Example subnet group
      SubnetIds:
      - Ref: Subnet
  ElastiCacheReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      CacheSubnetGroupName:
        Ref: SubnetGroup
      CacheNodeType: cache.t3.medium
      NumCacheClusters: 2
      Engine: redis
      ReplicationGroupDescription: Example replication group
      AtRestEncryptionEnabled: false


```

## [CT.ELASTICACHE.PR.5] Require an Amazon ElastiCache (Redis OSS) replication group to have encryption in transit activated

This control checks whether an Amazon ElastiCache replication group has encryption-in-transit enabled.

- **Control objective:** Encrypt data in transit
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::ElastiCache::ReplicationGroup`
- **AWS CloudFormation guard rule:**
  [CT.ELASTICACHE.PR.5 rule specification](#ct-elasticache-pr-5-rule "#ct-elasticache-pr-5-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.ELASTICACHE.PR.5 rule specification](#ct-elasticache-pr-5-rule "#ct-elasticache-pr-5-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.ELASTICACHE.PR.5 example templates](#ct-elasticache-pr-5-templates "#ct-elasticache-pr-5-templates")

**Explanation**

TLS can be used to help prevent potential attackers from eavesdropping on or manipulating network traffic using person-in-the-middle or similar attacks. Amazon ElastiCache in-transit encryption is an optional feature that you can use to help protect your data when it is moving from one location to another.

###### Usage considerations

- Encryption-in-transit is supported on Amazon ElastiCache (Redis OSS) replication groups running versions 3.2.6, 4.0.10 and later.
- Because of the processing required to encrypt and decrypt the data at the endpoints, implementing in-transit encryption can reduce performance. We recommend that you benchmark in-transit encryption, compared to no encryption, on your own data, to determine the impact of encryption-in-transit on performance for your implementation.

### Remediation for rule failure

Set the value of the `TransitEncryptionEnabled` parameter to true.

The examples that follow show how to implement this remediation.

#### Amazon ElastiCache Replication Group - Example

Amazon ElastiCache replication group configured with encryption-in-transit enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "ReplicationGroup": {
        "Type": "AWS::ElastiCache::ReplicationGroup",
        "Properties": {
            "ReplicationGroupDescription": "Sample replication group",
            "CacheNodeType": "cache.t3.micro",
            "SecurityGroupIds": [
                {
                    "Ref": "SecurityGroup"
                }
            ],
            "CacheSubnetGroupName": {
                "Ref": "SubnetGroup"
            },
            "NumCacheClusters": 2,
            "Engine": "redis",
            "TransitEncryptionEnabled": true
        }
    }
}

```

**YAML example**

```

ReplicationGroup:
  Type: AWS::ElastiCache::ReplicationGroup
  Properties:
    ReplicationGroupDescription: Sample replication group
    CacheNodeType: cache.t3.micro
    SecurityGroupIds:
      - !Ref 'SecurityGroup'
    CacheSubnetGroupName: !Ref 'SubnetGroup'
    NumCacheClusters: 2
    Engine: redis
    TransitEncryptionEnabled: true


```

### CT.ELASTICACHE.PR.5 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   elasticache_repl_grp_encrypted_in_transit_check
#
# Description:
#   This control checks whether an Amazon ElastiCache replication group has encryption-in-transit enabled.
#
# Reports on:
#   AWS::ElastiCache::ReplicationGroup
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any ElastiCache ReplicationGroup resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache ReplicationGroup resource
#       And: 'Engine' has not been provided or has been provided and is not set to 'redis'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache ReplicationGroup resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'TransitEncryptionEnabled' has not been provided
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache ReplicationGroup resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'TransitEncryptionEnabled' has been provided and set to a value other than bool(true)
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache ReplicationGroup resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'TransitEncryptionEnabled' has been provided and set to bool(true)
#      Then: PASS

#
# Constants
#
let ELASTICACHE_REPLICATION_GROUP_TYPE = "AWS::ElastiCache::ReplicationGroup"
let REDIS_ENGINE_TYPE = "redis"
let INPUT_DOCUMENT = this

#
# Assignments
#
let elasticache_replication_groups = Resources.*[ Type == %ELASTICACHE_REPLICATION_GROUP_TYPE ]

#
# Primary Rules
#
rule elasticache_repl_grp_encrypted_in_transit_check when is_cfn_template(%INPUT_DOCUMENT)
                                                          %elasticache_replication_groups not empty {
    check(%elasticache_replication_groups.Properties)
        <<
        [CT.ELASTICACHE.PR.5]: Require an Amazon ElastiCache (Redis OSS) replication group to have encryption in transit activated
        [FIX]: Set the value of the 'TransitEncryptionEnabled' parameter to true.
        >>
}

rule elasticache_repl_grp_encrypted_in_transit_check when is_cfn_hook(%INPUT_DOCUMENT, %ELASTICACHE_REPLICATION_GROUP_TYPE) {
    check(%INPUT_DOCUMENT.%ELASTICACHE_REPLICATION_GROUP_TYPE.resourceProperties)
        <<
        [CT.ELASTICACHE.PR.5]: Require an Amazon ElastiCache for Redis replication group to have encryption in transit activated
        [FIX]: Set the value of the 'TransitEncryptionEnabled' parameter to true.
        >>
}

#
# Parameterized Rules
#
rule check(elasticache_replication_group) {
    %elasticache_replication_group [
        # Scenario 2
        Engine exists
        Engine == %REDIS_ENGINE_TYPE
    ] {
        # Scenarios 3, 4 and 5
        TransitEncryptionEnabled exists
        TransitEncryptionEnabled == true
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.ELASTICACHE.PR.5 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Example subnet group
      SubnetIds:
      - Ref: Subnet
  ReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription:
        Fn::Sub: ${AWS::StackName}-example
      CacheNodeType: cache.t3.micro
      SecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      NumCacheClusters: 2
      Engine: redis
      TransitEncryptionEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Example subnet group
      SubnetIds:
      - Ref: Subnet
  ReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription:
        Fn::Sub: ${AWS::StackName}-example
      CacheNodeType: cache.t3.micro
      SecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      NumCacheClusters: 2
      Engine: redis
      TransitEncryptionEnabled: false


```

## [CT.ELASTICACHE.PR.6] Require an Amazon ElastiCache cache cluster to use a custom subnet group

This control checks whether an Amazon ElastiCache cache cluster is configured with a custom subnet group.

- **Control objective:** Limit network access
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::ElastiCache::CacheCluster`
- **AWS CloudFormation guard rule:**
  [CT.ELASTICACHE.PR.6 rule specification](#ct-elasticache-pr-6-rule "#ct-elasticache-pr-6-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.ELASTICACHE.PR.6 rule specification](#ct-elasticache-pr-6-rule "#ct-elasticache-pr-6-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.ELASTICACHE.PR.6 example templates](#ct-elasticache-pr-6-templates "#ct-elasticache-pr-6-templates")

**Explanation**

When you launch an ElastiCache cluster, AWS creates a default subnet group if none exists already. The default group utilizes subnets from the default VPC. Using custom subnet groups allows you to be more restrictive about network access to ElastiCache clusters.

###### Usage considerations

- This rule evaluates whether an Amazon ElastiCache cache cluster has been configured with a custom subnet group.
- Custom subnet groups may contain subnets that reside in the default Amazon VPC.

### Remediation for rule failure

Set the `CacheSubnetGroupName` parameter to the name of a custom Amazon ElastiCache cache subnet group.

The examples that follow show how to implement this remediation.

#### Amazon ElastiCache Cache Cluster - Example

An Amazon ElastiCache cache cluster configured with a custom subnet group. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "ElasticacheCluster": {
        "Type": "AWS::ElastiCache::CacheCluster",
        "Properties": {
            "Engine": "memcached",
            "CacheNodeType": "cache.t3.micro",
            "NumCacheNodes": "1",
            "CacheSubnetGroupName": {
                "Ref": "SubnetGroup"
            },
            "VpcSecurityGroupIds": [
                {
                    "Fn::GetAtt": [
                        "SecurityGroup",
                        "GroupId"
                    ]
                }
            ]
        }
    }
}

```

**YAML example**

```

ElasticacheCluster:
  Type: AWS::ElastiCache::CacheCluster
  Properties:
    Engine: memcached
    CacheNodeType: cache.t3.micro
    NumCacheNodes: '1'
    CacheSubnetGroupName: !Ref 'SubnetGroup'
    VpcSecurityGroupIds:
      - !GetAtt 'SecurityGroup.GroupId'


```

### CT.ELASTICACHE.PR.6 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   elasticache_subnet_group_check
#
# Description:
#   This control checks whether an Amazon ElastiCache cache cluster is configured with a custom subnet group.
#
# Reports on:
#   AWS::ElastiCache::CacheCluster
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any ElastiCache cluster resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cluster resource
#       And: 'CacheSubnetGroupName' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cluster resource
#       And: 'CacheSubnetGroupName' has been provided as an empty string or as a non-valid local reference
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cluster resource
#       And: 'CacheSubnetGroupName' has been provided and set to a value of 'default'
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache cluster resource
#       And: 'CacheSubnetGroupName' has been provided as a non-empty string or a valid local reference
#      Then: PASS

#
# Constants
#
let ELASTICACHE_CACHE_CLUSTER_TYPE = "AWS::ElastiCache::CacheCluster"
let INPUT_DOCUMENT = this

#
# Assignments
#
let elasticache_cache_clusters = Resources.*[ Type == %ELASTICACHE_CACHE_CLUSTER_TYPE ]

#
# Primary Rules
#
rule elasticache_subnet_group_check when is_cfn_template(%INPUT_DOCUMENT)
                                                %elasticache_cache_clusters not empty {
    check(%elasticache_cache_clusters.Properties)
        <<
        [CT.ELASTICACHE.PR.6]: Require an Amazon ElastiCache cache cluster to use a custom subnet group
        [FIX]: Set the 'CacheSubnetGroupName' parameter to the name of a custom Amazon ElastiCache cache subnet group.
        >>
}

rule elasticache_subnet_group_check when is_cfn_hook(%INPUT_DOCUMENT, %ELASTICACHE_CACHE_CLUSTER_TYPE) {
    check(%INPUT_DOCUMENT.%ELASTICACHE_CACHE_CLUSTER_TYPE.resourceProperties)
        <<
        [CT.ELASTICACHE.PR.6]: Require an Amazon ElastiCache cache cluster to use a custom subnet group
        [FIX]: Set the 'CacheSubnetGroupName' parameter to the name of a custom Amazon ElastiCache cache subnet group.
        >>
}

#
# Parameterized Rules
#
rule check(elasticache_cache_cluster) {
    %elasticache_cache_cluster {
        # Scenario 2
        CacheSubnetGroupName exists

        # Scenarios 3, 4 and 5
        check_subnet_group_is_not_default(this) or
        check_local_references(%INPUT_DOCUMENT, CacheSubnetGroupName, "AWS::ElastiCache::SubnetGroup")
    }
}

rule check_subnet_group_is_not_default(elasticache_cache_cluster) {
        %elasticache_cache_cluster {
            check_is_string_and_not_empty(CacheSubnetGroupName)
            CacheSubnetGroupName != "default"
        }
    }

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}

rule check_is_string_and_not_empty(value) {
    %value {
        this is_string
        this != /\A\s*\z/
    }
}

rule check_local_references(doc, reference_properties, referenced_resource_type) {
    %reference_properties {
        'Fn::GetAtt' {
            query_for_resource(%doc, this[0], %referenced_resource_type)
                <<Local Stack reference was invalid>>
        } or Ref {
            query_for_resource(%doc, this, %referenced_resource_type)
                <<Local Stack reference was invalid>>
        }
    }
}

rule query_for_resource(doc, resource_key, referenced_resource_type) {
    let referenced_resource = %doc.Resources[ keys == %resource_key ]
    %referenced_resource not empty
    %referenced_resource {
        Type == %referenced_resource_type
    }
}


```

### CT.ELASTICACHE.PR.6 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Example subnet group
      SubnetIds:
      - Ref: Subnet
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 11211
        ToPort: 11211
        CidrIp: 10.0.0.0/24
  CacheCluster:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      Engine: memcached
      CacheNodeType: cache.t3.micro
      NumCacheNodes: '1'
      CacheSubnetGroupName:
        Ref: SubnetGroup
      VpcSecurityGroupIds:
      - Fn::GetAtt: [SecurityGroup, GroupId]


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 11211
        ToPort: 11211
        CidrIp: 10.0.0.0/24
  CacheCluster:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      Engine: memcached
      CacheNodeType: cache.t3.micro
      NumCacheNodes: '1'
      VpcSecurityGroupIds:
      - Fn::GetAtt: [SecurityGroup, GroupId]


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 11211
        ToPort: 11211
        CidrIp: 10.0.0.0/24
  CacheCluster:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      Engine: memcached
      CacheNodeType: cache.t3.micro
      NumCacheNodes: '1'
      CacheSubnetGroupName: default
      VpcSecurityGroupIds:
      - Fn::GetAtt: [SecurityGroup, GroupId]


```

## [CT.ELASTICACHE.PR.7] Require an Amazon ElastiCache replication group of earlier Redis OSS versions to have Redis OSS AUTH activated

This control checks whether an Amazon ElastiCache replication group with an engine version earlier than 6.0 has Redis OSS AUTH enabled.

- **Control objective:** Enforce least privilege
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::ElastiCache::ReplicationGroup`
- **AWS CloudFormation guard rule:**
  [CT.ELASTICACHE.PR.7 rule specification](#ct-elasticache-pr-7-rule "#ct-elasticache-pr-7-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.ELASTICACHE.PR.7 rule specification](#ct-elasticache-pr-7-rule "#ct-elasticache-pr-7-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.ELASTICACHE.PR.7 example templates](#ct-elasticache-pr-7-templates "#ct-elasticache-pr-7-templates")

**Explanation**

Redis authentication tokens, or passwords, enable Redis to require a password before allowing clients to run commands, thereby improving data security.

###### Usage considerations

- This control applies only to Amazon ElastiCache replication groups of Redis OSS engine versions earlier than six (6).
- This control requires encryption-in-transit to be enabled on replication groups by means of the `TransitEncryptionEnabled` property.

### Remediation for rule failure

Set the value of the `AuthToken` parameter to a string between 16 characters and 128 characters in length, which contains only printable ASCII characters and does not contain non-alphanumeric characters outside of the set (!, &,

The examples that follow show how to implement this remediation.

#### Amazon ElastiCache Replication Group - Example

An Amazon ElastiCache replication group configured with Redis AUTH authentication enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "ReplicationGroup": {
        "Type": "AWS::ElastiCache::ReplicationGroup",
        "Properties": {
            "ReplicationGroupDescription": "Sample replication group",
            "CacheNodeType": "cache.t3.micro",
            "SecurityGroupIds": [
                {
                    "Ref": "SecurityGroup"
                }
            ],
            "CacheSubnetGroupName": {
                "Ref": "SubnetGroup"
            },
            "NumCacheClusters": 2,
            "Engine": "redis",
            "EngineVersion": "5.0.6",
            "TransitEncryptionEnabled": true,
            "AuthToken": {
                "Fn::Sub": "{{resolve:secretsmanager:${ReplicationGroupSecret}::password}}"
            }
        }
    }
}

```

**YAML example**

```

ReplicationGroup:
  Type: AWS::ElastiCache::ReplicationGroup
  Properties:
    ReplicationGroupDescription: Sample replication group
    CacheNodeType: cache.t3.micro
    SecurityGroupIds:
      - !Ref 'SecurityGroup'
    CacheSubnetGroupName: !Ref 'SubnetGroup'
    NumCacheClusters: 2
    Engine: redis
    EngineVersion: 5.0.6
    TransitEncryptionEnabled: true
    AuthToken: !Sub '{{resolve:secretsmanager:${ReplicationGroupSecret}::password}}'


```

### CT.ELASTICACHE.PR.7 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   elasticache_repl_grp_redis_auth_enabled_check
#
# Description:
#   This control checks whether an Amazon ElastiCache replication group with an engine version earlier than 6.0 has Redis OSS AUTH enabled.
#
# Reports on:
#   AWS::ElastiCache::ReplicationGroup
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any ElastiCache replication group resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache replication group resource
#       And: 'Engine' has not been provided or has been provided and is not set to 'redis'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache replication group resource
#       And: 'Engine' has been provided and is set to 'redis'
#       And: 'EngineVersion' has not been provided or has been provided and set to a version greater than or equal to 6
#      Then: SKIP
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache replication group resource
#       And: 'Engine' has been provided and is set to 'redis'
#       And: 'EngineVersion' has been provided and set to a version less than 6
#       And: 'AuthToken' has not been provided or has been provided and set to an empty string
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an ElastiCache replication group resource
#       And: 'Engine' has been provided and is set to 'redis'
#       And: 'EngineVersion' has been provided and set to a version less than 6
#       And: 'AuthToken' has been provided and set to a non-empty string
#      Then: PASS

#
# Constants
#
let ELASTICACHE_REPLICATION_GROUP_TYPE = "AWS::ElastiCache::ReplicationGroup"
let REDIS_ENGINE_TYPE = "redis"
let SUPPORTED_REDIS_ENGINE_VERSIONS_FOR_REDIS_AUTH = [
    /^2\./,
    /^3\./,
    /^4\./,
    /^5\./
]
let INPUT_DOCUMENT = this

#
# Assignments
#
let elasticache_replication_groups = Resources.*[ Type == %ELASTICACHE_REPLICATION_GROUP_TYPE ]

#
# Primary Rules
#
rule elasticache_repl_grp_redis_auth_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                                        %elasticache_replication_groups not empty {
    check(%elasticache_replication_groups.Properties)
        <<
        [CT.ELASTICACHE.PR.7]: Require an Amazon ElastiCache replication group of earlier Redis OSS versions to have Redis OSS AUTH activated
        [FIX]: Set the value of the 'AuthToken' parameter to a string between 16 characters and 128 characters in length, which contains only printable ASCII characters and does not contain non-alphanumeric characters outside of the set (!, &,
        >>
}

rule elasticache_repl_grp_redis_auth_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %ELASTICACHE_REPLICATION_GROUP_TYPE) {
    check(%INPUT_DOCUMENT.%ELASTICACHE_REPLICATION_GROUP_TYPE.resourceProperties)
        <<
        [CT.ELASTICACHE.PR.7]: Require an Amazon ElastiCache replication group of earlier Redis OSS versions to have Redis OSS AUTH activated
        [FIX]: Set the value of the 'AuthToken' parameter to a string between 16 characters and 128 characters in length, which contains only printable ASCII characters and does not contain non-alphanumeric characters outside of the set (!, &,
        >>
}

#
# Parameterized Rules
#
rule check(elasticache_replication_group) {
    %elasticache_replication_group [
        # Scenario 2
        Engine exists
        Engine == %REDIS_ENGINE_TYPE

        # Scenario 3
        EngineVersion exists
        EngineVersion in %SUPPORTED_REDIS_ENGINE_VERSIONS_FOR_REDIS_AUTH
    ] {
        # Scenarios 4 and 5
        AuthToken exists
        check_is_string_and_not_empty(AuthToken)
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}

rule check_is_string_and_not_empty(value) {
    %value {
        this is_string
        this != /\A\s*\z/
    }
}


```

### CT.ELASTICACHE.PR.7 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Cache subnet group
      SubnetIds:
      - Ref: Subnet
  ReplicationGroupSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: Replication group secret
      GenerateSecretString:
        SecretStringTemplate: "{}"
        GenerateStringKey: password
        PasswordLength: 64
        ExcludePunctuation: true
  ReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription:
        Fn::Sub: ${AWS::StackName}-example
      CacheNodeType: cache.t3.micro
      SecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      NumCacheClusters: 2
      Engine: redis
      EngineVersion: 5.0.6
      TransitEncryptionEnabled: true
      AuthToken:
        Fn::Sub: '{{resolve:secretsmanager:${ReplicationGroupSecret}::password}}'


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Cache subnet group
      SubnetIds:
      - Ref: Subnet
  ReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription:
        Fn::Sub: ${AWS::StackName}-example
      CacheNodeType: cache.t3.micro
      SecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      NumCacheClusters: 2
      Engine: redis
      EngineVersion: 3.2.6
      TransitEncryptionEnabled: true


```

## [CT.ELASTICACHE.PR.8] Require an Amazon ElastiCache replication group of later Redis OSS versions to have RBAC authentication activated

This control checks whether Amazon ElastiCache replication groups with an engine version greater than or equal to 6.0 have RBAC authentication enabled.

- **Control objective:** Enforce least privilege
- **Implementation:** AWS CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::ElastiCache::ReplicationGroup`
- **AWS CloudFormation guard rule:**
  [CT.ELASTICACHE.PR.8 rule specification](#ct-elasticache-pr-8-rule "#ct-elasticache-pr-8-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.ELASTICACHE.PR.8 rule specification](#ct-elasticache-pr-8-rule "#ct-elasticache-pr-8-rule")
- For examples of PASS and FAIL AWS CloudFormation Templates related to
  this control, see:
  [CT.ELASTICACHE.PR.8 example templates](#ct-elasticache-pr-8-templates "#ct-elasticache-pr-8-templates")

**Explanation**

Role-Based Access Control (RBAC) helps you create users and assign specific permissions to them, by using an access string.
You assign the users to user groups aligned with a specific role, such as administrators, or human resources. The roles are deployed to Amazon ElastiCache (Redis OSS) (Redis OSS) replication groups.
This technique establishes security boundaries between clients using the same Redis OSS replication groups, and it prevents clients from having access to other clients' data.
If you use RBAC authentication over Redis OSS AUTH, it reduces the number of credentials required for authenticated access to an Amazon ElastiCache replication group.

###### Usage considerations

- This control applies only to Amazon ElastiCache replication groups of Redis OSS engine versions greater than or equal to 6.0
- This control requires encryption in transit to be enabled on replication groups by means of the **TransitEncryptionEnabled** property

### Remediation for rule failure

Set the value of the UserGroupIds property to a list that contains at least one Amazon ElastiCache user group identifier.

The examples that follow show how to implement this remediation.

#### Amazon ElastiCache Replication Group - Example

An Amazon ElastiCache replication group configured with RBAC authentication enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "ReplicationGroup": {
        "Type": "AWS::ElastiCache::ReplicationGroup",
        "Properties": {
            "ReplicationGroupDescription": "Sample replication group",
            "CacheNodeType": "cache.t3.micro",
            "SecurityGroupIds": [
                {
                    "Ref": "SecurityGroup"
                }
            ],
            "CacheSubnetGroupName": {
                "Ref": "SubnetGroup"
            },
            "NumCacheClusters": 2,
            "Engine": "redis",
            "EngineVersion": 6.2,
            "TransitEncryptionEnabled": true,
            "UserGroupIds": [
                {
                    "Ref": "UserGroup"
                }
            ]
        }
    }
}

```

**YAML example**

```

ReplicationGroup:
  Type: AWS::ElastiCache::ReplicationGroup
  Properties:
    ReplicationGroupDescription: Sample replication group
    CacheNodeType: cache.t3.micro
    SecurityGroupIds:
      - !Ref 'SecurityGroup'
    CacheSubnetGroupName: !Ref 'SubnetGroup'
    NumCacheClusters: 2
    Engine: redis
    EngineVersion: 6.2
    TransitEncryptionEnabled: true
    UserGroupIds:
      - !Ref 'UserGroup'


```

### CT.ELASTICACHE.PR.8 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   elasticache_repl_grp_rbac_auth_enabled_check
#
# Description:
#   This control checks whether Amazon ElastiCache replication groups with an engine version greater than or equal to 6.0 have RBAC authentication enabled.
#
# Reports on:
#   AWS::ElastiCache::ReplicationGroup
#
# Evaluates:
#   AWS CloudFormation, AWS CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document does not contain any Amazon ElastiCache replication group resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon ElastiCache replication group resource
#       And: 'Engine' has not been provided or has been provided and is not set to 'redis'
#      Then: SKIP
#   Scenario: 3
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon ElastiCache replication group resource
#       And: 'Engine' has been provided and is set to 'redis'
#       And: 'EngineVersion' has been provided and set to a version less than 6
#      Then: SKIP
#   Scenario: 4
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon ElastiCache replication group resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'EngineVersion' has not been provided or has been provided and set to a version greater than or equal to 6
#       And: 'UserGroupIds' has not been provided or has been provided as an empty list or a list containing an empty
#            string or invalid local reference
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an AWS CloudFormation or AWS CloudFormation hook document
#       And: The input document contains an Amazon ElastiCache replication group resource
#       And: 'Engine' has been provided and set to 'redis'
#       And: 'EngineVersion' has not been provided or has been provided and set to a version greater than or equal to 6
#       And: 'UserGroupIds' has been provided as a list containing non-empty strings or valid local references
#      Then: PASS

#
# Constants
#
let ELASTICACHE_REPLICATION_GROUP_TYPE = "AWS::ElastiCache::ReplicationGroup"
let REDIS_ENGINE_TYPE = "redis"
let UNSUPPORTED_REDIS_ENGINE_VERSIONS_FOR_RBAC = [
    /^2\./,
    /^3\./,
    /^4\./,
    /^5\./
]
let INPUT_DOCUMENT = this

#
# Assignments
#
let elasticache_replication_groups = Resources.*[ Type == %ELASTICACHE_REPLICATION_GROUP_TYPE ]

#
# Primary Rules
#
rule elasticache_repl_grp_rbac_auth_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                                       %elasticache_replication_groups not empty {
    check(%elasticache_replication_groups.Properties)
        <<
        [CT.ELASTICACHE.PR.8]: Require an Amazon ElastiCache replication group of later Redis OSS versions to have RBAC authentication activated
        [FIX]: Set the value of the UserGroupIds property to a list that contains at least one Amazon ElastiCache user group identifier.
        >>
}

rule elasticache_repl_grp_rbac_auth_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %ELASTICACHE_REPLICATION_GROUP_TYPE) {
    check(%INPUT_DOCUMENT.%ELASTICACHE_REPLICATION_GROUP_TYPE.resourceProperties)
        <<
        [CT.ELASTICACHE.PR.8]: Require an Amazon ElastiCache replication group of later Redis OSS versions to have RBAC authentication activated
        [FIX]: Set the value of the UserGroupIds property to a list that contains at least one Amazon ElastiCache user group identifier.
        >>
}

#
# Parameterized Rules
#
rule check(elasticache_replication_group) {
    %elasticache_replication_group [
        # Scenario 2
        Engine exists
        Engine == %REDIS_ENGINE_TYPE

        # Scenario 3
        EngineVersion not exists or
        EngineVersion not in %UNSUPPORTED_REDIS_ENGINE_VERSIONS_FOR_RBAC
    ] {
        # Scenarios 4, 5 and 6
        UserGroupIds exists
        UserGroupIds is_list
        UserGroupIds not empty

        UserGroupIds[*] {
            check_is_string_and_not_empty(this) or
            check_local_references(%INPUT_DOCUMENT, this, "AWS::ElastiCache::UserGroup")
        }
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}

rule check_is_string_and_not_empty(value) {
    %value {
        this is_string
        this != /\A\s*\z/
    }
}

rule check_local_references(doc, reference_properties, referenced_resource_type) {
    %reference_properties {
        'Fn::GetAtt' {
            query_for_resource(%doc, this[0], %referenced_resource_type)
                <<Local Stack reference was invalid>>
        } or Ref {
            query_for_resource(%doc, this, %referenced_resource_type)
                <<Local Stack reference was invalid>>
        }
    }
}

rule query_for_resource(doc, resource_key, referenced_resource_type) {
    let referenced_resource = %doc.Resources[ keys == %resource_key ]
    %referenced_resource not empty
    %referenced_resource {
        Type == %referenced_resource_type
    }
}


```

### CT.ELASTICACHE.PR.8 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: test
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Cache Subnet Group
      SubnetIds:
      - Ref: Subnet
  UserGroup:
    Type: AWS::ElastiCache::UserGroup
    Properties:
      Engine: redis
      UserGroupId:
        Fn::Sub: ${AWS::StackName}-example-group
      UserIds:
      - default
  ReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription:
        Fn::Sub: ${AWS::StackName}-example
      CacheNodeType: cache.t3.micro
      SecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      NumCacheClusters: 2
      Engine: redis
      UserGroupIds:
      - Ref: UserGroup


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  Subnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPC
      CidrBlock: 10.0.0.0/16
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ''
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: test
      VpcId:
        Ref: VPC
      SecurityGroupIngress:
      - FromPort: 443
        IpProtocol: tcp
        ToPort: 443
        CidrIp: 0.0.0.0/0
  SubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Cache Subnet Group
      SubnetIds:
      - Ref: Subnet
  ReplicationGroup:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription:
        Fn::Sub: ${AWS::StackName}-example
      CacheNodeType: cache.t3.micro
      SecurityGroupIds:
      - Ref: SecurityGroup
      CacheSubnetGroupName:
        Ref: SubnetGroup
      NumCacheClusters: 2
      Engine: redis


```
