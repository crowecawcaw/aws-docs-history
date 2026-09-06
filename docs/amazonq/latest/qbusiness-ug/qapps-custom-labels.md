

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Custom labels for Amazon Q Apps
<a name="qapps-custom-labels"></a>

 To organize and classify apps based on your unique business needs, Administrators can customize the labels available for published Q Apps. You can add up to 10 labels, and remove or update existing labels. Labels help web experience users find Q Apps in the library. 

 For example, you might add custom HR organization-specific labels like *Employee onboarding* and *Benefits inquiries*. When members of your HR team create and use Q Apps, they can use these labels to classify them and help other users find the apps they need. 

**Topics**
+ [Prerequisites for customizing labels](#qapps-labels-prerequisites)
+ [Considerations for customizing labels](#qapps-labels-considersations)
+ [Customizing labels](#qapps-adding-custom-labels)

## Prerequisites for customizing labels
<a name="qapps-labels-prerequisites"></a>

Before your web experience users can use custom labels, the web experience IAM role for your application environment must have permission to perform the `qapps:ListCategories` action. We recommend updating the `QAppsResourceAgnosticPermissions` statement of the IAM policy attached to this role to include the action as follows: 

```
{
"Sid": "QAppsResourceAgnosticPermissions",
"Effect": "Allow",
"Action": [
    "qapps:CreateQApp",
    "qapps:PredictQApp",
    "qapps:PredictProblemStatementFromConversation",
    "qapps:PredictQAppFromProblemStatement",
    "qapps:ListQApps",
    "qapps:ListLibraryItems",
    "qapps:CreateSubscriptionToken"
    "qapps:ListCategories"
],
"Resource": "arn:aws:qbusiness:us-west-2:{{account-number}}:application/{{application-id}}"
}
```

## Considerations for customizing labels
<a name="qapps-labels-considersations"></a>

When you add labels, note the following:
+ The maximum number of labels for an application environment is 10. This includes predefined labels.
+ You can't add duplicate labels.
+ Labels can't include special characters.

## Customizing labels
<a name="qapps-adding-custom-labels"></a>

To customize labels available in an application environment for Q Apps, you can use the Amazon Q Business console or the following API operations.
+ [ListCategories](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListCategories.html)
+ [BatchUpdateCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchUpdateCategory.html)
+ [BatchCreateCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchCreateCategory.html)
+ [BatchDeleteCategory](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchDeleteCategory.html)

After you save your changes, the label updates appear in the web experience immediately. If users don't see the changes, make sure you have configure permissions for the web experience IAM role for your application environment correctly. For more information, see [Prerequisites for customizing labels](#qapps-labels-prerequisites).

The following shows how to customize Q Apps with the Amazon Q Business console or the AWS Command Line Interface.

### Console
<a name="qapps-adding-custom-labels-console"></a>

To customize labels for Q Apps, navigate to the **Q Apps** page for your application environment, choose the **Settings** tab, and add, update, or remove labels.

**To customize labels**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, choose the name of your application environment from the list of applications.

1. From the left navigation menu, choose **Enhancements**, and then choose **Amazon Q Apps**.

1. Choose the **Settings** tab, and add, update, or remove labels.

1. Choose **Save**. After you save your changes, the label updates appear in the web experience immediately.

### AWS CLI
<a name="qapps-adding-custom-labels-cli"></a>

To customize labels with the AWS CLI, use the `list-categories`, `batch-update-category`, `batch-create-category` or `batch-delete-category`commands. 
+ To view all custom labels for your application environment, use the `list-categories` command.

  ```
  aws qapps list-categories --instance-id {{instanceId}} --region {{region}}
  ```
+ If you have reached the 10 label limit, you can use the `batch-update-category` command to update an existing category name.

  ```
  aws qapps batch-update-category \ 
  --instance-id {{instanceId}} \ 
  --categories '[{"id":"{{existingCategoryId}}","title":"{{updatedCategoryName}}"}]' \ 
  --region {{region}}
  ```
+ If you have less than 10 labels, you can use the `batch-create-category` command to add new labels.

  ```
  aws qapps batch-create-category \
  --instance-id  {{instanceId}} \
  --categories '[{"id":"{{uniqueId}}","title":"{{newCategoryName}}"}]' \
  --region {{region}}
  ```
+ To delete categories, use the `batch-delete-category` command. For `categories`, specify the list of IDs of the categories to be deleted.

  ```
  aws qapps batch-delete-category \ 
  --instance-id {{instanceId}} \ 
  --categories '["{{categoryId1}}", "{{categoryId2}}"]' \ 
  --region {{region}}
  ```