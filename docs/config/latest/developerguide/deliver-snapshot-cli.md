

# Delivering Configuration Snapshots to an Amazon S3 Bucket
<a name="deliver-snapshot-cli"></a>

A *configuration snapshot* is a collection of the configuration items for the supported resources that exist in your account. This configuration snapshot is a complete picture of the resources that are being recorded and their configurations. The configuration snapshot can be a useful tool for validating your configuration. For example, you may want to examine the configuration snapshot regularly for resources that are configured incorrectly or that potentially should not exist. The configuration snapshot is available in multiple formats. You can have the configuration snapshot delivered to an Amazon Simple Storage Service (Amazon S3) bucket that you specify. Additionally, you can select a point in time in the AWS Config console and navigate through the snapshot of configuration items using the relationships between the resources.

## Delivering Configuration Snapshots
<a name="deliver-snapshot-cli-procedure"></a>

AWS Config generates configuration snapshots when you invoke the [DeliverConfigSnapshot](https://docs.aws.amazon.com/config/latest/APIReference/API_DeliverConfigSnapshot.html) action or you run the AWS CLI `deliver-config-snapshot` command. AWS Config stores configuration snapshots in the Amazon S3 bucket that you specified when you enabled AWS Config. 

Enter the [`deliver-config-snapshot`](http://docs.aws.amazon.com/cli/latest/reference/configservice/deliver-config-snapshot.html) command by specifying the name assigned by AWS Config when you configured your delivery channel, for example:

```
$ aws configservice deliver-config-snapshot --delivery-channel-name {{default}}
{
    "configSnapshotId": "94ccff53-83be-42d9-996f-b4624b3c1a55"
}
```