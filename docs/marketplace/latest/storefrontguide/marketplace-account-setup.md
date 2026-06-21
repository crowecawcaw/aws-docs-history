# Account setup

Connect and manage your AWS Marketplace seller accounts in the Storefront console.

## Connecting your AWS Marketplace account

You can connect your AWS Marketplace seller account to AWS Marketplace Storefront.
Connecting an account enables you to import your own product listings, create offers,
manage agreements, and track metering data directly from the Storefront console.

### Prerequisites

- An active AWS Marketplace seller account
- AWS IAM permissions to create CloudFormation stacks in your
  account
- Owner or Admin role at the organization level.

### To connect your AWS Marketplace seller account

1. In the organization main window, choose **Create Account**.
2. Enter the account **Name**, choose the cloud provider (AWS), and choose the account type (Seller). Choose **Continue**.
3. Enter your **AWS Account ID** and choose **Confirm**.
4. Choose **Launch Stack**. This opens the AWS CloudFormation console in a new tab.
5. In the CloudFormation console, run the CloudFormation template. After the stack creation completes, go to the Outputs tab and copy the IAM Role ARN.
6. Return to the account setup page. Paste the IAM Role ARN in the Seller Account Setup and Configuration section.
7. Choose **Start Discovery**, then choose **Start** in the console.
8. Return to the CloudFormation console. Go to Resources and copy the DFKMSKey ARN.
9. Return to the account page and paste the DFKMSKey ARN in the designated field.
10. Submit the Data Feed Storage Configuration on AWS Marketplace. This is required for the data feed to deliver to your account.
11. After the data feed configuration is confirmed, choose **Continue**, then choose **Create Account**.

Your seller account appears in the navigation pane and begins syncing marketplace data (listings, offers, agreements, and reports).

### What connecting enables

| Capability                                   | Without account | With connected account |
| -------------------------------------------- | --------------- | ---------------------- |
| Import public marketplace products           | Yes             | Yes                    |
| Import your own listings (including limited) | No              | Yes                    |
| Create private offers                        | No              | Yes                    |
| View agreements and entitlements             | No              | Yes                    |
| Track metering and usage                     | No              | Yes                    |
| View disbursements and revenue               | No              | Yes                    |
| Co-selling / ACE integration                 | No              | Yes                    |

### Multiple accounts

You can connect multiple AWS Marketplace seller accounts to a single organization.
Each account appears separately in the navigation and maintains its own listings,
offers, and agreements.

### Related topics

- [Account dashboard](#account-dashboard "#account-dashboard")
- [Account settings](#account-settings "#account-settings")
- Creating a SaaS listing

## Account dashboard

The account dashboard provides an overview of your AWS Marketplace activity, including
active subscriptions, revenue, opportunities, and key metrics.

### Dashboard widgets

When you open a connected marketplace account, the dashboard displays the
following widgets:

- Billed GSS
- Private offers
- Active subscriptions
- Reseller authorizations
- Listings
- Free trials
- Days sales outstanding
- Partner Revenue
- AWS Fee

### Business overview charts

The Business Overview card displays tabs for Private Offers, Active Subscribers,
and GSS as a line chart. The Goals panel shows GSS Goal and PO Goal with an Edit
Goals action.

### To customize the dashboard

Use the time-period selector to change the date range displayed. The T12M value
represents trailing 12 months.

The Widgets button at the top right of the metrics card lets you customize which
widgets are displayed. Several widgets show split counts, for example Reseller
authorizations (Active and Expired).

### Notes

- Dashboard data refreshes when you navigate to the page. It does not
  auto-refresh.
- Revenue and disbursement data may have a 24-48 hour delay from AWS
  Marketplace.
- If no account is connected, the dashboard shows a prompt to connect your
  account.

### Related topics

- Connecting your AWS Marketplace account
- [Account settings](#account-settings "#account-settings")
- Billed revenue

## Account settings

Account settings let you configure your connected AWS Marketplace account's metadata,
notification preferences, and team access within the Storefront console.

### To access account settings

Open your connected account, then choose the Settings tab. The account page
contains four tabs: Notifications, Metadata, Team, and Settings.

### General settings

| Setting           | Description                                               |
| ----------------- | --------------------------------------------------------- |
| Account name      | Display name for this account in the console              |
| AWS Account ID    | Your 12-digit AWS account ID (read-only after connection) |
| Connection status | Current status of the API connection                      |
| Last synced       | Timestamp of the most recent data sync                    |

### Notification preferences

On the Notifications tab, choose + Add to create a notification rule. Each rule
has a Name, a Resource, and a Webhook.

### Related topics

- Connecting your AWS Marketplace account
- [Account dashboard](#account-dashboard "#account-dashboard")
- Managing team members
