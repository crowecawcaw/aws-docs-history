# Creating a new Neptune Analytics graph using the AWS Management Console

You can use the Neptune console to create a new Neptune Analytics graph.

###### Note

If you are working with a large dataset (on the order of 50 GiB or larger)
that you intend to load at the same time the new graph is created, be sure to [create an IAM role](bulk-import-create-from-neptune.md#iam-create-role-export-neptune-analytics "bulk-import-create-from-neptune.md#iam-create-role-export-neptune-analytics") that grants
permissions to load the dataset from the location where it resides.

###### To use the Neptune console to create a graph

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at
   [https://console.aws.amazon.com/neptune/](https://console.aws.amazon.com/neptune/ "https://console.aws.amazon.com/neptune/").
2. In the navigation pane, select **Graphs** under
   **Analytics**.
3. Select **Create graph**.
4. Enter a name for the new graph.
5. The next steps depend on whether you are creating an empty graph or
   one preloaded with data.
   - If you choose **Create empty graph**,
     choose the number of memory-optimized Neptune Capacity Units (m-NCUs) to
     allocate to the new Neptune Analytics graph, between 128 and 1024. Each m-NCU has
     around one GiB of memory capacity and corresponding compute and
     networking.
   - If you choose **Create Graph from existing source**,
     Neptune Analytics will bulk-load data for you when the graph is created. Choose this
     option if you want to import a large dataset, on the order of 50 GiB or
     larger. See [Bulk import](bulk-import.md "bulk-import.md") for details.
     1. Set values for the minimum and maximum m-NCUs,
        or just leave them at their default values (128 m-NCUs).
        The units are memory-optimized Neptune Capacity Units (m-NCUs), each of which
        is roughly equivalent to 1 GiB of memory and corresponding compute and
        networking. Neptune Analytics evaluates the data that you want to load and estimates
        the resources needed to handle it, within the range of m-NCUs
        that you specify.
     2. Under **Load role ARN**, select an IAM role
        that you have created to provide the necessary permissions for the data import.
        See [Create an IAM role with permissions to export
        from Neptune to Neptune Analytics](bulk-import-create-from-neptune.md#iam-create-role-export-neptune-analytics "bulk-import-create-from-neptune.md#iam-create-role-export-neptune-analytics") for instructions about how to create the role.
     3. The next steps depend on what source you're loading data from:
        - If you choose **Create empty graph**, choose the number of memory-optimized Neptune Capacity
          Units (m-NCUs) to allocate to the new Neptune Analytics graph, between 16 and 4096. Each m-NCU has around one GiB of
          memory capacity and corresponding compute and networking.
        - If you choose **Neptune cluster snapshot** as the type of source,
          select one of your manual DB snapshots that you want to load from under **Neptune
          DB snapshot**.
        - If you choose **S3** as the type of source,
          enter the URL of the Amazon S3 location where the data file(s) to be loaded are
          located, under **Resource URI**. The path to the folder location
          must end in a slash rather than specify to a particular file.

6. Under **Availability settings**, choose how many failover
   replicas you want to create for the new graph. The default is one, but if you select
   Use custom number of replicas you can choose from zero to two failover replicas.

###### Important

Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. 7. Under **Network and security**, check **Allow
from public** to create a public endpoint for your new Neptune Analytics graph to make it
accessible over the internet. If you want to use your own KMS key to encrypt your
data, check **Customize encryption settings** a specify a KMS
key of your choosing. 8. Under **Vector search settings**, if you want to set up
a vector index for the graph, choose **Use vector dimension** and
then specify the number of dimensions for the vectors in the index. 9. Under **Advanced settings**, you can make it easier to
delete your new graph by selecting **Turn off deletion protection**.
Deletion protection is turned on by default. 10. Finally, under **Tags**, you can associate tags with
your new Neptune Analytics graph. 11. When everything is configured as you want it to be, choose
**Create Graph**.
