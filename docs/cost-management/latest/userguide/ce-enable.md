# Enabling Cost Explorer

You can enable Cost Explorer for your account by opening Cost Explorer for the first
time in the AWS Cost Management console. You can't enable Cost Explorer using the API. After you enable
Cost Explorer, AWS prepares the data about your costs for the current month and the
previous 13 months, and then calculates the forecast for the next 12 months. The current
month's data is available for viewing in about 24 hours. The rest of your data takes a few
days longer. Cost Explorer updates your cost data at least once every 24 hours.

As part of the process of enabling Cost Explorer, AWS automatically configures Cost Anomaly Detection for
your account. Cost Anomaly Detection is an AWS Cost Management feature. This feature uses machine learning models to detect
and alert on anomalous spend patterns in your deployed AWS services. To get you started
with Cost Anomaly Detection, AWS sets up an AWS services monitor and a daily summary alert subscription.
You're alerted about any anomalous spend that exceeds $100 and 40% of your expected spend
across the majority of your AWS services in your accounts. For more information, see
[limitations](management-limits.md "management-limits.md") and [Detecting
unusual spend with AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md").

###### Note

You can opt out of Cost Anomaly Detection at any time. For more information, see [Opting out of Cost Anomaly Detection](opting-out-cad.md "opting-out-cad.md").

You can launch Cost Explorer if your account is a member account in an organization where
the management account enabled Cost Explorer. Know that your organization's
management account can also deny your account access. For more information, see [Consolidated billing for AWS Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md").

###### Note

An account’s status within an organization determines what cost and usage data are
visible:

- A standalone account joins an organization. After this, the account can no
  longer access cost and usage data from when the account was a standalone
  account.
- A member account leaves an organization to become a standalone account. After
  this, the account can no longer access cost and usage data from when the account
  was a member of the organization. The account can access only the data that's
  generated as a standalone account.
- A member account leaves organization A to join organization B. After this, the
  account can no longer access cost and usage data from when the account was a
  member of organization A. The account can access only the data that's generated
  as a member of organization B.
- An account rejoins an organization that the account previously belonged to.
  After this, the account regains access to its historical cost and usage
  data.
  Signing up to receive the AWS Cost and Usage Reports or the Detailed Billing Report doesn't automatically
  enable Cost Explorer. To do so, follow this procedure.

###### To sign up for Cost Explorer

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Explorer**.
3. On the **Welcome to Cost Explorer** page, choose
   **Launch Cost Explorer**.
   For more information about controlling access to Cost Explorer, see [Controlling access to Cost Explorer](ce-access.md "ce-access.md").
