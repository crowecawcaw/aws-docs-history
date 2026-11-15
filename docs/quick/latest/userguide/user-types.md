

# AWS Quick user types
<a name="user-types"></a>

AWS Quick has three distinct user personas based on permission levels and use cases: administrator, author, and reader. Within these personas, there are six specific user roles that can be assigned, including Pro versions that provide access to advanced AWS Quick capabilities. The following sections describe the role and task boundaries of each type.

**Topics**
+ [Understanding AWS Quick subscriptions and roles](#subscription-role-mapping)
+ [Understanding reader capabilities](#reader-user-type)
+ [Understanding author capabilities](#author-user-type)
+ [Understanding admin capabilities](#admin-user-type)

## Understanding AWS Quick subscriptions and roles
<a name="subscription-role-mapping"></a>

The new capabilities for AWS Quick are available via the following monthly user subscriptions:
+ **AWS Quick Professional** (or AWS Quick Sight Reader Pro role)
+ **AWS Quick Enterprise** (or AWS Quick Sight Author Pro role)

To manage AWS Quick users, billing and services, you need the Admin Pro role, which is the same as AWS Quick Enterprise user subscription.

AWS Quick also provides the following monthly user subscriptions to support business only (BI) only use cases:
+ **AWS Quick Essentials** (or AWS Quick Sight Reader role) – For users who need to view and interact with dashboards and reports. Starting on October 30th, 2026, Essentials users also have access to AWS Quick AI features.
+ **AWS Quick Sight Author** – For users who need to create and manage BI content.

  To manage AWS Quick Sight users, billing and services, you need Admin role, which is the same as AWS Quick Sight Author user subscription.

**Note**  
For pricing information, see [AWS Quick pricing](https://aws.amazon.com/quicksuite/pricing/)

## Understanding reader capabilities
<a name="reader-user-type"></a>

Both Essentials (Reader) and Professional (Reader Pro) can use Quick to access company data and find answers through chat interactions with AI agents. They can upload files, run automations, create visualizations, and share spaces via direct links. Existing security controls still apply, including row-level and column-level security and administrator Custom Permissions. For pricing, see [AWS Quick pricing](https://aws.amazon.com/quick/pricing/).

## Understanding author capabilities
<a name="author-user-type"></a>

Authors are domain experts who build and manage Quick resources. In addition to reader capabilities, they can create datasets, dashboards, automations, and agents. They have expanded sharing permissions for spaces and can use AI to create visualizations. Author Pro users can additionally create content using natural language, build knowledge bases, configure actions, and access advanced automation capabilities. For detailed information about author capabilities and subscription types, see [AWS Quick pricing](https://aws.amazon.com/quicksuite/pricing/).

## Understanding admin capabilities
<a name="admin-user-type"></a>

Administrators manage user access, monitor costs, and maintain data sources with full reader and author capabilities. There are two types of administrators: system administrators oversee the broader AWS environment including AWS Quick signup, system health, and security; AWS Quick administrators manage users and resources within AWS Quick.

When your AWS Quick account is integrated with IAM Identity Center, admin capabilities are divided between IAM permissions and AWS Quick admin role permissions. Access to some sections of the AWS Quick administration console is restricted by IAM permissions. The following table summarizes the admin actions that you can perform in AWS Quick based on the access type that you choose.


| Admin action | IAM permissions | AWS Quick admin role permissions | 
| --- | --- | --- | 
| **Manage assets** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **Security & permissions** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **Manage VPC connections** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **KMS keys** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **Account settings** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **Account customization** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Manage users** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes (IAM Identity Center users) | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes (AWS Quick and IAM users) | 
| **Your subscriptions** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Mobile settings** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Domains and embedding** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **SPICE capacity** | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | ![](https://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 

Admin and Admin Pro users have full reader and author capabilities but focus primarily on system administration to ensure efficient and secure operations for all users. For detailed information about author capabilities and subscription types, see [AWS Quick pricing](https://aws.amazon.com/quicksuite/pricing/).