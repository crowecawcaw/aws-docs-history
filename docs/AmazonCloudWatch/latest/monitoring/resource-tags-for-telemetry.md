# Resource tags for telemetry

Use Amazon CloudWatch to discover, visualize, and alert on your AWS infrastructure metrics by AWS resource tags. You can set up comprehensive monitoring with CloudWatch metrics and alarms using tags. This helps monitor cloud infrastructure at scale by adapting
alarms and metrics analysis as resources change.

###### Important

Use ASCII characters in resource tags to ensure compatibility with Metrics Insights queries. Tags containing Unicode characters (such as international characters, emojis, or special symbols) does not appear in Metrics Insights queries and the results will return empty.

To begin discovering and visualizing your telemetry by tags, you must first enable the resource tags for telemetry feature for your AWS account. When you enable this feature, Resource Explorer creates an AWS index and managed view that
indexes and discovers resources and tags in your account. For more information, see [Index](../../../resource-explorer/latest/apireference/API_Index.md "../../../resource-explorer/latest/apireference/API_Index.md") in the Resource
Explorer API reference guide and [AWS managed views](../../../resource-explorer/latest/userguide/aws-managed-views.md "../../../resource-explorer/latest/userguide/aws-managed-views.md") in the Resource Explorer user guide. CloudWatch uses this information to enrich your AWS
infrastructure metrics with related AWS resource tags. You can enable **resource tags for telemetry** at no additional cost.

###### Topics

- [Enable resource tags on telemetry](EnableResourceTagsOnTelemetry.md "EnableResourceTagsOnTelemetry.md")
- [Using resource tags for telemetry](UsingResourceTagsForTelemetry.md "UsingResourceTagsForTelemetry.md")
- [Disable resource tags on telemetry](DisableResourceTagsOnTelemetry.md "DisableResourceTagsOnTelemetry.md")
- [Troubleshooting](ResourceTagsTelemetryTroubleshooting.md "ResourceTagsTelemetryTroubleshooting.md")
