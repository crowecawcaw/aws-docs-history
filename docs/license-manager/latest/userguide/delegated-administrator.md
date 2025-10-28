# Delegated administrator settings in License Manager

You can register a delegated administrator to perform administrative tasks for managed
licenses and Linux subscriptions in License Manager. To simplify administration, we recommend using
the License Manager console to register a single delegated administrator for each feature of License Manager.
When you use this approach, you will have a single delegated administrator in your
organization for License Manager.

Using the AWS CLI or SDKs, you can register different member accounts in your organization
as the delegated administrator for each supported feature of License Manager. This results in
different member accounts in your organization being able to perform administrative tasks
for managed licenses and Linux subscriptions.

###### Important

To use the delegated administration features in the License Manager console, you must have the
same member account registered as the delegated administrator for each feature of License Manager.
If you registered more than one member account as the delegated administrator, you first
have to deregister the existing member accounts, and then register the same account for
each feature of License Manager.

Before you register a delegated administrator, you must enable trusted access with Organizations.
For more information, see [Inviting an AWS
account to join your organization](../../../organizations/latest/userguide/orgs_manage_accounts_invites.md "../../../organizations/latest/userguide/orgs_manage_accounts_invites.md") and [Enable trusted access with AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-license-manager.md "../../../organizations/latest/userguide/services-that-can-integrate-license-manager.md").

The following are the features for which you can register a delegated
administrator:

###### Managed licenses

You can perform administrative tasks, such as sharing self-managed licenses with other
member accounts, performing cross-account resource discovery, and distributing managed
entitlements to other member accounts.

###### Linux subscriptions

You can perform administrative tasks, such as viewing and managing commercial Linux
subscriptions you own and run across AWS Regions and your accounts in AWS Organizations. You
can also create and manage Amazon CloudWatch alarms for your Linux subscriptions. The data must
first be discovered and aggregated before it is visible in the License Manager console
and any alarms can function if they are configured.

###### Important

Once registered, the delegated administrator has visibility into EC2 instances owned
by accounts in your organization.

You can register and deregister delegated administrators using the [AWS License Manager console](https://console.aws.amazon.com/license-manager "https://console.aws.amazon.com/license-manager"), [AWS CLI](https://aws.amazon.com/cli "https://aws.amazon.com/cli"), or [AWS SDKs.](https://aws.amazon.com/tools "https://aws.amazon.com/tools")

## Regions supported for

delegated License Manager administrators

The following Regions support License Manager delegated administrators:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Asia Pacific (Hong Kong)
- Middle East (Bahrain)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Stockholm)
- Europe (Milan)
- Africa (Cape Town)
- South America (São Paulo)

[Show moreShow less](# "#")

## Register a delegated License Manager

administrator

You can register a delegated administrator using the AWS CLI or AWS Management Console.

Console
To register a delegated administrator using the AWS License Manager console,
perform the following steps:

1. Sign in to AWS as the administrator of the management
   account.
2. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
3. Choose **Settings** from the left navigation
   pane.
4. Choose the **Delegated administration** tab.
5. Choose **Register delegated
   administrator**.
6. Enter the member account ID to register as the delegated
   administrator, confirm that you want to grant License Manager the required
   permissions, and then choose **Register**.
7. A message indicates if the specified account has been successfully
   registered as the delegated administrator License Manager.

AWS CLI
To register a delegated administrator for managed licenses using the AWS CLI, perform the
following steps:

1. From the command line, run the following AWS CLI command:

```
aws organizations register-delegated-administrator --service-principal=license-manager.amazonaws.com --account-id=`<account-id>`
```

2. Run the following command to verify that the specified account is
   successfully registered as the delegated administrator:

```
aws organizations list-delegated-administrators --service-principal=license-manager.amazonaws.com
```

To register a delegated administrator for Linux subscriptions using the AWS CLI, perform the
following steps:

1. From the command line, run the following AWS CLI command:

```
aws organizations register-delegated-administrator --service-principal=license-manager-linux-subscriptions.amazonaws.com --account-id=`<account-id>`
```

2. Run the following command to verify that the specified account is
   successfully registered as the delegated administrator:

```
aws organizations list-delegated-administrators --service-principal=license-manager-linux-subscriptions.amazonaws.com
```

## Deregister a delegated License Manager

administrator

You can deregister a delegated administrator using the AWS CLI or AWS Management Console.

Console
To deregister a delegated administrator using the AWS License Manager console,
perform the following steps:

1. Sign in to AWS as the administrator of the management
   account.
2. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
3. Choose **Settings** from the left navigation
   pane.
4. Choose the **Delegated administration**
   tab.
5. Choose **Remove**.
6. Enter the text `remove` to confirm you would
   like to remove the delegated administrator for License Manager and choose
   **Remove**.
7. A message indicates if the specified account has been successfully
   removed the delegated administrator for License Manager.

AWS CLI
To deregister a delegated administrator for managed licenses using the AWS CLI, perform the
following steps:

1. From the command line, run the following AWS CLI command:

```
aws organizations deregister-delegated-administrator --service-principal=license-manager.amazonaws.com --account-id=`<account-id>`
```

2. Run the following command to verify that the specified account is
   successfully deregistered as the delegated administrator:

```
aws organizations list-delegated-administrators --service-principal=license-manager.amazonaws.com
```

To deregister a delegated administrator for Linux subscriptions using the AWS CLI, perform the
following steps:

1. From the command line, run the following AWS CLI command:

```
aws organizations deregister-delegated-administrator --service-principal=license-manager-linux-subscriptions.amazonaws.com --account-id=`<account-id>`
```

2. Run the following command to verify that the specified account is
   successfully deregistered as the delegated administrator:

```
aws organizations list-delegated-administrators --service-principal=license-manager-linux-subscriptions.amazonaws.com
```

You can register a deregistered account again at any time.
