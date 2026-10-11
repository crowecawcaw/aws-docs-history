

# Compatibility with managed blueprints
<a name="tooling-managed-compatibility"></a>

In Amazon SageMaker Unified Studio, service-managed blueprints provide a wide variety of resource provisioning capabilities, such as Amazon EMR and Amazon Redshift Serverless. For more information, see [Supported blueprints](supported-blueprints.md). Service-managed blueprints require metadata populated by AWS CloudFormation exports from the project's Tooling environment. When you use a custom blueprint categorized as `TOOLING` in a project with a service-managed blueprint, ensure that your custom blueprint contains the following AWS CloudFormation exports.

------
#### [ IAM-based domain ]

```
Parameters:
  sagemakerUnifiedStudioNetworkSecurityGroupId: { Type: String, Default: '' }
  sagemakerUnifiedStudioNetworkSubnets:         { Type: String, Default: '' }
  sagemakerUnifiedStudioNetworkVpcId:           { Type: String, Default: '' }

Outputs:
  KmsKeyArn:
    Condition: kmsKeyArnExist
    Value: !Ref sagemakerUnifiedStudioKmsKeyArn
    Export: { Name: !Sub 'kmsKeyArn-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
  PrivateSubnets:
    Value: !Ref sagemakerUnifiedStudioNetworkSubnets
    Export: { Name: !Sub 'privateSubnets-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
  SecurityGroup:
    Value: !Ref sagemakerUnifiedStudioNetworkSecurityGroupId
    Export: { Name: !Sub 'securityGroup-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
  VpcId:
    Value: !Ref sagemakerUnifiedStudioNetworkVpcId
    Export: { Name: !Sub 'vpcId-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
```

------
#### [ Identity Center-based domain ]

```
Parameters:
  sagemakerUnifiedStudioNetworkSecurityGroupId: { Type: String, Default: '' }
  sagemakerUnifiedStudioNetworkSubnets:         { Type: String, Default: '' }

Outputs:
  KmsKeyArn:
    Condition: kmsKeyArnExist
    Value: !Ref sagemakerUnifiedStudioKmsKeyArn
    Export: { Name: !Sub 'kmsKeyArn-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
  LogGroupName:
    Value: !Ref ToolingLogGroup
    Export: { Name: !Sub 'logGroupName-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
  PrivateSubnets:
    Value: !Ref sagemakerUnifiedStudioNetworkSubnets
    Export: { Name: !Sub 'privateSubnets-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
  SecurityGroup:
    Value: !Ref sagemakerUnifiedStudioNetworkSecurityGroupId
    Export: { Name: !Sub 'securityGroup-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
  VpcId:
    Value: !Ref sagemakerUnifiedStudioNetworkVpcId
    Export: { Name: !Sub 'vpcId-${datazoneEnvironmentProjectId}-${datazoneScopeName}' }
```

------