

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Managing Amazon Q Business admin controls and guardrails
<a name="guardrails-management"></a>

To manage Amazon Q Business admin controls and guardrails, you can take the following actions:

**Note**  
You can't create or delete guardrail global controls. You can only update existing global controls in your application environment.

**Topics**
+ [Deleting topic controls](#guardrails-update)
+ [Getting topic control properties](#topic-control-properties)

## Deleting topic controls
<a name="guardrails-update"></a>

To delete configured chat controls, you can use AWS Management Console or the [DeleteChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteChatControlsConfiguration.html) API operation. The following tabs provide a procedure for the console and code examples for the AWS CLI.

------
#### [ Console ]

**To delete topic controls**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application environment from the list of applications.

1. From the left navigation menu, choose **Enhancements**, and then choose **Guardrails**.

1. In **Guardrails**, from **Topic specific controls**, choose the topic control you want to delete, and then choose **Delete**.

1. In the dialog box, type **delete** to confirm your action.

   The console displays a successful deletion message when the plugin deletion process is finished.

------
#### [ AWS CLI ]

**To delete a topic specific control**

```
aws qbusiness delete-chat-controls-configuration \
--application-id {{application-id}}
```

------

## Getting topic control properties
<a name="topic-control-properties"></a>

To get the details of Amazon Q Business topic controls, you can use either the AWS Management Console or the [GetChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetChatControlsConfiguration.html) API operation. The following tabs provide a procedure for the console and code examples for the AWS CLI.

------
#### [ Console ]

**To get configured details for admin controls and guardrails** 

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. From the Amazon Q Business console, in **Applications**, select the name of your application environment from the list of applications.

1. From the left navigation menu, choose **Enhancements**, and then choose **Admin controls and guardrails**.

   You will find the details of your configured **Global controls** and **Topic specific controls** on the page.

------
#### [ AWS CLI ]

**To get admin controls and guardrails details** 

```
aws qbusiness get-chat-control-configuration \
--application-id {{application-id}}
```

------