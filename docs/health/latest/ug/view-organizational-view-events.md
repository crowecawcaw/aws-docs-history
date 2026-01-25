# Viewing organizational view

You can use the AWS Health console to get a centralized view for health events in your
AWS organization.

Organizational view is available in the AWS Health console for all AWS Support plans at no
additional cost.

###### Note

If you want to allow users access to this feature in the management account, they must
have permissions such as the [AWSHealthFullAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess") policy. For more information, see
[AWS Health identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

Viewing organizational view events (Console)
After you enable organizational view, AWS Health displays health events for
all accounts in your organization.

When an account joins your organization, AWS Health automatically adds the
account to organizational view. When an account leaves your organization, new
events from that account are no longer logged to organizational view. However,
existing events remain and you can still query them up to the 90-day limit.

AWS retains the policy data for the account for 90 days from the effective date of the administrator account closure.
At the end of the 90 day period, AWS permanently deletes all policy data for the account.

- To retain findings for more than 90 days, you can archive the policies. You can also use a custom action with
  an EventBridge rule to store the findings in an S3 bucket.
- As long as AWS retains the policy data, when you reopen the closed account, AWS reassigns the account
  as the service administrator and recovers the service policy data for the account.
- For more information, see [Closing an account](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md").

###### Important

For customers in the AWS GovCloud (US) Regions:

- Before closing your account, back up and then delete account resources. You will no longer have access
  to them after you close the account.

###### Note

When you enable this feature, the AWS Health console can display public
events from the [AWS Health Dashboard – Service health](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status") for the last 7 days.
These public events aren't specific to accounts in your organization. Events
from the AWS Health Dashboard – Service health provide public information about the regional availability of
AWS services.

You can view organizational view events in the following pages:.

**Open and Recent Issues**

You can use the **Open and recent issues** tab to view events
that might affect your AWS infrastructure, such as changes to AWS services
and resources that affect your organization.

###### To view organizational view events

1. Open your AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/ "https://health.aws.amazon.com/health/").
2. In the navigation pane, under **Your organization
   health**, choose **Open and recent
   issues** to view recently reported events.
3. Choose an event. On the **Details** tab, you can
   review the following information about the event:
   - Event name
   - Status
   - Region / Availability Zone
   - Affected accounts
   - Start time
   - End time
   - Category
   - Description

**Scheduled Changes**

Use the **Scheduled changes** tab to view upcoming events
that might affect your organization. These events can include scheduled
maintenance activities for services.

**Other Notifications**

Use the **Notifications** tab to view all other notifications
and ongoing events from the past seven days that might affect your organization.
This can include events, such as certificate rotations, billing notifications,
and security vulnerabilities.

**Event Log**

You can also use the **Event log** tab to view AWS Health
events for organizational view. The column layout and behavior are similar to
the **Open and recent issues** tab, except that the
**Event log** tab includes additional columns and filter
options, such as the **Event category**,
**Status**, and **Start time**.

###### To view organizational view events in the Event log tab

1. Open your AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/ "https://health.aws.amazon.com/health/").
2. In the navigation pane, under **Your organization
   health**, choose **Event log**.
3. Under **Event log**, choose the event name. You can
   review the following information about the event:
   - Event name
   - Status
   - Region / Availability Zone
   - Affected accounts
   - Start time
   - End time
   - Category
   - Description

Viewing affected accounts and resources (Console)
Under **Your organization health**, you can view the accounts
in your organization that are affected by the event and any related resources.
For example, if there's an upcoming event for Amazon Elastic Compute Cloud (Amazon EC2) instance
maintenance, accounts in your organization that have Amazon EC2 instances can appear
in the **Details** tab. You can identify the specific resources
and then contact the account owner.

###### To view affected accounts and resources

1. Open your AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/ "https://health.aws.amazon.com/health/").
2. In the navigation pane, under **Your organization
   health**, choose one of the tabs.
3. Choose an event that has a value for **Affected
   accounts**.
4. Choose the **Affected accounts** tab.
5. Choose **Show account details** to view the following
   information for the accounts:
   - Account ID
   - Account name
   - Primary email
   - Organizational unit (OU)

6. Expand the account to view the affected resources.
7. If there are more than 10 resources, choose **View all
   resources** to view them.
8. To filter by account ID for this specific event, do the following:
   1. On the **Affected accounts** tab, choose
      **Add filter**, choose **Account
      ID**, and then enter the account ID. You can only
      enter one account ID at a time.
   2. Choose **Apply**. The account that you
      entered appears in the list.

Viewing organizational view events (CLI)
After you enable this feature, AWS Health starts to record events that affect
accounts in the organization. When an account joins your organization,
AWS Health automatically adds the account to organizational view.

###### Note

AWS Health doesn't record events that occurred in your organization
before you enabled organizational view.

When an account leaves your organization, new events from that account are no
longer logged to organizational view. However, existing events remain and you
can still query them up to the 90-day limit.

AWS retains the policy data for the account for 90 days from the effective date of the administrator account closure.
At the end of the 90 day period, AWS permanently deletes all policy data for the account.

- To retain findings for more than 90 days, you can archive the policies. You can also use a custom action with
  an EventBridge rule to store the findings in an S3 bucket.
- As long as AWS retains the policy data, when you reopen the closed account, AWS reassigns the account
  as the service administrator and recovers the service policy data for the account.
- For more information, see [Closing an account](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md").

###### Important

For customers in the AWS GovCloud (US) Regions:

- Before closing your account, back up and then delete account resources. You will no longer have access
  to them after you close the account.

You can use the AWS Health API operations to return events from
organizational view.

###### Example : Describe organizational view events

The following AWS CLI command returns health events for AWS accounts in
your organization.

```
aws health describe-events-for-organization --region us-east-1
```
