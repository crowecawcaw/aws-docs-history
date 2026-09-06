

# Receiving events from a SaaS partner with Amazon EventBridge
<a name="eb-saas"></a>

To receive events from SaaS partner applications and services, you need a *partner event source* from the partner. A partner event source is a resource created by a partner that you can then accept as an event source. To accept the partner event source, you create a custom event bus and match it to the partner event source.

![An SaaS partner sends an event to a partner event source, which sends it to the partner event bus.](http://docs.aws.amazon.com/eventbridge/latest/userguide/images/bus-saas_eventbridge_conceptual.svg)


 The following video covers SaaS integrations with EventBridge:




**Topics**
+ [Supported SaaS partner integrations](#eb-supported-integrations)
+ [Configuring Amazon EventBridge to receive events from a SaaS integration](#eb-saas-integration)
+ [Receiving SaaS events from AWS Lambda function URLs in Amazon EventBridge](eb-saas-furls.md)
+ [Receiving events from Salesforce in Amazon EventBridge](eb-saas-salesforce.md)

## Supported SaaS partner integrations
<a name="eb-supported-integrations"></a>

EventBridge supports the following SaaS partner integrations:
+ [Adobe](https://console.aws.amazon.com/events/#/partners/adobe.com?page=overview)
+ [Salesforce (via Amazon AppFlow)](https://console.aws.amazon.com/events/#/partners/appflow-salesforce.com?page=overview)
+ [Apptrail](https://console.aws.amazon.com/events/#/partners/apptrail.com?page=overview)
+ [Atlan](https://console.aws.amazon.com/events/#/partners/atlan.com?page=overview)
+ [Auth0](https://console.aws.amazon.com/events/#/partners/auth0.com?page=overview)
+ [Authress](https://console.aws.amazon.com/events/#/partners/authress.io?page=overview)
+ [Benchling](https://console.aws.amazon.com/events/#/partners/benchling.com?page=overview)
+ [BigCommerce](https://console.aws.amazon.com/events/#/partners/bigcommerce.com?page=overview)
+ [Blitline](https://console.aws.amazon.com/events/#/partners/blitline.com?page=overview)
+ [Buildkite](https://console.aws.amazon.com/events/#/partners/buildkite.com?page=overview)
+ [Chargebee](https://console.aws.amazon.com/events/#/partners/chargebee.com?page=overview)
+ [Checkout.com](https://console.aws.amazon.com/events/#/partners/checkout.com?page=overview)
+ [CleverTap](https://console.aws.amazon.com/events/#/partners/clevertap.com?page=overview)
+ [CloudAMQP](https://console.aws.amazon.com/events/#/partners/cloudamqp.com?page=overview)
+ [commercetools](https://console.aws.amazon.com/events/#/partners/commercetools.com?page=overview)
+ [Datadog](https://console.aws.amazon.com/events/#/partners/datadoghq.com?page=overview)
+ [EnergySys](https://console.aws.amazon.com/events/#/partners/energysys.com?page=overview)
+ [Epsagon](https://console.aws.amazon.com/events/#/partners/epsagon.com?page=overview)
+ [Freshworks](https://console.aws.amazon.com/events/#/partners/freshworks.com?page=overview)
+ [Genesys](https://console.aws.amazon.com/events/#/partners/genesys.com?page=overview)
+ [Gladly](https://console.aws.amazon.com/events/#/partners/gladly.com?page=overview)
+ [GS2](https://console.aws.amazon.com/events/#/partners/gs2.io?page=overview)
+ [Guidewire](https://console.aws.amazon.com/events/#/partners/guidewire.com?page=overview)
+ [Hitachi Solutions](https://console.aws.amazon.com/events/#/partners/hitachi-solutions.co.jp?page=overview)
+ [iLert](https://console.aws.amazon.com/events/#/partners/ilert.com?page=overview)
+ [Atlassian - Jira Service Management](https://console.aws.amazon.com/events/#/partners/jiraservicemanagement.com?page=overview)
+ [Karte](https://console.aws.amazon.com/events/#/partners/karte.io?page=overview)
+ [Kloudless](https://console.aws.amazon.com/events/#/partners/kloudless.com?page=overview)
+ [Mackerel](https://console.aws.amazon.com/events/#/partners/mackerel.io?page=overview)
+ [MongoDB](https://console.aws.amazon.com/events/#/partners/mongodb.com?page=overview)
+ [New Relic](https://console.aws.amazon.com/events/#/partners/newrelic.com?page=overview)
+ [nOps](https://console.aws.amazon.com/events/#/partners/nops.io?page=overview)
+ [Okta](https://console.aws.amazon.com/events/#/partners/okta.com?page=overview)
+ [OneLogin](https://console.aws.amazon.com/events/#/partners/onelogin.com?page=overview)
+ [Operata](https://console.aws.amazon.com/events/#/partners/operata.com?page=overview)
+ [Opsgenie](https://console.aws.amazon.com/events/#/partners/opsgenie.com?page=overview)
+ [PagerDuty](https://console.aws.amazon.com/events/#/partners/pagerduty.com?page=overview)
+ [Payshield](https://console.aws.amazon.com/events/#/partners/payshield.com.au?page=overview)
+ [Rhythm Software](https://console.aws.amazon.com/events/#/partners/rhythmsoftware.com?page=overview)
+ [Rightsline](https://console.aws.amazon.com/events/#/partners/rightsline.com?page=overview)
+ [Rootly](https://console.aws.amazon.com/events/#/partners/rootly.com?page=overview)
+ [SaaSus Platform](https://console.aws.amazon.com/events/#/partners/saasus.io?page=overview)
+ [SailPoint](https://console.aws.amazon.com/events/#/partners/sailpoint.com?page=overview)
+ [Scalr](https://console.aws.amazon.com/events/#/partners/scalr.com?page=overview)
+ [Segment](https://console.aws.amazon.com/events/#/partners/segment.com?page=overview)
+ [Shopify](https://console.aws.amazon.com/events/#/partners/shopify.com?page=overview)
+ [SignalFx](https://console.aws.amazon.com/events/#/partners/signalfx.com?page=overview)
+ [Site24x7](https://console.aws.amazon.com/events/#/partners/site24x7.com?page=overview)
+ [SnowcatCloud](https://console.aws.amazon.com/events/#/partners/snowcatcloud.com?page=overview)
+ [Snyk](https://console.aws.amazon.com/events/#/partners/snyk.io?page=overview)
+ [Stax](https://console.aws.amazon.com/events/#/partners/stax.io?page=overview)
+ [Stripe](https://console.aws.amazon.com/events/#/partners/stripe.com?page=overview)
+ [SugarCRM](https://console.aws.amazon.com/events/#/partners/sugarcrm.com?page=overview)
+ [Symantec](https://console.aws.amazon.com/events/#/partners/symantec.com?page=overview)
+ [Tealium](https://console.aws.amazon.com/events/#/partners/tealium.com?page=overview)
+ [Thundra](https://console.aws.amazon.com/events/#/partners/thundra.io?page=overview)
+ [TriggerMesh](https://console.aws.amazon.com/events/#/partners/triggermesh.com?page=overview)
+ [Whispir](https://console.aws.amazon.com/events/#/partners/whispir.com?page=overview)
+ [Zendesk](https://console.aws.amazon.com/events/#/partners/zendesk.com?page=overview)
+ [Amazon Seller Partner API](https://console.aws.amazon.com/events/#/partners/sellingpartnerapi.amazon.com?page=overview) 

## Configuring Amazon EventBridge to receive events from a SaaS integration
<a name="eb-saas-integration"></a>

Configuring EventBridge to receive partner events consists of two main steps:
+ Creating the partner event source
+ Associating that partner source with a partner event bus
**Note**  
Any events published by a partner to a partner event source that has not been associated with an event bus will be immediately dropped. Those events will not be persisted at rest in EventBridge.

**Create a partner event source (console only)**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, choose **Partner event sources**.

1. Find the partner that you want and then choose **Set up** for that partner.

1. To copy your account ID to the clipboard, choose **Copy**.

1. In the navigation pane, choose **Partner event sources**.

1. Go to the partner's website and follow the instructions to create a partner event source using your account ID. The event source that you create is available to only your account.

**Associate the partner source with a partner event bus (console)**

1. In the EventBridge console, choose **Partner event sources** in the navigation pane.

1. Select the button next to the partner event source and then choose **Associate with event bus**. 

   The status of the event source changes from `Pending` to `Active`, and the name of the event bus updates to match the partner event source name. You can now start creating rules that match events from the partner event source.

**Associate the partner source with a partner event bus (AWS CLI)**
+ Use [`create-event-bus`](https://docs.aws.amazon.com/cli/latest/reference/events/create-event-bus.html) to create a partner event bus associated with the partner event source. 

  Both `name` and `event-source-name` should be set to the partner event source name.

  For example:

  ```
  aws events create-event-bus \
      --name "{{aws.partner/saas-integration/name}}" \
      --event-source-name "{{aws.partner/saas-integration/name}}" \
      --region {{us-east-1}}
  ```

  After EventBridge creates the event bus, you can call [`describe-event-source`](https://docs.aws.amazon.com/cli/latest/reference/events/describe-event-source.html) to return details about the partner source. The `State` of the partner source should be `ACTIVE`.

  ```
  aws events describe-event-source
  --name "{{aws.partner/saas-integration/name}}"
  ```
**Note**  
Calling [`put-permission`](https://docs.aws.amazon.com/cli/latest/reference/events/put-permission.html) on a partner event bus returns an error. Only the partner account of the event source associated with the partner event bus is permitted to send events to it.

**Associate the partner source with a partner event bus (CloudFormation)**

1. Create a CloudFormation template that provisions an [`AWS::Events::EventBus`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html) resource with the partner event source. 

   Both `Name` and `EventSourceName` should be set to the partner event source name. For example:

   ```
   AWSTemplateFormatVersion: 2010-09-09
   
   Description: 
      Cloudformation template to create Event Bus for receiving partner events
   
   Resources:
     ExamplePartnerEventBus:
       Type: AWS::Events::EventBus
       Properties:
         EventSourceName: '{{aws.partner/saas-integration/name}}'
         Name: '{{aws.partner/saas-integration/name}}'
   ```

1. Use [`cloudformation create-stack`](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html) or the CloudFormation console to create a stack from the template. For example:

   ```
   aws cloudformation create-stack --stack-name {{eventbridge-saas}} --template-body {{file://template.yml}} --region {{us-east-1}}
   ```
**Note**  
Including an [`AWS::Events::EventBusPolicy`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html) resource for the partner event bus in your template will result in an error. Only the partner account of the event source associated with the partner event bus is permitted to send events to it.