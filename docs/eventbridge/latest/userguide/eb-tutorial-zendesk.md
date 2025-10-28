# Tutorial: Send events to Zendesk from Amazon EventBridge

You can use EventBridge to route [events](eb-events.md "eb-events.md") to third-party services like [Zendesk](https://www.zendesk.com/ "https://www.zendesk.com/").

In this tutorial, you'll use the EventBridge console to create a connection to Zendesk, an [API destination](eb-api-destinations.md "eb-api-destinations.md")
that points to Zendesk, and a [rule](eb-rules.md "eb-rules.md") to
route events to Zendesk.

###### Steps:

- [Prerequisites](#eb-zd-prereqs "#eb-zd-prereqs")
- [Step 1: Create connection](#eb-zd-create-connection "#eb-zd-create-connection")
- [Step 2: Create API destination](#eb-zd-api-destination "#eb-zd-api-destination")
- [Step 3: Create rule](#eb-zd-create-rule "#eb-zd-create-rule")
- [Step 4: Test the rule](#eb-zd-test-rule "#eb-zd-test-rule")
- [Step 5: Clean up your resources](#cleanup "#cleanup")

## Prerequisites

To complete this tutorial, you'll need the following resources:

- A [Zendesk account](https://www.zendesk.com/register/#step-1 "https://www.zendesk.com/register/#step-1").
- An EventBridge-enabled [Amazon Simple Storage Service (Amazon S3)](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") bucket.

## Step 1: Create connection

To send events to Zendesk, you'll first have to establish a connection to the Zendesk
API.

###### To create the connection

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **API destinations**.
3. Choose the **Connections** tab, and then choose **Create
   connection**.
4. Enter a name and description for the connection. For example, enter
   `Zendesk` for the name, and `Connection to Zendesk
API` for the description.
5. For **Authorization type**, choose **Basic (Username/Password)**.
6. For **Username**, enter your Zendesk username.
7. For **Password**, enter your Zendesk password.
8. Choose **Create**.

## Step 2: Create API destination

Now that you've created the connection, you'll next create the API destination to use as
the [target](eb-targets.md "eb-targets.md") of the rule.

###### To create the API Destination

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **API destinations**.
3. Choose **Create API destination**.
4. Enter a name and description for the API destination. For example, enter
   `ZendeskAD` for the name, and `Zendesk API
destination` for the description.
5. For **API destination endpoint**, enter
   `https://`your-subdomain`.zendesk.com/api/v2/tickets.json`,
   where `your-subdomain` is the subdomain associated with your
   Zendesk account.
6. For **HTTP method**, choose **POST**.
7. For **Invocation rate limit**, enter
   `10`.
8. For **Connection**, choose **Use an existing
   connection** and choose the `Zendesk` connection you created in step
9.
10. Choose **Create**.

## Step 3: Create rule

Next, create a rule to send events to Zendesk when an Amazon S3 object is created.

###### To create a rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. For example, enter
   `ZendeskRule` for the name, and `Rule to send events to
Zendesk when S3 objects are created` for the description.
5. For **Event bus**, choose **default**.
6. For **Rule type**, choose **Rule with an event
   pattern**.
7. Choose **Next**.
8. For **Event source**, choose
   **Other**.
9. For **Event pattern**, enter the following:

```
{
  "source": ["aws.s3"]
}
```

10. Choose **Next**.
11. For **Target types**, choose **EventBridge API destination**.
12. For **API destination**, choose **Use an existing API
    destination**, and then choose the `ZendeskAD` destination you created in step
13.
14. For **Execution role**, choose **Create a new for role for this specific resource**.
15. For **Additional settings**, do the following:
    1.  For **Configure target input**, choose **Input transformer** from the drop-down list.
    2.  Choose **Configure input transformer**
    3.  for **Sample events**, enter the following:

    ```
    `{
     "detail":[]
    }`
    ```

    4.  For **Target input transformer** do the following:
        1. For **Input Path**, enter the following:

        ```
        `{"detail":"$.detail"}`
        ```

        2. For **Input Template**, enter the following:

        ```
        `{"message": <detail>}`
        ```

    5.  Choose **Confirm.**.

16. Choose **Next**.
17. Choose **Next**.
18. Review the details of the rule and choose **Create rule**.

## Step 4: Test the rule

To test your rule, create an [Amazon S3
object](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") by uploading a file to an EventBridge-enabled bucket.
When the event matches the rule, EventBridge will call the [Zendesk
Create Ticket API](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket "https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket"). The new ticket will appear in the Zendesk dashboard.

## Step 5: Clean up your resources

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you are no longer using, you prevent unnecessary charges to your AWS account.

###### To delete the EventBridge Connections(s)

1. Open the [API destination page](https://console.aws.amazon.com/events/home#/apidestinations "https://console.aws.amazon.com/events/home#/apidestinations") of the EventBridge console.
2. Choose the **Connections** tab.
3. Select the Connection(s) you created.
4. Choose **Delete**.
5. Enter the name of the connection and choose **Delete**.

###### To delete the EventBridge API destination(s)

1. Open the [API destination page](https://console.aws.amazon.com/events/home#/apidestinations "https://console.aws.amazon.com/events/home#/apidestinations") of the EventBridge console.
2. Select the API destinations(s) you created.
3. Choose **Delete**.
4. Enter the name of the API destination and choose **Delete**.

###### To delete the EventBridge rule(s)

1. Open the [Rules page](https://console.aws.amazon.com/events/home#/rules "https://console.aws.amazon.com/events/home#/rules") of the EventBridge console.
2. Select the rule(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.
