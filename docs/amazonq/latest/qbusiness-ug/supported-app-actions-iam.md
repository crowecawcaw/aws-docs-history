# Managing Amazon Q Business

applications

To manage an Amazon Q Business application environment, you can take the following
actions:

###### Actions

- [Deleting an application](#delete-app-iam "#delete-app-iam")
- [Getting application environment properties](#describe-app-iam "#describe-app-iam")
- [Listing applications](#list-app-iam "#list-app-iam")
- [Updating an application environment](#update-app-iam "#update-app-iam")

## Deleting an application

To delete an Amazon Q Business application environment, you can use the console or
the [DeleteApplication](../api-reference/API_DeleteApplication.md "../api-reference/API_DeleteApplication.md") API
operation.

The following tabs provide a procedure for the console and code examples for
the AWS CLI.

Console
**To delete an Amazon Q Business
application**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, choose
   **Actions**.
3. Choose **Delete**.
4. In the dialog box that opens, type
   `Delete` to confirm deletion, and
   then choose **Delete**.

You are returned to the service console while your
application environment is deleted. When the deletion process is
complete, the console displays a message confirming
successful deletion.

AWS CLI
**To delete an Amazon Q Business
application environment**

```

aws qbusiness delete-application \
--application-id `application-id`

```

## Getting application environment properties

To get the properties of an Amazon Q Business application environment, you can use
the console or the [GetApplication](../api-reference/API_GetApplication.md "../api-reference/API_GetApplication.md") API
operation.

The following tabs provide a procedure for the console and code examples for
the AWS CLI.

Console
**To get properties of an Amazon Q Business application environment**

1.  Sign in to the AWS Management Console and open the Amazon Q Business console.
2.  For **Applications**, select the name of
    your application environment from the list of applications.
3.  On **Application settings**, the
    following properties are available:

        * **Application name** – The
         name that you chose for your application environment.
        * **Application ID** – The
         ID assigned to your application environment.
        * **Subtitle** – The
         subtitle that you chose to assign to your
         application environment.
        * **Service access** – The
         service access role that your application environment is
         using.
        * **Title** – The title that
         you gave to your application environment.
        * **Application status** –
         The status of your application environment.

    To update a setting, select
    **Edit**.

AWS CLI
**To get Amazon Q Business application
properties**

```

aws qbusiness get-application \
--application-id `application-id`

```

## Listing applications

To list Amazon Q Business applications, you can use the console or the
[ListApplications](../api-reference/API_ListApplications.md "../api-reference/API_ListApplications.md") API
operation.

The following tabs provide a procedure for the console and code examples for
the AWS CLI.

Console
**To list your Amazon Q Business
application environments**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, all your configured
   application environments are listed.

AWS CLI
**To list Amazon Q Business
application environments**

```

aws qbusiness list-applications \
--max-results `max-results-to-return`

```

## Updating an application environment

To update an Amazon Q Business application environment, you can use the console or
the [UpdateApplication](../api-reference/API_UpdateApplication.md "../api-reference/API_UpdateApplication.md") API
operation.

###### Note

You can't update the retriever you've chosen or change users and groups
added to the application environment when you update it. If you need to update your
retriever, create a new application environment.

If you're integrating your Amazon Q Business application environment with
IAM Identity Center (IDC) as an [AWS-managed](../../../singlesignon/latest/userguide/awsapps.md "../../../singlesignon/latest/userguide/awsapps.md") application environment using and you
want to update users and groups, you can do so from the [application environment summary](../business-use-dg/supported-app-actions.md "../business-use-dg/supported-app-actions.md") page.

The following tabs provide a procedure for the console and code examples for
the AWS CLI.

Console
**To update an Amazon Q Business
application environment**

###### Option 1

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application environment from the list of applications.
3. In **Applications**, choose
   **Actions**.
4. Choose **Edit**.

On the **Update application** page, edit
your application environment settings.

###### Option 2

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application environment from the list of applications.
3. On the application page, select **Edit**
   from the page header, or select **Edit**
   from **Application settings**.
4. Choose **Edit**.

On the **Update application** page, edit
your application environment settings.

AWS CLI
**To update an Amazon Q Business
application environment**

```

aws qbusiness update-application \
--application-id `application-id` \
--display-name `application-name` \
--role-arn `roleArn` \
--description `application-description` \
--attachments-configuration `attachmentsControlMode=ENABLED`

```
