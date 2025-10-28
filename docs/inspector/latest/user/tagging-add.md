# Adding tags

You can add tags to Amazon Inspector resources.
These resources include suppression rules and CIS scan configurations.
Tags help you categorize AWS resources based on specific criteria.
This topic describes how to add tags to Amazon Inspector resources.

## Adding tags to Amazon Inspector resources

You can tag [suppression rules](findings-managing-supression-rules.md "findings-managing-supression-rules.md") and [CIS scan configurations](scanning-cis-create-cis-scan-configuration.md "scanning-cis-create-cis-scan-configuration.md").
The following procedures describe how to add tags in the console and with the Amazon Inspector API.

### Adding tags in the console

You can add tags to Amazon Inspector resources in the console.

###### Adding tags to suppression rules

You can add tags to suppression rules during creation.
For more information, see [Creating a suppression rule](findings-managing-supression-rules.md#findings-managing-supression-rules-create "findings-managing-supression-rules.md#findings-managing-supression-rules-create").

You can also edit a suppression rule to include tags.
For more information, see [Editing a suppression rule](findings-managing-supression-rules.md#findings-managing-supression-rules-change "findings-managing-supression-rules.md#findings-managing-supression-rules-change").

###### Adding tags to a CIS scan configuration

You can add tags to a CIS scan configuration during creation.
For more information, see [Creating a CIS scan configuration](scanning-cis-create-cis-scan-configuration.md "scanning-cis-create-cis-scan-configuration.md").

You can also edit a CIS scan configuration to include tags.
For more information, see [Editing a CIS scan configuration](scanning-cis-view-edit-cis-scan-configuration.md "scanning-cis-view-edit-cis-scan-configuration.md").

### Adding tags with the Amazon Inspector API

You can add tags to Amazon Inspector resources with the Amazon Inspector API.

###### Adding tags to Amazon Inspector resources

Use the `TagResource` API to add tags to Amazon Inspector resources.
You must include the ARN of the resource and the key-value pair for the tag in the command.
The following example command uses an empty resource ARN for a suppression filter.
The key is `CostAllocation` and value is `dev`.
For information about resource types for Amazon Inspector, see [Actions, resources, and condition keys for Amazon Inspector2](../../../service-authorization/latest/reference/list_amazoninspector2.md#amazoninspector2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazoninspector2.md#amazoninspector2-resources-for-iam-policies") in the _Service Authorization Reference_.

```
aws inspector2 tag-resource \
--resource-arn "`arn:${Partition}:inspector2:${Region}:${Account}:owner/${OwnerId}/filter/${FilterId}`" \
--tags CostAllocation=dev \
--region us-west-2
```

###### Adding tags to suppression rules during creation

Use the `CreateFilter` API to add tags to a suppression rule during creation.

```
aws inspector2 create-filter \
--name "ExampleSuppressionRuleECR" \
--action SUPPRESS \
--filter-criteria 'resourceType=[{comparison="EQUALS", value="AWS_ECR_IMAGE"}]' \
--tags Owner=ApplicationSecurity \
--region us-west-2
```

###### Adding tags to a CIS scan configuration

Use the `CreateCisScanConfiguration` API to add a tag to a CIS scan configuration.

```
aws inspector2 create-cis-scan-configuration \
--scan-name "CreateConfigWithTagsSample" \
--security-level LEVEL_2 \
--targets accountIds=SELF,targetResourceTags={InspectorCisScan=True} \
--schedule 'daily={startTime={timeOfDay=11:10,timezone=UTC}}' \
--tags Owner=SecurityEngineering \
--region us-west-2
```
