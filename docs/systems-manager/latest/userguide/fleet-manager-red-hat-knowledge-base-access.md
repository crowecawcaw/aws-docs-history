• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Accessing the Red Hat

Knowledge base portal

You can use Fleet Manager, a tool in AWS Systems Manager, to access the Knowledge base portal if you
are a Red Hat customer. You are considered a Red Hat customer if you run Red Hat Enterprise Linux
(RHEL) instances or use RHEL services on AWS. The Knowledge base portal includes
binaries, and knowledge-share and discussion forums for community support that are
available only to Red Hat licensed customers.

In addition to the required AWS Identity and Access Management (IAM) permissions for Systems Manager and Fleet Manager, the
user or role you use to access the console must allow the `rhelkb:GetRhelURL`
action to access the Knowledge base portal.

###### To access the Red Hat Knowledgebase Portal

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the RHEL instance you want to use to connect to the Red Hat
   Knowledgebase Portal.
4. Choose **Account management**, **Access Red Hat
   Knowledgebase** to open the Red Hat Knowledge base page.
   If you use RHEL on AWS to run fully supported RHEL workloads, you can also
   access the Red Hat Knowledge base through Red Hat's website by using your AWS
   credentials.
