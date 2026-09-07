

# Release history for Amazon WorkSpaces Secure Browser
<a name="version-history"></a>

On May 20, 2024, Amazon WorkSpaces Web was renamed to Amazon WorkSpaces Secure Browser. For existing customers, there was no change to how they manage users or resources with the service. The following list describes the applicable updates that also took place as a result of this rename. 

The *workspaces-web* API namespace remains unchanged for backward compatibility. As a result, the following resources are still the same:
+ CLI commands.
+  Amazon CloudWatch metrics. For more information, see [Monitoring Amazon WorkSpaces Secure Browser with Amazon CloudWatch](monitoring-cloudwatch.md).
+ Service endpoints. For more information, see [Amazon WorkSpaces Secure Browser endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/workspacesweb.html).
+ AWS CloudFormation resources. For more information, see [Amazon WorkSpaces Secure Browser resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpacesWeb.html).
+ Service-linked role containing *workspaces-web*. For more information, see [Using service-linked roles for Amazon WorkSpaces Secure Browser](using-service-linked-roles.md).
+ Console URLs containing *workspaces-web*.
+ Documentation URLs containing *workspaces-web*. For more information, see [Amazon WorkSpaces Secure Browser Documentation](https://docs.aws.amazon.com/workspaces-web).
+ Existing ReadOnly managed role. For more information, see [AWS managed policies for WorkSpaces Secure Browser](security-iam-awsmanpol.md).
+ KMS grant name.
+ UAL(User-Activity Logging) Kinesis stream prefix.

In addition, existing portal URLs remain the same. URLs for portals created before May 20, 2024 used the format <UUID>.workspaces-web.com. WorkSpaces Secure Browser portals continue to use this format and the workspaces-web.com domain.