# Using RDS Proxy with AWS CloudFormation

You can use RDS Proxy with AWS CloudFormation. This helps you to create groups of related resources.
Such a group can include a proxy that can connect to a newly created Amazon RDS DB instance. RDS Proxy support in CloudFormation involves two new registry types:
`DBProxy` and `DBProxyTargetGroup`.

The following listing shows a sample CloudFormation template for RDS Proxy.

```
Resources:
 DBProxy:
   Type: AWS::RDS::DBProxy
   Properties:
     DBProxyName: CanaryProxy
     EngineFamily: MYSQL
     RoleArn:
      Fn::ImportValue: SecretReaderRoleArn
     Auth:
       - {AuthScheme: SECRETS, SecretArn: !ImportValue ProxySecret, IAMAuth: DISABLED}
     VpcSubnetIds:
       Fn::Split: [",", "Fn::ImportValue": SubnetIds]

 ProxyTargetGroup:
   Type: AWS::RDS::DBProxyTargetGroup
   Properties:
     DBProxyName: CanaryProxy
     TargetGroupName: default
     DBInstanceIdentifiers:
       - Fn::ImportValue: DBInstanceName
   DependsOn: DBProxy

```

For more information about the resources in this sample, see
[`DBProxy`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.md") and
[`DBProxyTargetGroup`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.md").

For more information about resources that you can create using CloudFormation, see
[RDS resource type
reference](../../../AWSCloudFormation/latest/UserGuide/AWS_RDS.md "../../../AWSCloudFormation/latest/UserGuide/AWS_RDS.md").
