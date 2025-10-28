# Working with CloudTrail Insights

AWS CloudTrail Insights help AWS users identify and respond to unusual activity associated with API
call rates and API error rates by continuously analyzing CloudTrail management events. CloudTrail Insights
analyzes your past management events to establish your normal patterns of API call rates and
API error rates, also called the _baseline_. CloudTrail then generates Insights events
when the current API call rates or error rates deviate from the baseline.

You can collect two types of Insights:

- **API call rate** – A measurement of write-only management
  API calls that occur per minute against a baseline API call volume. To log Insights events on the API call rate, the trail or event data store must enable Insights and log
  `write` management events.
- **API error rate** – A measurement of management API calls
  that result in error codes. The error is shown if the API call is unsuccessful. To
  log Insights events on API error rate, the trail or event data store must enable Insights and
  log `read` or `write` management events, or both
  `read` and `write` management events.
  CloudTrail Insights analyzes the management events that occur in each Region for the trail or event data
  store and generates an Insights event when unusual activity is detected that deviates from the
  baseline. A CloudTrail Insights event is generated in the same Region as its supporting management event
  is generated.

Additional charges apply for Insights events. You will be charged separately if you enable Insights
for both trails and event data stores. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

###### Topics

- [Costs for Insights events](insights-events-costs.md "insights-events-costs.md")
- [Delivery of Insights events](insights-events-understanding.md "insights-events-understanding.md")
- [Logging Insights events with the CloudTrail console](insights-events-enable.md "insights-events-enable.md")
- [Logging Insights events with the AWS CLI](insights-events-CLI-enable.md "insights-events-CLI-enable.md")
- [Viewing Insights events for trails](view-insights-events.md "view-insights-events.md")
- [Viewing Insights events for event data stores](insights-events-view-lake.md "insights-events-view-lake.md")
