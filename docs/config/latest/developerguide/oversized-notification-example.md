# Example Oversized Configuration Item

Change Notification

When AWS Config detects a configuration change for a resource, it sends a configuration item (CI)
notification. If the notification exceeds the maximum size allowed by Amazon Simple Notification Service (Amazon SNS),
the notification includes a brief summary of the configuration item.

You can view the
complete notification in the Amazon S3 bucket location specified in the
`s3BucketLocation` field.

The following example notification shows a CI for an Amazon EC2 instance.
The notification includes a summary of the changes and the location of the notification
in the Amazon S3 bucket.

```
View the Timeline for this Resource in the Console:
    https://console.aws.amazon.com/config/home?region=us-west-2#/timeline/AWS::EC2::Instance/resourceId_14b76876-7969-4097-ab8e-a31942b02e80?time=2016-10-06T16:46:16.261Z

    The full configuration item change notification for this resource exceeded the maximum size allowed by Amazon Simple Notification Service (SNS). A summary of the configuration item is provided here. You can view the complete notification in the specified Amazon S3 bucket location.

    New State Record Summary:
    ----------------------------
    {
      "configurationItemSummary": {
        "changeType": "UPDATE",
        "configurationItemVersion": "1.2",
        "configurationItemCaptureTime": "2016-10-06T16:46:16.261Z",
        "configurationStateId": 0,
        "awsAccountId": "123456789012",
        "configurationItemStatus": "OK",
        "resourceType": "AWS::EC2::Instance",
        "resourceId": "resourceId_14b76876-7969-4097-ab8e-a31942b02e80",
        "resourceName": null,
        "ARN": "arn:aws:ec2:us-west-2:123456789012:instance/resourceId_14b76876-7969-4097-ab8e-a31942b02e80",
        "awsRegion": "us-west-2",
        "availabilityZone": null,
        "configurationStateMd5Hash": "8f1ee69b287895a0f8bc5753eca68e96",
        "resourceCreationTime": "2016-10-06T16:46:10.489Z"
      },
      "s3DeliverySummary": {
        "s3BucketLocation": "amzn-s3-demo-bucket/AWSLogs/123456789012/Config/us-west-2/2016/10/6/OversizedChangeNotification/AWS::EC2::Instance/resourceId_14b76876-7969-4097-ab8e-a31942b02e80/123456789012_Config_us-west-2_ChangeNotification_AWS::EC2::Instance_resourceId_14b76876-7969-4097-ab8e-a31942b02e80_20161006T164616Z_0.json.gz",
        "errorCode": null,
        "errorMessage": null
      },
      "notificationCreationTime": "2016-10-06T16:46:16.261Z",
      "messageType": "OversizedConfigurationItemChangeNotification",
      "recordVersion": "1.0"
    }

```

## How to access oversized configuration items

When a configuration item is oversized, only a summary is sent to Amazon SNS. The complete configuration item (CI) is stored in Amazon S3

The following code example shows how to access the the complete CI.

```
import boto3
import json

def handle_oversized_configuration_item(event):
    """
    Example of handling an oversized configuration item notification

    When a configuration item is oversized:
    1. AWS Config sends a summary notification through SNS
    2. The complete configuration item is stored in S3
    3. Use get_resource_config_history API to retrieve the complete configuration
    """

    # Extract information from the summary notification
    if event['messageType'] == 'OversizedConfigurationItemChangeNotification':
        summary = event['configurationItemSummary']
        resource_type = summary['resourceType']
        resource_id = summary['resourceId']

        # Initialize AWS Config client
        config_client = boto3.client('config')

        # Retrieve the complete configuration item
        response = config_client.get_resource_config_history(
            resourceType=resource_type,
            resourceId=resource_id
        )

        if response['configurationItems']:
            config_item = response['configurationItems'][0]

            # For EC2 instances, the configuration contains instance details
            configuration = json.loads(config_item['configuration'])
            print(f"Instance Configuration: {configuration}")

            # Handle supplementary configuration if present
            if 'supplementaryConfiguration' in config_item:
                for key, value in config_item['supplementaryConfiguration'].items():
                    if isinstance(value, str):
                        config_item['supplementaryConfiguration'][key] = json.loads(value)
                print(f"Supplementary Configuration: {config_item['supplementaryConfiguration']}")

            return config_item

        # If needed, you can also access the complete notification from S3
        s3_location = event['s3DeliverySummary']['s3BucketLocation']
        print(f"Complete notification available in S3: {s3_location}")

    return None
```

## How it works

1. The function accepts an event parameter containing the AWS Config notification.
2. It checks if the message type is an oversized configuration notification.
3. The function extracts the resource type and ID from the summary.
4. Using the AWS Config client, it retrieves the complete configuration history.
5. The function processes both main and supplementary configurations.
6. If needed, you can access the complete notification from the provided S3 location.
