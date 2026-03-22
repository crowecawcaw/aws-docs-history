# Preparing a cluster in ElastiCache

Following, you can find instructions on creating a cluster using the ElastiCache console, the
AWS CLI, or the ElastiCache API.

You can also create an ElastiCache cluster using [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md").
For more information, see [AWS::ElastiCache::CacheCluster](../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.md") in the _AWS Cloud Formation User Guide_,
which includes guidance on how to implement that approach.

Whenever you create a cluster or replication group, it is
a good idea to do some preparatory work so you won't need to upgrade or make changes right away.

###### Topics

- [Determining your ElastiCache cluster requirements](cluster-create-determine-requirements.md "cluster-create-determine-requirements.md")
- [Choosing your node size](CacheNodes.SelectSize.md "CacheNodes.SelectSize.md")
