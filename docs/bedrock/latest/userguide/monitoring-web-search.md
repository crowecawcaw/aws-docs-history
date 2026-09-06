

# Monitor Web Search
<a name="monitoring-web-search"></a>

Web Search on Amazon Bedrock is integrated with AWS CloudTrail. CloudTrail captures API activity for Web Search so you can audit who invoked the tool, when, and from where.

Web Search activity is recorded as CloudTrail data events. Data events are not logged by default. To capture them, create a trail (or event data store) and enable data event logging for Web Search. For the steps, see [Logging data events with AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html). Additional charges apply for data events.

Once data event logging is enabled, CloudTrail captures the following for each recorded call:
+ The identity that invoked the action
+ The time the call occurred
+ The specific `bedrock-websearch` action that was called
+ The source identity, including the forward access sessions (FAS) session originator
+ The account and Region context of the request

For an `InvokeFetch` event, CloudTrail also records the following fields:
+ `requestParameters.fetchMode` – The effective mode for a successful Fetch: `USE_CACHE_ONLY` or `USE_CACHE_WITH_EXTERNAL_WEB_FALLBACK`. For a denied request, this field records the requested mode.
+ `requestParameters.urlCount` – The number of URLs in the Fetch call.
+ `additionalEventData.failedUrlCount` – The number of URLs for which Fetch returned no content.
+ `additionalEventData.fetchedSources` – Counts of URLs successfully retrieved from `CACHE` and `EXTERNAL_WEB`. These counts let you determine whether a Fetch was served from the Amazon Bedrock cache or reached the external web.

For a completed Fetch, the `CACHE` and `EXTERNAL_WEB` counts plus `failedUrlCount` account for `urlCount`. A Fetch denied because the caller lacks `bedrock-websearch:ExternalWebAccess` records `errorCode: AccessDenied` and no `fetchedSources`, because no page retrieval was attempted. The caller's Responses API request can still return HTTP `200` after this backend denial, so use the CloudTrail event rather than the model response to detect it.

Access-denied outcomes are only logged when you opt into data event delivery for `bedrock-websearch`. Otherwise they are not reported. An `AccessDenied` event includes the error code and can include the IAM authorization message, which helps you diagnose policy issues.

By design, CloudTrail does not expose the query text, the URLs, or the raw search results from Web Search. Query text is treated the same way as an inference prompt.