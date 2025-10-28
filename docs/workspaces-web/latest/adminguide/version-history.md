# Release history for Amazon WorkSpaces Secure Browser

On May 20, 2024, Amazon WorkSpaces Web was renamed to Amazon WorkSpaces Secure Browser. For existing customers,
there was no change to how they manage users or resources with the service. The following list
describes the applicable updates that also took place as a result of this rename.

The _workspaces-web_ API namespace remains unchanged for backward
compatibility. As a result, the following resources are still the same:

- CLI commands.
- Amazon CloudWatch metrics. For more information, see [Monitoring Amazon WorkSpaces Secure Browser with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- Service endpoints. For more information, see [Amazon WorkSpaces Secure Browser endpoints and quotas](../../../general/latest/gr/workspacesweb.md "../../../general/latest/gr/workspacesweb.md").
- AWS CloudFormation resources. For more information, see [Amazon WorkSpaces Secure Browser resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_WorkSpacesWeb.md "../../../AWSCloudFormation/latest/UserGuide/AWS_WorkSpacesWeb.md").
- Service-linked role containing _workspaces-web_. For more information,
  see [Using service-linked roles for
  Amazon WorkSpaces Secure Browser](using-service-linked-roles.md "using-service-linked-roles.md").
- Console URLs containing _workspaces-web_.
- Documentation URLs containing _workspaces-web_. For more information,
  see [Amazon WorkSpaces Secure Browser
  Documentation](../../../workspaces-web.md "../../../workspaces-web.md").
- Existing ReadOnly managed role. For more information, see [AWS managed policies for WorkSpaces Secure Browser](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
- KMS grant name.
- UAL(User-Activity Logging) Kinesis stream prefix.
  In addition, existing portal URLs remain the same. URLs for portals created before May 20,
  2024 used the format <UUID>.workspaces-web.com. WorkSpaces Secure Browser portals continue to use this format and
  the workspaces-web.com domain.
