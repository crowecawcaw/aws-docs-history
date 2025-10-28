# Configuring Aurora DSQL clusters using AWS CloudFormation

You can use the same AWS CloudFormation resource `AWS::DSQL::Cluster` to deploy and manage
single-Region and multi-Region Aurora DSQL clusters.

See the [Amazon Aurora DSQL resource type
reference](../../../AWSCloudFormation/latest/TemplateReference/AWS_DSQL.md "../../../AWSCloudFormation/latest/TemplateReference/AWS_DSQL.md") for more on how to create, modify, and manage clusters using the
`AWS::DSQL::Cluster` resource.

## Creating the Initial Cluster Configuration

First, create an AWS CloudFormation template to define your multi-Region cluster:

```
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

## Finding Cluster Identifiers

Retrieve the physical resource IDs for your clusters:

```
aws cloudformation describe-stack-resources -region us-east-2 \
    --stack-name MRCluster \
    --query 'StackResources[].PhysicalResourceId'
[
  "auabudrks5jwh4mjt6o5xxhr4y"
]
```

```
aws cloudformation describe-stack-resources -region us-east-1 \
    --stack-name MRCluster \
    --query 'StackResources[].PhysicalResourceId'
[
  "imabudrfon4p2z3nv2jo4rlajm"
]
```

## Updating the Cluster Configuration

Update your AWS CloudFormation template to include both cluster ARNs:

```
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
