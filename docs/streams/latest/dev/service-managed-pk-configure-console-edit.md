

# View and edit the record distribution strategy for an existing stream
<a name="service-managed-pk-configure-console-edit"></a>

1. Open the Kinesis Data Streams console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. Choose the data stream you want to update.

1. Choose the **Configuration** tab. The current record distribution strategy is shown in the **Data stream capacity** panel.

1. Choose **Edit** next to **Record distribution strategy**.

1. Choose **Auto** or **User set**, then save your changes. The change takes effect immediately.
**Note**  
The console displays a warning when you switch strategies, reminding you that service-managed (**Auto**) distribution eliminates partition-key ordering guarantees, and that user-managed (**User set**) distribution requires producers to supply a partition key.

You can also view the record distribution strategy in the following places in the console:
+ The **Record distribution strategy** column in the data streams table shows **Auto**, **User set**, or a dash for provisioned streams.
+ The **Data stream summary** panel on the stream detail page shows the current record distribution strategy.