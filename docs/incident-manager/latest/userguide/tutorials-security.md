AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Tutorial: Managing security incidents in

Incident Manager

You can use AWS Security Hub CSPM, Amazon EventBridge, and Incident Manager together to identify and manage
security incidents in your AWS hosted-applications. This tutorial walks you through
configuring an EventBridge rule that creates an incident based on Security Hub CSPM automatically sent
findings.

###### Note

This tutorial uses EventBridge Security Hub CSPM. You may incur costs from using these
services.

###### Prerequisites

- Set up Security Hub CSPM. For more information, see [Setting up
  AWS Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md").
- Create or update findings in Security Hub CSPM. For more information, see [Findings in
  AWS Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-findings.md "../../../securityhub/latest/userguide/securityhub-findings.md").
- Configure a response plan that Incident Manager will use as the template when
  creating your security incident. For more information, see [Preparing for incidents in Incident Manager](incident-response.md "incident-response.md").
  For this tutorial, we use a predefined pattern to create the EventBridge rule. To create the
  rule using a custom pattern, see [Using a custom pattern to create the rule](../../../securityhub/latest/userguide/securityhub-cwe-all-findings.md#securityhub-cwe-all-findings-custom-pattern "../../../securityhub/latest/userguide/securityhub-cwe-all-findings.md#securityhub-cwe-all-findings-custom-pattern") in the AWS Security Hub CSPM user
  guide.

###### Create an EventBridge rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a **Name** and **Description** for the
   rule.

A rule can't have the same name as another rule in the same Region and on the
same event bus. 5. For **Event bus**, choose
**default**. 6. For **Rule type**, choose **Rule with an event
pattern**. 7. Choose **Next**. 8. For **Event source**, choose **AWS events or EventBridge
partner events**. 9. For **Event pattern**, choose **Event pattern
form**. 10. For **Event source**, choose **AWS
services**. 11. For **AWS service**, choose
**Security Hub CSPM**. 12. For **Event type**, choose **Security Hub CSPM Findings -
Imported**. 13. By default, EventBridge configures the event pattern without any filter values. For
each attribute, the **Any `attribute
 name`** option is selected. Update these filters to
create incidents based on the security findings that most impact your
environment. 14. Click **Next**. 15. For **Target types**, choose **AWS
service**. 16. For **Select a target**, choose **Incident Manager
response plan**. 17. For **Response plan**, choose a response plan to use as a
template for created incidents. 18. EventBridge can create the IAM role needed for your rule to run.

    * To create an IAM role automatically, choose **Create a new
     role for the specific resource**.
    * To use an IAM role that already exists in your account, choose
     **Use existing role**.

19. (Optional) Enter one or more tags for the rule.
20. Choose **Next**.
21. Review the details of the rule and choose **Create
    rule**.
    Now that you've created this EventBridge rule, security findings that match the attribute
    values you defined will create incidents in Incident Manager. You can triage, manage,
    monitor, and create post-incident analysis from these incidents.
