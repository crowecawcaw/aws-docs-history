# Viewing the number of resources monitored by Alarm Manager for Accelerate

Alarm Manager sends metrics every hour to Amazon CloudWatch, in the `AMS/AlarmManager` namespace. Metrics are emitted only for resource types supported by Alarm Manager.

| Metric Name                   | Dimensions                                | Description                                                                                                                                                                                                                                                                            |
| ----------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ResourceCount                 | Component, ResourceType                   | Number of resources (of the specified resource type) deployed in this Region.<br>Units: Count                                                                                                                                                                                          |
| ResourcesMissingManagedAlarms | Component, ResourceType                   | Number of resources (of the specified resource type) that require managed alarms, but Alarm Manager has not applied the alarms yet.<br>Units: Count                                                                                                                                    |
| UnmanagedResources            | Component, ResourceType                   | Number of resources (of the specified resource type) that do not have any<br>managed alarms applied to them by Alarm Manager. Typically, these resources did not<br>match any Alarm Manager configuration block, or are explicitly excluded from configuration blocks.<br>Units: Count |
| MatchingResourceCount         | Component, ResourceType, ConfigClauseName | Number of resources (of the specified resource type) that match the Alarm<br>Manager configuration block. For a resource to match the configuration block, the<br>block must be enabled, and the resource must have same tags specified in the configuration block.<br>Units: Count    |

These metrics are also viewable as graphs, in the **AMS-Alarm-Manager-Reporting-Dashboard**. To see the dashboard, from the
AWS CloudWatch management console, select **AMS-Alarm-Manager-Reporting-Dashboard**. By default, the graphs in this
dashboard display the data for the prior 12-hour period.

AMS Accelerate deploys CloudWatch alarms to your account to detect significant increases in the number of unmanaged resources, for example, resources
excluded from management by AMS Alarm Manager. AMS Operations will investigate increases in unmanaged resources that
exceed: either three resources of the same type, or a 50% increase over all resources of the
same type. If the change does not appear to be deliberate, AMS Operations may contact you to review the change.
