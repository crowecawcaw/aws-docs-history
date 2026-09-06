

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Associating IAM roles with an AWS account connection in AWS Migration Hub Journeys
<a name="associate-roles"></a>

**Note**  
The account-connection feature is in preview release. It is available in US East (N. Virginia).  
This is pre-release documentation. Both the account-connection feature and this documentation are subject to change.

After you create an AWS account connection, you can associate IAM roles with it so that the journey that has the connection can use these roles to create and update AWS resources as needed by the tasks of the journey.

**To associate IAM roles with an account connection**

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md).

1. In the left navigation pane, choose **Migration journeys**.

1. In the list of migration journeys, choose the name of the journey for which you want to create the account connection.

1. Choose the **Account connections** tab.

1. Choose the name of the connection with which you want to associate IAM roles. The connection page opens.

1. Choose **Associate roles with connection**. The connection page opens in the console.

1. In the connection page in the console, choose **Create and associate roles with journey**.

1. Review the list of roles, and then choose **Create and associate roles**.