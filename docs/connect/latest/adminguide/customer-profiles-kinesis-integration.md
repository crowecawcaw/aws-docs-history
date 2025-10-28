# Create a Kinesis Integration with

Amazon Connect Customer Profiles

The following steps outline the process of streaming objects from an Amazon Kinesis Data
Stream into Amazon Connect Customer Profiles. The integration consists of two main steps:

1. Configure an EventBridge Pipe to stream data from your Kinesis Data Stream to an EventBridge
   bus.
2. Set up a Customer Profiles data integration with your Kinesis Data Stream using
   your created EventBridge Pipe

## Step 1: Stream Data

from Kinesis to EventBridge

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/")
2. In the navigation pane, choose **Event
   buses**.
3. Choose **Create event bus**.
4. In the **Event bus details** section,
   provide a descriptive name. For example,
   `kinesis-to-customer-profiles`.
5. Choose **Create**.
6. Go to your Kinesis Data Stream details page.
7. Select the **EventBridge Pipes** tab and choose
   **Connect Kinesis Data Stream to Pipe**.
8. Create a name for your EventBridge pipe.
9. Follow the setup wizard until you reach the **Target
   setup** page.
10. For the target, select the Event Bus created in step 1. For example,
    `kinesis-to-customer-profiles`.
11. After the **Target** section, expand the
    **Target Input Transformer** accordion.
12. Set the target input transformer as follows:

```
{
    "data": <$.data>
}
```

1. Choose **Create pipe** to complete the
   setup.

At this point, you have successfully configured the routing of Kinesis events to
EventBridge. Next, we will create an integration with Customer Profiles.

## Step 2:

Ingest EventBridge Data into Customer Profiles

1. Go to **Customer Profiles** in the Amazon
   Connect console.
2. Select the **Data source Integrations** tab
   and choose **Add a data source integration**.
3. Select **Kinesis** from the **Data source** dropdown
4. In the **EventBridge pipe name** dropdown, select
   the pipe that was created in Step 1 and choose **Next**.
5. On the **Map data** page, select the
   appropriate object type mapping and choose **Next**.
6. Review your configuration on the **Review and
   integrate** page and choose **Add data
   source integration** to complete the setup.

Your Kinesis Data Stream is now integrated with Amazon Connect Customer Profiles, and you are now ready to
send events from Kinesis to Customer Profiles.
