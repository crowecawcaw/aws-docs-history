# Migrating an Amazon Q Business direct SAML 2.0

application to IAM Identity Center

###### Important

This content applies only to Amazon Q Business applications that need to migrate
from using legacy SAML identity management to using IAM Identity Center for user access
management.

To migrate an Amazon Q Business application connected directly to an external
identity provider (IdP) to IAM Identity Center for user access management, follow the steps in this
section.

If your existing external IdP application is connected to a [supported
Amazon Q Business data source connector](connectors-list.md "connectors-list.md") that already has access
control (ACL) and identity crawling enabled, it's ready to migrate to IAM Identity Center. If your
existing external IdP application is connected to a [supported
Amazon Q Business data source connector](connectors-list.md "connectors-list.md") that doesn't already have ACL
or identity crawling enabled, you need to first enable these before you can begin migrating
your application to IAM Identity Center. You do this by [updating your application](supported-app-actions.md#update-app "supported-app-actions.md#update-app").

If you've not used IAM Identity Center before, Amazon Q Business will give you the option to
create an IAM Identity Center instance from the Amazon Q Business console as part of the migration
path. However, we recommend configuring an IAM Identity Center instance before migrating your existing
SAML 2.0 compliant application to IAM Identity Center, especially if you're planning to connect your IAM Identity Center
to an Active Directory or external identity provider. If you're managing users and groups in
one identity source, changing to a different identity source might remove all user and group
assignments.

For important information on creating an IAM Identity Center instance for your Amazon Q Business
application, see [Configuring an IAM Identity Center instance](idc-setup.md "idc-setup.md").

The following tabs provide a procedure for migrating an existing, legacy SAML 2.0 based
Amazon Q Business application to IAM Identity Center using the AWS Management Console and the AWS CLI.

###### Topics

- [Migrating an application](#migrating-application "#migrating-application")

## Migrating an application

The following tabs provide a procedure for migrating your application on the AWS Management Console
and code examples for the AWS CLI.

Console
**To migrate an Amazon Q Business
application**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In **Applications**, select the name of your SAML
   2.0 integrated application from the list of applications.
3. In **Advanced IAM Identity Center settings**, activate
   **Enable cross-region calls** to access
   resources to allow Amazon Q Business to connect to an IAM Identity Center
   instance that exists in a region not already supported by Amazon Q Business. For more information, see [Creating a cross-region IAM Identity Center
   integration](idc-setup.md#cross-region-idc "idc-setup.md#cross-region-idc").
4. Then, depending on your Amazon Q Business application
   configuration you will see one of the following:
   1. If the **Connect to IAM Identity Center** banner on the
      top of the page asks you to activate your ACL and identity
      crawling in preparation for migrating your application, you
      will need to activate ACL and identity crawling for the data
      sources connected to your application before migrating your
      application to IAM Identity Center. To do this, [update your application](supported-datasource-actions.md#update-datasources "supported-datasource-actions.md#update-datasources").
      Then, move to the next step.
   2. If the **Connect to IAM Identity Center** banner on the
      top of the page displays a **Connect to
      IAM Identity Center** option, it means ACL and identity
      crawling are already enabled for your application and it's
      ready to migrate to IAM Identity Center. You can move to the next
      step.

5. From the **Connect to IAM Identity Center** banner on the top
   of the page, select **Connect to IAM Identity Center**.
6. In **Connect Amazon Q Business to IAM Identity Center**,
   you will see the following options based on whether you have an
   IAM Identity Center instance already configured, or need to create one.
   1. If you don't have an IAM Identity Center instance configured, you see
      the following:
      - The region your Amazon Q Business
        application is in. This is so you can make sure that
        the region for your Amazon Q Business
        application and IAM Identity Center instance match.
      - **Specify tags for IAM Identity Center**
        – Add tags to keep track of your IAM Identity Center
        instance.
      - **Create IAM Identity Center** – Select
        to create a minimally-configured IAM Identity Center instance. The
        console will display an ARN for your newly created
        resource after it's created.

   2. If you have _both_ an IAM Identity Center
      organization instance and an account instance configured,
      your instances will be auto-detected, and you see the
      following options:
      - **[Connect to organization
        instance of IAM Identity Center](../../../singlesignon/latest/userguide/organization-instances-identity-center.md "../../../singlesignon/latest/userguide/organization-instances-identity-center.md")** –
        Select this option to manage access to Amazon Q Business by assigning users and groups from
        the Identity Center directory for your
        organization.
      - **[Connect to account instance
        of IAM Identity Center](../../../singlesignon/latest/userguide/organization-instances-identity-center.md "../../../singlesignon/latest/userguide/organization-instances-identity-center.md")** – Select this
        option to manage access to Amazon Q Business
        by assigning existing users and groups from your
        Identity Center directory.
      - The region your Amazon Q Business
        application is in. This is so you can make sure that
        the region for your Amazon Q Business
        application and IAM Identity Center instance match.
      - **IAM Identity Center** – The ARN for
        your IAM Identity Center instance.

   3. If you have an IAM Identity Center account instance configured, your
      account instance will be auto-detected and you will see the
      following:
      - The region your Amazon Q Business
        application is in. This is so you can make sure that
        the region for your Amazon Q Business
        application and IAM Identity Center instance match.
      - **IAM Identity Center** – The ARN for
        your IAM Identity Center instance.

   4. If you have an IAM Identity Center organization instance configured, you
      will see a message asking you to tell your admin to give you
      access to IAM Identity Center. You will need access to IAM Identity Center before you
      can proceed.

###### Note

If you plan to connect your IAM Identity Center to an Active Directory or
external identity provider we recommend canceling this setup and
configuring IAM Identity Center from the IAM Identity Center console. If you're managing
users and groups in one identity source, changing to a different
identity source might remove all user and group
assignments. 7. From the application summary page, select **Groups and
users**, and add users.

###### Note

If you plan to add groups to your application create these
groups in IAM Identity Center before you create your application. If you don't
have already configured IAM Identity Center groups, Amazon Q Business
will redirect you to the IAM Identity Center console to configure groups
before you can add them to your applicaton. 8. Then, from the application summary page, select **Migrate
application** from the banner on the top of the
page. 9. In the **Migrate application traffic** dialog box
that opens, for **Service access**, choose an
existing service role or create a new one. Amazon Q Business
needs these permissions to access the resources it needs to migrate
your application. For more information on the permissions required,
see [IAM role for Amazon Q Business data source
connectors](iam-roles.md "iam-roles.md"). 10. Select **Migrate**.

When the migration is complete, the console displays a
**Successfully migrated application traffic to
IAM Identity Center** message.

AWS CLI
**To migrate an Amazon Q Business
application**

**Before starting the migration process, confirm the
presence of you web experience using the following
command:**

```

aws qbusiness list-web-experiences \
--application-id `application-id`

```

If the `list-web-experiences` command returns a
`webExperienceId`, you can proceed with migrating your
application regardless of the status of the web experience.

**If the `list-web-experiences` command
doesn't return a `webExperienceId`, you
_must_ create a new web experience before
proceeding with migration using the following command:**

```

aws qbusiness create-web-experience \
--application-id `application-id`

```

**Then, update your Amazon Q Business
application using the following command:**

```

aws qbusiness update-application \
--application-id `application-id` \
--identity-center-instance-arn `idc-instance-arn`

```

**Wait for your application status to change from
`UPDATING` to `ACTIVE`. The response should
include the `identityCenterApplicationArn` as one of the
response fields. Check this is the case using the following
command:**

```

aws qbusiness get-application \
--application-id `application-id`

```

**After your application status changes to
`UPDATING`, add users and groups to your application
using the following commands:**

To add users to an application

```

aws sso-admin create-application-assignment \
--application-arn `idc-app-arn` \
--principal-id `idc-user-ID` \
--principal-type USER
```

To add groups to an application

```

aws sso-admin create-application-assignment \
--application-arn `idc-app-arn` \
--principal-id `idc-group-ID` \
--principal-type GROUP
```

**Then, update your Amazon Q Business web
experience using the following command:**

```

aws qbusiness update-web-experience \
--role-arn `role-arn-value` \
--application-id `application-id` \
--web-experience-id `web-experience-id`

```

###### Note

For IAM role permissions required, see [IAM role for an Amazon Q Business web
experience](iam-roles.md#deploy-experience-iam-role "iam-roles.md#deploy-experience-iam-role").
