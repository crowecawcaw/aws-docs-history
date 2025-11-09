AWS Migration Hub Refactor Spaces is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Step 1: Create an environment

This step describes how to create an environment as part of the Refactor Spaces **Getting
started** wizard. You can also create an environment by choosing
**Environments** under **App Refactor** in the Refactor Spaces
navigation pane.

A Refactor Spaces environment contains the applications, services, and the AWS infrastructure
used to safely and incrementally refactor. Refactor Spaces provides a unified view across multiple
AWS accounts and simplifies multi-account use cases to accelerate application refactoring. You
can create an environment that orchestrates AWS Transit Gateway to bridge cross-account service
communication. Alternatively, you can create an environment without a bridge and manage
service-to-service communication with your own infrastructure. If you choose to use an
environment's network bridge, you can achieve greater deployment independence across accounts and
teams.

After an environment is created, you can share the environment with other AWS accounts,
organizational units (OUs) in AWS Organizations, or an entire AWS
organization. By sharing the environment with other AWS accounts, users in those accounts can
create applications, services, and routes within the environment, unless you use AWS Identity and Access Management
(IAM) to restrict access.

###### To create an environment

1. Using the AWS account that you created in [Setting up](setting-up.md "setting-up.md"), sign in to the AWS Management Console and open the Migration Hub
   console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane, choose **Refactor Spaces**.
3. Choose **Getting started**.
4. Select **Create a refactor environment to start to incrementally modernize to
   microservices in multiple AWS accounts**.
5. Choose **Start**.
6. Enter a name for the environment.
7. (Optional) Add a description for the environment.
8. (Optional) If you select the **Provision Multi-account network bridge**
   check box, Refactor Spaces creates a Transit Gateway for your microservices to communicate with your monolith
   directly across AWS accounts. If you want to use your own network infrastructure for
   communication across accounts, don't select the check box.
9. Refactor Spaces uses a service-linked role to connect to AWS services to orchestrate them on
   your behalf. When you use Refactor Spaces for the first time, the service-linked role is created for
   you with the correct permissions. For more information about the service-linked role, see [Using service-linked roles for
   Refactor Spaces](using-service-linked-roles.md "using-service-linked-roles.md").
10. Choose **Next** to move to the **Create application**
    page.
