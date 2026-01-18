# Cluster resource

The CloudFormation cluster resource is formatted as shown in the following CloudFormation template snippet:

```
PclusterCluster:
  Type: Custom::PclusterCluster
  Properties:
    ServiceToken: !GetAtt [ PclusterClusterProvider , Outputs.ServiceToken ]
    ClusterName: !Sub 'c-${AWS::StackName}' # Must be different from StackName
    ClusterConfiguration:
    # Your Cluster Configuration
```

**Properties:**

**ServiceToken:**

The AWS ParallelCluster provider stack `ServiceToken` output.

**ClusterName:**

The name of the cluster to be created and managed. The name must not match the CloudFormation stack’s name.
The name can't be changed after the cluster has been created.

**ClusterConfiguration:**

The cluster configuration YAML file, as described in [Cluster configuration file](cluster-configuration-file-v3.md "cluster-configuration-file-v3.md").
However, you can use the usual CloudFormation constructs, such as [Intrinsic functions](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md").

**DeletionPolicy:**

Defines whether to delete the cluster when the root stack is deleted.
The default is `Delete`.

**Retain:**

Retain the cluster if the custom resource is deleted.

###### Note

To keep the retained cluster functioning, cluster-dependent resources, such as storage and networking, must have a
deletion policy set to retain.

**Delete:**

Delete the cluster if the custom resource is deleted.

**`Fn::GetAtt` return values:**

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of a type. For more information about using the `Fn::GetAtt intrinsic` function, see
[Fn::GetAtt](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md").

**ClusterProperties:**

The values from the [pcluster describe-cluster](pcluster.md "pcluster.md") operation.

**validationMessages:**

A string containing all the validation messages that occurred during the last create or update operation.

**logGroupName:**

The name of the log group that's used for logging Lambda cluster operations. The log events are retained for 90 days and
the log group is retained after cluster deletion.

Example: `Fn::GetAtt`:

```
# Provide the public IP address of the head node as an output of a stack
Outputs:
  HeadNodeIp:
    Description: The public IP address of the head node
    Value: !GetAtt [ PclusterCluster, headNode.publicIpAddress ]
```

Example: Simple, complete CloudFormation template with an AWS ParallelCluster custom resource:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: >
 AWS ParallelCluster CloudFormation Template

Parameters:
  HeadNodeSubnet:
    Description: Subnet where the HeadNode will run
    Type: AWS::EC2::Subnet::Id

  ComputeSubnet:
    Description: Subnet where the Compute Nodes will run
    Type: AWS::EC2::Subnet::Id

  KeyName:
    Description: KeyPair to login to the head node
    Type: AWS::EC2::KeyPair::KeyName

Resources:
  PclusterClusterProvider:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: !Sub
        - https://${AWS::Region}-aws-parallelcluster.s3.${AWS::Region}.${AWS::URLSuffix}/parallelcluster/${Version}/templates/custom_resource/cluster.yaml
        - { Version: 3.14.1 }

  PclusterCluster:
    Type: Custom::PclusterCluster
    Properties:
      ServiceToken: !GetAtt [ PclusterClusterProvider , Outputs.ServiceToken ]
      ClusterName: !Sub 'c-${AWS::StackName}'
      ClusterConfiguration:
        Image:
          Os: alinux2
        HeadNode:
          InstanceType: t2.medium
          Networking:
            SubnetId: !Ref HeadNodeSubnet
          Ssh:
            KeyName: !Ref KeyName
        Scheduling:
          Scheduler: slurm
          SlurmQueues:
          - Name: queue0
            ComputeResources:
            - Name: queue0-cr0
              InstanceType: t2.micro
            Networking:
              SubnetIds:
              - !Ref ComputeSubnet

Outputs:
  HeadNodeIp:
    Description: The Public IP address of the HeadNode
    Value: !GetAtt [ PclusterCluster, headNode.publicIpAddress ]
  ValidationMessages:
    Description: Any warnings from cluster create or update operations.
    Value: !GetAtt PclusterCluster.validationMessages
```

To learn more about how to use the CloudFormation AWS ParallelCluster custom resource,
see [Creating a cluster with CloudFormation](tutorials_09_cfn-custom-resource-v3.md "tutorials_09_cfn-custom-resource-v3.md").
