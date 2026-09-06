

# Discovering resources with AWS Cloud Control API
<a name="resource-operations-list"></a>

Use the `list-resources` command to discover the resources currently provisioned in your AWS account and AWS Region. This includes all resources of the specified resource type, regardless of whether they were provisioned through Cloud Control API, directly through the underlying service, or other mechanism (such as being part of an AWS CloudFormation stack).

The information returned for each resource includes:
+ The resource's primary identifier.
+ Optionally, it may include the *part or all* resource's properties, detailing the current state of the resource. For more information, see [Viewing resource type schemas](resource-types.md#resource-types-schemas).

The follow example returns a list of `AWS::Logs::LogGroup` resources.

```
$ aws cloudcontrol list-resources --type-name AWS::Logs::LogGroup
```

Cloud Control API returns a list of the resources in your account of the specified resource type. For the example , `list-resources` returns the primary identifier and resource properties of all `AWS::Logs::LogGroup` resources in your account, regardless of whether they were provisioned by Cloud Control API. The returned information resembles the following, depending on the resources in your account.

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
$ aws cloudcontrol list-resources --type-name AWS::Kinesis::Stream
```

For Kinesis streams, Cloud Control API returns the primary identifier of each stream, along with a *subset* of the resource properties. In this case, just a single property, `Name`. You could then use a stream's primary identifier with `get-resource` to request the resource's full current state.

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
<a name="resource-operations-list-containers"></a>

Certain resources require that you provide additional information about the resources that you want to list as part of your request. In these cases, you must use the `ResourceModel` parameter to specify these properties.

The table below lists these resources, and the properties you to specify in the `ResourceModel` parameter during list requests.


| Resources | Required properties | 
| --- | --- | 
| [`AWS::ApiGateway::DocumentationVersion`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html) | `RestApiId` | 
| [`AWS::ApiGateway::Step`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html) | `RestApiId` | 
| [`AWS::CloudFormation::ResourceVersion`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html) | `TypeArn` or `TypeName` | 
|  [`AWS::CustomerProfiles::Integration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html)  | `DomainName` | 
|  [`AWS::CustomerProfiles::ObjectType`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html)  | `DomainName` | 
| [`AWS::EC2::TransitGatewayMulticastGroupMember`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html) | `TransitGatewayMulticastDomainId` | 
| [`AWS::EC2::TransitGatewayMulticastGroupSource`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html) | `TransitGatewayMulticastDomainId` | 
| [`AWS::ECS::TaskSet`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html) | `Cluster`, `Service`, and `ID` | 
| [`AWS::EKS::AddOn`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html) | `ClusterName` | 
| [`AWS::EKS::FargateProfile`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html) | `ClusterName` | 
| [`AWS::ElasticLoadBalancingV2::Listener`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html) | `LoadBalancerArn` | 
| [`AWS::ElasticLoadBalancingV2::ListenerRule`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html) | `ListenerArn` | 
| [`AWS::Glue::Attach::SchemaVersion`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html) |  +  `SchemaDefinition`, `Schema/RegistryName`, and `Schema/SchemaName` <br />+  `SchemaDefinition` and `Schema/SchemaArn`   | 
| [`AWS::Glue::Attach::SchemaVersionMetadata`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html) | `SchemaVersionId` | 
| [`AWS::IoTSiteWise::AccessPolicy`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html) |  +  /`AccessPolicyResource`/`Portal` <br />+  /`AccessPolicyResource`/`Project`   | 
| [`AWS::IoTSiteWise::Dashboard`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html) | `ProjectId` | 
| [`AWS::IoTSiteWise::Project`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html) | `PortalId` | 
| [`AWS::Kendra::DataSource`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html) | `IndexId` | 
| [`AWS::Kendra::Faq`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html) | `IndexId` | 
| [`AWS::MediaConnect::FlowEntitlement`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html) | `FlowArn` | 
| [`AWS::MediaConnect::FlowOutput`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html) | `FlowArn` | 
| [`AWS::MediaConnect::FlowSource`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html) | `FlowArn` | 
| [`AWS::MediaConnect::FlowVpcInterface`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html) | `FlowArn` | 
|  [`AWS::MediaPackage::Asset`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html)  | `PackagingGroupId` | 
|  [`AWS::MediaPackage::PackagingConfiguration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html)  | `PackagingGroupId` | 
|  [`AWS::NetworkFirewall::LoggingConfiguration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html)  |  +  `FirewallArn` <br />+  `FirewallName`   | 
| [`AWS::QuickSight::Analysis`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html) | `AwsAccountId` | 
| [`AWS::QuickSight::Dashboard`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html) | `AwsAccountId` | 
| [`AWS::QuickSight::DataSet`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html) | `AwsAccountId` | 
| [`AWS::QuickSight::DataSource`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html) | `AwsAccountId` | 
| [`AWS::QuickSight::Template`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html) | `AwsAccountId` | 
| [`AWS::QuickSight::Theme`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html) | `AwsAccountId` | 
| [`AWS::RDS::DBProxyTargetGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html) | `DBProxyName` | 
|  [`AWS::S3Outposts::AccessPoint`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html)  | `Bucket` | 
|  [`AWS::S3Outposts::Bucket`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html)  | `OutpostId` | 
| [`AWS::SSO::Assignment`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html) | `InstanceArn`, `PermissionSetArn`, `PrincipalId`, `PrincipalType`, `TargetId`, and `TargetType` | 
| [`AWS::SSO::InstanceAccessControlAttributeConfiguration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html) | `InstanceArn` | 
| [`AWS::SSO::PermissionSet`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html) | `InstanceArn` | 
| [`AWS::WAFv2::WebACL`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html) | `Scope` | 