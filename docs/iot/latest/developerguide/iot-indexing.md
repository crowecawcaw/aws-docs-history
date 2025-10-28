# Fleet indexing

You can use fleet indexing to index, search, and aggregate your devices' data from the
following sources: [AWS IoT registry](thing-registry.md "thing-registry.md"), [AWS IoT Device Shadow](iot-device-shadows.md "iot-device-shadows.md"), [AWS IoT connectivity](life-cycle-events.md "life-cycle-events.md"), [AWS IoT Device Management Software Package Catalog](software-package-catalog.md "software-package-catalog.md"), and
[AWS IoT Device Defender](../../../iot-device-defender/latest/devguide/what-is-device-defender.md "../../../iot-device-defender/latest/devguide/what-is-device-defender.md")
violations. You can query a group of devices, and aggregate statistics on device records that
are based on different combinations of device attributes, including state, connectivity, and
device violations. With fleet indexing, you can organize, investigate, and troubleshoot your
fleet of devices.

Fleet indexing provides the following capabilities.

## Managing index updates

You can set up a fleet index to index updates for your thing groups, thing registries,
device shadows, device connectivity, and device violations. When you activate fleet indexing,
AWS IoT creates an index for your things or thing groups. `AWS_Things` is the index
created for all of your things. `AWS_ThingGroups` is the index that contains all of
your thing groups. After fleet indexing is active, you can run queries on your index. For
example, you can find all devices that are handheld and have more than 70 percent battery
life. AWS IoT updates the index continually with your latest data. For more information, see
[Managing fleet indexing](managing-fleet-index.md "managing-fleet-index.md").

## Querying connectivity status for a specific device

This API provides low-latency, high-throughput access to the most recent device-specific
connectivity information. For more information, see [Device connectivity status.](device-connectivity-status.md "device-connectivity-status.md")

## Searching across data sources

You can create a query string based on [a query
language](query-syntax.md "query-syntax.md") and use it to search across data sources. You also need to configure data
sources in the fleet indexing setting so that the indexing configuration contains the data
sources you want to search from. The query string describes the things that you want to find.
You can create queries by using AWS managed fields, custom fields, and any attributes from
your indexed data sources. For more information about data sources that support fleet
indexing, see [Managing thing indexing](managing-index.md "managing-index.md").

## Querying for aggregate data

You can search your devices for aggregate data and return statistics, percentile,
cardinality, or a list of things with search queries about particular fields. You can run
aggregations on AWS managed fields or any attributes you configure as custom fields within
fleet indexing settings. For more information about aggregation query, see [Querying for aggregate data](index-aggregate.md "index-aggregate.md").

## Monitoring aggregate data and creating

alarms by using fleet metrics

You can use fleet metrics to send aggregate data to CloudWatch automatically, analyze trends,
and create alarms to monitor the aggregate state of your fleet based on pre-defined
thresholds. For more information about fleet metrics, see [Fleet metrics](iot-fleet-metrics.md "iot-fleet-metrics.md").
