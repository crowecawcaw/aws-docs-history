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

| Available settings                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name of the Change Manager category to assign to AWS Change<br>Template from AWS Systems Manager Change Manager | The setting correlates to the Catalog item category in<br>ServiceNow to which the synchronized AWS Change templates are<br>associated.                                                                                                                                                                                                                                          |
| Assignment Group (`SYS_ID`) to use when creating<br>Change Requests from Change Template                        | The setting automatically assigns the change requests created<br>from the change templates to the Assignment Group that relates<br>to the `sys_id`.                                                                                                                                                                                                                             |
| Default role name that allows the Automation to perform the<br>actions on your behalf                           | The setting contains the default role to create change requests<br>from AWS change templates. The setting is available if the<br>user does not fill in the `AutomationAssumeRole`<br>field when requesting a change from AWS Systems Manager Change<br>Manager. The value is case-sensitive and must exist<br>in every account using the AWS Systems Manager Change<br>Manager. |
| AWS CloudTrail Lake: Event Data Store Name                                                                      | Defines the Name of the AWS CloudTrail Lake: Event Data Store Name<br>to target.<br>Note that to use AWS Systems Manager Change Manager's CloudTrail<br>Lake Event integration an Event Data Store with this Name MUST exist<br>in all regions defined in AWS Accounts with AWS Systems Manager<br>Change Manager enabled.                                                      |
| AWS CloudTrail Lake: Maximum number of events to retrieve per<br>synchronization                                | Default : 1000                                                                                                                                                                                                                                                                                                                                                                  |
