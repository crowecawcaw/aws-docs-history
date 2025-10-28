# Onboarding tasks

## 1. Partner registration

As a one-time registration step, the partner must provide AWS with the following information:

- DNS fully qualified domain that the partner owns. AWS will append .test at the end of the domain for testing purposes.
- Development/testing:
  - A list of Regions to support
  - A list of accounts to publish events
  - A list of accounts to consume events

- Production:
  - A list of Regions to support
  - A list of accounts to publish events

Additionally, AWS requires the information listed in the topic [Partner Terms](partner_terms.md "partner_terms.md").

## 2. Creating partner event sources

The partner updates their user experience to enable the SaaS administrator to create a partner event source.

- User specifies an event generator, an AWS account ID, and a Region in which they want the event source to be created.
- Perform any required authentication checks to ensure that the SaaS administrator has appropriate permissions on the event generator, as determined by the partner.
- Call the [`CreatePartnerEventSource`](../APIReference/API_CreatePartnerEventSource.md "../APIReference/API_CreatePartnerEventSource.md") API using the Region supplied by the customer. Specify the event generator and the AWS account ID, using the partner’s AWS credentials.
  - To avoid incorrect delivery of events, the event generator name must be unique within the SaaS system. For example, if two SaaS customers set up an event bus for an event generator named "my-channel", then the event generator name should include additional disambiguating information, such as an account ID: “1234.my-channel”.

### Best practices

**Immediate creation:** You should make the call to `CreatePartnerEventSource` immediately after the customer submits their account ID and Region selection. You should not wait for events to occur in your system before creating the event source.

**Regional selection:** You must allow customers to select the AWS Region where they want to receive events and create the event source in that Region. Customers can only associate event buses with event sources in the same Region.

## 3. Sending events

The partner updates their backend system to push events to AWS.

- When an event is generated, check the persistent data store to determine whether a partner event source exists for the resource that generated this event. If not, do nothing.
- Call the [`PutPartnerEvents`](../APIReference/API_PutPartnerEvents.md "../APIReference/API_PutPartnerEvents.md") API, specifying the event source name, using the partner’s AWS credentials.
- Inspect the results to see if there are any failures.
  - For retry-able failures, call the API again (for example, "Internal Service Error").
  - For non-retry-able failures, delete the record from the data store (for example, "Event Bus Not Found").

### Best practices

**Event source status:** As soon as the partner event source is successfully created you should begin sending events to it. You do not need to wait for the event source to become active (i.e. the customer associated an event bus) before sending events. The customer is not charged for events until they associate an event bus.

**Batching events:** When calling the `PutPartnerEvents` API call you can batch up to 20 events in a single API call as long as the aggregate size of all events is less than 256 kb.

**Event detail types:** Each event you publish will include a detail type field. This field should be used to identify different types of events produced by your service. All events for a given detail type should share a common schema for the primary event payload (the event detail field). Most SaaS providers will have between 1-15 different detail types. If you have significantly more types of events, consider consolidating some of your types that share the same payload schema into a single detail type and provide a subtype identifier within the event detail itself. Customers will be able to write rules that match against both the detail type in the envelope as well as the information included in event detail. Do not include personally identifiable information (PII) in the detail type field.

**Event resources:** The resources field on events is optional. If you choose to use it you should provide a list of unique identifiers for the resources the event is about. For instance, when an Amazon EC2 instance is terminated, the instance’s Amazon Resource Name (ARN) is listed in the resources field.

## 4. Managing partner event buses

The partner updates their user experience to enable the AWS customer to list and delete partner event buses associated with a given event generator.

- Perform any required authentication checks to ensure that the SaaS administrator has appropriate permissions on the event generator, as determined by the partner.
- Call the [`ListPartnerEventSources`](../APIReference/API_ListPartnerEventSources.md "../APIReference/API_ListPartnerEventSources.md") and [`DeletePartnerEventSource`](../APIReference/API_DeletePartnerEventSource.md "../APIReference/API_DeletePartnerEventSource.md") APIs, as appropriate, using the partner’s AWS credentials.
