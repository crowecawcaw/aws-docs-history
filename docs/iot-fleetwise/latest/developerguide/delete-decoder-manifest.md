

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Delete an AWS IoT FleetWise decoder manifest
<a name="delete-decoder-manifest"></a>

You can use the AWS IoT FleetWise console or API to delete a decoder manifest.

**Important**  
Vehicles associated with the decoder manifest must be deleted first. For more information, see [Delete an AWS IoT FleetWise vehicle](delete-vehicle.md).

**Topics**
+ [Delete a decoder manifest (console)](#delete-decoder-manifest-console)
+ [Delete a decoder manifest (AWS CLI)](#delete-decoder-manifest-cli)

## Delete a decoder manifest (console)
<a name="delete-decoder-manifest-console"></a>

You can use the AWS IoT FleetWise console to delete a decoder manifest.

**To delete a decoder manifest**

1. <a name="fleetwise-open-console"></a>Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. <a name="choose-vehicle-models"></a>On the navigation pane, choose **Vehicle models**.

1. Choose the target vehicle model.

1. On the vehicle model summary page, choose the **Decoder manifests** tab.

1. Choose the target decoder manifest, and then choose **Delete**.

1. In **Delete **decoder-manifest-name**?**, enter the name of the decoder manifest to delete, and then choose **Confirm**.

## Delete a decoder manifest (AWS CLI)
<a name="delete-decoder-manifest-cli"></a>

You can use the [DeleteDecoderManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteDecoderManifest.html) API operation to delete a decoder manifest. The following example uses AWS CLI.

**Important**  
Before you delete the decoder manifest, delete the associated vehicles first. For more information, see [Delete an AWS IoT FleetWise vehicle](delete-vehicle.md).

To delete a decoder manifest, run the following command.

Replace {{decoder-manifest-name}} with the name of the decoder manifest that you're deleting.

```
aws iotfleetwise delete-decoder-manifest --name {{decoder-manifest-name}}
```

### Verify decoder manifest deletion
<a name="verify-decoder-deletion"></a>

You can use the [ListDecoderManifests](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifests.html) API operation to verify if a decoder manifest has been deleted. The following example uses AWS CLI.

To retrieve a paginated list of summaries of all decoder manifests, run the following command.

```
aws iotfleetwise list-decoder-manifests
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListDecoderManifests` API operation. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": [
                "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{KMS_KEY_ID}}"
            ]
        }
    ]
}
```

------