# Stopping Service Quotas Automatic Management

Use the following procedure to stop Service Quotas Automatic Management of service quotas for supported AWS services
in your AWS account using the AWS Management Console or AWS CLI.

AWS Management Console

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the navigation pane, choose
   **Automatic Management**.
3. Choose **Stop Automatic Management** at the top corner of
   the page.
4. Confirm your selection in the confirmation pop-up box.

AWS CLI
Use the following command to stop Automatic Management. Replace the
`italicized placeholder text` in the example
command with your information.

```
aws service-quotas stop-auto-management-configuration --region `ca-central-1`
```
