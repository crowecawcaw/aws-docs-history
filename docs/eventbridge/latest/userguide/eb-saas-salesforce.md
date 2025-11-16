# Receiving events from Salesforce in Amazon EventBridge

You can use Amazon EventBridge to receive [events](eb-events.md "eb-events.md") from Salesforce in following ways:

- By using Salesforce's Event Bus Relay feature to receive events directly on an EventBridge partner event bus.
- By configuring a flow in [Amazon AppFlow](https://aws.amazon.com/appflow/ "https://aws.amazon.com/appflow/") that
  uses Salesforce as a data source. Amazon AppFlow then sends Salesforce events to EventBridge by using a
  [partner event bus](eb-saas.md "eb-saas.md").
  You can send event information to Salesforce using API destinations. Once the event is sent to Salesforce,
  it can be processed by [Flows](https://help.salesforce.com/s/articleView?id=flow.htm "https://help.salesforce.com/s/articleView?id=flow.htm") or
  [Apex triggers](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers.htm "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers.htm"). For more
  information about setting up a Salesforce API destination, see [Tutorial: Send events to Salesforce from Amazon EventBridge](eb-tutorial-salesforce.md "eb-tutorial-salesforce.md").

###### Topics

- [Receiving events from Salesforce using Event Bus Relay](#eb-saas-salesforce-relay "#eb-saas-salesforce-relay")
- [Receiving events from Salesforce using Amazon AppFlow](#eb-saas-salesforce-appflow "#eb-saas-salesforce-appflow")

## Receiving events from Salesforce using Event Bus Relay

### Step 1: Set up Salesforce Event Bus Relay and an EventBridge partner event source

When you create an event relay configuration on Salesforce, Salesforce creates a partner event
source in EventBridge in the pending state.

###### To configure Salesforce Event Bus Relay

1. [Set Up a REST API Tool](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.z63eim1tqkm3 "https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.z63eim1tqkm3")
2. [(Optional) Define a Platform Event](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.2m5t2i52o23m "https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.2m5t2i52o23m")
3. [Create a Channel for a Custom Platform Event](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.s0spl5puf9d0 "https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.s0spl5puf9d0")
4. [Create a Channel Member to Associate the Custom Platform Event](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.rdhi4awp8cvv "https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.rdhi4awp8cvv")
5. [Create a Named Credential](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.etec44jyv3og "https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.etec44jyv3og")
6. [Create an Event Relay Configuration](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.43rfyeehz0w5 "https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.43rfyeehz0w5")

### Step 2: Activate Salesforce partner event source in the EventBridge console

and start the event relay

1. Open the [Partner event sources](https://console.aws.amazon.com/events/home?#/partners "https://console.aws.amazon.com/events/home?#/partners") page in the EventBridge console.
2. Select the Salesforce partner event source that you created in Step 1.
3. Choose **Associate with event bus**.
4. Validate the name of the partner event bus.
5. Choose **Associate**.
6. [Start the Event Relay](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.t01b3xp87vhu "https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/Salesforce_Event_Bus_Relay_Pilot.pdf#h.t01b3xp87vhu")

Now that you've set up and started the Event Bus Relay and configured the partner event source you can create an
[EventBridge rule that reacts to events](eb-create-rule-visual.md "eb-create-rule-visual.md") to filter and send the data to a [target](eb-targets.md "eb-targets.md").

## Receiving events from Salesforce using Amazon AppFlow

Amazon AppFlow encapsulates events from Salesforce in an EventBridge event envelope. The following
example shows a Salesforce event received by an EventBridge partner event bus.

```
{
    "version": "0",
    "id": "5c42b99e-e005-43b3-c744-07990c50d2cc",
    "detail-type": "AccountChangeEvent",
    "source": "aws.partner/appflow.test/salesforce.com/364228160620/CustomSF-Source-Final",
    "account": "000000000",
    "time": "2020-08-20T18:25:51Z",
    "region": "us-west-2",
    "resources": [],
    "detail": {
        "ChangeEventHeader": {
            "commitNumber": 248197218874,
            "commitUser": "0056g000003XW7AAAW",
            "sequenceNumber": 1,
            "entityName": "Account",
            "changeType": "UPDATE",
            "changedFields": [
                "LastModifiedDate",
                "Region__c"
            ],
            "changeOrigin": "com/salesforce/api/soap/49.0;client=SfdcInternalAPI/",
            "transactionKey": "000035af-b239-0581-9f14-461e4187de11",
            "commitTimestamp": 1597947935000,
            "recordIds": [
                "0016g00000MLhLeAAL"
            ]
        },
        "LastModifiedDate": "2020-08-20T18:25:35.000Z",
        "Region__c": "America"
    }
}
```

### Step 1: Configure Amazon AppFlow to use Salesforce as a partner

event source

To send events to EventBridge, you first need to configure Amazon AppFlow to use Salesforce as a partner event
source.

1. In the [Amazon AppFlow
   console](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/"), choose **Create flow**.
2. In the **Flow details** section, in **Flow
   name** enter a name for your flow.
3. (Optional) Enter a description for the flow and then choose
   **Next**.
4. Under **Source details**, choose
   _Salesforce_ from the **Source name**
   drop-down, and then choose **Connect** to create a new
   connection.
5. In the **Connect to Salesforce** dialog box, choose either
   **Production** or **Sandbox** for the
   Salesforce environment.
6. In the **Connection name** field, enter a unique name for the
   connection, and then choose **Continue**.
7. In the Salesforce dialog box, do the following:
   1. Enter your Salesforce sign-in credentials to log in to
      Salesforce.
   2. Select Salesforce events for the types of data for Amazon AppFlow to
      process.

8. In the **Choose Salesforce event** drop-down, select the type
   of event to send to EventBridge.
9. For a destination, select **Amazon EventBridge**.
10. Select **Create new partner event source**.
11. (Optional) Specify a unique suffix for the partner event source.
12. Choose **Generate partner event source**.
13. Choose an Amazon S3 bucket to store event payload files that are larger than
    256 KB.
14. In the **Flow trigger** section, ensure that **Run
    flow on event** is selected. This setting ensures that the flow is
    executed when a new Salesforce event occurs.
15. Choose **Next**.
16. For field mapping, select **Map all fields directly**.
    Alternatively, you can select the fields that are of interest from the
    **Source field name** list.

For more information about field mapping, see [Map data
fields](../../../appflow/latest/userguide/getting-started.md#map-fields "../../../appflow/latest/userguide/getting-started.md#map-fields"). 17. Choose **Next**. 18. (Optional) Configure filters for data fields in Amazon AppFlow. 19. Choose **Next**. 20. Review the settings and then choose **Create flow**.

With the flow configured, Amazon AppFlow creates a new partner event source that you then need to associate
with a partner event bus in your account.

### Step 2: Configure EventBridge to receive Salesforce

events

Ensure that the Amazon AppFlow flow that is triggered from Salesforce events with EventBridge as a
destination is configured before following instructions in this section.

###### To configure EventBridge to receive Salesforce events

1. Open the [Partner event sources](https://console.aws.amazon.com/events/home?#/partners "https://console.aws.amazon.com/events/home?#/partners") page in the EventBridge console.
2. Select the Salesforce partner event source that you created in Step 1.
3. Choose **Associate with event bus**.
4. Validate the name of the partner event bus.
5. Choose **Associate**.
6. In the Amazon AppFlow console, open the flow you created and choose **Activate
   flow**.
7. Open the [Rules](https://console.aws.amazon.com/events/home?#/rules "https://console.aws.amazon.com/events/home?#/rules") page in the EventBridge console.
8. Choose **Create rule**.
9. Enter a unique name for the rule.
10. Choose **Event pattern** in the **Define
    pattern** section.
11. For **Event matching pattern**, select **Pre-defined
    pattern by service**.
12. For **Service provider** section, select **All
    Events**.
13. For **Select event bus**, choose **Custom or partner
    event bus**.
14. Select the event bus that you associated with the Amazon AppFlow partner event
    source.
15. For **Select targets**, choose the AWS service that is to
    act when the rule runs. One rule can have up to five targets.
16. Choose **Create**.

The target service receives all Salesforce events configured for your account. To
filter the events or send some events to different targets, you can use
[content-based filtering
with event patterns](eb-create-pattern.md#eb-event-patterns-content-based-filtering "eb-create-pattern.md#eb-event-patterns-content-based-filtering").

###### Note

For events larger than 256KB, Amazon AppFlow doesn't send the full event to EventBridge. Instead,
Amazon AppFlow puts the event into an S3 bucket in your account, and then sends an event to
EventBridge with a pointer to the Amazon S3 bucket. You can use the pointer to get the full
event from the bucket.
