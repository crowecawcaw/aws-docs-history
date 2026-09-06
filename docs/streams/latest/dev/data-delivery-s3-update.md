

# Update an Amazon S3 delivery
<a name="data-delivery-s3-update"></a>

 Update an existing Amazon S3 delivery. On an existing delivery, you can change only the data freshness interval (`DataFreshnessInSeconds`) and the CloudWatch Logs configuration. All other properties are immutable after creation. To change any other setting, delete the delivery and create a new one. 

## Using the AWS Management Console
<a name="data-delivery-s3-update-console"></a>

 You edit a delivery from its details page. Choose the tab for the settings you want to change, and then choose **Edit**. 

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis), choose **S3 general purpose delivery**, and then choose the delivery you want to edit.

1. To change the data freshness setting, on the **Configurations** tab, choose **Edit**. Update the editable settings, and then save your changes.

1. To change log delivery or tags, on the **Logs and tags** tab, choose **Edit**. Update log delivery or tags, and then save your changes.

**Note**  
You can also edit or delete a delivery from the list page by selecting the delivery and using the **Actions** menu.

## Using the AWS CLI
<a name="data-delivery-s3-update-cli"></a>

 Use the `update-channel` command to change the data freshness interval. The following command updates a delivery to a data freshness interval of 600 seconds: 

```
aws kinesis update-channel \
    --channel-arn "arn:aws:kinesis:us-east-1:123456789012:channel/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" \
    --s3-destination-configuration '{
        "DataFreshnessInSeconds": 600
    }'
```

 The delivery transitions to UPDATING and then back to ACTIVE after the change is applied. 

 **API reference** – see `UpdateChannel` in the *Amazon Kinesis Data Streams API Reference*. 