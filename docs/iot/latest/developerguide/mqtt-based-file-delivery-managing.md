

# Managing a stream in the AWS Cloud
<a name="mqtt-based-file-delivery-managing"></a>

AWS IoT provides AWS SDK and AWS CLI commands that you can use to manage a stream in the AWS Cloud. You can use these commands to do the following:
+ Create a stream. [CLI](https://docs.aws.amazon.com/cli/latest/reference/iot/create-stream.html) / [SDK](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateStream.html)
+ Describe a stream to get its information. [CLI](https://docs.aws.amazon.com/cli/latest/reference/iot/describe-stream.html) / [SDK](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeStream.html)
+ List streams in your AWS account. [CLI](https://docs.aws.amazon.com/cli/latest/reference/iot/list-streams.html) / [SDK](https://docs.aws.amazon.com/iot/latest/apireference/API_ListStreams.html)
+ Update the file list or stream description in a stream. [CLI](https://docs.aws.amazon.com/cli/latest/reference/iot/update-stream.html) / [SDK](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateStream.html)
+ Delete a stream. [CLI](https://docs.aws.amazon.com/cli/latest/reference/iot/delete-stream.html) / [SDK](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteStream.html)

**Note**  
At this time, streams are not visible in the AWS Management Console. You must use the AWS CLI or AWS SDK to manage a stream in AWS IoT. Also, [Embedded C SDK](https://github.com/aws/aws-iot-device-sdk-embedded-C) is the only SDK that supports MQTT-based file transfers.

Before you use AWS IoT MQTT-based file delivery from your devices, you must ensure the following conditions are met for your devices as shown in the next sections:
+ A policy reflecting the correct permissions required for transmitting data via MQTT.
+ Your device can connect to the AWS IoT Device Gateway.
+ A policy statement stating you can tag resources. If `CreateStream` is called with tags, then `iot:TagResource` is required.

Before you use AWS IoT MQTT-based file delivery from your devices, you must follow the steps in the next sections to make sure that your devices are properly authorized and can connect to the AWS IoT Device Gateway. 

## Grant permissions to your devices
<a name="mqtt-based-file-delivery-permissions"></a>

You can follow the steps in [Create an AWS IoT policy](https://docs.aws.amazon.com/iot/latest/developerguide/create-iot-resources.html#create-iot-policy) to create a device policy or use an existing device policy. Attach the policy to the certificates associated with your devices and add the following permissions to the device policy.

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iot:Connect"
            ],
            "Resource": [
            "arn:aws:iot:{{us-east-1}}:{{123456789012}}:client/${iot:Connection.Thing.ThingName}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iot:Receive",
                "iot:Publish"
            ],
            "Resource": [
            "arn:aws:iot:{{us-east-1}}:{{123456789012}}:topic/$aws/things/${iot:Connection.Thing.ThingName}/streams/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "iot:Subscribe",
            "Resource": [
            "arn:aws:iot:{{us-east-1}}:{{123456789012}}:topicfilter/$aws/things/${iot:Connection.Thing.ThingName}/streams/*"
            ]
        }
    ]
}
```

## Connect your devices to AWS IoT
<a name="mqtt-based-file-delivery-connect-devices"></a>

Devices that use AWS IoT MQTT-based file delivery are required to connect with AWS IoT. AWS IoT MQTT-based file delivery integrates with AWS IoT in the AWS Cloud, so your devices should directly connect to [the endpoint of the AWS IoT Data Plane](https://docs.aws.amazon.com/iot/latest/apireference/Welcome.html#Welcome_AWS_IoT_Data_Plane). 

**Note**  
The endpoint of the AWS IoT data plane is specific to the AWS account and Region. You must use the endpoint for the AWS account and the Region in which your devices are registered in AWS IoT.

See [Connect to AWS IoT Core](connect-to-iot.md) for more information.

## TagResource Usage
<a name="mqtt-based-file-delivery-tag-resource"></a>

The `CreateStream` API action creates a stream for delivering one or more large files in chunks over MQTT.

A successful `CreateStream` API call requires the following permissions:
+ `iot:CreateStream`
+ `iot:TagResource` (if `CreateStream` is with tags)

The policy supporting those two permissions is shown below:

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": {
        "Action": [
            "iot:CreateStream",
            "iot:TagResource"
        ],
        "Effect": "Allow",
        "Resource": "arn:aws:iot:us-east-1:{{123456789012}}:stream/streamId"
    }
}
```

The `iot:TagResource` policy statement action is required to ensure a user can't create or update a tag on a resource without the proper permissions. Without the specifc policy statement action of `iot:TagResource`, the `CreateStream` API call will return an `AccessDeniedException` if the request comes with tags.

For more information, refer to the following links:
+ [CreateStream](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateStream.html)
+ [TagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_TagResource.html)
+ [Tag](https://docs.aws.amazon.com/iot/latest/apireference/API_Tag.html)