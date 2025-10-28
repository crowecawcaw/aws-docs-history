# Create connector

This procedure describes how to create a connector using the AWS Management Console.

###### To create the connector

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. In the left pane, expand **MSK Connect**, then choose
   **Connectors**.
3. Choose **Create connector**.
4. In the list of plugins, choose `mkc-tutorial-plugin`, then
   choose **Next**.
5. For the connector name enter `mkc-tutorial-connector`.
6. In the list of clusters, choose `mkc-tutorial-cluster`.
7. Copy the following configuration and paste it into the connector configuration field.

Make sure that you replace region with the code of the AWS Region where you're creating the connector. Also, replace the Amazon S3 bucket name `<amzn-s3-demo-bucket-my-tutorial>` with the name of your bucket in the following example.

```
connector.class=io.confluent.connect.s3.S3SinkConnector
s3.region=`us-east-1`
format.class=io.confluent.connect.s3.format.json.JsonFormat
flush.size=1
schema.compatibility=NONE
tasks.max=2
topics=mkc-tutorial-topic
partitioner.class=io.confluent.connect.storage.partitioner.DefaultPartitioner
storage.class=io.confluent.connect.s3.storage.S3Storage
s3.bucket.name=`<amzn-s3-demo-bucket-my-tutorial>`
topics.dir=tutorial
```

8. Under **Access permissions** choose
   `mkc-tutorial-role`.
9. Choose **Next**. On the **Security** page,
   choose **Next** again.
10. On the **Logs** page choose
    **Next**.
11. Under **Review and create** choose **Create
    connector**.
    **Next Step**

[Send data to the MSK cluster](mkc-send-data.md "mkc-send-data.md")
