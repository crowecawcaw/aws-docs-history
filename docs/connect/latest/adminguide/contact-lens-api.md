

# Use conversational analytics APIs for chat analytics
<a name="contact-lens-api"></a>

Conversational analytics includes two APIs that support conversational analytics. Use these APIs to build solutions that make your contact center more efficient. 
+ [ListRealtimeContactAnalysisSegments](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_ListRealtimeContactAnalysisSegments.html): Use for voice contacts.
+ [ListRealtimeContactAnalysisSegmentsV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListRealtimeContactAnalysisSegmentsV2.html): Use for chat contacts.

These conversational analytics APIs are polling APIs, with a standard request/response exchange, where you don't need to integrate with any other service. However, there are [rate limitations](amazon-connect-service-limits.md#connect-contactlens-api-quotas). If needed, you can eliminate these limitations by using the [streaming API](contact-analysis-segment-streams.md). It requires integration with Amazon Kinesis Data Streams. 

Following are two use cases for the call and chat analytics API.

## Better contact transfers
<a name="contact-lens-api-transfers"></a>

When a contact is transferred from one agent to another agent, you can transfer a transcript of the conversation to the new agent. The new agent then has context for why the customer is contacting your contact center. The customer doesn't need to repeat information they already provided. Use the [ListRealtimeContactAnalysisSegments](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_ListRealtimeContactAnalysisSegments.html) API for voice contacts and the [ListRealtimeContactAnalysisSegmentsV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListRealtimeContactAnalysisSegmentsV2.html) API for chats to get the entire transcript of the conversation up to a certain point, and share it with the new agent. 

## Highlight key parts of the conversation as labels, issues, action items, and outcomes
<a name="contact-lens-api-call-summary"></a>

With key highlights agents can quickly makes notes after the contact ends, and supervisors can quickly identify contacts for quality and agent performance management. This makes agents and supervisors more productive at their jobs.