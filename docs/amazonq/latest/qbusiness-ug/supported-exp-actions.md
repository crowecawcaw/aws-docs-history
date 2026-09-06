

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Managing Amazon Q Business web experiences
<a name="supported-exp-actions"></a>

To manage Amazon Q Business web experiences, you can take the following actions:

**Topics**
+ [Creating a web experience](#create-experience)
+ [Deleting a web experience](#delete-web-experience)
+ [Getting properties of a web experience](#describe-web-experience)
+ [Listing web experiences](#list-web-experiences)
+ [Updating a web experience](#update-web-experience-idp)

## Creating a web experience
<a name="create-experience"></a>

To create an Amazon Q Business web experience, you can use the console or the [CreateWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateWebExperience.html) API operation.

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

If you use the console, this action is spread across two steps: [Configuring an Amazon Q Business application using AWS IAM Identity Center](create-application.md) and [Customizing web experience](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/customizing-web-experience-app.html). To create a web experience, you must create an application environment.

------
#### [ AWS CLI ]

**To create an Amazon Q Business web experience**

```
aws qbusiness create-web-experience \
--application-id {{application-id}} \ 
--sample-prompts-control-mode {{sample-prompts}} \      
--subtitle {{subtitle}} \     
--tags {{tags}} \ 
--title {{title}} \
--welcome-message {{welcome-message}} \
```

------

## Deleting a web experience
<a name="delete-web-experience"></a>

To delete an Amazon Q Business web experience, you can use the console or the [DeleteWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteWebExperience.html) API operation.

If you're using the API, you can delete a web experience without deleting the application environment that it's a part of.

If you're using the console, the only way to delete your Amazon Q Business web experience is to delete the Amazon Q Business application environment that it's attached to.

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

**To delete an Amazon Q Business web experience** 

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, choose **Actions**.

1. Choose **Delete**.

1. In the dialog box that opens, type **Delete** to confirm deletion, and then choose **Delete**.

   You are returned to the service console while your application environment is deleted. When the deletion process is complete, the console displays a message confirming successful deletion. Both the application environment and the web experience are deleted.

------
#### [ AWS CLI ]

**To delete an Amazon Q Business web experience**

```
aws qbusiness delete-web-experience \
--application-id {{application-id}} \
--web-experience-id {{web-experience-id}}
```

------

## Getting properties of a web experience
<a name="describe-web-experience"></a>

To get the properties of an Amazon Q Business web experience, you can use the console or the [GetWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetWebExperience.html) API operation.

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

**To get properties of an Amazon Q Business web experience ** 

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application environment from the list of applications.

1. For **Web experience settings**, the following settings are available:
   + **Web experience IAM role ARN** – The IAM role assumed by end users when they log in to your web experience. 
   + **Deployed URL** – The deployed URL of your web experience. 
   + **Tags** – Tags that are attached to your web experience. 

   To update a setting, choose **Edit**.

------
#### [ AWS CLI ]

**To get properties of an Amazon Q Business web experience**

```
aws qbusiness get-web-experience \
--application-id {{application-id}} \
--web-experience-id {{web-experience-id}}
```

------

## Listing web experiences
<a name="list-web-experiences"></a>

To list Amazon Q Business web experiences, you can use the console or the [ListWebExperiences](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListWebExperiences.html) API operation.

If you use the console, you can only see the web experience that's attached to a single application environment.

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

**To list Amazon Q Business web experiences**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. For **Applications**, the Amazon Q Business web experience attached to your application environment is shown.

------
#### [ AWS CLI ]

**To list Amazon Q Business web experiences**

```
aws qbusiness get-web-experience \
--application-id {{application-id}} \
--web-experience-id {{web-experience-id}} \
--max-results {{max-results-to-return}}
```

------

## Updating a web experience
<a name="update-web-experience-idp"></a>

To update an Amazon Q Business web experience, you can use the console or the [UpdateWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateWebExperience.html) API operation.

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

**To update an Amazon Q Business web experience**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application environment from the list of applications.

1. Select **Customize web experience**.

1. Expand the right navigation menu to edit your web experience settings.

------
#### [ AWS CLI ]

**To update an Amazon Q Business web experience**

```
aws qbusiness update-web-experience \
--application-id {{application-id}} \
--web-experience-id {{web-experience-id}} \
--authentication-configuration {{authentication-configuration}} \  
--sample-prompts-control-mode {{sample-prompts}} \      
--subtitle {{subtitle}} \     
--title {{title}} \
--welcome-message {{welcome-message}}
```

------