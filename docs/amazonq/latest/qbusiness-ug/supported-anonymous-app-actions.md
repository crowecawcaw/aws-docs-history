# Managing Amazon Q Business anonymous application environments

To manage an Amazon Q Business application environment, you can take the following
actions:

###### Actions

- [Deleting an anonymous application environment](#delete-anonymous-app "#delete-anonymous-app")
- [Getting anonymous application environment properties](#describe-anonymous-app "#describe-anonymous-app")
- [Listing anonymous application environments](#list-anonymous-app "#list-anonymous-app")
- [Updating an application environment](#update-anonymous-app "#update-anonymous-app")

## Deleting an anonymous application environment

To delete an Amazon Q Business anonymous application environment, you can use the
console or the [DeleteApplication](../api-reference/API_DeleteApplication.md "../api-reference/API_DeleteApplication.md") API
operation.

The following tabs provide a procedure for the console and code example for
the AWS CLI.

Console
**To delete an Amazon Q Business
application environment**

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

## Getting anonymous application environment properties

To get the properties of an Amazon Q Business application environment, you can use
the console or the [GetApplication](../api-reference/API_GetApplication.md "../api-reference/API_GetApplication.md") API
operation.

The following tabs provide a procedure for the console and code examples for
the AWS CLI.

Console
**To get properties of an Amazon Q Business application environment**

1.  Sign in to the AWS Management Console and open the Amazon Q Business console.
2.  For **Applications**, select the name of
    your application environment from the list of application environments.
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
**To get Amazon Q Business application environment
properties**

```

aws qbusiness get-application \
--application-id `application-id`

```

## Listing anonymous application environments

To list Amazon Q Business application environments, you can use the console or the
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

The following tabs provide a procedure for the console and code examples for
the AWS CLI.

Console
**To update an Amazon Q Business
application environment**

###### Option 1

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application environment from the list of application environments.
3. In **Applications**, choose
   **Actions**.
4. Choose **Edit**.

On the **Update application environment** page,
edit your application environment settings.

###### Option 2

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   your application environment from the list of application environments.
3. On the application environment page, select
   **Edit** from the page header, or
   select **Edit** from **Application
   settings**.
4. Choose **Edit**.

On the **Update application environment** page,
edit your application environment settings.

AWS CLI
**To update an Amazon Q Business
application environment**

```

aws qbusiness update-application \
--application-id `application-id` \
--display-name `application-name` \
--role-arn `your-role-arn` \
--description `application-description` \
```
