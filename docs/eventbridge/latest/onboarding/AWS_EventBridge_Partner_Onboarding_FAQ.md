

# FAQ
<a name="AWS_EventBridge_Partner_Onboarding_FAQ"></a>

1.  **What delivery guarantees will EventBridge make?** 

   EventBridge tries to deliver an event to a target for up to 24 hours, except in scenarios where your target resource is constrained. The first attempt is made as soon as the event arrives in the event stream. However, if the target service is having problems, EventBridge automatically reschedules another delivery in the future. If 24 hours has passed since the arrival of event, no more attempts are scheduled and the `FailedInvocations` metric is published in Amazon CloudWatch. We recommend that you create a CloudWatch alarm on the `FailedInvocations` metric.

   For more information, see [My event’s delivery to the target experienced a delay](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-troubleshooting.html#eb-delayed-event-delivery) in the *Amazon EventBridge User Guide*.

1.  **What happens when the APN partner deletes an event source?** 

   If the APN partner deletes an event source, any rules attached to the corresponding event bus remain in a Deleted state in the customer’s AWS account. If the event source is later recreated and reassociated, these rules become active again.

1.  **What happens when the AWS customer deletes an event bus?** 

   If the AWS customer deletes an event bus associated with a partner event source, the event source will return to a Pending state. For more information, see [Event source states](https://docs.aws.amazon.com/eventbridge/latest/onboarding/amazon_eventbridge_partner_onboarding_guide.html#EventBridge-Partner-Onboarding-States). The event source will accept events sent by a SaaS partner system when calling PutPartnerEvents, but does not deliver them to customer. The event source will expire after being in a Pending state for an extended period of time and will automatically be deleted. For more infprmation, see: [Event source expiration](https://docs.aws.amazon.com/eventbridge/latest/onboarding/amazon_eventbridge_partner_onboarding_guide.html#event_source_expiration).

1.  **How can customers create event buses in different Regions?** 

   EventBridge is a regional service and event buses must exist in the same Region as the partner event sources they are attached to. You should allow your customers to select which Region they want to create the event source in when they register their AWS account with you. You can call [`CreatePartnerEventSource`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreatePartnerEventSource.html) in any Region regardless of where the call originates from. You can use SDK to specify the Region when you create a client.

1.  **What happens to events sent to a partner event source before the customer attaches an event bus?** 

   Events sent to an event source in the PENDING state will be dropped.

1.  **What is the retry policy if messages cannot be delivered?** 

   The separation between the partner event source and customer event bus is a logical one. Messages successfully sent to an event source in the ACTIVE state with a customer event bus attached will always propagate to the event bus.

   Message delivery to downstream customer-owned targets follows the same retry policies as the policies documented in [Troubleshooting Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-troubleshooting.html).