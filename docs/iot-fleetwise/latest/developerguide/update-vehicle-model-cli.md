

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Update an AWS IoT FleetWise vehicle model
<a name="update-vehicle-model-cli"></a>

You can use the [UpdateModelManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateModelManifest.html) API operation to update an existing vehicle model (model manifests). The following example uses the AWS CLI. 

To update an existing vehicle model, run the following command.

Replace {{update-vehicle-model-configuration}} with the name of the .json file that contains the configuration.

```
aws iotfleetwise update-model-manifest --cli-input-json file://{{update-vehicle-model-configuration}}.json
```

## Update vehicle model configuration
<a name="update-vehicle-model-configuration"></a>
+ Replace {{vehicle-model-name}} with the name of the vehicle model that you're updating.
+ (Optional) To activate the vehicle model, replace {{vehicle-model-status}} with `ACTIVE`. 
**Important**  
After the vehicle model is activated, you can't change the vehicle model.
+ (Optional) Replace {{description}} with an updated description to help you identify the vehicle model.

```
{
    "name": "{{vehicle-model-name}}",
    "status": "{{vehicle-model-status}}",                        
    "description": "{{description}}",
    "nodesToAdd": ["Vehicle.Front.Left"],
    "nodesToRemove": ["Vehicle.Chassis.SteeringWheel"],   
}
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `UpdateModelManifest` API operation. 

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

## Verify vehicle model update
<a name="verify-model-update"></a>

You can use the [ListModelManifestNodes](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListModelManifestNodes.html) API operation to verify if a vehicle model was updated. The following example uses AWS CLI.

To retrieve a paginated list of summaries of all signals (nodes) in a given vehicle model, run the following command.

Replace {{vehicle-model-name}} with the name of the vehicle model that you're checking.

```
aws iotfleetwise list-model-manifest-nodes /
                 --name {{vehicle-model-name}}
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListModelManifestNodes` API operation. 

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