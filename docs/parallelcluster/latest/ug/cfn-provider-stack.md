# Provider stack hosted by AWS ParallelCluster

The custom resource provider stack is formatted as shown in the following CloudFormation template snippet:

```
PclusterClusterProvider:
  Type: AWS::CloudFormation::Stack
  Properties:
    Parameters:
      CustomLambdaRole: # (Optional) RoleARN to override default
      AdditionalIamPolicies: # (Optional) comma-separated list of IAM policies to add
    TemplateURL: !Sub
      - https://${AWS::Region}-aws-parallelcluster.s3.${AWS::Region}.${AWS::URLSuffix}/parallelcluster/${Version}/templates/custom_resource/cluster.yaml
      - { Version: 3.14.1 }
```

**Properties:**

**Parameters:**

**CustomLambdaRole (optional):**

A custom role with permissions to run the AWS Lambda
that creates and manages the cluster. By default, the role uses the same policies defined by default in the [AWS ParallelCluster documentation](iam-roles-in-parallelcluster-v3.md "iam-roles-in-parallelcluster-v3.md").

**AdditionalIamPolicies (optional):**

A comma-separated list of additional IAM Policy Amazon Resource Names (ARNs) to add to the role that the Lambda uses. This is
only used if a `CustomLambdaRole` isn't specified and can be kept blank.

If you need additional policies for the head node, compute nodes, or for access to an Amazon S3 bucket, add them to the `CustomLambdaRole`
or `AdditionalIamPolicy` property.

If you need to attach additional policies to the head node, you must also grant the necessary
permissions to attach or detach those policies to the IAM role associated with the head node.
Specifically, you'll need to attach the "iam:AttachRolePolicy" and "iam:DetachRolePolicy"
permissions (or their equivalent in a managed policy) to the IAM role used by the head node. For
more information, see [AWS ParallelCluster user example policies for managing IAM
resources](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-user-policy-manage-iam "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-user-policy-manage-iam").

For more information about the default policies, see [AWS Identity and Access Management permissions in AWS ParallelCluster](iam-roles-in-parallelcluster-v3.md "iam-roles-in-parallelcluster-v3.md").

**TemplateURL (required):**

The AWS ParallelCluster custom resource file URL.

**Outputs:**

**ServiceToken:**

A value that can be used as a custom resource `ServiceToken` property. A custom
resource `ServiceToken` specifies where CloudFormation sends requests. This is a
required input for a cluster resource that you include in your CloudFormation template.

**LogGroupArn:**

The ARN of the CloudWatch `LogGroup` that the underlying resource logs to.

**LambdaLayerArn:**

The ARN of the Lambda layer that's used for running AWS ParallelCluster operations.
