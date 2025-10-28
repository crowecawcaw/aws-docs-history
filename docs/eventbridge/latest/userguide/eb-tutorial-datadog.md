# Tutorial: Send events to Datadog from Amazon EventBridge

You can use EventBridge to route [events](eb-events.md "eb-events.md") to third-party
services,such as [Datadog](https://www.datadoghq.com/ "https://www.datadoghq.com/").

In this tutorial, you'll use the EventBridge console to create a connection to Datadog, an [API destination](eb-api-destinations.md "eb-api-destinations.md")
that points to Datadog, and a [rule](eb-rules.md "eb-rules.md") to
route events to Datadog.

###### Steps:

- [Prerequisites](#eb-dd-prereqs "#eb-dd-prereqs")
- [Step 1: Create connection](#eb-dd-create-connection "#eb-dd-create-connection")
- [Step 2: Create API destination](#eb-dd-api-destination "#eb-dd-api-destination")
- [Step 3: Create rule](#eb-dd-create-rule "#eb-dd-create-rule")
- [Step 4: Test the rule](#eb-dd-test-rule "#eb-dd-test-rule")
- [Step 5: Clean up your resources](#cleanup "#cleanup")

## Prerequisites

To complete this tutorial, you'll need the following resources:

- A [Datadog account](https://www.datadoghq.com/free-datadog-trial/ "https://www.datadoghq.com/free-datadog-trial/").
- A [Datadog API key](https://docs.datadoghq.com/account_management/api-app-keys/ "https://docs.datadoghq.com/account_management/api-app-keys/").
- An EventBridge-enabled [Amazon Simple Storage Service (Amazon S3)](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") bucket.

## Step 1: Create connection

To send events to Datadog, you'll first have to establish a connection to the Datadog
API.

###### To create the connection

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **API destinations**.
3. Choose the **Connections** tab, and then choose **Create
   connection**.
4. Enter a name and description for the connection. For example, enter
   `Datadog` as a name, and `Datadog API
Connection` as a description.
5. For **Authorization type**, choose **API key**.
6. For **API key name**, enter `DD-API-KEY`.
7. For **Value**, paste your Datadog secret API key.
8. Choose **Create**.

## Step 2: Create API destination

Now that you've created the connection, next you'll create the API destination to use as
the [target](eb-targets.md "eb-targets.md") of the rule.

###### To create the API Destination

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **API destinations**.
3. Choose **Create API destination**.
4. Enter a name and description for the API destination. For example, enter
   `DatadogAD` for the name, and `Datadog API
Destination` for the description..
5. For **API destination endpoint**, enter the Datadog Logs endpoint:
   `https://http-intake.logs.datadoghq.com/api/v2/logs`.

###### Note

This tutorial delivers events to Datadog Logs. You can also deliver events to Datadog using the events endpoint: `https://api.datadoghq.com/api/v1/events`. 6. For **HTTP method**, choose **POST**. 7. For **Invocation rate limit**, enter
`300`. 8. For **Connection**, choose **Use an existing
connection** and choose the `Datadog` connection you created in step

1.
2. Choose **Create**.

## Step 3: Create rule

Next, you'll create a rule to send events to Datadog when an Amazon S3 object is
created.

###### To create a rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. For example, enter
   `DatadogRule` for the name, and `Rule to send events to
Datadog for S3 object creation` for the description.
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
    destination**, and then choose the `DatadogAD` destination you created in step
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
object](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") by uploading a file to an EventBridge-enabled bucket. The created object will be
logged in the Datadog Logs console.

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
