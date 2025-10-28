# Provision storage throughput for Standard brokers in a Amazon MSK cluster

Amazon MSK brokers persist data on storage volumes. Storage I/O is consumed when producers
write to the cluster, when data is replicated between brokers, and when consumers read
data that isn't in memory. The volume storage throughput is the rate at which data can
be written into and read from a storage volume. Provisioned storage throughput is the
ability to specify that rate for the brokers in your cluster.

You can specify the provisioned throughput rate in MiB per second for clusters whose
brokers are of size `kafka.m5.4xlarge` or larger and if the storage
volume is 10 GiB or greater. It is possible to specify provisioned throughput during
cluster creation. You can also enable or disable provisioned throughput for a
cluster that is in the `ACTIVE` state.

For information about managing throughput, see [Manage storage throughput for Standard brokers in a Amazon MSK cluster](msk-provision-throughput-management.md "msk-provision-throughput-management.md").

###### Topics

- [Provision Amazon MSK cluster storage throughput using the AWS Management Console](#provisioned-throughput-console "#provisioned-throughput-console")
- [Provision Amazon MSK cluster storage throughput using the AWS CLI](#provisioned-throughput-cli "#provisioned-throughput-cli")
- [Provision storage throughput when creating a Amazon MSK cluster using the API](#provisioned-throughput-api "#provisioned-throughput-api")

## Provision Amazon MSK cluster storage throughput using the AWS Management Console

This process shows an example of how you can use the AWS Management Console to create a Amazon MSK cluster with provisioned throughput enabled.

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. Choose **Create cluster**.
3. Choose **Custom create**.
4. Specify a name for the cluster.
5. In the **Storage** section, choose **Enable**.
6. Choose a value for storage throughput per broker.
7. Choose a VPC, zones and subnets, and a security group.
8. Choose **Next**.
9. At the bottom of the **Security** step, choose **Next**.
10. At the bottom of the **Monitoring and tags** step, choose **Next**.
11. Review the cluster settings, then choose **Create cluster**.

## Provision Amazon MSK cluster storage throughput using the AWS CLI

This process shows an example of how you can use the AWS CLI to create a cluster with provisioned throughput enabled.

1. Copy the following JSON and paste it into a file. Replace the subnet IDs and security group ID
   placeholders with values from your account. Name the file
   `cluster-creation.json` and save it.

```
{
    "Provisioned": {
        "BrokerNodeGroupInfo":{
            "InstanceType":"kafka.m5.4xlarge",
            "ClientSubnets":[
                "`Subnet-1-ID`",
                "`Subnet-2-ID`"
            ],
            "SecurityGroups":[
                "`Security-Group-ID`"
            ],
            "StorageInfo": {
                "EbsStorageInfo": {
                    "VolumeSize": 10,
                    "ProvisionedThroughput": {
                        "Enabled": true,
                        "VolumeThroughput": 250
                    }
                }
            }
        },
        "EncryptionInfo": {
            "EncryptionInTransit": {
                "InCluster": false,
                "ClientBroker": "PLAINTEXT"
            }
        },
        "KafkaVersion":"2.8.1",
        "NumberOfBrokerNodes": 2
    },
    "ClusterName": "provisioned-throughput-example"
}
```

2. Run the following AWS CLI command from the directory where you saved the JSON file in the previous step.

```
aws kafka create-cluster-v2 --cli-input-json file://cluster-creation.json
```

## Provision storage throughput when creating a Amazon MSK cluster using the API

To configure provisioned storage throughput while creating a cluster, use [CreateClusterV2](../../../MSK/2.0/APIReference/v2-clusters.md#CreateClusterV2 "../../../MSK/2.0/APIReference/v2-clusters.md#CreateClusterV2").
