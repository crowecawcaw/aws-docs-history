# Enabling GuardDuty agent for Amazon EC2

resources in multiple-account environment

In a multiple-account environments, only the delegated GuardDuty administrator account can enable or disable automated
agent configuration for the resource types belonging to the member accounts in their
organization. The GuardDuty member accounts can't modify this configuration from their
accounts. The delegated GuardDuty administrator account account manages their member accounts using AWS Organizations. For more
information about multi-account environments, see [Managing multiple
accounts](guardduty_accounts.md "guardduty_accounts.md").

Configure for all instances
If you chose **Enable for all accounts** for
Runtime Monitoring, then choose one of the following options for the
delegated GuardDuty administrator account:

- **Option 1**

Under **Automated agent configuration**,
in the **EC2** section, select
**Enable for all accounts**.

- **Option 2**
  - Under **Automated agent
    configuration**, in the
    **EC2** section, select
    **Configure accounts
    manually**.
  - Under **Delegated Administrator (this
    account)**, choose
    **Enable**.

- Choose **Save**.

If you chose **Configure accounts manually** for
Runtime Monitoring, then perform the following steps:

- Under **Automated agent configuration**,
  in the **EC2** section, select
  **Configure accounts manually**.
- Under **Delegated Administrator (this
  account)**, choose
  **Enable**.
- Choose **Save**.

Regardless of which option you choose to enable the automated
agent configuration for delegated GuardDuty administrator account, you can verify that the SSM
association that GuardDuty creates will install and manage the security
agent on all the EC2 resources belonging to this account.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Open the **Targets** tab for the SSM
   association
   (`GuardDutyRuntimeMonitoring-do-not-delete`).
   Observe that the **Tag key** appears as
   **InstanceIds**.

Using inclusion tag in selected instances

###### To configure GuardDuty agent for selected Amazon EC2 instances

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Add the `GuardDutyManaged`:`true`
   tag to the instances that you want GuardDuty to monitor and
   detect potential threats. For information about adding this
   tag, see [To add a tag to an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").

Adding this tag will permit GuardDuty to install and manage
the security agent for these selected EC2 instances. You
**don't** need to
enable automated agent configuration explicitly. 3. You can verify that the SSM association that GuardDuty creates
will install and manage the security agent only on the EC2
resources that are tagged with the inclusion tags.

Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").

    1. Open the **Targets** tab for the
     SSM association that gets created
     (`GuardDutyRuntimeMonitoring-do-not-delete`).
     The **Tag key** appears as
     **tag:GuardDutyManaged**.

Using exclusion tag in selected instances

###### Note

Ensure that you add the exclusion tag to your Amazon EC2 instances before you launch them. Once you have enabled automated agent
configuration for Amazon EC2, any EC2 instance that launches
without an exclusion tag will be covered under GuardDuty automated agent configuration.

###### To configure GuardDuty agent for selected Amazon EC2 instances

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Add the `GuardDutyManaged`:`false`
   tag to the instances that you **don't** want GuardDuty to monitor and detect
   potential threats. For information about adding this tag,
   see [To add a tag to an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").
3. ###### For the [exclusion tags to be available](prereq-runtime-monitoring-ec2-support.md#general-runtime-monitoring-prereq-ec2 "prereq-runtime-monitoring-ec2-support.md#general-runtime-monitoring-prereq-ec2") in the instance

   metadata, perform the following steps:
   1. Under the **Details** tab of your
      instance, view the status for **Allow tags
      in instance metadata**.

   If it is currently **Disabled**,
   use the following steps to change the status to
   **Enabled**. Otherwise, skip this
   step. 2. Under the **Actions** menu,
   choose **Instance
   settings**. 3. Choose **Allow tags in instance
   metadata**.

4. After you have added the exclusion tag, perform the same
   steps as specified in the **Configure
   for all instances** tab.

You can now assess the runtime [Runtime coverage and troubleshooting for Amazon EC2
instance](gdu-assess-coverage-ec2.md "gdu-assess-coverage-ec2.md").

###### Note

It may take up to 24 hours to update the configuration for the member
accounts.

Configure for all instances
The following steps assume that you chose **Enable for all
accounts** in the Runtime Monitoring section:

1. Choose **Enable for all accounts** in the
   **Automated agent configuration**
   section for **Amazon EC2**.
2. You can verify that the SSM association that GuardDuty creates
   (`GuardDutyRuntimeMonitoring-do-not-delete`)
   will install and manage the security agent on all the EC2
   resources belonging to this account.
   1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
   2. Open the **Targets** tab for the
      SSM association. Observe that the **Tag
      key** appears as
      **InstanceIds**.

Using inclusion tag in selected instances

###### To configure GuardDuty agent for selected Amazon EC2 instances

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Add the `GuardDutyManaged`:`true`
   tag to the EC2 instances that you want GuardDuty to monitor and
   detect potential threats. For information about adding this
   tag, see [To add a tag to an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").

Adding this tag will permit GuardDuty to install and manage
the security agent for these selected EC2 instances. You
**don't** need to
enable automated agent configuration explicitly. 3. You can verify that the SSM association that GuardDuty creates
will install and manage the security agent on all the EC2
resources belonging to your account.

    1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
    2. Open the **Targets** tab for the
     SSM association
     (`GuardDutyRuntimeMonitoring-do-not-delete`).
     Observe that the **Tag key**
     appears as **InstanceIds**.

Using exclusion tag in selected instances

###### Note

Ensure that you add the exclusion tag to your Amazon EC2 instances before you launch them. Once you have enabled automated agent
configuration for Amazon EC2, any EC2 instance that launches
without an exclusion tag will be covered under GuardDuty automated agent configuration.

###### To configure GuardDuty security agent for selected Amazon EC2

instances

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Add the `GuardDutyManaged`:`false`
   tag to the instances that you **don't** want GuardDuty to monitor and detect
   potential threats. For information about adding this tag,
   see [To add a tag to an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").
3. ###### For the [exclusion tags to be available](prereq-runtime-monitoring-ec2-support.md#general-runtime-monitoring-prereq-ec2 "prereq-runtime-monitoring-ec2-support.md#general-runtime-monitoring-prereq-ec2") in the instance

   metadata, perform the following steps:
   1. Under the **Details** tab of your
      instance, view the status for **Allow tags
      in instance metadata**.

   If it is currently **Disabled**,
   use the following steps to change the status to
   **Enabled**. Otherwise, skip this
   step. 2. Under the **Actions** menu,
   choose **Instance
   settings**. 3. Choose **Allow tags in instance
   metadata**.

4. After you have added the exclusion tag, perform the same
   steps as specified in the **Configure
   for all instances** tab.

You can now assess the runtime [Runtime coverage and troubleshooting for Amazon EC2
instance](gdu-assess-coverage-ec2.md "gdu-assess-coverage-ec2.md").

The delegated GuardDuty administrator account can set the automated agent configuration for Amazon EC2 resource to
enable automatically for the new member accounts as they join the organization.

Configure for all instances
The following steps assume that you selected
**Automatically enable for new member
accounts** under the **Runtime Monitoring**
section:

1. In the navigation pane, choose
   **Runtime Monitoring**.
2. On the **Runtime Monitoring** page, choose
   **Edit**.
3. Select **Automatically enable for new member
   accounts**. This step ensures that whenever a
   new account joins your organization, automated agent
   configuration for Amazon EC2 will be automatically enabled for
   their account. Only the delegated GuardDuty administrator account of the organization can
   modify this selection.
4. Choose **Save**.

When a new member account joins the organization, this
configuration will be enabled for them automatically. For GuardDuty to
manage the security agent for the Amazon EC2 instances that belong to
this new member account, make sure that all the prerequisites [For EC2
instance](prereq-runtime-monitoring-ec2-support.md "prereq-runtime-monitoring-ec2-support.md")
are met.

When an SSM association gets created
(`GuardDutyRuntimeMonitoring-do-not-delete`), you can
verify that the SSM association will install and manage the security
agent on all the EC2 instances belonging to the new member
account.

- Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
- Open the **Targets** tab for the SSM
  association. Observe that the **Tag key**
  appears as **InstanceIds**.

Using inclusion tag in selected instances

###### To configure GuardDuty security agent for selected instances in

your account

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Add the `GuardDutyManaged`:`true`
   tag to the instances that you want GuardDuty to monitor and
   detect potential threats. For information about adding this
   tag, see [To add a tag to an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").

Adding this tag will permit GuardDuty to install and manage
the security agent for these selected instances. You
don't need to enable automated agent configuration
explicitly. 3. You can verify that the SSM association that GuardDuty creates
will install and manage the security agent only on the EC2
resources that are tagged with the inclusion tags.

    1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
    2. Open the **Targets** tab for the
     SSM association that gets created. The **Tag
     key** appears as
     **tag:GuardDutyManaged**.

Using exclusion tag in selected instances

###### Note

Ensure that you add the exclusion tag to your Amazon EC2 instances before you launch them. Once you have enabled automated agent
configuration for Amazon EC2, any EC2 instance that launches
without an exclusion tag will be covered under GuardDuty automated agent configuration.

###### To configure GuardDuty security agent for specific instances in

your standalone account

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Add the `GuardDutyManaged`:`false`
   tag to the instances that you **don't** want GuardDuty to monitor and detect
   potential threats. For information about adding this tag,
   see [To add a tag to an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").
3. ###### For the [exclusion tags to be available](prereq-runtime-monitoring-ec2-support.md#general-runtime-monitoring-prereq-ec2 "prereq-runtime-monitoring-ec2-support.md#general-runtime-monitoring-prereq-ec2") in the instance

   metadata, perform the following steps:
   1. Under the **Details** tab of your
      instance, view the status for **Allow tags
      in instance metadata**.

   If it is currently **Disabled**,
   use the following steps to change the status to
   **Enabled**. Otherwise, skip this
   step. 2. Under the **Actions** menu,
   choose **Instance
   settings**. 3. Choose **Allow tags in instance
   metadata**.

4. After you have added the exclusion tag, perform the same
   steps as specified in the **Configure
   for all instances** tab.

You can now assess the runtime [Runtime coverage and troubleshooting for Amazon EC2
instance](gdu-assess-coverage-ec2.md "gdu-assess-coverage-ec2.md").

Configure for all instances

1. On the **Accounts** page, select one or
   more accounts for which you want to enable
   **Runtime Monitoring-Automated agent configuration
   (Amazon EC2)**. Make sure that the accounts that you
   select in this step already have Runtime Monitoring enabled.
2. From **Edit protection plans**, choose
   the appropriate option to enable
   **Runtime Monitoring-Automated agent configuration
   (Amazon EC2)**.
3. Choose **Confirm**.

Using inclusion tag in selected instances

###### To configure GuardDuty security agent for selected

instances

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Add the `GuardDutyManaged`:`true`
   tag to the instances that you want GuardDuty to monitor and
   detect potential threats. For information about adding this
   tag, see [To add a tag to an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").

Adding this tag will permit GuardDuty to manage the security
agent for your tagged Amazon EC2 instances. You don't need
to explicitly enable automated agent configuration
(**Runtime Monitoring - Automated agent configuration
(EC2)**.

Using exclusion tag in selected instances

###### Note

Ensure that you add the exclusion tag to your Amazon EC2 instances before you launch them. Once you have enabled automated agent
configuration for Amazon EC2, any EC2 instance that launches
without an exclusion tag will be covered under GuardDuty automated agent configuration.

###### To configure GuardDuty security agent for selected

instances

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Add the `GuardDutyManaged`:`false`
   tag to the EC2 instances that you **don't** want GuardDuty to monitor or detect
   potential threats. For information about adding this tag,
   see [To add a tag to an individual resource](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags").
3. ###### For the [exclusion tags to be available](prereq-runtime-monitoring-ec2-support.md#general-runtime-monitoring-prereq-ec2 "prereq-runtime-monitoring-ec2-support.md#general-runtime-monitoring-prereq-ec2") in the instance

   metadata, perform the following steps:
   1. Under the **Details** tab of your
      instance, view the status for **Allow tags
      in instance metadata**.

   If it is currently **Disabled**,
   use the following steps to change the status to
   **Enabled**. Otherwise, skip this
   step. 2. Under the **Actions** menu,
   choose **Instance
   settings**. 3. Choose **Allow tags in instance
   metadata**.

4. After you have added the exclusion tag, perform the same
   steps as specified in the **Configure
   for all instances** tab.

You can now assess [Runtime coverage and troubleshooting for Amazon EC2
instance](gdu-assess-coverage-ec2.md "gdu-assess-coverage-ec2.md").
