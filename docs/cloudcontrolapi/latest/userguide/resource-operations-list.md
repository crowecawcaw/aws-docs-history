# Discovering resources with AWS Cloud Control API

Use the `list-resources` command to discover the resources currently provisioned in your
AWS account and AWS Region. This includes all resources of the specified resource type, regardless of whether
they were provisioned through Cloud Control API, directly through the underlying service, or other mechanism (such as being
part of an AWS CloudFormation stack).

The information returned for each resource includes:

- The resource's primary identifier.
- Optionally, it may include the _part or all_ resource's properties, detailing the current
  state of the resource. For more information, see [Viewing resource type schemas](resource-types.md#resource-types-schemas "resource-types.md#resource-types-schemas").
  The follow example returns a list of `AWS::Logs::LogGroup` resources.

```
`$` `aws cloudcontrol list-resources --type-name AWS::Logs::LogGroup`
```

Cloud Control API returns a list of the resources in your account of the specified resource type. For the example ,
`list-resources` returns the primary identifier and resource properties of all
`AWS::Logs::LogGroup` resources in your account, regardless of whether they were provisioned by Cloud Control API.
The returned information resembles the following, depending on the resources in your account.

```
{
  "TypeName": "AWS::Logs::LogGroup",
  "ResourceDescriptions":
  [
    {
      "Identifier": "CloudControlExample",
      "Properties": '{"RetentionInDays":180, "LogGroupName": "CloudControlExample", "Arn": "arn:aws:logs:us-west-2:123456789012:log-group:CloudControlExample:*"}'
    },
    {
      "Identifier": "AnotherLogGroupResourceExample",
      "Properties": '{"RetentionInDays":90, "LogGroupName": "AnotherLogGroupResourceExample", "Arn": "arn:aws:logs:us-west-2:123456789012:log-group:AnotherLogGroupResourceExample:*"}'
    }
  ]
}
```

The follow example requests a list of `AWS::Kinesis::Stream` resources.

```
`$` `aws cloudcontrol list-resources --type-name AWS::Kinesis::Stream`
```

For Kinesis streams, Cloud Control API returns the primary identifier of each stream, along with a
_subset_ of the resource properties. In this case, just a single property, `Name`. You
could then use a stream's primary identifier with `get-resource` to request the resource's full current
state.

```
{
    "TypeName": "AWS::Kinesis::Stream",
    "ResourceDescriptions": [
        {
            "Identifier": "MyKinesisStream",
            "Properties": '{"Name": "MyKinesisStream"}'
        },
        {
            "Identifier": "AnotherStream",
            "Properties": '{"Name": "AnotherStream"}'
        }
    ]
}
```

## Resources that require additional information

Certain resources require that you provide additional information about the resources that you want to list as
part of your request. In these cases, you must use the `ResourceModel` parameter to specify these
properties.

The table below lists these resources, and the properties you to specify in the `ResourceModel`
parameter during list requests.

| Resources                                                                                                                                                                                                                                                                            | Required properties                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| [`AWS::ApiGateway::DocumentationVersion`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.md")                                                 | `RestApiId`                                                                                                            |
| [`AWS::ApiGateway::Step`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.md")                                                                                               | `RestApiId`                                                                                                            |
| [`AWS::CloudFormation::ResourceVersion`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.md")                                                    | `TypeArn` or `TypeName`                                                                                                |
| [`AWS::CustomerProfiles::Integration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.md")                                                          | `DomainName`                                                                                                           |
| [`AWS::CustomerProfiles::ObjectType`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.md")                                                             | `DomainName`                                                                                                           |
| [`AWS::EC2::TransitGatewayMulticastGroupMember`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.md")                            | `TransitGatewayMulticastDomainId`                                                                                      |
| [`AWS::EC2::TransitGatewayMulticastGroupSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.md")                            | `TransitGatewayMulticastDomainId`                                                                                      |
| [`AWS::ECS::TaskSet`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.md")                                                                                                             | `Cluster`, `Service`, and `ID`                                                                                         |
| [`AWS::EKS::AddOn`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.md")                                                                                                                   | `ClusterName`                                                                                                          |
| [`AWS::EKS::FargateProfile`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.md")                                                                                        | `ClusterName`                                                                                                          |
| [`AWS::ElasticLoadBalancingV2::Listener`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.md")                                                 | `LoadBalancerArn`                                                                                                      |
| [`AWS::ElasticLoadBalancingV2::ListenerRule`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.md")                                     | `ListenerArn`                                                                                                          |
| [`AWS::Glue::Attach::SchemaVersion`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.md")                                                                                | • `SchemaDefinition`, `Schema/RegistryName`, and<br>`Schema/SchemaName`<br>• `SchemaDefinition` and `Schema/SchemaArn` |
| [`AWS::Glue::Attach::SchemaVersionMetadata`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.md")                                                        | `SchemaVersionId`                                                                                                      |
| [`AWS::IoTSiteWise::AccessPolicy`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.md")                                                                      | • /`AccessPolicyResource`/`Portal`<br>• /`AccessPolicyResource`/`Project`                                              |
| [`AWS::IoTSiteWise::Dashboard`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.md")                                                                               | `ProjectId`                                                                                                            |
| [`AWS::IoTSiteWise::Project`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.md")                                                                                     | `PortalId`                                                                                                             |
| [`AWS::Kendra::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.md")                                                                                           | `IndexId`                                                                                                              |
| [`AWS::Kendra::Faq`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.md")                                                                                                                | `IndexId`                                                                                                              |
| [`AWS::MediaConnect::FlowEntitlement`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.md")                                                          | `FlowArn`                                                                                                              |
| [`AWS::MediaConnect::FlowOutput`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.md")                                                                         | `FlowArn`                                                                                                              |
| [`AWS::MediaConnect::FlowSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.md")                                                                         | `FlowArn`                                                                                                              |
| [`AWS::MediaConnect::FlowVpcInterface`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.md")                                                       | `FlowArn`                                                                                                              |
| [`AWS::MediaPackage::Asset`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.md")                                                                                        | `PackagingGroupId`                                                                                                     |
| [`AWS::MediaPackage::PackagingConfiguration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.md")                                     | `PackagingGroupId`                                                                                                     |
| [`AWS::NetworkFirewall::LoggingConfiguration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.md")                                  | • `FirewallArn`<br>• `FirewallName`                                                                                    |
| [`AWS::QuickSight::Analysis`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.md")                                                                                     | `AwsAccountId`                                                                                                         |
| [`AWS::QuickSight::Dashboard`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.md")                                                                                  | `AwsAccountId`                                                                                                         |
| [`AWS::QuickSight::DataSet`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.md")                                                                                        | `AwsAccountId`                                                                                                         |
| [`AWS::QuickSight::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.md")                                                                               | `AwsAccountId`                                                                                                         |
| [`AWS::QuickSight::Template`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.md")                                                                                     | `AwsAccountId`                                                                                                         |
| [`AWS::QuickSight::Theme`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.md")                                                                                              | `AwsAccountId`                                                                                                         |
| [`AWS::RDS::DBProxyTargetGroup`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.md")                                                                            | `DBProxyName`                                                                                                          |
| [`AWS::S3Outposts::AccessPoint`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.md")                                                                            | `Bucket`                                                                                                               |
| [`AWS::S3Outposts::Bucket`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.md")                                                                                           | `OutpostId`                                                                                                            |
| [`AWS::SSO::Assignment`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.md")                                                                                                    | `InstanceArn`, `PermissionSetArn`, `PrincipalId`,<br>`PrincipalType`, `TargetId`, and `TargetType`                     |
| [`AWS::SSO::InstanceAccessControlAttributeConfiguration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.md") | `InstanceArn`                                                                                                          |
| [`AWS::SSO::PermissionSet`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.md")                                                                                           | `InstanceArn` and `PermissionSetArn`                                                                                   |
| [`AWS::WAFv2::WebACL`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.md")                                                                                                          | `Scope`                                                                                                                |
