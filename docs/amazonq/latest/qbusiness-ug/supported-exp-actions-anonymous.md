

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Managing Amazon Q Business web experiences for anonymous access
<a name="supported-exp-actions-anonymous"></a>

To manage Amazon Q Business web experiences for anonymous access, you can take the following actions:

**Topics**
+ [Share an anonymous web experience](#create-experience-anonymous-url)
+ [Deleting a web experience](#delete-web-experience-anonymous)
+ [Getting properties of a web experience](#describe-web-experience-anonymous)
+ [Listing web experiences](#list-web-experiences-anonymous)
+ [Updating a web experience](#update-web-experience-anonymous)

## Share an anonymous web experience
<a name="create-experience-anonymous-url"></a>

If you created a web experience when you created your application, you can preview that Amazon Q Business web experience for anonymous access, using the console or the [CreateAnonymousWebExperienceUrl](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateAnonymousWebExperienceUrl.html) API operation.

**Note**  
The preview URL for the web experience is for one-time use only and has to be regenerated every time. This URL must be accessed within 5 minutes of creation. Once accessed, the session remains active for the configured duration. To use the web experience in your applications, you must use the [Amazon Q embedded](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/embed-amazon-q-business.html) feature and call the [CreateAnonymousWebExperienceUrl](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateAnonymousWebExperienceUrl.html) API operation whenever you need a new application session or after one hour whichever comes first.
All anonymous web experience URLs generated are able to process billable chat requests until the sessions expire. For more information, see [Amazon Q Business pricing](https://aws.amazon.com/q/business/pricing/).

The following tabs provide a procedure for the AWS Management Console and code examples for the AWS CLI.

------
#### [ Console ]

1. After [Creating an anonymous access application environment](create-anonymous-application.md#create-anonymous-app) in the console with a web experience, you can navigate to your anonymous application. 

1. In the **Web experience settings** section in the console, you can **Preview web experience** to view the web experience. 

1. Alternatively, you can choose to **Share the web experience URL** to share the web experience. To do this, you can choose the duration your **Testing link is valid for** and choose **Create URL**. The URL will be automatically copied to your clipboard.

------
#### [ AWS CLI ]

**To share an Amazon Q Business anonymous web experience url**

After [Creating an anonymous access application environment](create-anonymous-application.md#create-anonymous-app) with a web experience, you can do the following.

```
aws qbusiness create-anonymous-web-experience-url \ 
--application-id {{<your-application-id>}} \
--web-experience-id {{<web-experience-id>}}
--session-duration-in-minutes{{<x-minutes >}}
```

------

## Deleting a web experience
<a name="delete-web-experience-anonymous"></a>

To delete an Amazon Q Business web experience, you can use the console or the [DeleteWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteWebExperience.html) API operation.

If you're using the API, you can delete a web experience without deleting the application environment that it's a part of.

If you're using the console, the only way to delete your Amazon Q Business web experience is to delete the Amazon Q Business application environment that it's attached to.

**Note**  
Even after deleting the web experience all URLs connected to this web experience continue to process billable chat requests until their sessions expire. For more information, see [Share an anonymous web experience](#create-experience-anonymous-url).

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
<a name="describe-web-experience-anonymous"></a>

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
<a name="list-web-experiences-anonymous"></a>

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
<a name="update-web-experience-anonymous"></a>

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
--subtitle {{subtitle}} \     
--title {{title}} \
--welcome-message {{welcome-message}}
```

------