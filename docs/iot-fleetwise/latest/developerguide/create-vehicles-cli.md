

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Create multiple AWS IoT FleetWise vehicles
<a name="create-vehicles-cli"></a>

You can use the [BatchCreateVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_BatchCreateVehicle.html) API operation to create multiple vehicles at one time. The following example uses the AWS CLI.

To create multiple vehicles, run the following command.

Replace {{file-name}} with the name of the .json file that contains the configurations of multiple vehicles.

```
aws iotfleetwise batch-create-vehicle --cli-input-json file://{{file-name}}.json
```

**Example – vehicle configurations**  

```
{
    "vehicles": [
        {
                "associationBehavior": "{{associationBehavior}}",
                "vehicleName": "{{vehicle-name}}", 
                "modelManifestArn": "{{model-manifest-ARN}}",
                "decoderManifestArn": "{{decoder-manifest-ARN}}",           
                "attributes": {
                    "{{key}}": "{{value}}"
                }
        },
        {
                "associationBehavior": "{{associationBehavior}}",
                "vehicleName": "{{vehicle-name}}", 
                "modelManifestArn": "{{model-manifest-ARN}}",
                "decoderManifestArn": "{{decoder-manifest-ARN}}",           
                "attributes": {
                    "{{key}}": "{{value}}"                           
                }
        }
    ]
}
```

You can create up to 10 vehicles for each batch operation. For more information about the vehicle configuration, see [Create an AWS IoT FleetWise vehicle](create-vehicle.md).

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `BatchCreateVehicle` API operation. 

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
                "kms:GenerateDataKey*",
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