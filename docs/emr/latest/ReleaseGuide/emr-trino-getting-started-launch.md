# Launch an Amazon EMR cluster with Trino

The following describes the correct configuration choices when you create a
cluster with Trino.

## Using a Hive connector to make data available for querying

You can configure a Trino connector for a Hive metastore for the purpose of querying metastore data from your cluster. A metastore is an abstraction layer that
makes file-based content or data available as tables, so it's easy to query. You have to configure a connector in Amazon EMR to
make the Hive metastore tables available to the cluster. The following procedure shows you how to do this:

1. Choose AWS Glue in the console and create a table, based on your source data in Amazon S3. A table in the AWS Glue Data Catalog is the metadata definition for the data. It makes sense in this
   context to create the table manually, creating columns as you like, from your source data. For more information about
   creating tables in AWS Glue from semi-structured data in Amazon S3, see [Creating tables using the
   console](../../../glue/latest/dg/tables-described.md#console-tables "../../../glue/latest/dg/tables-described.md#console-tables") in the _AWS Glue User Guide_.
2. Set your configuration as part of cluster creation. Select the **Configurations** tab. Configurations are optional specifications for your
   cluster. When you enter a configuration, add JSON like the following sample, which instructs
   Trino to use the AWS Glue Data Catalog as its external Hive metastore for table metadata:

```
{
    "classification": "trino-connector-hive",
    "properties": {
        "hive.metastore": "glue"
    }
}
```

Alternatively, you can apply configurations in the **Software settings** section when you create a cluster.

Additionally,
you can set up other
connector types, such as for connecting with Apache Iceberg. For more information,
see [Use an Iceberg cluster with Trino](emr-iceberg-use-trino-cluster.md "emr-iceberg-use-trino-cluster.md") in the _Amazon EMR Release Guide_. Configuring
additional settings is optional.

To continue the getting-started steps, see [Connect to the primary node for the Amazon EMR cluster and run queries](emr-trino-getting-started-connect.md "emr-trino-getting-started-connect.md").

## Create a cluster with Trino

The following describes the correct configuration choices when you create a cluster that you want to use with Trino.

###### Important

Before you create your cluster, complete AWS Glue Data Catalog configuration as your Hive metastore, which we recommend for getting started. For more information, see [Using a Hive connector to make data available for querying](#emr-trino-getting-started-connect-hive "#emr-trino-getting-started-connect-hive").

1. In the AWS console, select Amazon EMR from the services. When you choose Amazon EMR, if you have existing clusters, your
   **EMR on EC2** clusters are listed.
2. Choose **Create cluster**. From here, you start the process for building a cluster.
3. Give your cluster a name and choose an **Amazon EMR release**. You can choose the most current release for the tutorial.
4. Choose the **Trino** bundle, which has the Trino application pre-selected. Bundles are set up for convenience when you
   know the purpose for the cluster ahead of time. Otherwise, you can simply select the check box for Trino.
5. For **Cluster configuration**, choose **Uniform instance groups**. Go ahead and remove additional instance groups.
6. Choose an **Instance type**. Generally we recommend you choose an instance type with at least 16 GiB memory. Also, for **Cluster scaling and provisioning**
   choose **Set cluster size manually**.
7. At this point, set your Hive metastore configuration to point to AWS Glue. This is detailed in the section [Using a Hive connector to make data available for querying](#emr-trino-getting-started-connect-hive "#emr-trino-getting-started-connect-hive"). Complete this before you build the cluster.
8. Choose **Create cluster**. It can take a few minutes to finish.

The steps here don't cover all of the configuration steps
in detail. More information about
setting up a cluster is available at [Plan, configure and launch Amazon EMR clusters](../ManagementGuide/emr-plan.md "../ManagementGuide/emr-plan.md").

###### Note

Don't select both Presto and Trino for use on the same cluster. Running them together isn't supported. It's also recommended
that if you run Trino, you don't run any other applications on the cluster, such as Spark.
