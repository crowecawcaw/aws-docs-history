# AMS self-service reports dashboards

AMS self-service reports offers two dashboards:
[Resource Tagger dashboard](#resource-tagger-dashboard "#resource-tagger-dashboard") and
[Security Config Rules dashboard](#sec-config-dashboard "#sec-config-dashboard").

## Resource Tagger dashboard

The AMS Resource Tagger Dashboard provides detailed information about the resources supported by Resource Tagger, as well as the current status of the tags that
Resource Tagger is configured to apply to those resources.

### Resource Tagger coverage by resource type

This dataset consists of a list of resources that have tags managed by Resource Tagger.

Resource coverage by resource type is visualized as four line charts that describe the following metrics:

- **Resource Count:** The total number of resources in the Region, by resource type.
- **Resources Missing Managed Tags:** The total number of resources in the Region, by resource type, that require managed tags but aren't tagged by Resource Tagger.
- **Unmanaged Resources:** The total number of resources in the Region, by resource type, that don't have managed tags applied to them by Resource Tagger. This usually means that these resources are not matched by any Resource Tagger configurations, or are explicitly excluded from configurations.
- **Managed Resources:** Counterpart to **Unmanaged Resources** metric (**Resource Count - Unmanaged Resources**).

The following table lists the data provided by this report.

| Field name                  | Dataset field name                  | Definition                                                                                                                                                                                                                                   |
| --------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Report Datetime             | dataset_datetime                    | The date and time the report was generated (UTC time)                                                                                                                                                                                        |
| AWS account ID              | aws_account_id                      | AWS account ID                                                                                                                                                                                                                               |
| Admin Account Id            | aws_admin_account_id                | Trusted AWS Organizations account enabled by you.                                                                                                                                                                                            |
| Region                      | region                              | AWS Region                                                                                                                                                                                                                                   |
| Resource Type               | resource_type                       | This field identifies the type of resource. Only resource types supported by Resource Tagger are included.                                                                                                                                   |
| Resource Count              | resource_count                      | Number of resources (of the specified resource type) deployed in this Region.                                                                                                                                                                |
| ResourcesMissingManagedTags | resource_missing_managed_tags_count | Number of resources (of the specified resource type) that require managed tags, according to the configuration profiles, but have not yet been tagged by Resource Tagger.                                                                    |
| UnmanagedResources          | unmanaged_resource_count            | Number of resources (of the specified resource type) with no managed tags applied by Resource Tagger. Typically, these resources didn't match any Resource Tagger configuration block, or are explicitly excluded from configuration blocks. |

### Resource Tagger configuration rule compliance

This dataset consists of a list of resources in an AWS Region, by resource type, that have a certain configuration profile applied to them. It's visualized as a line chart.

The following table lists the data provided by this report.

| Field name               | Dataset field name       | Definition                                                                                                                                                                                                                                   |
| ------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Report Datetime          | dataset_datetime         | The date and time the report was generated (UTC time)                                                                                                                                                                                        |
| AWS account ID           | aws_account_id           | AWS account ID                                                                                                                                                                                                                               |
| Admin Account Id         | aws_admin_account_id     | Trusted AWS Organizations account enabled by you.                                                                                                                                                                                            |
| Region                   | region                   | AWS Region                                                                                                                                                                                                                                   |
| Resource Type            | resource_type            | This field identifies the type of resource. Only resource types supported by Resource Tagger are included.                                                                                                                                   |
| Configuration Profile ID | configuration_profile_id | The ID of the Resource Tagger configuration profile. A configuration profile is used to define policies and rules used to tag your resources.                                                                                                |
| MatchingResourceCount    | resource_count           | Number of resources (of the specified resource type) that match the Resource Tagger configuration profile ID. For a resource to match the configuration profile, the profile must be enabled and the resource must match the profile's rule. |

### Resource Tagger non-compliant resources

This dataset consists of a list of resources that are non-compliant for a single Resource Tagger configuration.
This data is a daily snapshot of resource compliance, showing the state of customer resources at the time these reports are delivered to customer accounts (there isn't a historical view). It's visualized as a pivot table consisting of resources that are non-complaint for a given configuration.

The following table lists the data provided by this report.

| Field name               | Dataset field name       | Definition                                                                                                                                    |
| ------------------------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Report Datetime          | dataset_datetime         | The date and time the report was generated (UTC time)                                                                                         |
| AWS account ID           | aws_account_id           | AWS account ID                                                                                                                                |
| Admin Account Id         | aws_admin_account_id     | Trusted AWS Organizations account enabled by you.                                                                                             |
| Region                   | region                   | AWS Region                                                                                                                                    |
| Resource Type            | resource_type            | This field identifies the type of resource. Only resource types supported by Resource Tagger are included.                                    |
| Resource ID              | resource_id              | The unique identifier for resources supported by Resource Tagger.                                                                             |
| Coverage State           | coverage_state           | This field indicates if the resource is tagged as configured by the Resource Tagger configuration ID.                                         |
| Configuration Profile ID | configuration_profile_id | The ID of the Resource Tagger configuration profile. A configuration profile is used to define policies and rules used to tag your resources. |

## Security Config Rules dashboard

The Security Config Rules Dashboard provides an in-depth look at resource and AWS Config rule compliance of AMS accounts. You can filter the report by rule severity to prioritize the most critical findings.
The following table lists the data provided by this report.

| Field name              | Dataset field name      | Definition                                                                                                                                                                                                                                                    |
| ----------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS account ID          | AWS account ID          | The account ID tied to related resources.                                                                                                                                                                                                                     |
| Admin Account Id        | aws_admin_account_id    | Trusted AWS Organizations account enabled by you.                                                                                                                                                                                                             |
| report datetime         | Report Date             | The date and time the report was generated.                                                                                                                                                                                                                   |
| customer_name           | Customer Name           | The customer name.                                                                                                                                                                                                                                            |
| account_name            | Account Name            | The name associated with the account ID                                                                                                                                                                                                                       |
| resource_id             | Resource ID             | An identifier for a resource.                                                                                                                                                                                                                                 |
| resource_region         | Resource Region         | The AWS Region where the resource is located.                                                                                                                                                                                                                 |
| resource_type           | Resource Type           | The AWS service or resource type.                                                                                                                                                                                                                             |
| resource_name           | Resource Name           | The name for the resource.                                                                                                                                                                                                                                    |
| resource_ams_flag       | Resource AMS Flag       | If the resource is AMS owned, then this flag is set to **TRUE**. If the resource is customer-owned, then this flag is set to **FALSE**. If ownership is not known, then this flag is set to **UNKNOWN**.                                                      |
| config_rule             | Config Rule             | The non-customizable name for the config rule.                                                                                                                                                                                                                |
| config_rule_description | Config Rule Description | A description of the config rule.                                                                                                                                                                                                                             |
| source_identifier       | Source Identifier       | A unique identifier for the managed config rule and no identifier for a custom config rule.                                                                                                                                                                   |
| compliance_flag         | Compliance Flag         | Shows if the resources are compliant or non-compliant with the config rules.                                                                                                                                                                                  |
| rule_type               | Rule Type               | Indicates if the rule is predefined or custom built.                                                                                                                                                                                                          |
| exception_flag          | Exception Flag          | The resource exception flag shows the risk acceptance against a noncompliant resource. If the resource exception flag is **TRUE\*<br>• for a resource, then the resource is exempted. If the exception flag is **NULL\*\*, then the resource is not exempted. |
| cal_dt                  | Date                    | The evaluation date of the rule.                                                                                                                                                                                                                              |
| remediation_description | Remediation Description | A description of how to remediate rule compliance.                                                                                                                                                                                                            |
| severity                | Severity                | Config rule severity indicates the impact of non-compliance.                                                                                                                                                                                                  |
| customer_action         | Customer Action         | Action needed by you to remediate thus rule.                                                                                                                                                                                                                  |
| recommendation          | Recommendation          | A description of what the config rule checks for.                                                                                                                                                                                                             |
| remediation_category    | Remediation Category    | The default actions that AMS takes when this rule becomes non-compliant.                                                                                                                                                                                      |
