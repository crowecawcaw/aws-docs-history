

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Managing Amazon Q Business applications
<a name="supported-app-actions-iam"></a>

To manage an Amazon Q Business application environment, you can take the following actions:

**Topics**
+ [Deleting an application](#delete-app-iam)
+ [Getting application environment properties](#describe-app-iam)
+ [Listing applications](#list-app-iam)
+ [Updating an application environment](#update-app-iam)

## Deleting an application
<a name="delete-app-iam"></a>

To delete an Amazon Q Business application environment, you can use the console or the [DeleteApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteApplication.html) API operation.

The following tabs provide a procedure for the console and code examples for the AWS CLI.

------
#### [ Console ]

**To delete an Amazon Q Business application** 

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, choose **Actions**.

1. Choose **Delete**.

1. In the dialog box that opens, type **Delete** to confirm deletion, and then choose **Delete**.

   You are returned to the service console while your application environment is deleted. When the deletion process is complete, the console displays a message confirming successful deletion.

------
#### [ AWS CLI ]

**To delete an Amazon Q Business application environment**

```
aws qbusiness delete-application \
--application-id {{application-id}}
```

------

## Getting application environment properties
<a name="describe-app-iam"></a>

To get the properties of an Amazon Q Business application environment, you can use the console or the [GetApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetApplication.html) API operation.

The following tabs provide a procedure for the console and code examples for the AWS CLI.

------
#### [ Console ]

**To get properties of an Amazon Q Business application environment** 

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. For **Applications**, select the name of your application environment from the list of applications.

1. On **Application settings**, the following properties are available:
   + **Application name** – The name that you chose for your application environment. 
   + **Application ID** – The ID assigned to your application environment. 
   + **Subtitle** – The subtitle that you chose to assign to your application environment. 
   + **Service access** – The service access role that your application environment is using. 
   + **Title** – The title that you gave to your application environment. 
   + **Application status** – The status of your application environment.

   To update a setting, select **Edit**.

------
#### [ AWS CLI ]

**To get Amazon Q Business application properties **

```
aws qbusiness get-application \
--application-id {{application-id}}
```

------

## Listing applications
<a name="list-app-iam"></a>

To list Amazon Q Business applications, you can use the console or the [ListApplications](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListApplications.html) API operation.

The following tabs provide a procedure for the console and code examples for the AWS CLI.

------
#### [ Console ]

**To list your Amazon Q Business application environments**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, all your configured application environments are listed.

------
#### [ AWS CLI ]

**To list Amazon Q Business application environments **

```
aws qbusiness list-applications \
--max-results {{max-results-to-return}}
```

------

## Updating an application environment
<a name="update-app-iam"></a>

To update an Amazon Q Business application environment, you can use the console or the [UpdateApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateApplication.html) API operation.

**Note**  
You can't update the retriever you've chosen or change users and groups added to the application environment when you update it. If you need to update your retriever, create a new application environment.  
If you're integrating your Amazon Q Business application environment with IAM Identity Center (IDC) as an [AWS-managed](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps.html) application environment using and you want to update users and groups, you can do so from the [application environment summary](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/supported-app-actions.html) page.

The following tabs provide a procedure for the console and code examples for the AWS CLI.

------
#### [ Console ]

**To update an Amazon Q Business application environment**

**Option 1**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application environment from the list of applications.

1. In **Applications**, choose **Actions**.

1. Choose **Edit**.

   On the **Update application** page, edit your application environment settings.

**Option 2**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application environment from the list of applications.

1. On the application page, select **Edit** from the page header, or select **Edit** from **Application settings**.

1. Choose **Edit**.

   On the **Update application** page, edit your application environment settings.

------
#### [ AWS CLI ]

**To update an Amazon Q Business application environment **

```
aws qbusiness update-application \
--application-id {{application-id}} \
--display-name {{application-name}} \
--role-arn {{roleArn}} \
--description {{application-description}} \
--attachments-configuration {{attachmentsControlMode=ENABLED}}
```

------