# Application aware incident notifications in AMS

Use application aware automated incident notifications to customize your communication experience for support cases that AMS creates on your behalf. When you use this feature, AMS retrieves custom workload preferences from [AWS Service Catalog AppRegistry](../../../servicecatalog/latest/arguide/intro-app-registry.md "../../../servicecatalog/latest/arguide/intro-app-registry.md") to enrich your AMS incident communications with metadata about your applications and to customize the severity of support cases created by AMS on your behalf. To use this feature, you must first onboard to AWS Service Catalog AppRegistry.

To learn more about AMS Accelerate monitoring defaults, see
[Monitoring and event management in AMS Accelerate](acc-mon-event-mgmt.md "acc-mon-event-mgmt.md").

## Onboard to AppRegistry and create applications

To onboard to AppRegistry, see [Getting started with AppRegistry](../../../servicecatalog/latest/arguide/getting-started-ar.md "../../../servicecatalog/latest/arguide/getting-started-ar.md") in the _AWS Service Catalog AppRegistry Administrator Guide_.
After onboarding, use one of the following methods to create applications:

1. **AWS console:** To learn more about creating an application in AppRegistry through the AWS console,
   see [Creating Applications](../../../servicecatalog/latest/arguide/create-apps.md "../../../servicecatalog/latest/arguide/create-apps.md") in the _AWS Service Catalog AppRegistry Administrator Guide_.
2. **CloudFormation:** You can define your AppRegistry application just like you define any other resource. For more information,
   see [AWS Service Catalog AppRegistry resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_ServiceCatalogAppRegistry.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ServiceCatalogAppRegistry.md") in the _AWS CloudFormation User Guide_.
3. **AMS automation:** To simplify the application registration process, AMS provides you with the SSM automation document `AWSManagedServices-CreateAppRegistryApplication`.
   To use this method, invoke the document from the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/"), or with the AWS CLI as described in the following example.

```
# The following registers a new application with customized severity
aws ssm start-automation-execution \
  --document-name "AWSManagedServices-CreateAppRegistryApplication" \
  --parameters '{"ResourceAssociationType":["TAGS"],"AppTagValue":["MyApp"],"CFNStackNames":[],"ApplicationName":["BananaStand"],"ApplicationDescription":["This is my banana stand application"],"AppCriticality":["normal"],"AutomationAssumeRole":["arn:aws:iam::123456789012:role/SSMAdminRole"]}' \
  --region us-east-1
# The following registers a new application with no customizations
aws ssm start-automation-execution \
  --document-name "AWSManagedServices-CreateAppRegistryApplication" \
  --parameters '{"ResourceAssociationType":["TAGS"],"AppTagValue":["MyApp"],"CFNStackNames":[],"ApplicationName":["BananaStand"],"ApplicationDescription":["This is my banana stand application"],"AppCriticality":["unset"],"AutomationAssumeRole":["arn:aws:iam::123456789012:role/SSMAdminRole"]}' \
  --region us-east-1
# You can also register applications using CloudFormation stacks
aws ssm start-automation-execution \
  --document-name "AWSManagedServices-CreateAppRegistryApplication" \
  --parameters '{"ResourceAssociationType":["STACKS"],"AppTagValue":[""],"CFNStackNames":["arn:aws:cloudformation:us-east-1:123456789012:stack/stack-2343eddq/1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"],"ApplicationName":["BananaStand"],"ApplicationDescription":["This is my banana stand application"],"AppCriticality":["unset"],"AutomationAssumeRole":["arn:aws:iam::123456789012:role/SSMAdminRole"]}' \
  --region us-east-1
```

## Create tags to enable case enrichment

You must tag your applications before AMS can access application metadata. The following table lists the required tags.

Tags with the prefix `ams:rt:` are applied through
[Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md").

| Tag key            | Tag value |
| ------------------ | --------- |
| ams-managed        | true      |
| ams:rt:ams-managed | true      |

## Customize AMS support case severity for your applications

You can customize the severity of AMS created support cases by specifying how critical your application is for your organization. This setting is controlled by an attribute group associated
with your application in AppRegistry. The name of the attribute group name must match the following pattern:

```
AMS.<ApplicationName>.CommunicationOptions
```

In the preceding pattern, the `ApplicationName` must match the name used in AppRegistry when you created the application.

Example content:

```
{
"SchemaVersion": "1.0",
"Criticality": "low"
}
```

**SchemaVersion**

This determines the schema version that you're using and the subset of features available to use.

| Schema version | Feature                                                     |
| -------------- | ----------------------------------------------------------- |
| 1.0            | Customized support case severity based on Criticality value |

**Criticality**

The criticality of this application determines the severity of the support cases created by the AMS automated systems.

Valid values:

```
low|normal|high|urgent|critical
```

For more information on severity levels, see [SeverityLevel](../../../awssupport/latest/APIReference/API_SeverityLevel.md "../../../awssupport/latest/APIReference/API_SeverityLevel.md") in the _AWS Support API Reference_.

Required: Yes

## Review required permissions

To use this feature, AMS requires access to the following AWS Identity and Access Management permissions:

- iam:ListRoleTags
- iam:ListUserTags
- resourcegroupstaggingapi:GetResources
- servicecatalog-appregistry:GetApplication
- servicecatalog-appregistry:ListAssociatedAttributeGroups
- servicecatalog-appregistry:GetAttributeGroup

###### Important

Make sure that there isn't an IAM policy or service control policy (SCP) that denies the preceding actions.

The API calls are made by the `ams-access-admin` role. The following is an example of what you might see:

```
arn:aws:sts::111122223333:assumed-role/ams-access-admin/AMS-AMSAppMetadataLookup-*
```
