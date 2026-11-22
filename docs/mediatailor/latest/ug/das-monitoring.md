

# Monitoring dynamic avail sizing

Use CloudWatch metrics and the ADS logs to see how dynamic avail sizing is behaving for a session.

## Metrics
<a name="das-monitoring-metrics"></a>

MediaTailor publishes the following CloudWatch metrics only for sessions with dynamic avail sizing enabled. Durations are in milliseconds. For the full definitions, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md).
+ [`Avail.OmittedDuration`](monitoring-cloudwatch-metrics.md#metrics-avail-omittedduration) – Duration that MediaTailor removed when it shortened the avail.
+ [`Avail.ObservedOmittedDuration`](monitoring-cloudwatch-metrics.md#metrics-avail-observedomittedduration) – The same, based on the avail's actual segment durations.
+ [`Avail.UnpersonalizedDuration`](monitoring-cloudwatch-metrics.md#metrics-avail-unpersonalizedduration) – Duration of slate or unpersonalized avail content, when the reserve couldn't cover the underfill.
+ [`Avail.ObservedUnpersonalizedDuration`](monitoring-cloudwatch-metrics.md#metrics-avail-observedunpersonalizedduration) – The same, based on the avail's actual segment durations.
+ [`Avail.OverfillDuration`](monitoring-cloudwatch-metrics.md#metrics-avail-overfillduration) – Duration that an inflated avail filled beyond its original duration, which replenishes the reserve.
+ [`Avail.ObservedOverfillDuration`](monitoring-cloudwatch-metrics.md#metrics-avail-observedoverfillduration) – The same, based on the avail's actual segment durations.
+ [`Avail.ContentReserveDurationBeforeAvail`](monitoring-cloudwatch-metrics.md#metrics-avail-contentreservedurationbeforeavail) – Duration of the reserve before the avail.
+ [`Avail.RequestedDuration`](monitoring-cloudwatch-metrics.md#metrics-avail-requestedduration) – Duration that MediaTailor requested from the ADS, including inflation.
+ [`AdDecisionServer.RequestFillRate`](monitoring-cloudwatch-metrics.md#metrics-ads-requestfillrate) – Fraction of the requested duration that the ADS returned ads for.

MediaTailor emits `Avail.RequestedDuration` and `AdDecisionServer.RequestFillRate` only when the ADS URL includes `[session.avail_duration_ms]` or `[session.avail_duration_secs]`.

## Log fields
<a name="das-monitoring-logs"></a>

For sessions with dynamic avail sizing enabled, `FILLED_AVAIL` events in the ADS logs include the following `avail` properties. Values are in seconds. For all avail properties, see [ADS log avail properties](ads-log-format.md#ads-logs-avail).
+ [`avail.omittedDuration`](ads-log-format.md#ads-logs-avail-omittedduration) – Duration that MediaTailor removed when it shortened the avail.
+ [`avail.unpersonalizedDuration`](ads-log-format.md#ads-logs-avail-unpersonalizedduration) – Duration of slate or unpersonalized avail content, when the reserve couldn't cover the underfill.
+ [`avail.overfillDuration`](ads-log-format.md#ads-logs-avail-overfillduration) – Duration that an inflated avail filled beyond its original duration, which replenishes the reserve.
+ [`avail.contentReserveDurationBeforeAvail`](ads-log-format.md#ads-logs-avail-contentreservedurationbeforeavail) – Duration of the reserve before the avail.
+ [`avail.requestedDuration`](ads-log-format.md#ads-logs-avail-requestedduration) – Duration that MediaTailor requested from the ADS, including inflation.

MediaTailor includes `avail.requestedDuration` only when the ADS URL includes `[session.avail_duration_ms]` or `[session.avail_duration_secs]`.