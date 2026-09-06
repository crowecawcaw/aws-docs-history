

# Create a Kinesis Integration with Connect Customer Customer Profiles
<a name="customer-profiles-kinesis-integration"></a>

 The following steps outline the process of streaming objects from an Amazon Kinesis Data Stream into Connect Customer Customer Profiles. The integration consists of two main steps: 

1.  Configure an EventBridge Pipe to stream data from your Kinesis Data Stream to an EventBridge bus. 

1.  Set up a Customer Profiles data integration with your Kinesis Data Stream using your created EventBridge Pipe 

## Step 1: Stream Data from Kinesis to EventBridge
<a name="step-1-stream-data-from-kinesis-to-eventbridge"></a>

1.  Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/) 

1.  In the navigation pane, choose **Event buses**. 

1.  Choose **Create event bus**. 

1.  In the **Event bus details** section, provide a descriptive name. For example, `kinesis-to-customer-profiles`. 

1.  Choose **Create**. 

1.  Go to your Kinesis Data Stream details page. 

1.  Select the **EventBridge Pipes** tab and choose **Connect Kinesis Data Stream to Pipe**. 

1.  Create a name for your EventBridge pipe. 

1.  Follow the setup wizard until you reach the **Target setup** page. 

1.  For the target, select the Event Bus created in step 1. For example, `kinesis-to-customer-profiles`. 

1.  After the **Target** section, expand the **Target Input Transformer** accordion. 

1.  Set the target input transformer as follows: 

```
{
    "data": <$.data>
}
```

1.  Choose **Create pipe** to complete the setup. 

 At this point, you have successfully configured the routing of Kinesis events to EventBridge. Next, we will create an integration with Customer Profiles. 

## Step 2: Ingest EventBridge Data into Customer Profiles
<a name="step-2-ingest-eventbridge-data-into-customer-profiles"></a>

1.  Go to **Customer Profiles** in the Amazon Connect console. 

1.  Select the **Data source Integrations** tab and choose **Add a data source integration**. 

1.  Select **Kinesis** from the **Data source** dropdown 

1.  In the **EventBridge pipe name** dropdown, select the pipe that was created in Step 1 and choose **Next**. 

1.  On the **Map data** page, select the appropriate object type mapping and choose **Next**. 

1.  Review your configuration on the **Review and integrate** page and choose **Add data source integration** to complete the setup. 

 Your Kinesis Data Stream is now integrated with Connect Customer Customer Profiles, and you are now ready to send events from Kinesis to Customer Profiles. 