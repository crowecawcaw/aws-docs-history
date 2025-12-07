# GuardDuty API changes in March

2023

The GuardDuty APIs configure protection features that don't belong to the list of [GuardDuty foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md"). A feature object
contains feature details, such as feature name and status, and may contain additional
configuration for some of the protection plans. This migration affects the following APIs in the
_Amazon GuardDuty API Reference_:

- [CreateDetector](../APIReference/API_CreateDetector.md "../APIReference/API_CreateDetector.md")
- [GetDetector](../APIReference/API_GetDetector.md "../APIReference/API_GetDetector.md")
- [UpdateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md")
- [GetMemberDetectors](../APIReference/API_GetMemberDetectors.md "../APIReference/API_GetMemberDetectors.md")
- [UpdateMemberDetectors](../APIReference/API_UpdateMemberDetectors.md "../APIReference/API_UpdateMemberDetectors.md")
- [DescribeOrganizationConfiguration](../APIReference/API_DescribeOrganizationConfiguration.md "../APIReference/API_DescribeOrganizationConfiguration.md")
- [UpdateOrganizationConfiguration](../APIReference/API_UpdateOrganizationConfiguration.md "../APIReference/API_UpdateOrganizationConfiguration.md")
- [GetRemainingFreeTrialDays](../APIReference/API_GetRemainingFreeTrialDays.md "../APIReference/API_GetRemainingFreeTrialDays.md")
- [GetUsageStatistics](../APIReference/API_GetUsageStatistics.md "../APIReference/API_GetUsageStatistics.md")

## Features compared to data

sources

Historically, all GuardDuty features were passed through a `dataSources` object in
the API. From March 2023, GuardDuty prefers `features` object instead of the
`dataSources` object in the API. All earlier data sources have corresponding
features, but newer features may not have corresponding data sources.

The following list shows the comparison between `dataSources` and
`features` object when passed through an API:

- The `dataSources` object contains objects for each protection type and its
  status. The `features` object is a list of available features that correspond to
  each protection type within GuardDuty.

Starting March 2023, feature activation will be the only way to configure new GuardDuty
features in your AWS environment.

- The `dataSources` schema in the API request or response is the same in each
  AWS Region where GuardDuty is available. However, every feature may not be available in each
  Region. Therefore, the available feature names may differ based on the Region.

## Understanding how APIs with

features work

The GuardDuty APIs will continue to return a `dataSources` object as applicable, and
they will also return a `features` object containing the same information in a
different format. GuardDuty features launched before March 2023 will be available through
`dataSources` object and `features` object. GuardDuty launched features since
March 2023 will only be available through the `features` object. You can't create or
update a detector, or describe your AWS Organizations using both `dataSources` and
`features` object notation in the same API request. To enable GuardDuty protection
types, you will need to migrate your existing data sources to the `features` object
by using the same APIs that now include the `features` object too.

###### Note

GuardDuty will not add new data source after this modification.

GuardDuty has deprecated the use of data sources that are associated with the protection plans.
However, it still supports the [GuardDuty foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md"). The GuardDuty best practices recommend using features for
enabling or editing the configuration for any protection plan in your account.

## Incorporating feature changes in

APIs

- If you manage GuardDuty configurations through APIs, SDKs, or CloudFormation template, and want to
  enable potential new GuardDuty features, you will need to modify your code and template,
  respectively. For more information, see the updated APIs in the _[Amazon GuardDuty API Reference](../APIReference/API_Operations.md "../APIReference/API_Operations.md")_.
- For GuardDuty features configured prior to this upgrade, you can continue using the APIs,
  SDKs, or CloudFormation template. However, we recommend that you switch to using `feature`
  object.

All the data sources have an equivalent feature object. For more information, see [Mapping
dataSources to features](#guardduty-feature-enablement-datasource-relation "#guardduty-feature-enablement-datasource-relation").

- Presently, `additionalConfiguration` in the `features` object is
  only available for certain protection types.
  - For such protection types, if your feature's `AdditionalConfiguration`
    `status` is set to `ENABLED` but your feature's configuration
    `status` is not set to `ENABLED`, GuardDuty will not take any action in
    this case.
  - The following APIs get impacted by this:
    - [UpdateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md")
    - [UpdateMemberDetectors](../APIReference/API_UpdateMemberDetectors.md "../APIReference/API_UpdateMemberDetectors.md")
    - [UpdateOrganizationConfiguration](../APIReference/API_UpdateOrganizationConfiguration.md "../APIReference/API_UpdateOrganizationConfiguration.md")

## Mapping

`dataSources` to `features`

The following table shows the mapping of protection types, `dataSources`, and
`features`.

| GuardDuty protection type                                                                                                | Data source name\*                                                                                                                         | Feature name                                 |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| [VPC Flow Logs](guardduty_data-sources.md#guardduty_vpc "guardduty_data-sources.md#guardduty_vpc")                       | `flowLogs` (read only; can't be modified)                                                                                                  | `FLOW_LOGS` (read only; can't be modified)   |
| [Route53 Resolver DNS query logs](guardduty_data-sources.md#guardduty_dns "guardduty_data-sources.md#guardduty_dns")     | `dnsLogs` (read only; can't be modified)                                                                                                   | `DNS_LOGS` (read only; can't be modified)    |
| [CloudTrail events](guardduty_data-sources.md#guardduty_controlplane "guardduty_data-sources.md#guardduty_controlplane") | `cloudTrail` (read only; can't be modified)                                                                                                | `CLOUD_TRAIL` (read only; can't be modified) |
| [S3](s3-protection.md "s3-protection.md")                                                                                | `s3Logs`                                                                                                                                   | `S3_DATA_EVENTS`                             |
| [EKS Protection](kubernetes-protection.md "kubernetes-protection.md")                                                    | `kubernetes.auditlogs`                                                                                                                     | `EKS_AUDIT_LOGS`                             |
| [Malware Protection for EC2](malware-protection.md "malware-protection.md")                                              | `malwareProtection.scanEc2InstanceWithFindings.ebsVolumes`                                                                                 | `EBS_MALWARE_PROTECTION`                     |
| [RDS Login<br>events](rds-protection.md "rds-protection.md")                                                             | GuardDuty provides only feature activation support for these protection types.                                                             | `RDS_LOGIN_EVENTS`                           |
| EKS Runtime Monitoring                                                                                                   | `EKS_RUNTIME_MONITORING`                                                                                                                   |
| [Runtime Monitoring](runtime-monitoring.md "runtime-monitoring.md")                                                      | `RUNTIME_MONITORING`                                                                                                                       |
| GuardDuty security agent for Amazon EKS clusters                                                                         | `EKS_RUNTIME_MONITORING.additionalConfiguration.EKS_ADDON_MANAGEMENT`<br>`RUNTIME_MONITORING.additionalConfiguration.EKS_ADDON_MANAGEMENT` |
| GuardDuty security agent for Amazon ECS-Fargate clusters                                                                 | `RUNTIME_MONITORING.additionalConfiguration.ECS_FARGATE_AGENT_MANAGEMENT`                                                                  |
| GuardDuty security agent for Amazon EC2 instances                                                                        | `RUNTIME_MONITORING.additionalConfiguration.EC2_AGENT_MANAGEMENT`                                                                          |
| [Lambda Protection](lambda-protection.md "lambda-protection.md")                                                         | `LAMBDA_NETWORK_LOGS`                                                                                                                      |

\*GetUsageStatistics uses its own `dataSource` names. For more
information, see [Monitoring GuardDuty Usage and Estimating Costs](monitoring_costs.md "monitoring_costs.md") or [GetUsageStatistics](../APIReference/API_GetUsageStatistics.md "../APIReference/API_GetUsageStatistics.md").
