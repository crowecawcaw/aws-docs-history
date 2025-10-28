# Set up multi-user mode (admin)

With a multi-user account setup, organizers (such as account administrators) can provide
participants access to AWS DeepRacer service under their account ID. They can also set
usage
quotas on participants' training hours, monitor spending on training and
storage, start and stop training, and view and manage models for every user in their
account from the AWS DeepRacer console.

Multi-user mode is particularly useful for large events with multiple participants who don't have individual AWS accounts.
Instead of creating and managing accounts for each participant in an event, an AWS DeepRacer administrator can host all of their sponsored participants
through a single AWS account.

In multi-user mode, sponsored participants can compete and train without incurring any of
their own costs. Their training and storage charges are billed to the sponsoring multi-user AWS
account billing. If an administrator stops sponsoring participants' usage, participants keep
their racer aliases and profiles.

## Multi-user stakeholders

This walkthrough refers to the following typical multi-user stakeholders for setting
up and using multi-user mode.

- **AWS administrator for IAM/SSO
  configuration.** The AWS administrator for IAM/SSO
  configuration sets up IAM or SSO for the AWS DeepRacer administrator and for
  participants to use multi-user mode. The AWS administrator for IAM/SSO has
  IAM and SSO administrator permissions. For information about creating IAM
  users, see [Creating an IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md").
- **AWS DeepRacer administrator.** The AWS DeepRacer administrator manages AWS DeepRacer participants' sponsorship and can pause and resume
  sponsorship, delete models and artifacts, configure and host virtual races, and enable and disable multi-user
  mode. The AWS DeepRacer administrator has [AWSDeepRacerAccountAdminAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess") permissions.
- **AWS DeepRacer participant.** AWS DeepRacer participants are
  invited
  to participate in events under an administrator's AWS
  account in multi-user mode. Participants have [AWSDeepRacerDefaultMultiUserAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerDefaultUserAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerDefaultUserAccess") permissions to train, evaluate,
  and store models in the sponsor's account. Participants also configure their
  racer profile, enter virtual races, and download their models for deploying on a
  physical AWS DeepRacer vehicle.

In this walkthrough, you perform the following steps:

- Step 1. Perform prerequisites.
- Step 2. Activate multi-user mode on your AWS DeepRacer account.
- Step 3. Invite participants.
- Step 4. Set usage quotas.
- Step 5. Monitor usage of your sponsored participants.

## Step 1. Prerequisites for AWS DeepRacer multi-user mode

Complete the following prerequisites for multi-user
mode

- [Set up your account with AWS DeepRacer admin permissions for multi-user.](#deepracer-set-up-admin-account "#deepracer-set-up-admin-account") If you are organizing a race with
  multi-user mode and performing typical AWS DeepRacer administrator tasks, you need to set up your account as an AWS DeepRacer admin with [AWSDeepRacerAccountAdminAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess") permission.
- [Provide AWS console access and racer policy permission to the participants you want to sponsor.](#deepracer-provide-console-access "#deepracer-provide-console-access")

### Set up your account with AWS DeepRacer admin permissions for

multi-user

To set up as an AWS DeepRacer admin for multi-user mode, you need to have the IAM AWS DeepRacer
administrator policy, [AWSDeepRacerAccountAdminAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess"), attached to your user, group, or role.
Depending on your organization, you may set yourself up with the administrator
policy by using the console to create a user or role and attaching the required
IAM policy, or you may have your IT administrator provide it. For information
about the required administrator policy, see [AWSDeepRacerAccountAdminAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess").
For more information about IAM policies, see [Access Management](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

### Provide AWS console access to your sponsored

participants

To provide racers you sponsor with access to the AWS DeepRacer console, we recommend using
standard AWS authorization protocols such as [AWS IAM Identity Center](../../../singlesignon/latest/userguide/useraccess.md "../../../singlesignon/latest/userguide/useraccess.md") or [AWS Identity and Access Management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md"). You can also provide access through your
organization’s preexisting SSO. When participants log in to the AWS DeepRacer console using
the credentials you provide, they are prompted to create an AWS player account to
log in and access the AWS DeepRacer console under your AWS account. For more information about
AWS Player accounts, see [AWS Player accounts.](../student-userguide/setting-up.md "../student-userguide/setting-up.md")

1. Create an IAM username and password for each participant. See [Creating an IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") .
2. Grant each participant the permissions in [AWSDeepRacerDefaultMultiUserAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerDefaultUserAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDeepRacerDefaultUserAccess").

For more information, see [AWS managed policies for AWS DeepRacer](security-iam-awsmanpol.md "security-iam-awsmanpol.md"). 3. Email participants with IAM usernames and passwords as well as a link to the console. Using the
provided link and entering their IAM usernames and passwords, participants can access the console.
For information about creating IAM users, see [Creating an IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md").

1. Open the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/"), create a custom
   permission set, and assign users to the account. For more
   information, see [Permission sets](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md").
2. When creating the custom permission set, provide the following values:

- **Relay state:**
  `https://console.aws.amazon.com/deepracer/home?region=us-east-1#getStarted`

###### Note

The **Relay state** redirects participants
within the account to a specified URL; in this case, it directs
them to the AWS DeepRacer console.

- **AWS managed policies:**
  `AWSDeepRacerDefaultMultiUserAccess`

After you have fulfilled the prerequisites, you are ready to activate multi-user mode and invite participants to
race through your account.

## Step 2: Activate multi-user account mode

After you have set up your AWS DeepRacer admin account and granted console access and permissions to your sponsored
participants, you can activate multi-user mode on your AWS DeepRacer account.

###### Note

By default, there are quotas on accounts sponsoring participants in multi-user mode. For more information, see
the section on account quotas in [Monitor usage](#deepracer-monitor-usage.title "#deepracer-monitor-usage.title").

1. In the left navigation pane, navigate to **Multi-user management** and the
   **Setup** page.
2. In **Enable multi-user account mode**, turn on **Enable multi-user
   mode**.
3. In the **Enable multi-user mode** dialog box, select the checkboxes to confirm that your
   sponsored participants have required access and permissions.
4. Choose **Enable multi-user mode**.

When you meet the prerequisites and activate multi-user mode, each of your
sponsored participants can create races and train models with all training and storage charges
billed to the administrator's AWS account. By default, a participant has a
quota of 3 concurrent models and can manage up to 10 open or future races at a time (includes LIVE, Classic, and Student races).

### Disable multi-user account mode

Disabling multi-user mode ensures that no new profiles can be created under your
administrator account and the profiles of previously sponsored participants are no
longer visible on the administrator's account. Participants are no longer prompted
to log in to their AWS player accounts and can't access or train models created
under the administrator's account.

The administrator can download, save, and import
sponsored participants' models.

1. Navigate to **Multi-user management** and the **Setup** page.
2. In **Disable multi-user account mode**, choose **Disable multi-user
   mode**.
3. In the **Disabling multi-user mode** dialog box, select the checkbox to confirm that
   you want to disable multi-user mode. Choose **Disable multi-user mode**.

Multi-user mode is disabled.

###### Note

All models created under a sponsoring AWS multi-user account
persist and model storage costs continue on the AWS account until models are deleted.

## Step 3: Invite participants to be sponsored

You can invite participants to train and race as sponsored participants by using the provided email template.

To invite participants

1. In the left navigation pane, navigate to **Multi-user management** and the
   **Setup** page. Under **Set up multi-user mode**
   in the **Invite users**
   section, choose **View invite template**.
2. Copy the email template that appears into your email client application and use it to craft an email to send
   to the participants you want to invite to be sponsored. If you are using your company's existing SSO, you can
   include a SSO URL for your participants to use. Alternatively, you can provide IAM credentials for the
   participants to use to log in to the AWS console.

## Step 4: Set

usage
quotas

After your sponsored participants have received their invitation email and have
created their profiles under your account, they appear in the **Sponsored
users** list in the **Monitor Usage** screen. In this
screen, you can then set
usage
quotas on the number of available training hours and models for
sponsored participants. By setting
quotas,
you can control
costs per participant under your account and ensure that participants can't exceed
their usage quota.
You
can also increase or decrease usage quotas as needed to provide
sponsored
participants
with
the hours they need to effectively train an AWS DeepRacer model.

###### Note

By default, sponsored participants in multi-user mode receive 5 hours of training time.

To edit
usage
quotas for sponsored racers

1. In the left navigation pane, navigate to **Multi-user management** and the
   **Monitor usage** screen. In the **Monitor
   usage** screen in **Sponsored users**, select the
   participants for whom you want to set quotas. Choose
   **Actions** to open the dropdown list and choose
   **Set
   usage
   quotas**.
2. In the **Set
   usage
   quotas** pop-up, enter the **Maximum
   training hours** and **Maximum model count** for
   the participants you selected. Choose **Confirm** to keep your changes
   or **Cancel** to discard them.

## Step 5: Monitor usage

You can monitor the usage of your sponsored participants, including estimated spending
and training model hours. You can also pause sponsorship of participants, delete models,
and view summaries of usage. You perform all tasks related to monitoring usage in AWS DeepRacer
**Multi-user management** in the **Monitor usage**
page.

All information about expenses for sponsored racers is an estimate only and should not be used for budgeting or cost
accounting purposes. Estimates are in USD and do not reflect any special pricing. For more information about pricing,
see [Pricing](https://aws.amazon.com/deepracer/pricing/ "https://aws.amazon.com/deepracer/pricing/").

**Account quotas for multi-user mode**

By default, a sponsoring account in multi-user mode has the following quotas which are shared among all sponsored profiles:

- 100 concurrent training jobs
- 100 concurrent evaluation jobs
- 100 open or future races (includes LIVE, Classic, and Student races)
- 1000 cars
- 50 private leaderboards

To adjust these quotas, contact [Customer Service](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

**To view an estimate of spending**

On the **Monitor usage** page, under **Monitor usage**, you can view an estimated
summary of your participants' usage.

**To set up billing alerts**

You can set up billing alerts for your account. Billing alerts help you to keep up to
date on spending. For more information, see [Billing](../../../awsaccountbilling/latest/aboutv2/billing-getting-started.md "../../../awsaccountbilling/latest/aboutv2/billing-getting-started.md").

###### To pause sponsorship

You can pause sponsorship of a single participant, multiple participants, or all participants. When you pause sponsorship, your
sponsored participants can't create new models or train models under your account. Training that is in progress runs through to completion and is included in estimates for spending.
You can resume sponsorship at any time. Participants whose multi-user access has been paused can still view their
models and post models to leaderboards, but they can't perform any cost-generating activities.

1. On the **Monitor usage** page, under **Monitor usage**, in the
   **Sponsored users** section, select the users for whom you want to pause
   sponsorship.
2. Choose **Pause sponsorship**.
3. In the **Pause sponsorship** dialog box, choose **Pause sponsorship** to
   pause sponsorship. Choose **Cancel** if you decide that you don't want to pause sponsorship.

###### To resume sponsorship

You can resume sponsorship of racers for whom you have paused sponsorship.

1. On the **Monitor usage** page, under **Monitor usage**, in the
   **Sponsored users** section, select the racers for whom you want to resume
   sponsorship.
2. Choose **Resume sponsorship**.

###### To view racers' models

- On the **Your Models** page, under **Models**, you can view your models
  and your users' models.

## Next steps

After you have set up and activated multi-user mode, you can take the following steps:

- Create a community race.
- Request an AWS DeepRacer workshop.

### Create a community race

Community races provide an exciting way for your sponsored participants to experience reinforcement learning.

You can create community races and invite your sponsored participants.

For more information, see [Create a virtual community race: a quick start guide](deepracer-create-community-race.md "deepracer-create-community-race.md") .

### Request a workshop

You can request a workshop to learn more about AWS DeepRacer with a 60-minute online or in-person workshop.

For more information, see [Workshop.](https://pages.awscloud.com/GLOBAL-ln-GC-DeepRacer-Enterprise-Events-2021-interest.html "https://pages.awscloud.com/GLOBAL-ln-GC-DeepRacer-Enterprise-Events-2021-interest.html")
