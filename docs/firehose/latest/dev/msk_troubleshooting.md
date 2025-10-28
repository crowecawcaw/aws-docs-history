# Troubleshooting MSK As Source

This section describes common troubleshooting steps while using MSK As Source

###### Note

For troubleshooting processing, transformation or S3 delivery issues, please refer the earlier sections

## Hose creation fails

Check the following if your hose with MSK As Source is failing creation:

- Check that the source MSK cluster is in Active state.
- If you are using Private connectivity, ensure that [Private Link on the cluster is turned on](../../../msk/latest/developerguide/aws-access-mult-vpc.md "../../../msk/latest/developerguide/aws-access-mult-vpc.md").

If you are using Public connectivity, ensure that [Public access on the cluster is turned on](../../../msk/latest/developerguide/public-access.md "../../../msk/latest/developerguide/public-access.md").

- If you are using Private connectivity, make sure that you add a [resource based policy that allows Firehose to create Private Link](controlling-access.md#access-to-msk "controlling-access.md#access-to-msk").
  Also refer: [MSK cross account permissions](../../../msk/latest/developerguide/mvpc-cross-account-permissions.md "../../../msk/latest/developerguide/mvpc-cross-account-permissions.md").
- Ensure that the role in source configuration has [permission to ingest data from cluster's Topic](controlling-access.md#firehose-assume-role "controlling-access.md#firehose-assume-role").
- Ensure that your VPC security groups allow incoming traffic on [ports used by the cluster's bootstrap servers](../../../msk/latest/developerguide/port-info.md "../../../msk/latest/developerguide/port-info.md").

## Hose Suspended

Check the following if your hose is in SUSPENDED state

- Check that the source MSK cluster is in Active state.
- Check that the source topic exists. In case the topic was deleted and
  re-created, you will have to delete and re-create the Firehose stream as well.

## Hose Backpresurred

The value of DataReadFromSource.Backpressured will be 1 when BytesPerSecondLimit per partition
is exceeded or that the normal flow of delivery is slow or stopped.

- If you are hitting BytesPerSecondLimit please check DataReadFromSource.Bytes metric and request a limit increase.
- Check the CloudWatch logs, destination metrics, Data Transformation metrics and Format Conversion metrics to identify the bottlenecks.

## Incorrect Data Freshness

Data freshness seems incorrect

- Firehose calculates the data freshness based on the timestamp of the consumed record. To ensure that this timestamp is correctly recorded
  when the producer record is persisted in the Kafka's broker logs, set the Kafka topic timestamp type configuration to be
  `message.timestamp.type=LogAppendTime`.

## MSK cluster connection issues

The following procedure explain how you can validate connectivity to MSK clusters. For
details about setting up Amazon MSK client, see [Getting started using Amazon
MSK](../../../msk/latest/developerguide/getting-started.md "../../../msk/latest/developerguide/getting-started.md") in the _Amazon Managed Streaming for Apache Kafka Developer Guide_.

###### To validate connectivity to MSK clusters

1. Create a Unix-based (preferably AL2) Amazon EC2 instance. If you have only VPC connectivity enabled
   on your cluster then make sure your EC2 instance runs in the same VPC. SSH into
   the instance once its available. For more information, see [this
   tutorial](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the _Amazon EC2 User Guide_.
2. Install Java using the Yum package manager by running the following command. For more
   information, see the [installation
   instructions](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the Amazon Corretto 8 User Guide.

```
sudo yum install java-1.8.0
```

3. Install the [AWS client](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") by running the
   following command.

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

4. Download the Apache Kafka client 2.6\* version by running the following command.

```
wget https://archive.apache.org/dist/kafka/2.6.2/kafka_2.12-2.6.2.tgz
tar -xzf kafka_2.12-2.6.2.tgz
```

5. Go to the `kafka_2.12-2.6.2/libs` directory, then run the following
   command to download the Amazon MSK IAM JAR file.

```
wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.3/aws-msk-iam-auth-1.1.3-all.jar
```

6. Create `client.properties` file in Kafka bin folder.
7. Replace `awsRoleArn` with the role ARN that you have used in your
   Firehose `SourceConfiguration` and verify the cert location. Allow
   your AWS client user to assume role `awsRoleArn`. AWS client user
   will attempt to assume the role that you specified here.

```

[ec2-user@ip-xx-xx-xx-xx bin]$ cat client.properties
security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required awsRoleArn="<role arn>" awsStsRegion="<region name>";
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler
awsDebugCreds=true
ssl.truststore.location=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.342.b07-1.amzn2.0.1.x86_64/jre/lib/security/cacerts
ssl.truststore.password=changeit
```

8. Run the following Kafka command to list topics. If your connection is public, use the public
   endpoint Bootstrap servers. If your connection is private, use the private
   endpoint Bootstrap servers.

```
bin/kafka-topics.sh --list --bootstrap-server `<bootstrap servers>` --command-config bin/client.properties
```

If the request is successful, you should see an output similar to the
following example.

```
[ec2-user@ip-xx-xx-xx-xx kafka_2.12-2.6.2]$ bin/kafka-topics.sh --list --bootstrap-server `<bootstrap servers>` --command-config bin/client.properties

[xxxx-xx-xx 05:49:50,877] WARN The configuration 'awsDebugCreds' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[xxxx-xx-xx 05:49:50,878] WARN The configuration 'ssl.truststore.location' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[xxxx-xx-xx 05:49:50,878] WARN The configuration 'sasl.jaas.config' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[xxxx-xx-xx 05:49:50,878] WARN The configuration 'sasl.client.callback.handler.class' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[xxxx-xx-xx 05:49:50,878] WARN The configuration 'ssl.truststore.password' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[xxxx-xx-xx 05:50:21,629] WARN [AdminClient clientId=adminclient-1] Connection to node...
__amazon_msk_canary
__consumer_offsets
```

9. If you have any issues running the previous script, verify that the bootstrap servers you
   provided are reachable on the specified port. To do this, you could download and
   use **telnet** or a similar utility as shown in the
   following command.

```
sudo yum install telnet
telnet `<bootstrap servers>``<port>`
```

If the request is successful, you will get the following output. This
means that you're able to connect to your MSK cluster within your local VPC and
bootstrap servers are healthy on the specified port.

```
Connected to ..
```

10. If the request is unsuccessful, check inbound rules on your VPC [security
    group](../../../AWSEC2/latest/UserGuide/security-group-rules.md "../../../AWSEC2/latest/UserGuide/security-group-rules.md"). As an example, you could use the following properties on the
    inbound rule.

```
Type: All traffic
Port: Port used by the bootstrap server (e.g. 14001)
Source: 0.0.0.0/0
```

Retry the **telnet** connection as shown in
the previous step. If you're still unable to connect or your Firehose connection
is still failing, contact the [AWS support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").
