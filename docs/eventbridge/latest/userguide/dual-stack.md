# Dual-stack service endpoints in Amazon EventBridge

In addition to the IPv4 service endpoints, EventBridge also provides dual-stack endpoints for the following resources.
You can access these endpoints using either IPv4 or IPv6 requests.

| Resource                                                                     | Region endpoint                           | FIPS endpoint                                  | Regions                                                                                                                                                                                  |
| ---------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Event buses](eb-event-bus.md "eb-event-bus.md")                             | `HTTPS://events.`region-code`.api.aws`    | `HTTPS://events-fips.`region-code`.api.aws`    | [EventBridge](../../../general/latest/gr/ev.md#ev_region "../../../general/latest/gr/ev.md#ev_region")                                                                                   |
| [Pipes](eb-pipes.md "eb-pipes.md")                                           | `HTTPS://pipes.`region-code`.api.aws`     | `HTTPS:://pipes-fips.`region-code`.api.aws`    | [EventBridge Pipes](../../../general/latest/gr/ev_pipes.md#ev_pipes_region "../../../general/latest/gr/ev_pipes.md#ev_pipes_region")                                                     |
| [Scheduler](using-eventbridge-scheduler.md "using-eventbridge-scheduler.md") | `HTTPS://scheduler.`region-code`.api.aws` | `HTTPS://scheduler-fips.`region-code`.api.aws` | [EventBridge Scheduler](../../../general/latest/gr/eventbridgescheduler.md#eventbridgescheduler_region "../../../general/latest/gr/eventbridgescheduler.md#eventbridgescheduler_region") |
| [Schemas](eb-schema.md "eb-schema.md")                                       | `HTTPS://schemas.`region-code`.api.aws`   | `HTTPS://schemas-fips.`region-code`.api.aws`   | [EventBridge Schemas](../../../general/latest/gr/eventbridgeschemas.md#eventbridgeschemas_region "../../../general/latest/gr/eventbridgeschemas.md#eventbridgeschemas_region")           |

To make a request to a dual-stack endpoint, you must use the mechanism provided by the tool
or AWS SDK to specify the endpoint. For more information, see [Dual-stack and FIPS endpoints](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md") in the
_AWS SDKs and Tools Reference Guide_.

For example, the AWS CLI provides the `--endpoint-url` option. The
following example uses `--endpoint-url` to specify the dual-stack endpoint for event
buses in the US West (Oregon) Region.

```
aws events describe-event-bus --region us-west-2 --endpoint-url https://events.us-west-2.api.aws
```

For a list of Region codes to use when specifying regional endpoints, see
[Regional endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") in the _AWS General Reference_.

## Considerations when using dual-stack

endpoints

Keep the following considerations in mind when using dual-stack endpoints to access EventBridge
resources.

For event buses:

- Dual-stack support for event buses includes archives and replays.
- EventBridge does not currently support dual-stack endpoints for [global endpoints](eb-global-endpoints.md "eb-global-endpoints.md").

If you configure the AWS SDK to use dual-stack endpoints, calls to [`PutEvents`](../APIReference/API_PutEvents.md "../APIReference/API_PutEvents.md") will result in an error. This is because the SDK uses the dual-stack domain
(`events.`region-code`.api.aws`)
rather than
`events.`region-code`.amazonaws.com`
when constructing the endpoint, resulting in the request being sent to an endpoint that does not exist.

For EventBridge Pipes:

- EventBridge Pipes supports dual-stack requests with [Interface VPC endpoints](eb-related-service-vpc.md "eb-related-service-vpc.md").
