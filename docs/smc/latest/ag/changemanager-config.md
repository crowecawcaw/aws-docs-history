# Configuring Support integration system properties with ServiceNow

The AWS Systems Manager Change Manager integration for AWS Service Management
Connector aligns with the Change Management process in ServiceNow. It enables you to
align the internal Change Management process for executing pre-approved change
templates directly from a ServiceNow instance.

###### \*\*To conﬁgure the AWS Support integration system

properties\*\*

1. In the navigator, enter `AWS Service
Management`.
2. Choose **System Properties**, then **AWS Systems Manager Change Manager**.
3. Review the available settings and recommendations in the table
   below.

| Available settings                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name of the Change Manager category to assign to AWS Change Template from AWS Systems Manager Change Manager | The setting correlates to the Catalog item category in ServiceNow to which the synchronized AWS Change templates are associated.                                                                                                                                                                                                                              |
| Assignment Group (`SYS_ID`) to use when creating Change Requests from Change Template                        | The setting automatically assigns the change requests created from the change templates to the Assignment Group that relates to the `sys_id`.                                                                                                                                                                                                                 |
| Default role name that allows the Automation to perform the actions on your behalf                           | The setting contains the default role to create change requests from AWS change templates. The setting is available if the user does not fill in the `AutomationAssumeRole` field when requesting a change from AWS Systems Manager Change Manager. The value is case-sensitive and must exist in every account using the AWS Systems Manager Change Manager. |
| AWS CloudTrail Lake: Event Data Store Name                                                                   | Defines the Name of the AWS CloudTrail Lake: Event Data Store Name to target. Note that to use AWS Systems Manager Change Manager's CloudTrail Lake Event integration an Event Data Store with this Name MUST exist in all regions defined in AWS Accounts with AWS Systems Manager Change Manager enabled.                                                   |
| AWS CloudTrail Lake: Maximum number of events to retrieve per synchronization                                | Default : 1000                                                                                                                                                                                                                                                                                                                                                |
