End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Calling AWS services from your application code

You can use the AWS SDK for Python (Boto) to call AWS services from your application code. For example, if your model detects
something out of the ordinary, you could post metrics to Amazon CloudWatch, send an notification with Amazon SNS, save an image to
Amazon S3, or invoke a Lambda function for further processing. Most AWS services have a public API that you can use with
the AWS SDK.

The appliance does not have permission to access any AWS services by default. To grant it permission, [create a role for the application](permissions-application.md "permissions-application.md"), and assign it to the application
instance during deployment.

###### Sections

- [Using Amazon S3](#applications-awssdk-s3 "#applications-awssdk-s3")
- [Using the AWS IoT MQTT topic](#monitoring-messagestream "#monitoring-messagestream")

## Using Amazon S3

You can use Amazon S3 to store processing results and other application data.

```
import boto3
s3_client=boto3.client("s3")
s3_clients3.upload_file(data_file,
                    s3_bucket_name,
                    os.path.basename(data_file))
```

## Using the AWS IoT MQTT topic

You can use the SDK for Python (Boto3) to send messages to an [MQTT topic](../../../iot/latest/developerguide/topics.md "../../../iot/latest/developerguide/topics.md") in
AWS IoT. In the following example, the application posts to a topic named after the appliance's _thing
name_, which you can find in [AWS IoT
console](https://console.aws.amazon.com/iot/home#/thinghub "https://console.aws.amazon.com/iot/home#/thinghub").

```
import boto3
iot_client=boto3.client('iot-data')
topic = "panorama/`panorama_my-appliance_Thing_a01e373b`"
iot_client.publish(topic=topic, payload="my message")
```

Choose a name that indicates the device ID or other identifier of your choice. To publish messages, the
application needs permission to call `iot:Publish`.

###### To monitor an MQTT queue

1. Open the [AWS IoT console Test
   page](https://console.aws.amazon.com/iot/home?region=us-east-1#/test "https://console.aws.amazon.com/iot/home?region=us-east-1#/test").
2. For **Subscription topic**, enter the name of the topic. For example,
   `panorama/panorama_my-appliance_Thing_a01e373b`.
3. Choose **Subscribe to topic**.
