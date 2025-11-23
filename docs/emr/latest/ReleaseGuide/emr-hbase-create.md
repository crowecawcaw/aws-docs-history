# Creating a cluster with HBase

The procedures in this section cover the basics of launching a cluster using the AWS Management Console and the AWS CLI. For detailed information about how to plan, configure, and launch Amazon EMR clusters, see [Plan and configure clusters](../ManagementGuide/emr-plan.md "../ManagementGuide/emr-plan.md") in the _Amazon EMR Management Guide_.

## Creating a cluster with HBase using the console

For quick steps to
launch clusters with the console, see [Getting started with Amazon EMR](../ManagementGuide/emr-gs.md "../ManagementGuide/emr-gs.md") in the _Amazon EMR Management Guide_.

###### To launch a cluster with HBase installed using the console

1. Open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr/ "https://console.aws.amazon.com/emr/").
2. Choose **Create cluster** and **Go to advanced
   options**.
3. For **Software Configuration**, choose an **Amazon
   Release Version** of 4.6.0 or later (we recommend the latest version). Choose
   **HBase** and other applications as desired.
4. With Amazon EMR version 5.2.0 and later, under **HBase Storage Settings**, select **HDFS** or **S3**. For more information, see [HBase on Amazon S3 (Amazon S3 storage mode)](emr-hbase-s3.md "emr-hbase-s3.md").
5. Select other options as necessary and then choose **Create
   cluster**.

## Creating a cluster with HBase using the AWS CLI

Use the following command to create a cluster with HBase installed:

```
aws emr create-cluster --name "`Test cluster`" --release-label `emr-7.12.0` \
--applications Name=`HBase` --use-default-roles --ec2-attributes KeyName=`myKey` \
--instance-type `m5.xlarge` --instance-count `3`
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

If you use HBase on Amazon S3, specify the `--configurations` option
with a reference to a JSON configuration object. The configuration object must contain an
`hbase-site` classification that specifies the location in Amazon S3 where
HBase data is stored using the `hbase.rootdir` property. It also must contain
an `hbase` classification, which specifies `s3` using the
`hbase.emr.storageMode` property. The following example demonstrates a
JSON snippet with these configuration settings.

```
[
    {
        "Classification": "hbase-site",
        "Properties": {
            "hbase.rootdir": "`s3://amzn-s3-demo-bucket/MyHBaseStore`"
        }
    },
    {
        "Classification": "hbase",
        "Properties": {
            "hbase.emr.storageMode": "`s3`"
        }
    }
]
```

For more information about HBase on Amazon S3, see [HBase on Amazon S3 (Amazon S3 storage mode)](emr-hbase-s3.md "emr-hbase-s3.md"). For more information about classifications, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").
