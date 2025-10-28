# Resource Tagger Configuration Profiles in AMS Accelerate

Configuration profiles help ensure that tags are applied uniformly to resources throughout the lifetime of the resources.

## Syntax and structure

A configuration profile is a JSON object with the following structure:

```
{
   "Options": {
      "ReadOnly": false
   },
   "`ResourceType`": {
      "`ConfigurationID`": {
			   "Enabled": true,
			   "Filter": { ... },
			   "Tags": [  ...  ]
      },
      "`ConfigurationID`": {
			   ...
      }
   },
   "`ResourceType`": {
		   ...
   }
}
```

**Options**: (optional) Specify options for how you would like the ResourceTagger to behave. Omitting the block is equivalent
to setting all options to their default values. See below for available **Options** settings:

- **ReadOnly**: (optional, defaults to false): Specifies ReadOnly mode for
  Resource Tagger. Set ReadOnly to true to disable Resource Tagger creating or removing tags
  on AWS resources. For more information, see
  [Preventing Resource Tagger from modifying resources](acc-rt-using.md#acc-rt-preventing-rt-changes "acc-rt-using.md#acc-rt-preventing-rt-changes").

**ResourceType**: This key must be one of the following supported strings, and represents
all configuration related to the resource type indicated:

- AWS::AutoScaling::AutoScalingGroup
- AWS::DynamoDB::Table
- AWS::EC2::Instance
- AWS::EC2::NatGateway
- AWS::EC2::VPNConnection
- AWS::EFS::FileSystem
- AWS::EKS::Cluster
- AWS::ElasticLoadBalancing::LoadBalancer
- AWS::ElasticLoadBalancingV2::LoadBalancer
- AWS::Elasticsearch::Domain
- AWS::FSx::FileSystem
- AWS::OpenSearch::Domain
- AWS::RDS::DBCluster
- AWS::RDS::DBInstance
- AWS::Redshift::Cluster
- AWS::S3::Bucket
- AWS::Synthetics::Canary

**ConfigurationID**: This key must be unique in the profile document,
and uniquely names the following block of configuration. If two configuration blocks in the same
**ResourceType** block have the same **ConfigurationID**, the one that
appears last in the profile takes effect. If you specify a **ConfigurationID** in your
customization profile that is the same as one specified in the default document, the configuration block
defined in the customization profile takes effect.

###### Important

The **ConfigurationID** should
**`not`** overlap with the AMS Accelerate profile; for
example, it should not be **AMSMonitoringLinux** or **AMSMonitoringWindows**,
otherwise it disables the respective configuration of the **AMSManagedTags** configuration
profile.

**Enabled** (optional, defaults to **true**): Specifies
if the configuration block takes effect. Set this to **false** to disable a configuration
block. A disabled configuration block has no effect.

**Filter**: Specifies the resources that the configuration applies to. Each filter
object can have any one (but only one) of the following fields:

- **AWS::AutoScaling::AutoScalingGroup**:
  - **AutoScalingGroupName**: The Autoscaling Group name.
    This field supports wildcard matching.

- **AWS::DynamoDB::Table**:
  - **TableName**: The name of the DynamoDB table. This field supports wildcard matching.

- **AWS::EC2::Instance**:
  - **AvailabilityZone**: The filter matches an EC2 instance in the specified
    availability zone. This field supports wildcard matching, so **\*a**
    matches us-east-1a, ap-northeast-1a, and so on.
  - **InstanceId**: The
    filter matches an EC2 instance with the specified instance ID. This field supports wildcard matching,
    so **i-00000\*** would match any instance that has an instance ID starting with
    **i-00000**.
  - **Platform**: The filter
    matches an EC2 instance with the specified platform. Valid values are **windows**,
    **linux** or the wildcard **\*** (to match any
    platform).

- **AWS::EC2::NatGateway**:
  - **NatGatewayId**: The ID of the NAT Gateway. This field supports wildcard matching.
  - **State**: The state of the NAT gateway (pending | failed | available | deleting | deleted or wildcard "\*")
  - **VpcId**: The ID of the VPC in which the NAT Gateway resides. This field supports wildcard matching.
  - **SubnetId**: The ID of the Subnet in which the NAT Gateway resides. This field supports wildcard
    matching

- **AWS::EC2::VPNConnection**:
  - **VpnConnectionId**: The ID of the connection. This field supports wildcard matching.

- **AWS::EFS::FileSystem**:
  - **FileSystemId**: The ID of the EFS file system. This field supports wildcard matching.

- **AWS::EKS::Cluster**:
  - **ClusterName**: The name of the cluster. This field supports wildcard matching.

- **AWS::ElasticLoadBalancing::LoadBalancer (Classic Load Balancer)**:
  - **LoadBalancerName**: The LoadBalancer Name. This field supports wildcard
    matching.
  - **Scheme**: Can be either "internet-facing", "internal" or
    wildcard "\*".
  - **VPCId**: The VPCId in which the loadbalancer is deployed, can be
    wildcard "\*".

- **AWS::ElasticLoadBalancingV2::LoadBalancer (Application Load Balancer
  (ALB))**:
  - **LoadBalancerArn**: The LoadBalancer Amazon Resource Name (ARN).
  - **DNSName**: The DNSName of the LoadBalancer. This field supports wildcard
    matching.
  - **LoadBalancerName**: The LoadBalancer Name. This field supports wildcard
    matching.

- **AWS::Elasticsearch::Domain**:
  - **DomainId**: The DomainId of the ElasticSearch resource. This field supports wildcard matching.
  - **DomainName**: The DomainName of the ElasticSearch resource. This field supports wildcard matching.
  - **HasMasterNode**: Boolean value of true or false. Matches if the Domain has a dedicated master node.
  - **HasKmsKey**Boolean value of true or false. Matches if the Domain has a KMS key for encryption at rest.

- **AWS::FSx::FileSystem**:
  - **FileSystemId**: The ID of the FSx filesystem. This field supports wildcard matching.

- **AWS::OpenSearch::Domain**:
  - **DomainId**: The DomainId of the OpenSearch resource. This field supports
    wildcard matching.
  - **DomainName**: The DomainName of the OpenSearch resource. This field supports
    wildcard matching.
  - **HasMasterNode**: Boolean; If the Domain has a dedicated master node, this can be
    set to true.
  - **HasKmsKey**: If the Domain has a KMS key for encryption at rest, this can be set
    to true.

- **AWS::RDS::DBCluster**:
  - **DBClusterIdentifier**: The filter matches an RDS cluster identifier with the
    specified identifier. This field does not support wildcard matching, so a cluster identifier must be specified.
  - **Engine**: The engine in use by the RDS Instance. This field supports wildcard
    matching.
  - **EngineVersion**: The engine version. This field supports wildcard matching.

- **AWS::RDS::DBInstance**:
  - **DBInstanceIdentifier**: The filter matches an RDS instance with the specified
    instance ID. This field does not support wildcard matching, so an instance identifier must be specified.
  - **Engine**: The engine in use by the RDS Instance. This field supports wildcard
    matching.
  - **EngineVersion**: The engine version. This field supports wildcard
    matching.

- **AWS::Redshift::Cluster**:
  - **ClusterIdentifier**: The Cluster Identifier. This field supports wildcard
    matching.

- **AWS::S3::Bucket**:
  - **BucketName**: The name of the S3 bucket. This field supports wildcard matching.

- **AWS::Synthetics::Canary**:
  - **CanaryName**: The name of the Synthetics canary.

**Other Filter properties:**

- **Tag**: The filter applies to any resource that already has the
  given tag applied. The value for this property must be a JSON object with the following fields:
  - **Key**: Must be an exact string, and specifies that the resources must
    have a tag with that exact key.
  - **Value**: Specifies the matching value for the tag. Supports wildcards,
    so a value of **Sample** matches any value that ends with the string
    **Sample**.

- **Fn::AND**: A JSON array of JSON objects. Each object follows the same
  rules as the **Filter** configuration block. This specifies that the filter match any resource
  that matches all of the sub-filters.
- **Fn::OR**: A JSON array of JSON objects. Each object follows the same
  rules as the **Filter** configuration block. This specifies that the filter
  match any resource that matches any of the sub-filters.
- **Fn::NOT**: A JSON object that follows the same rules as the
  **Filter** configuration block. This specifies that the filter explicitly not match any
  resource that matches the sub-filter. Use this to specify exclusions to your tagging rules.

**Tags**: The tags to be applied to the matched resources. (See
[Tag naming and usage conventions](../../../mediaconnect/latest/ug/tagging-restrictions.md "../../../mediaconnect/latest/ug/tagging-restrictions.md").) This field is an
array of key-value pairs:

- **Key**: The key of the tag to be applied.
- **Value**: The value of the tag to be applied.

###### Note

Tags applied by Resource Tagger always have keys that begin with **ams:rt:**.
If you don't specify this prefix in your profile, Resource Tagger inserts it for you. This
is how Resource Tagger distinguishes the tags it owns and manages from tags used by other
tools for other purposes.
