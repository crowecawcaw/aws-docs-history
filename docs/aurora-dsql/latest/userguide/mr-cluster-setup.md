

# Configuring Aurora DSQL clusters using AWS CloudFormation

 You can use the same CloudFormation resource `AWS::DSQL::Cluster` to deploy and manage single-Region and multi-Region Aurora DSQL clusters. 

See the [Amazon Aurora DSQL resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_DSQL.html) for more on how to create, modify, and manage clusters using the `AWS::DSQL::Cluster` resource.

You can select the two peer Regions and the witness Region from the Regions that support Aurora DSQL multi-Region clusters. The three Regions must be distinct. For the list of supported Regions, see [Multi-Region cluster availability](what-is-aurora-dsql.html#aurora-dsql-multi-region-availability).

## Creating the initial cluster configuration
<a name="mr-cluster-initial"></a>

First, create an AWS CloudFormation template to define your multi-Region cluster:

```yaml
---
Resources:
  MRCluster:
    Type: AWS::DSQL::Cluster
    Properties:
      DeletionProtectionEnabled: true
      MultiRegionProperties:
        WitnessRegion: us-west-2
```

Create stacks in both Regions using the following AWS CLI commands:

```
aws cloudformation create-stack --region us-east-2 \
    --stack-name MRCluster \
    --template-body file://mr-cluster.yaml
```

```
aws cloudformation create-stack --region us-east-1 \
    --stack-name MRCluster \
    --template-body file://mr-cluster.yaml
```

## Finding cluster identifiers
<a name="mr-cluster-find"></a>

Retrieve the physical resource IDs for your clusters:

```sh
aws cloudformation describe-stack-resources --region us-east-2 \
    --stack-name MRCluster \
    --query 'StackResources[].PhysicalResourceId'
[
  "auabudrks5jwh4mjt6o5xxhr4y"
]
```

```sh
aws cloudformation describe-stack-resources --region us-east-1 \
    --stack-name MRCluster \
    --query 'StackResources[].PhysicalResourceId'
[
  "imabudrfon4p2z3nv2jo4rlajm"
]
```

## Updating the cluster configuration
<a name="mr-cluster-update"></a>

Update your AWS CloudFormation template to include both cluster ARNs:

```yaml
---
Resources:
  MRCluster:
    Type: AWS::DSQL::Cluster
    Properties:
      DeletionProtectionEnabled: true
      MultiRegionProperties:
        WitnessRegion: us-west-2
        Clusters:
        - arn:aws:dsql:us-east-2:123456789012:cluster/auabudrks5jwh4mjt6o5xxhr4y
        - arn:aws:dsql:us-east-1:123456789012:cluster/imabudrfon4p2z3nv2jo4rlajm
```

Apply the updated configuration to both Regions:

```
aws cloudformation update-stack --region us-east-2 \
    --stack-name MRCluster \
    --template-body file://mr-cluster.yaml
```

```
aws cloudformation update-stack --region us-east-1 \
    --stack-name MRCluster \
    --template-body file://mr-cluster.yaml
```