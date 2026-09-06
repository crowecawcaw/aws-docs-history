

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Shield Advanced attack flow logs
<a name="ddos-flow-logs"></a>

Flow logs enable you to capture information about traffic going to network interfaces in your Shield Advanced protected resources. Flow log data is published to Amazon S3, Amazon CloudWatch Logs, or Amazon Data Firehose, where you can retrieve and view your data after you've enabled flow logs.

**Note**  
You must view CloudWatch metrics and logs for Shield Advanced protected resources in the US East (N. Virginia) Region. This applies to both the console and the AWS CLI. When you use the AWS CLI, include the following parameter: `--region us-east-1`

**Note**  
CloudWatch Logs charges apply when you use flow logs, even when logs are published directly to Amazon S3. For more information, see Vended Logs under the Logs tab at [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Enable publishing flow logs to Amazon S3
<a name="ddos-flow-logs-enable"></a>

To publish flow logs to Amazon S3, you must configure IAM permissions for the log delivery actions and for the Shield service.

### IAM permissions for publishing flow logs
<a name="ddos-flow-logs-iam-permissions"></a>

An IAM principal, such as an IAM role or user, must have sufficient permissions to publish flow logs to the Amazon S3 bucket. The IAM policy must include the following permissions:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ReadWriteAccessForLogDeliveryActions",
            "Effect": "Allow",
            "Action": [
                "logs:GetDelivery",
                "logs:GetDeliverySource",
                "logs:PutDeliveryDestination",
                "logs:GetDeliveryDestinationPolicy",
                "logs:DeleteDeliverySource",
                "logs:PutDeliveryDestinationPolicy",
                "logs:CreateDelivery",
                "logs:GetDeliveryDestination",
                "logs:PutDeliverySource",
                "logs:DeleteDeliveryDestination",
                "logs:DeleteDeliveryDestinationPolicy",
                "logs:DeleteDelivery",
                "logs:UpdateDeliveryConfiguration"
            ],
            "Resource": [
                "arn:aws:logs:us-east-1:{{accountID}}:delivery:*",
                "arn:aws:logs:us-east-1:{{accountID}}:delivery-source:*",
                "arn:aws:logs:us-east-1:{{accountID}}:delivery-destination:*"
            ]
        },
        {
            "Sid": "ListAccessForLogDeliveryActions",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeDeliveryDestinations",
                "logs:DescribeDeliverySources",
                "logs:DescribeDeliveries",
                "logs:DescribeConfigurationTemplates"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowUpdatesToResourcePolicyS3",
            "Effect": "Allow",
            "Action": [
                "s3:PutBucketPolicy",
                "s3:GetBucketPolicy"
            ],
            "Resource": "arn:aws:s3:::{{bucket-name}}"
        }
    ]
}
```

In the preceding policy, replace {{accountID}} with your AWS account ID and {{bucket-name}} with the name of your Amazon S3 bucket.

### Shield service-specific permissions
<a name="ddos-flow-logs-shield-permissions"></a>

In addition to the destination-specific permissions, AWS Shield requires explicit authorization that you can send logs from your resources. This provides an additional layer of security. Shield authorizes the `AllowVendedLogDeliveryForResource` action for protection resources that vend logs:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ServiceLevelAccessForLogDelivery",
            "Effect": "Allow",
            "Action": [
                "shield:AllowVendedLogDeliveryForResource"
            ],
            "Resource": "arn:aws:shield::{{accountID}}:protection/*"
        }
    ]
}
```

Replace {{accountID}} with your AWS account ID.

## To enable flow log delivery
<a name="ddos-flow-logs-delivery"></a>

A working log delivery consists of three elements. Use the following procedure to configure each element using the AWS CLI.

1. Create a `DeliverySource`, which is a logical object that represents the resources that send the logs. Run the following command:

   ```
   aws logs put-delivery-source \
     --name {{delivery-source-name}} \
     --resource-arn "arn:aws:shield::{{accountID}}:protection/{{protectionID}}" \
     --log-type FLOW_LOGS \
     --region us-east-1
   ```

   Replace {{delivery-source-name}} with a name for your delivery source, {{accountID}} with your AWS account ID, and {{protectionID}} with your Shield Advanced protection ID.

   Ensure that the user issuing this command has the service-level permission `shield:AllowVendedLogDeliveryForResource`.

1. Create a `DeliveryDestination`, which is a logical object that represents the actual delivery destination. Run the following command:

   ```
   aws logs put-delivery-destination \
     --name {{delivery-destination-name}} \
     --output-format json \
     --delivery-destination-configuration "destinationResourceArn=arn:aws:s3:::{{bucket-name}}" \
     --region us-east-1
   ```

   Replace {{delivery-destination-name}} with a name for your delivery destination and {{bucket-name}} with the name of your Amazon S3 bucket.

1. Create a `Delivery`, which connects a delivery source to a delivery destination. Run the following command:

   ```
   aws logs create-delivery \
     --delivery-source-name {{delivery-source-name-from-step1}} \
     --delivery-destination-arn "{{arn-returned-in-step2}}" \
     --region us-east-1
   ```

   Replace {{delivery-source-name-from-step1}} with the delivery source name from step 1, and {{arn-returned-in-step2}} with the ARN returned in step 2.

## Flow log files
<a name="ddos-flow-logs-files"></a>

Flow logs from your Shield protection are published to an Amazon S3 bucket at 5-minute intervals during an attack. Log files are written every five minutes, and each log file contains flow log records for the IP address traffic recorded in the previous five minutes.

The maximum file size for a log file is 75 MB. If the log file reaches this limit within the 5-minute period, the flow log stops adding records to it. The flow log then publishes the file to the Amazon S3 bucket and creates a new log file.

Log files are compressed. If you open the files using the Amazon S3 console, Amazon S3 decompresses the log records and displays them. If you download the log files, you must decompress them to view the records.

A single log file contains interleaved entries with multiple records. To see all the log files for a protection, look for entries aggregated by the protection name, Region, and your account ID.

## Flow log record syntax
<a name="ddos-flow-logs-record-syntax"></a>

A flow log record is a space-separated string with the following fields.


| Field | Description | 
| --- | --- | 
| version | Flow log version number. | 
| protection\_arn | AWS protection ARN that identifies the resource protected in Shield Advanced. | 
| srcaddr | Source IP address of the packet. | 
| dstaddr | Destination IP address of the packet. | 
| srcport | Source port of the packet. | 
| dstport | Destination port of the packet. | 
| protocol | Protocol of the packet. | 
| packets | Number of packets within the aggregation window. | 
| bytes | Number of bytes within the aggregation window. | 
| starttime | Aggregation window start time. | 
| endtime | Aggregation window end time. | 
| action | Action taken by Shield Advanced. | 
| tcp\_flags | TCP flags field from the packet. | 
| sampling\_rate | Sampling rate used during packet processing. | 
| location | AWS ingress location. | 
| srccountry | Two-letter country code representing the country of ingress traffic. | 