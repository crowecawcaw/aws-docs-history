End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Custom partitions

AWS IoT Analytics supports data partitioning so you can organize the data in your data store. When you
use data partitioning to organize data, you can query on pruned data. This decreases the
amount of data scanned per query and improves latency.

You can partition your data according to message data attributes or attributes added through pipeline activities.

To get started, enable data partitioning in a data store.
Specify one or more data partition dimensions and connect your partitioned data store to an AWS IoT Analytics pipeline.
Then, write queries that leverage the `WHERE` clause to optimize performance.

## Create a data store (console)

The following procedure shows you how to create a data store with a custom partition.

###### To create a data store

1.  Sign in to the [AWS IoT Analytics console](https://console.aws.amazon.com/iotanalytics/ "https://console.aws.amazon.com/iotanalytics/").
2.  In the navigation pane, choose **Data stores**.
3.  On the **Data stores** page, choose **Create data
    store**.
4.  On the **Specify data store details** page, enter basic
    information about your data store.
    1. For **Data store ID**, enter a unique data store ID.
       You can't change this ID after you create it.
    2. (Optional) For **Tags**, choose **Add new
       tag** to add one or more custom tags (key-value pairs) to
       your data store. Tags can help you identify resources that you create
       for AWS IoT Analytics.
    3. Choose **Next**.

5.  On the **Configure storage type** page, specify how to store
    your data.
    1. For **Storage type**, choose **Service
       managed storage**.
    2. For **Configure how long you want to keep your processed
       data**, choose **Indefinitely**.
    3. Choose **Next**.

6.  On the **Configure data format** page, define the structure
    and format of your data records.
    1. For your data store data format **Classification**,
       choose **JSON** or **Parquet**. For
       more information about AWS IoT Analytics supported file types, see [File formats](iotanalytics-schema.md "iotanalytics-schema.md").

    ###### Note

    You can't change this format after you create the data store. 2. Choose **Next**.

7.  Create custom partitions for this data store.
    1. For **Add data partitions**, select **Enable**.
    2. For **Data partition source**, specify basic
       information about the source of your partition.

    Choose **Sample source**, and select the AWS IoT Analytics channel that collects messages for this data store. 3. For **Message sample attributes**, select the message
    attributes you want to use to partition your data store. Then, add your
    selections as attribute partition dimensions or timestamp partition
    dimensions under **Actions**.

    ###### Note

    You can add only one timestamp partition to your data store. 4. For **Custom data store partition dimensions**, define basic information about your partition dimensions.
    Each message sample attribute you selected in the previous step will become the dimensions of your partition.
    Customize each dimension with these options:

        * **Partition type** - Specify if this partition dimension is an **Attribute** or a **Timestamp** partition type.
        * **Attribute name** and **Dimension name** - By default, AWS IoT Analytics will use the name of the message sample attribute you selected as an identifier for your attribute partition dimension.
         Edit the attribute name to customize the name of your partition dimension.
         You can use the dimension name in the `WHERE` clause to optimize query performance.




        	+ The name of any partition attribute dimension is
        	 prefixed with `__partition_`.
        	+ For timestamp partition types, AWS IoT Analytics creates the
        	 following four dimensions with names
        	 `__year`, `__month`,
        	 `__day`, `__hour`.
        * **Ordering** - Rearrange your partition
         dimensions to improve the latency for your queries.

    For **Timestamp format**, specify the format of your
    timestamp partition by matching the ingested timestamp from your message
    data. You can choose one of AWS IoT Analytics listed format options, or specify one
    that matches the format of your data. Learn more about specifying [date time formatters](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/format/DateTimeFormatter.html " https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/format/DateTimeFormatter.html").

    To add a new dimension that isn’t a message attribute, choose **Add new partitions**. 5. Choose **Next**.

8.  On the **Review and create** page, review your choices, and
    then choose **Create data store**.

###### Important

    * You can't change the data store ID after you create the data store.
    * To edit existing partitions, you must create another data store and reprocess the data through a pipeline.

9. Verify that your new data store appears on the **Data
   stores** page.
