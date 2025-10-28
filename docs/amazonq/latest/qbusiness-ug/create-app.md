# Creating an Amazon Q Business application environment

To create an Amazon Q Business application environment, you can use either the AWS Management Console
or the Amazon Q Business API. When you create an application, response generation
from large language model (LLM) knowledge is enabled by default.

As a prerequisite, make sure that you complete the [setting
up](setting-up.md "setting-up.md") tasks and go through the [Configuring an
IAM Identity Center instance](idc-setup.md "idc-setup.md") section. If you're using the AWS CLI or the API, make sure that
you've created the required [IAM roles](setting-up.md "setting-up.md").

When you create an application environment, you can also choose to create a Amazon Q Business web experience. If you use the console to create an application environment,
the web experience is created automatically, unless you choose otherwise. If you use the
[CreateApplication](../api-reference/API_CreateApplication.md "../api-reference/API_CreateApplication.md") API operation to
create an application environment, use the [CreateWebExperience](../api-reference/API_CreateWebExperience.md "../api-reference/API_CreateWebExperience.md") API operation to create your web
experience.

When you create an application, you can also add any existing IAM Identity Center users and groups
to your Amazon Q Business application. After you add users or groups to an application environment, you
can then assign and choose [subscription tiers](tiers.md "tiers.md") for each
user or group. If you don't have an existing IAM Identity Center instance or user, you can create both
of these from the Amazon Q Business console when you create your application. You
can't create IAM Identity Center groups from the Amazon Q Business console.

###### Important

You must add, assign, and subscribe at least one user to your Amazon Q Business application environment for it to work as intended. For more information
on user subscriptions for an IAM Identity Center-integrated Amazon Q Business application,
see [Subscriptions for applications using IAM Identity Center](tiers.md#managing-sub-tiers-sso "tiers.md#managing-sub-tiers-sso").

###### Note

As of Oct 31, 2024, once you have created a new Amazon Q Business
application environment, the default web experience will allow users to interact directly with the
LLM to get answers from its general knowledge or uploaded file content, even if the Admin has not yet connected any enterprise data sources.

For existing application environments, the _Allow direct access to LLM_
setting will remain as previously configured. For new application environments, the
_Allow direct access to LLM_ setting will be enabled by default,
though Admins can still disable this if desired.

For a consolidated view of your user subscriptions—including a list of
subscribed users, their subscription status, and applications, accounts, or services a
user can access through their subscriptions—see the [Amazon Q subscriptions page](https://console.aws.amazon.com/amazonq/subscriptions "https://console.aws.amazon.com/amazonq/subscriptions").

The following tabs provide a procedure for creating your Amazon Q Business
application environment and adding subscriptions using the AWS Management Console and code examples for using
the AWS CLI.

Console
**To create an application**

1.  Sign in to the AWS Management Console and open the Amazon Q Business
    console.
2.  On the **Create application** page, for
    **What kind of application do you want to
    build?**, enter the following information for your
    Amazon Q Business application:
    1. **Application name** – A name for
       your Amazon Q Business application environment for easy
       identification. This name is only visible in the AWS Management Console.
       The name can include hyphens (-), but not spaces, and can
       have a maximum of 1,000 alphanumeric characters. Amazon Q Business auto-generates an application name for
       you, unless you choose to enter a custom name.
    2. **Outcome** – Select **Web
       experience** to create a web experience for
       your application. Amazon Q Business creates a web
       experience by default when you create an application. If you
       don't want to create a web experience, unselect this
       option.

3.  For **Access management method**, choose
    **IAM Identity Center (recommended)**. Then, complete the
    following steps:
    1.  (Optional) **Advanced IAM Identity Center settings –
        _optional_** –
        Activate **Enable cross-region calls** to
        allow Amazon Q Business to connect to an IAM Identity Center
        instance that exists in a region not already supported by
        Amazon Q Business. For more information, see
        [Creating a cross-region IAM Identity Center
        integration](setting-up.md#cross-region-idc "setting-up.md#cross-region-idc").
    2.  Then, you will see the following options based on whether
        you have an IAM Identity Center instance already configured, or need to
        create one.
        1. If you don't have an IAM Identity Center instance
           configured, you see the following:
           1. The region your Amazon Q Business
              application environment is in.
           2. **Specify tags for IAM Identity Center**
              – Add tags to keep track of your IAM Identity Center
              instance.
           3. **Create IAM Identity Center** –
              Select to create an IAM Identity Center instance. Depending on
              your setup, you may be prompted to create either
              an account instance, or an organization instance,
              or be given the option to choose between creating
              an account instance and an organization instance.
              The console will display an ARN for your newly
              created resource after it's created.

        2. If you have _both_ an IAM Identity Center
           organization instance and an account instance
           configured, your instances will be auto-detected,
           and you see the following options:
           1. **[Organization instance of
              IAM Identity Center](../../../singlesignon/latest/userguide/organization-instances-identity-center.md "../../../singlesignon/latest/userguide/organization-instances-identity-center.md")** – Select this
              option to manage access to Amazon Q Business
              by assigning users and groups from the Identity
              Center directory for your organization.
           2. **[Account instance of
              IAM Identity Center](../../../singlesignon/latest/userguide/organization-instances-identity-center.md "../../../singlesignon/latest/userguide/organization-instances-identity-center.md")** – Select this
              option to manage access to Amazon Q Business
              by assigning existing users and groups from your
              Identity Center directory.
           3. The region your Amazon Q Business
              application environment is in.
           4. **IAM Identity Center** – The ARN
              for your IAM Identity Center instance.

        3. If you have an IAM Identity Center account instance configured,
           your account instance will be auto-detected.
        4. If you have an IAM Identity Center organization instance
           configured, your organization instance will be
           auto-detected.
        5. If your IAM Identity Center instance is configured in an AWS
           region Amazon Q Business isn’t available in,
           and you haven’t activated cross-region IAM Identity Center calls,
           you will see a message saying that a connection is
           unavailable with an option to **Switch
           region**. Once you allow a cross-region
           connection between Amazon Q Business and IAM Identity Center
           using **Advanced IAM Identity Center settings**,
           your cross-region IAM Identity Center instance will be
           auto-detected by Amazon Q Business.

        ###### Note

        Selecting **Switch region**
        will only give you the option to change your
        AWS Management Console region. To create a cross-region IAM Identity Center
        connection, use **Advanced IAM Identity Center
        settings**.

    3.  In **Quick start user –
        _optional_**, do the
        following:
        1.  In **Select user**, choose from
            the following options:
            1.  If you've connected a pre-configured IAM Identity Center
                instance with users and groups already configured,
                Amazon Q Business detects the users and
                groups you have configured in IAM Identity Center. In this case,
                you can select **Choose a user**
                and, from the dropdown menu that opens, add users
                and groups directly from your IAM Identity Center
                directory.
            2.  If you've created a IAM Identity Center instance from
                within the Amazon Q Business console for your Amazon Q Business
                application, you can add a new user to your
                application and IAM Identity Center instance. Choose
                **Add new users and groups** and
                then complete the following steps:
                1. In the **Add new users**
                   dialog box that opens, enter the details of your
                   user. Then select **Next** and
                   **Add**.

                ###### Note

                You can add multiple users by selecting
                **Add new user** and entering
                each user's details before you select
                **Add**.

                Then, select **Assign**.
                The user is automatically added to an IAM Identity Center
                directory. 2. The details you must enter for each user
                include:

                    * **Username** – A
                     username is required for a user to sign into the
                     AWS access portal. You can't change the
                     username later. Maximum length 128 characters. Can
                     only contain alphanumeric characters or any of the
                     following: +=,.@-\_
                    * **First name** –
                     First name of user.
                    * **Last name** – Last
                     name of user.
                    * **Email address** –
                     Email address of user.
                    * **Confirm email address**
                     – Enter email address again to confirm
                     it.
                    * **Display name** –
                     The display name assigned to your user.

        2.  For **Select subscription**
            – Choose between **Q Business
            Pro** and **Q Business
            Lite**

        ###### Note

        Amazon Q Business assigns Q Business Pro
        subscriptions to users and groups by default. To
        learn more about subscription tiers, see [User subscription
        tiers](tiers.md#user-sub-tiers "tiers.md#user-sub-tiers").

        ###### Important

        If you add a user to a group in IAM Identity Center and have
        given that group access to your application, it
        can take up to 24 hours for the change to take
        effect and for the user to be able to access your
        Amazon Q Business application.

4.  For **Application details** – Amazon Q Business chooses the following configuration settings for
    your application by default:
    1. For **Application service access**
       – Amazon Q Business will create a new
       service-linked role for your application.
    2. **Encryption** – Amazon Q Business will create an AWS owned AWS KMS key to
       encrypt your data.
    3. **Web experience service access**
       – If you've chosen to create a web experience,
       Amazon Q Business creates a service access role to
       allow end users to log in to a Amazon Q Business web
       experience.

5.  (Optional) To customize **Application details**,
    expand the **Application details section**, and
    then do the following:
    1. In **Application service access**, for
       **Choose a method to authorize Amazon Q Business**, choose from the
       following options:
       1. **Create and use a new service-linked role
          (SLR)** – Create and use a new
          Amazon Q Business-managed IAM role to
          allow it to access the AWS resources
          it needs to create your application.
       2. **Create and use a new service role
          (SR)** – Create and use a new
          IAM role for Amazon Q Business to allow it to access the AWS
          resources it needs to create your
          application.
       3. **Use an existing service role
          (SR)/service-linked role (SLR)** –
          Use an existing service role or service-linked
          IAM role to allow Amazon Q Business to access the AWS
          resources it needs to create your
          application.

       ###### Note

       For more information about example service
       roles, see [IAM role for an Amazon Q Business application](create-application-iam-role.md "create-application-iam-role.md"). For
       information on service-linked roles, including to
       manage them, see [Using service-linked
       roles](../business-use-dg/using-service-linked-roles.md "../business-use-dg/using-service-linked-roles.md"). 4. **Service role name** – A
       name for the service (IAM) role you
       created for easy identification on the
       console.

    2. For **Encryption** – Amazon Q Business encrypts your data by default using
       AWS managed AWS KMS keys. To customize your
       encryption settings, select **Customize encryption
       settings (advanced)**. Then, you can choose to
       use an existing AWS KMS key or create a new
       one.
    3. In **Web experience service access**,
       enter the following information:
       1. For **Choose a method to authorize Amazon Q Business** – A service
          access role assumed by end users when they sign in
          to your web experience that grants them permission
          to start and manage conversations Amazon Q Business. You can choose to use an existing
          role or create a new role.
       2. **Service role name** – A
          name for the service role you created for easy
          identification on the console.

6.  To start creating your application, choose
    **Create**.

###### Note

If you're creating a web experience, you can also choose to
create your application and [view and customize your web
experience](customizing-web-experience.md "customizing-web-experience.md") by selecting **Create and open
web experience**.

AWS CLI
**To configure an Amazon Q Business application**

```

aws qbusiness create-application \
--display-name `application-name` \
--identity-center-instance-arn `identity-center-instance-arn` \
--role-arn `roleArn` \
--description `application-description` \
--encryption-configuration `kmsKeyId=<kms-key-id>` \
--attachments-configuration `attachmentsControlMode=ENABLED`

```

**To add users to an application environment**

```

aws sso-admin create-application-assignment \
--application-arn `idc-app-arn` \
--principal-id `idc-user-ID` \
--principal-type USER
```

**To provision a user subscription**

```

aws qbusiness create-subscription \
--application-id `application-id` \
--principal user=`idc-user-id` \
--type `subscription-type`
```

**To add groups to an application environment**

```

aws sso-admin create-application-assignment \
--application-arn `idc-app-arn` \
--principal-id `idc-group-ID` \
--principal-type GROUP
```

**To provision a group subscription**

```

aws qbusiness create-subscription \
--application-id `application-id` \
--principal group=`idc-group-id` \
--type `subscription-type`

```
