**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint journey execution metrics

The following table lists and describes standard execution metrics that you can query to
assess the status of participants in an Amazon Pinpoint journey. To query data for these metrics, use the
[Journey
execution metrics](../apireference/apps-application-id-journeys-journey-id-execution-metrics.md "../apireference/apps-application-id-journeys-journey-id-execution-metrics.md") resource of the Amazon Pinpoint API. The **Field**
column in the table identifies the name of the field that appears in the query results for each
metric.

| Metric                                 | Field                      | Description                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active participants                    | `ENDPOINT_ACTIVE`          | The number of participants who are actively proceeding through the activities in the journey. This metric is calculated as the number of participants who started the journey, minus the number of participants who left the journey and the number of participants who were removed from the journey.                                                    |
| Participant cancellations              | `CANCELLED`                | The number of participants who didn't complete the journey because the journey was cancelled.                                                                                                                                                                                                                                                             |
| Participant departures                 | `ENDPOINT_LEFT`            | The number of participants who left the journey.                                                                                                                                                                                                                                                                                                          |
| Participant entries                    | `ENDPOINT_ENTERED`         | The number of participants who started the journey.                                                                                                                                                                                                                                                                                                       |
| Participant exceptions, reentry limits | `REENTRY_CAP_EXCEEDED`     | The number of participants who didn't complete the journey because they would have exceeded the maximum number of times that a single participant can re-enter the journey.                                                                                                                                                                               |
| Participant exceptions, rejections     | `ACTIVE_ENDPOINT_REJECTED` | The number of participants who can't start the journey because they are already active participants in the journey. A participant is rejected if they start a journey and you subsequently update their endpoint definition in a way that affects their inclusion in a segment (based on segment criteria) or the journey (based on activity conditions). |
