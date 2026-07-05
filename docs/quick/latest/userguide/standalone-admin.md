# Managing a Amazon Quick Free or Plus account

Amazon Quick Free and Plus accounts – created through the direct signup process at
[aws.com/quick](https://aws.com/quick "https://aws.com/quick") – include a built-in
administration interface for managing your account, users, assets, billing, and support.
This interface is accessible directly within the Amazon Quick web application, without
requiring access to the AWS Management Console.

###### Note

This section applies to Amazon Quick Free and Plus accounts only. If your organization
accesses Amazon Quick through the AWS Management Console, see [Administering Amazon Quick](../../../quicksuite/latest/userguide/qsysadmin.md "../../../quicksuite/latest/userguide/qsysadmin.md") for information about managing your account
using IAM, IAM Identity Center, and other AWS services.

###### Topics

- [Account administration overview](#standalone-admin-overview "#standalone-admin-overview")
- [Accessing the Manage Account page](#standalone-admin-access "#standalone-admin-access")
- [Manage Account page layout](#standalone-admin-layout "#standalone-admin-layout")
- [Free and Plus vs. AWS Console administration](#standalone-admin-comparison "#standalone-admin-comparison")

## Account administration overview

When you create a Amazon Quick Free or Plus account at aws.com/quick, the person who
completes the signup process is automatically assigned the **administrator** role. As the account administrator, you have full access
to all account management capabilities, including user management, asset oversight,
plan and billing configuration, and support resources.

Free and Plus account administration is organized into the following sections:

| Section              | Description                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Users**            | Invite team members, manage active users, view usage<br>statistics, and manage pending invitations. For more information, see<br>[Managing users in a Amazon Quick Free or Plus<br>account](../../../quicksuite/latest/userguide/standalone-users.md "../../../quicksuite/latest/userguide/standalone-users.md").                     |
| **Assets**           | View and manage all account resources including chat agents,<br>spaces, automations, and built-in tools. For more information, see<br>[Managing assets in a Amazon Quick Free or Plus<br>account](../../../quicksuite/latest/userguide/standalone-assets.md "../../../quicksuite/latest/userguide/standalone-assets.md").             |
| **Plan and billing** | View your current plan, estimated charges, payment methods,<br>and billing history. Upgrade or change your plan. For more<br>information, see [Plan and billing for Amazon Quick Free and Plus<br>accounts](../../../quicksuite/latest/userguide/standalone-billing.md "../../../quicksuite/latest/userguide/standalone-billing.md"). |
| **Support**          | Access AWS Support resources for help with your<br>Amazon Quick account.                                                                                                                                                                                                                                                              |

## Accessing the Manage Account page

###### To access account administration

1. Sign in to Amazon Quick at [aws.com/quick](https://aws.com/quick "https://aws.com/quick").
2. From the navigation panel, choose your username
   (displayed with your initials and name).
3. From the profile menu, choose **Manage account**.

The Manage Account page opens, displaying an overview dashboard with a
summary of your account sections.

## Manage Account page layout

The Manage Account page uses a left-side navigation panel with the following
sections:

- **Manage account** – The overview
  dashboard. Displays a summary card for each section, including a user count
  and a **Manage** link that navigates directly to the Users
  page.
- **Users** – Manage active users and
  pending invitations. See [Managing users](../../../quicksuite/latest/userguide/standalone-users.md "../../../quicksuite/latest/userguide/standalone-users.md").
- **Assets** – View and manage account
  resources. See [Managing assets](../../../quicksuite/latest/userguide/standalone-assets.md "../../../quicksuite/latest/userguide/standalone-assets.md").
- **Plan and billing** – Opens the plan
  and billing settings page in a new browser tab. See [Plan and billing](../../../quicksuite/latest/userguide/standalone-billing.md "../../../quicksuite/latest/userguide/standalone-billing.md").
- **Support** – Opens the AWS Support
  portal in a new browser tab for submitting support requests.

## Free and Plus vs. AWS Console administration

The following table summarizes the key differences between Free and Plus account
administration and AWS Console–based administration.

| Feature               | Free or Plus account (aws.com/quick)                 | AWS Console account                             |
| --------------------- | ---------------------------------------------------- | ----------------------------------------------- |
| **Identity provider** | Email or social login                                | IAM Identity Center, IAM, or federated identity |
| **Admin interface**   | Built-in Quick web UI (Manage Account<br>page)       | AWS Management Console                          |
| **User management**   | Email-based invitations                              | IAM Identity Center groups, IAM users           |
| **Billing**           | Billing portal<br>(account.global.app.aws)           | AWS Billing and Cost Management console         |
| **Plans**             | Free, Plus                                           | Standard AWS subscription pricing               |
| **Account creation**  | Automatic (AWS account created behind the<br>scenes) | Manual AWS account setup required               |

###### Note

Regardless of how your Amazon Quick account was created, all product features
– including chat, chat agents, spaces, research, automations, Amazon Quick Sight,
integrations, and extensions – function identically. The differences are
limited to account setup, identity management, and billing.
