**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint journey and campaign execution

metrics

You can query standard execution metrics to assess the status of participants in each type
of individual activity for an Amazon Pinpoint journey or campaign. To query data for these metrics, use the
[Journey run activity execution metrics](../apireference/apps-application-id-journeys-journey-id-runs-run-id-activities-journey-activity-id-execution-metrics.md "../apireference/apps-application-id-journeys-journey-id-runs-run-id-activities-journey-activity-id-execution-metrics.md") or [Campaign Metrics](../apireference/apps-application-id-campaigns-campaign-id-kpis-daterange-kpi-name.md "../apireference/apps-application-id-campaigns-campaign-id-kpis-daterange-kpi-name.md") resource of the Amazon Pinpoint API. The following table
lists the fields that appear in the query results for each type of activity.

| Metric Name                 | Applies to Journeys, Campaigns, or Both | Description                                                                                                                                                                                      |
| --------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ENDPOINT_PRODUCED           | Both                                    | The number of endpoints initially produced from the segment or event before any filtering.                                                                                                       |
| ENDPOINTS_FROM_USER         | Both                                    | If the customer has a user-id only segment, then all the endpoints of those users will be added. This metric measures the number of endpoints added in this way.                                 |
| ENDPOINT_OPT_OUT            | Both                                    | The endpoint was opted out and didn't enter the campaign or journey.                                                                                                                             |
| ENDPOINT_INACTIVE           | Both                                    | The endpoint was inactive and didn't enter the campaign or journey.                                                                                                                              |
| FILTERED_OUT_BY_SEGMENT     | Both                                    | Endpoint didn't match segment filters and didn't enter the campaign or journey.                                                                                                                  |
| ENDPOINT_MISSING_ADDRESS    | Both                                    | Endpoint was missing an address and didn't enter the campaign or journey.                                                                                                                        |
| ENDPOINT_MISSING_CHANNEL    | Both                                    | Endpoint was missing a channel and didn't enter the campaign or journey.                                                                                                                         |
| ENDPOINT_MISSING_TIMEZONE   | Both                                    | Endpoint was missing a value for timezone and was filtered out. This only happens when a timezone value is required.                                                                             |
| ENDPOINT_TIMEZONE_MISMATCH  | Both                                    | Endpoint was in a timezone that wasn't included in the execution at that time.                                                                                                                   |
| ENDPOINT_CHANNEL_MISMATCH   | Campaigns                               | The campaign doesn't have a message configured for this endpoint's channel type.                                                                                                                 |
| DUPLICATE_ENDPOINT          | Both                                    | Duplicate endpoints were found and de-duped.                                                                                                                                                     |
| DUPLICATE_USER              | Both                                    | Duplicate users were found and de-duped from a user-id only segment. If they have the same user id, a metric of 1 will be emitted.                                                               |
| PAUSED                      | Journeys                                | Removed from execution because the journey was paused.                                                                                                                                           |
| ENDED                       | Journeys                                | Removed from execution because the journey was ended.                                                                                                                                            |
| TREATMENT_HOLDOUT           | Campaigns                               | This is emitted in A/B campaigns, for endpoints whose cohorts don’t match the current treatment. For example in a 50/50 A/B split, 50% of the endpoints will emit this metric for each treatment |
| ENDPOINT_ESTIMATED_TIMEZONE | Journeys                                | Time zone estimation was able to estimate a time zone for the endpoint.                                                                                                                          |
