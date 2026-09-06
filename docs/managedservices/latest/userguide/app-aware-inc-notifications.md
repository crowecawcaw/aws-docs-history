

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Application aware incident notifications in AMS
<a name="app-aware-inc-notifications"></a>

Use application aware automated incident notifications to customize your communication experience for support cases that AMS creates on your behalf. When you use this feature, AMS retrieves custom workload preferences from [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) to enrich your AMS incident communications with metadata about your applications and to customize the severity of support cases created by AMS on your behalf. To use this feature, you must first provision AWS Service Catalog AppRegistry in your AMS account.

To learn more about AMS monitoring defaults, see [Monitoring and event management in AMS](monitoring.md).

## Provision AppRegistry in your AMS account and create applications
<a name="case-enrich-onboard-appregistry"></a>

The AppRegistry service is available in Self-service Provisioning (SSP) mode for your AMS account. For instructions on how to request access, see [Use AMS SSP to provision AWS Service Catalog AppRegistry in your AMS account](https://docs.aws.amazon.com/managedservices/latest/userguide/service-catalog-appregistry.html).

After provisioning AppRegistry, use one of the following methods to create applications:

1. **AWS console:** To learn more about creating an application in AppRegistry through the AWS console, see [Creating Applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-apps.html) in the *AWS Service Catalog AppRegistry Administrator Guide*.

1. **CloudFormation:** You can define your AppRegistry application just like you define any other resource. For more information, see [AWS Service Catalog AppRegistry resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ServiceCatalogAppRegistry.html) in the *CloudFormation User Guide*.

## Create tags to enable case enrichment
<a name="app-aware-case-enrichment"></a>

You must tag your applications before AMS can access application metadata. The following table lists the required tag.


| Tag key | Tag value | 
| --- | --- | 
| ams-managed | true | 

## Customize AMS support case severity for your applications
<a name="app-aware-comm-atts"></a>

You can customize the severity of AMS created support cases by specifying how critical your application is for your organization. This setting is controlled by an attribute group associated with your application in AppRegistry. The name of the attribute group name must match the following pattern:

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


| Schema version | Feature | 
| --- | --- | 
| 1.0 | Customized support case severity based on Criticality value | 

**Criticality**

The criticality of this application determines the severity of the support cases created by the AMS automated systems.

Valid values:

```
low|normal|high|urgent|critical 
```

For more information on severity levels, see [SeverityLevel](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_SeverityLevel.html) in the *AWS Support API Reference*.

Required: Yes

## Review required permissions
<a name="app-aware-permissions"></a>

To use this feature, AMS requires access to the following AWS Identity and Access Management permissions:
+ iam:ListRoleTags
+ iam:ListUserTags
+ resourcegroupstaggingapi:GetResources
+ servicecatalog-appregistry:GetApplication
+ servicecatalog-appregistry:ListAssociatedAttributeGroups
+ servicecatalog-appregistry:GetAttributeGroup

**Important**  
Make sure that there isn't an IAM policy or service control policy (SCP) that denies the preceding actions.

The API calls are made by the `ams-access-admin` role. The following is an example of what you might see:

```
arn:aws:sts::111122223333:assumed-role/ams-access-admin/AMS-AMSAppMetadataLookup-*
```