# Sending findings to a custom Security Hub CSPM action

You can create AWS Security Hub CSPM custom actions to automate Security Hub CSPM with Amazon EventBridge. For custom
actions, the event type is **Security Hub Findings - Custom
Action**. After you set up a custom action, you can send findings
to it. For more information and detailed steps on creating custom actions, see [Using EventBridge for automated response and remediation](securityhub-cloudwatch-events.md "securityhub-cloudwatch-events.md").

###### To send findings to a custom action (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. To display a finding list, do one of the following:
   - In the Security Hub CSPM navigation pane, choose **Findings**.
   - In the Security Hub CSPM navigation pane, choose **Insights**. Choose an insight.
     Then on the results list, choose an insight result.
   - In the Security Hub CSPM navigation pane, choose **Integrations**. Choose
     **See findings** for an integration.
   - In the Security Hub CSPM navigation pane, choose **Security standards**. Choose
     **View results** to display a list of controls. Then choose the control
     name.

3. In the finding list, select the check box for each finding to send to the custom
   action.

You can send up to 20 findings at a time. 4. For **Actions**, choose the custom action.
