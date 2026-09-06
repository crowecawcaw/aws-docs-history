

# Add attributes for personalizing quick responses in Connect Customer
<a name="add-attributes"></a>

You can personalize quick responses by adding user-defined attributes. To do so, you use the Connect Customer admin website to create responses that include [Connect Customer contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-attributes.html). You can also use the [Set contact attributes](set-contact-attributes.md) block to create user-defined attributes in flows.

When quick responses contain user-defined attributes, the value of those attributes, such as customer name, appear when an [agent searches for a response in CCP](search-qr-ccp.md).

The following steps explain how to add user-defined attributes to quick responses. You first create a set-contact attribute, and then you add the attribute to a quick response.

**To create a set-contact attribute**

1. Log in to the Connect Customer admin website at https://*instance name*.my.connect.aws/. Use an **Admin** account, or an account assigned to a security profile that has **Flows - Edit or Create** permissions.

1. On the navigation bar, choose **Routing**, then **Flows**.  
![Menu showing Routing and Flows.](http://docs.aws.amazon.com/connect/latest/adminguide/images/routing-flows.png)

1. On the **Flows** page, the **Type** column lists each type of flow. Choose the flow that you want to add attributes to.

1. Follow the steps in [Creating a set contact attribute](set-contact-attributes.md).
**Note**  
In the contact attribute configuration, select the **User defined** namespace, then save and publish the flow.

1. When finished, complete the next set of steps.

You can follow these steps when creating or updating a quick response.

**To add an attribute to a quick response**

1. Log in to the Connect Customer admin website at https://*instance name*.my.connect.aws/. Use an **Admin** account, or an account assigned to a security profile that has **Content Management - Quick responses - Create or Edit** permission.

1. On the left navigation bar, choose **Content Management**, then **Quick responses**.  
![Menu showing Content Management and Quick responses.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-application-1.png)

1. Choose **Add response** to create a response.

   —or—

   Select the checkbox next to the quick response that you want to personalize, then choose **Edit**.

1. Choose the content section, enter the quick response content, then use handlebar syntax to enter a user-defined attribute. Make sure you include the `Attributes` namespace prefix. For example, **{{Attributes.Customer}}**.

   The following image shows a quick response for an email.   
![A quick response with an attribute for the customer name.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-quick-response-attributes.png)

1. Choose **Save**.

The following steps explain how to test attributes in CCP.

**To test attributes**

1. Log in to the Connect Customer admin website chat testing page at https://*instance name*.my.connect.aws/test-chat.

1. Choose the flow with the user-defined attribute.

1. Start a chat and enter **/\#*searchText***, where *searchText* is the assigned shortcut key.

**Note**  
For more information, see [Test voice, chat, and task experiences in Connect Customer](chat-testing.md).