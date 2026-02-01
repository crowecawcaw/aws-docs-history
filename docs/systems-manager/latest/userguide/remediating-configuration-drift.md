• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Diagnosing and remediating drifted

configurations

Systems Manager can diagnose and then help you remediate the following types of drifted
configurations:

- Core setup for organization member accounts
- Core setup for delegated administrator account
- Core setup for your account
  Use the following procedure to attempt to remediate these types of drifted
  configurations.

###### To diagnose and remediate drifted configurations

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Diagnose and
   remediate**.
3. Choose the **Deployment issues** tab.
4. In the **Drifted deployments** section, review the list of
   finding for failed deployments.

-or-

To run a new diagnosis, choose **Detect drift**. 5. In the **Setup step** column, choose the name of a finding to
review additional details about the issue. For example: **Core setup for
organization member accounts**. 6. In the detail page for that failed deployment, you can view a list of accounts
and how many Regions in each have experienced configuration drifts. 7. Select an account ID to view information about the reason for configuration
drifts in that account. 8. In the **Drifted resources** area, the
**Resource** column reports names of resources that have
experienced drift. The **Drift type** column reports whether
the resource was modified or deleted.. 9. To redeploy the intended configuration, choose
**Redeploy**.
