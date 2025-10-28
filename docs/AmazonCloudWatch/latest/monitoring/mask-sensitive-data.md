# Protect sensitive data

Amazon CloudWatch Logs uses data protection policies to identify sensitive data and define actions to protect that data. You use data identifiers to
select the sensitive data of interest. Amazon CloudWatch Logs then detects the sensitive data using machine learning and pattern matching. You can define audit and
masking operations to log sensitive data findings and mask sensitive data when viewing log events.

For more information, see [Protecting sensitive log data with masking](../logs/cloudwatch-logs-data-protection-policies.md "../logs/cloudwatch-logs-data-protection-policies.md").

## Configure data protection in the console

1. Open the CloudWatch console.
2. In the navigation pane, choose **Settings**.
3. Choose the **Logs** tab.
4. Choose **Configure the Data protection account policy**.
5. Choose from the list of data identifiers relevant to your data, or add custom data identifiers using REGEX filters.
6. Choose **Activate data protection**.
