# Creating and setting up an App Studio instance for the first time

## Sign up for an AWS account

An AWS account is required to set up App Studio. Only one AWS account is required to
use App Studio—builders and administrators don't need an AWS account to use
App Studio because access is managed with AWS IAM Identity Center.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Create an administrative user for managing AWS resources

When you first create an AWS account, you begin with a default set of credentials with
complete access to all AWS resources in your account. This identity is called the [AWS account
root user](../../../IAM/latest/UserGuide/root-user-best-practices.md "../../../IAM/latest/UserGuide/root-user-best-practices.md"). For creating AWS roles and resources to be used with App Studio, we
strongly recommend that you do not use the AWS account root user. Instead, we recommend that
you create and use an administrative user.

Use the following topics to create an administrative user for managing AWS roles and resources for use with App Studio.

- For a single, standalone AWS account, see [Create your first
  IAM user](../../../IAM/latest/UserGuide/getting-started-iam-user.md "../../../IAM/latest/UserGuide/getting-started-iam-user.md") in the _IAM User Guide_. You can provide any user
  name, but it must have the `AdministratorAccess` permissions policy.
- For multiple AWS accounts managed through AWS Organizations, see
  [Set up AWS account access for an IAM Identity Center administrative user](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md")
  in the _AWS IAM Identity Center User Guide_.

## Create an App Studio instance in the AWS Management Console

To use App Studio, you must create an instance from the App Studio landing page in the AWS Management Console. There are two methods that can be used
to create an App Studio instance:

1. Easy create: With this simplified method, you set up only one user to access and use App Studio as part of setting up. You should use
   this method if you're evaluating App Studio for your organization or team, or if you only plan to use App Studio yourself. You can add more
   users or groups to App Studio after setup. Note that if you have an organization instance of IAM Identity Center, you can't use this method.
2. Standard create: With this method, you add users or groups and assign them roles in App Studio as part of setting up. You should use
   this method if you want to add more than one user to App Studio when setting up.

###### Note

You can only create one instance of App Studio, across all AWS Regions. If you have an existing instance, you must delete it
before creating another one. For more information, see [Deleting an App Studio instance](instance-delete.md "instance-delete.md").

Easy create

###### To create an App Studio instance in the AWS Management Console with easy create

1.  Open the App Studio console at [https://console.aws.amazon.com/appstudio/](https://console.aws.amazon.com/appstudio/ "https://console.aws.amazon.com/appstudio/").
2.  Navigate to the AWS Region in which you want to create an App Studio instance.
3.  Choose **Get started**.
4.  Choose **Easy create** and choose **Next**.
5.  The next steps to set up App Studio are determined by whether or not you have an IAM Identity Center account instance.
    To find more information about IAM Identity Center instances, including the different types and how to find which type you have, see
    [Manage organization and account instances of IAM Identity Center](../../../singlesignon/latest/userguide/identity-center-instances.md "../../../singlesignon/latest/userguide/identity-center-instances.md")
    in the _AWS IAM Identity Center User Guide_.
    - If you have an account instance of IAM Identity Center:
      1. In **Account permissions**, review the required permissions for enabling App Studio. If your account doesn't have the
         required permissions, you won't be able to enable App Studio.
         You must either get the required permissions added to your account, or switch to an account that has them.
      2. In **Add a user**, search for and select the email address of the user in your
         IAM Identity Center account instance that will access App Studio. This user will have the Admin role in the App Studio instance. If you do not see the user you
         want to provide access to App Studio, you may need to add them to your IAM Identity Center instance.

    - If you do not have an account instance of IAM Identity Center:

    ###### Note

    Setting up App Studio automatically creates an IAM Identity Center account instance with the user you configure during the set up process. After the
    setup is complete, you can add or manage users and groups in the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").

        1. In **Account permissions**, review the required permissions for enabling App Studio. If your account does not have the
         required permissions, you will not be able to enable App Studio.
         You must either get the required permissions added to your account, or switch to an account that has them.
        2. In **Add a user**, provide an **Email address**, **First name**, **Last name**, and
         **Username** for the user accessing App Studio. This user will have the Admin role in the App Studio instance.

6.  In **Service access and roles**, review the service roles and service-linked role that are created automatically
    when you set up App Studio to provide the service with necessary permissions. Choose **View permissions** to see the
    exact permissions granted for service roles, or **View policy** to see the permissions policy attached to the service-linked role.
7.  In **Acknowledgement**, acknowledge the statements by choosing their checkboxes.
8.  Choose **Set up** to create your instance.

###### Note

To add more users or groups to your App Studio instance after setup, you must add them to your IAM Identity Center instance.

Standard create

###### To create an App Studio instance in the AWS Management Console with the standard method

1.  Open the App Studio console at [https://console.aws.amazon.com/appstudio/](https://console.aws.amazon.com/appstudio/ "https://console.aws.amazon.com/appstudio/").
2.  Navigate to the AWS Region in which you want to create an App Studio instance.
3.  Choose **Get started**.
4.  Choose **Standard create** and choose **Next**.
5.  The steps to set up App Studio are determined by whether or not you have an IAM Identity Center instance, and the type of instance.
    To find more information about IAM Identity Center instances, including the different types and how to find which type you have, see
    [Manage organization and account instances of IAM Identity Center](../../../singlesignon/latest/userguide/identity-center-instances.md "../../../singlesignon/latest/userguide/identity-center-instances.md")
    in the _AWS IAM Identity Center User Guide_.
    - If you have an organization instance of IAM Identity Center:
      1. In **Configure access to App Studio with Single Sign-On**, select existing IAM Identity Center groups to provide them with access to App Studio.
         App Studio groups will be created based on the specified configuration. Members of groups added to **Admin groups** will have the
         **Admin** role, and members of groups added to **Builder groups** will have the **Builder**
         role in App Studio. The roles are defined as follows:
         - Admins can manage users and groups within App Studio, add and manage connectors, and manage applications created by builders. Additionally, users
           with the Admin role have all of the permissions included with the Builder role.
         - Builders can create and build applications. Builders cannot manage users or groups, add or edit connector instances, or manage other builders' applications.

    - If you have an account instance of IAM Identity Center instance:
      1. In **Account permissions**, review the required permissions for enabling App Studio. If your account does not have the required permissions, you will not be able to enable App Studio.
         You must either get the required permissions added to your account, or switch to an account that has them.
      2. In **Configure access to App Studio with Single Sign-On**, in **IAM Identity Center account**, choose
         **Use an existing account instance**
      3. In **AWS Region**, choose the Rergion where your IAM Identity Center account instance is located.
      4. Select existing IAM Identity Center groups to provide them with access to App Studio.
         App Studio groups will be created based on the specified configuration. Members of groups added to **Admin groups** will have the
         **Admin** role, and members of groups added to **Builder groups** will have the **Builder**
         role in App Studio. The roles are defined as follows:
         - Admins can manage users and groups within App Studio, add and manage connectors, and manage applications created by builders. Additionally, users
           with the Admin role have all of the permissions included with the Builder role.
         - Builders can create and build applications. Builders cannot manage users or groups, add or edit connector instances, or manage other builders' applications.

    - If you don't have an IAM Identity Center instance:

    ###### Note

    Setting up App Studio automatically creates an IAM Identity Center account instance with the groups you configure during the set up process. After the
    setup is complete, you can add or manage users and groups in the IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").

        1. In **Account permissions**, review the required permissions for enabling App Studio. If your account doesn't have the required permissions, you won't be able to enable App Studio.
         You must either get the required permissions added to your account, or switch to an account that has them.
        2. In **Configure access to App Studio with Single Sign-On**, in **IAM Identity Center account**, choose
         **Create an account instance for me.**
        3. In **Create users and groups and add them to App Studio**, provide a name and add users to an admin group and builder group. Users that are added to the admin group will have the **Admin** role in App Studio, and
         users that are added to the builder group will have the **Builder** role. The roles are defined as follows:




        	+ Admins can manage users and groups within App Studio, add and manage connectors, and manage applications created by builders. Additionally, users
        	with the Admin role have all of the permissions included with the Builder role.
        	+ Builders can create and build applications. Builders cannot manage users or groups, add or edit connector instances, or manage other builders' applications.
        ###### Important

        You must add yourself as a user of the admin group to set up App Studio and have admin access after setting up.

6.  In **Service access and roles**, review the service roles and service-linked role that are created automatically
    when you set up App Studio to provide the service with necessary permissions. Choose **View permissions** to see the
    exact permissions granted for service roles, or **View policy** to see the permissions policy attached to the service-linked role.
7.  In **Acknowledgement**, acknowledge the statements by selecting their checkboxes.
8.  Choose **Set up** to create your instance.
