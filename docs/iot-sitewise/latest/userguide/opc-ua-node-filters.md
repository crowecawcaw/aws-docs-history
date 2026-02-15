# Use OPC UA node filters in SiteWise Edge

When you define OPC UA data sources for an SiteWise Edge gateway, you can define
node filters. Node filters let you limit which data stream paths the SiteWise Edge
gateway sends to the cloud. You can use node filters to reduce your SiteWise Edge
gateway's startup time and CPU usage by only including paths to data that you
model in AWS IoT SiteWise. By default, SiteWise Edge gateways upload all OPC UA paths except
those that start with `/Server/`. You can use the `*` and
`**` wildcard characters in your node filters to include multiple
data stream paths with one filter. To learn how to set up OPC UA sources for
your SiteWise Edge gateway, see [OPC UA data sources for AWS IoT SiteWise Edge
gateways](configure-sources-opcua.md "configure-sources-opcua.md").

###### Note

AWS IoT SiteWise restarts your SiteWise Edge gateway each time you add or edit a source.
Your SiteWise Edge gateway won't ingest data while it's updating source configuration. The time to restart your
SiteWise Edge gateway depends on the number of tags on your SiteWise Edge gateway's sources. Restart time can range
from a few seconds (for a SiteWise Edge gateway with few tags) to several minutes (for a SiteWise Edge gateway with many tags).

The following table lists the wildcards that you can use to filter OPC UA data
sources.

| OPC UA node filter wildcards | Wildcard                                       | Description |
| ---------------------------- | ---------------------------------------------- | ----------- |
| `*`                          | Matches a single level in a data stream path.  |
| `**`                         | Matches multiple levels in a data stream path. |

###### Note

If you configure a source with a broad filter and then later change the
source to use a more restrictive filter, AWS IoT SiteWise stops storing data that
doesn't match the new filter.

###### Example: Scenario using node filters

Consider the following hypothetical data streams:

- `/WA/Factory 1/Line 1/PLC1`
- `/WA/Factory 1/Line 1/PLC2`
- `/WA/Factory 1/Line 2/Counter1`
- `/WA/Factory 1/Line 2/PLC1`
- `/OR/Factory 1/Line 1/PLC1`
- `/OR/Factory 1/Line 2/Counter2`
  Using the previous data streams, you can define node filters to limit what
  data to include from your OPC UA source.

- To select all nodes in this example, use `/` or
  `/**/`. You can include multiple directories or
  folders with the `**` wildcard characters.
- To select all `PLC` data streams, use
  `/*/*/*/PLC*` or `/**/PLC*`.
- To select all counters in this example, use
  `/**/Counter*` or
  `/*/*/*/Counter*`.
- To select all counters from `Line 2`, use
  `/**/Line 2/Counter*`.
