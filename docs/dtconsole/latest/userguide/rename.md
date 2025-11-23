# Connections rename - Summary of changes

The connections feature in the Developer Tools console allows you to connect your AWS resources to
third-party source repositories. On March 29, 2024, AWS CodeStar Connections was renamed to
AWS CodeConnections. The following sections describe the different parts of the feature that changed with
the rename, and what actions you need to take to ensure that your resources continue to function
properly.

Note that this list is not exhaustive. While other parts of the product also changed, these
updates are the most relevant.

###### Note

Actions for resources that are created under the new service prefix
`codeconnections` are available. Creating a resource under the new service prefix
will use `codeconnections` in the resource ARN. Actions and resources for the
`codestar-connections` service prefix remain available. When specifying a
resource in the IAM policy, the service prefix needs to match that of the resource.

###### Note

Beginning July 1, 2024, the console creates connections with `codeconnections` in the resource ARN. Resources with both service prefixes will continue to display in the console.

## Renamed service prefix

Connections APIs use a renamed service prefix: **codeconnections**.

To use the new prefix in CLI commands, download the version 2 of the AWS CLI. The following
is an example command with the updated prefix.

```
aws codeconnections delete-connection --connection-arn arn:aws:codeconnections:us-west-2:`account_id`:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f
```

## Renamed actions in IAM

The actions in IAM use the new prefix, as shown in the following examples:

```
codeconnections:CreateConnection
codeconnections:DeleteConnection
codeconnections:GetConnection
codeconnections:ListConnections
```

## New resource ARN

Connections resources that are created will have a new ARN:

```
arn:aws:codeconnections:us-west-2:`account-ID`:connection/*
```

## Affected service role policies

For the following services, service role policies will use the new prefix in policy
statements. You can also update your existing service role policies to use the new
permissions, but policies created with the old prefix will continue to be supported.

- The CodePipeline customer-managed service role policy
- The AWS CodeStar service role `AWSCodeStarServiceRole` policy

## New CloudFormation resource

To use the CloudFormation resources for connections, a new resource will be available. The existing
resource will still be supported.

- The new [AWS CloudFormation](http://aws.amazon.com/cloudformation/ "http://aws.amazon.com/cloudformation/") resource is
  named AWS::CodeConnections::Connection. See [AWS::CodeConnections::Connection](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-connection.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-connection.md") in the CloudFormation User Guide.
- The existing AWS::CodeStarConnections::Connection resource will still be supported. See [AWS::CodeStarConnections::Connection](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.md") in the CloudFormation User Guide.
