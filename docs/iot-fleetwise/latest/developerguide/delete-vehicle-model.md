

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Delete an AWS IoT FleetWise vehicle model
<a name="delete-vehicle-model"></a>

You can use the AWS IoT FleetWise console or API to delete vehicle models.

**Important**  
Vehicles and decoder manifests associated with the vehicle model must be deleted first. For more information, see [Delete an AWS IoT FleetWise vehicle](delete-vehicle.md) and [Delete an AWS IoT FleetWise decoder manifest](delete-decoder-manifest.md).

## Delete a vehicle model (console)
<a name="delete-vehicle-model-console"></a>

To delete a vehicle model, use the AWS IoT FleetWise console.

**To delete a vehicle model**

1. <a name="fleetwise-open-console"></a>Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. <a name="choose-vehicle-models"></a>On the navigation pane, choose **Vehicle models**.

1. On the **Vehicle models** page, choose the target vehicle model.

1. Choose **Delete**.

1. In **Delete **vehicle-model-name**?**, enter the name of the vehicle model to delete, and then choose **Confirm**.

## Delete a vehicle model (AWS CLI)
<a name="delete-vehicle-model-cli"></a>

You can use the [DeleteModelManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteModelManifest.html) API operation to delete an existing vehicle model (model manifests). The following example uses the AWS CLI. 

To delete a vehicle model, run the following command.

Replace {{model-manifest-name}} with the name of the vehicle model that you're deleting.

```
aws iotfleetwise delete-model-manifest --name {{model-manifest-name}}
```

### Verify vehicle model deletion
<a name="verify-model-deletion"></a>

You can use the [ListModelManifests](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListModelManifests.html) API operation to verify if a vehicle model was deleted. The following example uses AWS CLI.

To retrieve a paginated list of summaries of all vehicle models, run the following command.

```
aws iotfleetwise list-model-manifests
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListModelManifests` API operation. 

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