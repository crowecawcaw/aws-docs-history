

# Set up integration for Connect Customer Cases
<a name="set-up-integration-for-amazon-connect-cases"></a>

To update your Connect Customer Cases data in Connect Customer Customer Profiles and use features like calculated attributes, you can integrate using Amazon AppIntegrations. Start by setting up a Cases event stream to send system fields to an EventBridge bus, then use Amazon AppIntegrations to forward these events to Customer Profiles.

## Stream data from Connect Customer Cases to Event Bridge
<a name="stream-data-from-connect-cases-to-event-bridge"></a>

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1.  On the instances page, choose the instance alias. The instance alias is also your **instance name**, which appears in your Connect Customer URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box around the instance alias. 

![The instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/stream-data-from-connect-cases-to-event-bridge-1.png)


1.  In the navigation pane, choose **Cases** and note your Cases domain ID from the **Domain details** section. 

![The Cases page, the Domain details section showing the domain ID.](http://docs.aws.amazon.com/connect/latest/adminguide/images/stream-data-from-connect-cases-to-event-bridge-2.png)


1.  Using the AWS CLI, create a Case event configuration to send Connect Customer Cases Events to the default EventBridge bus for your AWS account. 

```
// set up Case Event Configuration including all system fields
aws connectcases put-case-event-configuration --domain-id <YOUR_CASES_DOMAIN_ID> --region <YOUR_AWS_REGION> --event-bridge "{                     
    \"enabled\": true,
    \"includedData\": {
       \"caseData\": {
          \"fields\": [
          {
          \"id\": \"status\"
          },
          {
          \"id\": \"title\"
          },
          {
          \"id\": \"summary\"
          },
          {
          \"id\": \"reference_number\"
          },
          {
          \"id\": \"created_datetime\"
          },
          {
          \"id\": \"last_updated_datetime\"
          },
          {
          \"id\": \"last_closed_datetime\"
          },      
          {
          \"id\": \"customer_id\"
          }
        ]
      }
    }
  }"
```

1.  Open the Event Bridge console for your AWS Region. For example, [https://us-west-2.console.aws.amazon.com/events/home?region=us-west-2\#/eventbuses](https://us-west-2.console.aws.amazon.com/events/home?region=us-west-2#/eventbuses) 

1.  Choose **Create event bus**.

![The Event buses page in the Amazon EventBridge console, the Create event bus button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/stream-data-from-connect-cases-to-event-bridge-3.png)


1.  Create an event bus with name `connect-cases-to-customer-profiles`.

![The Create event bus page, the Name box.](http://docs.aws.amazon.com/connect/latest/adminguide/images/stream-data-from-connect-cases-to-event-bridge-4.png)


1.  Go back to your **default event bus** and create a rule with name `connect-cases-to-customer-profiles-rule`. 

![The default event bus, the Create rule button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/stream-data-from-connect-cases-to-event-bridge-5.png)


![The Build event pattern step.](http://docs.aws.amazon.com/connect/latest/adminguide/images/stream-data-from-connect-cases-to-event-bridge-6.png)

+  Event Pattern snippet: 

```
{
  "source": ["aws.cases"],
  "detail": {
    "eventType": ["CASE.UPDATED", "CASE.CREATED", "CASE.DELETED"]
  }
}
```

![The Creation method section, the Custom pattern (JSON editor) option, the Event pattern code.](http://docs.aws.amazon.com/connect/latest/adminguide/images/stream-data-from-connect-cases-to-event-bridge-7.png)

+  Choose **Skip to Review and Create** and then **Create rule**. 

![The Skip to Review and create button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/stream-data-from-connect-cases-to-event-bridge-8.png)


## Ingest Event Bridge case data to Customer Profiles by using AppIntegrations
<a name="ingest-event-bridge-case-data-to-customer-profiles-via-appintegrations"></a>

1.  Using the AWS CLI, create an Event Integration with AppIntegrations and record the ARN output.  This represents a source data that a Connect Customer instance can use. 

```
aws appintegrations create-event-integration --region
    {{<YOUR_REGION>}} --name Connect-Cases-Event-Integration
    --event-bridge-bus connect-cases-to-customer-profiles --event-filter
    "{\"Source\": \"aws.cases\" }"
    --description "Event Integration for Cases Event Bus"
```

1.  Using the AWS CLI, create an integration with Customer Profiles using the put-integration API. This will start the flow of data to Customer Profiles, replacing the placeholder values with your Event Integration ARN and Customer Profile domain name. 

```
aws customer-profiles put-integration --region
    {{<YOUR_REGION>}} --domain-name {{<YOUR_CP_DOMAIN_NAME>}} 
    --uri {{<YOUR_EVENT_INTEGRATION_ARN>}} --object-type-name Connect-case
```

## Verify your Cases integration
<a name="verify-your-cases-integration"></a>

1.  Create a case in Connect Customer Cases.

1.  The event delivery should be almost instantaneous but allow a minute for it to be delivered and associate with the customer profile.

1.  Using the AWS CLI, find the Connect-case object under the profile, replacing the placeholders with the correct values. 

```
aws customer-profiles list-profile-objects --domain-name
    {{<YOUR_CP_DOMAIN_NAME>}} --region {{<YOUR_REGION>}} 
    --object-type-name Connect-case --profile-id {{<YOUR_PROFILE_ID>}}
```

1.  If you don't find an item in the response of the above API call, then there is a problem with your integration. To troubleshoot: 

   1.  Go to the Amazon EventBridge console. 

   1.  Check whether the EventSource is Active and the matching EventBus exists and is running. 

   1.  Check whether your Case Event Configuration is correctly configured. 

   1.  If these are working, contact Support for assistance investigating the issue. 