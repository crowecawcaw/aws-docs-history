# Use Contact Lens APIs for chat

analytics

Contact Lens includes two APIs that support conversational analytics. Use
these APIs to build solutions that make your contact center more efficient.

- [ListRealtimeContactAnalysisSegments](../../../contact-lens/latest/APIReference/API_ListRealtimeContactAnalysisSegments.md "../../../contact-lens/latest/APIReference/API_ListRealtimeContactAnalysisSegments.md"): Use for voice
  contacts.
- [ListRealtimeContactAnalysisSegmentsV2](../APIReference/API_ListRealtimeContactAnalysisSegmentsV2.md "../APIReference/API_ListRealtimeContactAnalysisSegmentsV2.md"): Use for chat
  contacts.
  These conversational analytics APIs are polling APIs, with a standard
  request/response exchange, where you don't need to integrate with any other service.
  However, there are [rate
  limitations](amazon-connect-service-limits.md#connect-contactlens-api-quotas "amazon-connect-service-limits.md#connect-contactlens-api-quotas"). If needed, you can eliminate these limitations by using the
  [streaming API](contact-analysis-segment-streams.md "contact-analysis-segment-streams.md"). It
  requires integration with Amazon Kinesis Data Streams.

Following are two use cases for the call and chat analytics API.

## Better contact transfers

When a contact is transferred from one agent to another agent, you can
transfer a transcript of the conversation to the new agent. The new agent then
has context for why the customer is contacting your contact center, and the
customer doesn't need to repeat information they already provided. Use the
[ListRealtimeContactAnalysisSegments](../../../contact-lens/latest/APIReference/API_ListRealtimeContactAnalysisSegments.md "../../../contact-lens/latest/APIReference/API_ListRealtimeContactAnalysisSegments.md") API for voice contacts and the
[ListRealtimeContactAnalysisSegmentsV2](../APIReference/API_ListRealtimeContactAnalysisSegmentsV2.md "../APIReference/API_ListRealtimeContactAnalysisSegmentsV2.md") API for chats to get the
entire transcript of the conversation up to a certain point, and share it with
the new agent.

## Highlight key parts of the

conversation as labels, issues, action items, and outcomes

With key highlights agents can quickly makes notes after the contact ends, and
supervisors can quickly identify contacts for quality and agent performance
management. This makes agents and supervisors more productive at their
jobs.
