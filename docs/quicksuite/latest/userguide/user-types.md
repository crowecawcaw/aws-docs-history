# Amazon Quick Suite user types

Amazon Quick Suite has three distinct user personas based on permission levels and use cases:
administrator, author, and reader. Within these personas, there are six specific user roles
that can be assigned, including Pro versions that provide access to advanced Amazon Quick Suite
capabilities. The following sections describe the role and task boundaries of each
type.

###### Topics

- [Understanding Amazon Quick Suite subscriptions and
  roles](#subscription-role-mapping "#subscription-role-mapping")
- [Understanding reader capabilities](#reader-user-type "#reader-user-type")
- [Understanding author capabilities](#author-user-type "#author-user-type")
- [Understanding admin capabilities](#admin-user-type "#admin-user-type")

## Understanding Amazon Quick Suite subscriptions and

roles

The new capabilities for Amazon Quick Suite are available via the following monthly user
subscriptions:

- **Amazon Quick Suite Professional** (or Amazon Quick Sight Reader
  Pro role)
- **Amazon Quick Suite Enterprise** (or Amazon Quick Sight Author
  Pro role)

To manage Amazon Quick Suite users, billing and services, you need the Admin Pro role, which
is the same as Amazon Quick Suite Enterprise user subscription.

Amazon Quick Suite also provides the following monthly user subscriptions to support
business only (BI) only use cases:

- **Amazon Quick Sight Reader** – For users who need to
  view and interact with dashboards and reports.
- **Amazon Quick Sight Author** – For users who need to
  create and manage BI content.

To manage Amazon Quick Sight users, billing and services, you need Admin role, which is
the same as Amazon Quick Sight Author user subscription.

###### Note

For pricing information, see [Amazon Quick Suite
pricing](https://aws.amazon.com/quicksuite/pricing/ "https://aws.amazon.com/quicksuite/pricing/")

## Understanding reader capabilities

Readers can use Quick Suite to access company data and find answers through chat
interactions with AI agents. They can upload files, run automations, create
visualizations, and share spaces via direct links. Reader Pro users additionally have
access to advanced Amazon Quick Suite features including AI chat agents, collaborative spaces,
flows, and extensions. For detailed information about reader capabilities and
subscription types, see [Amazon Quick Suite pricing](https://aws.amazon.com/quicksuite/pricing/ "https://aws.amazon.com/quicksuite/pricing/").

## Understanding author capabilities

Authors are domain experts who build and manage Quick Suite resources. In
addition to reader capabilities, they can create datasets, dashboards, automations, and
agents. They have expanded sharing permissions for spaces and can use AI to create
visualizations. Author Pro users can additionally create content using natural language,
build knowledge bases, configure actions, and access advanced automation capabilities.
For detailed information about author capabilities and subscription types, see [Amazon Quick Suite
pricing](https://aws.amazon.com/quicksuite/pricing/ "https://aws.amazon.com/quicksuite/pricing/").

## Understanding admin capabilities

Administrators manage user access, monitor costs, and maintain data sources with full
reader and author capabilities. There are two types of administrators: system
administrators oversee the broader AWS environment including Amazon Quick Suite signup,
system health, and security; Amazon Quick Suite administrators manage users and resources
within Amazon Quick Suite.

When your Amazon Quick Suite account is integrated with IAM Identity Center, admin capabilities are
divided between IAM permissions and Amazon Quick Suite admin role permissions. Access to
some sections of the Amazon Quick Suite administration console is restricted by IAM
permissions. The following table summarizes the admin actions that you can perform in
Amazon Quick Suite based on the access type that you choose.

| Admin action               | IAM permissions                 | Amazon Quick Suite admin role permissions |
| -------------------------- | ------------------------------- | ----------------------------------------- |
| **Manage assets**          | Yes                             | No                                        |
| **Security & permissions** | Yes                             | No                                        |
| **Manage VPC connections** | Yes                             | No                                        |
| **KMS keys**               | Yes                             | No                                        |
| **Account settings**       | Yes                             | No                                        |
| **Account customization**  | No                              | Yes                                       |
| **Manage users**           | Yes (IAM Identity Center users) | Yes (Amazon Quick Suite and IAM users)    |
| **Your subscriptions**     | No                              | Yes                                       |
| **Mobile settings**        | No                              | Yes                                       |
| **Domains and embedding**  | No                              | Yes                                       |
| **SPICE capacity**         | No                              | Yes                                       |

Admin and Admin Pro users have full reader and author capabilities but focus primarily
on system administration to ensure efficient and secure operations for all users. For
detailed information about author capabilities and subscription types, see [Amazon Quick Suite
pricing](https://aws.amazon.com/quicksuite/pricing/ "https://aws.amazon.com/quicksuite/pricing/").
