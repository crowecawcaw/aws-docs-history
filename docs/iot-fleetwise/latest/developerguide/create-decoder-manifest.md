# Create an AWS IoT FleetWise decoder manifest

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can use the AWS IoT FleetWise console or API to create a decoder manifest for your
vehicle model.

###### Topics

- [Create a decoder manifest
  (console)](#create-decoder-manifest-console "#create-decoder-manifest-console")
- [Create a decoder manifest
  (AWS CLI)](#create-decoder-manifest-cli "#create-decoder-manifest-cli")

## Create a decoder manifest

(console)

You can use the AWS IoT FleetWise console to create a decoder manifest that's
associated with your vehicle model.

###### Important

You can't configure vision system data signals in decoder manifests using the AWS IoT FleetWise
console. Instead, use the AWS CLI. Vision system data is in preview release
and is subject to change.

###### To create a decoder manifest

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
2. On the navigation pane, choose **Vehicle models**.
3. Choose the target vehicle model.
4. On the vehicle model summary page, choose **Create decoder
   manifest**, and then do the following.

###### Topics

- [Step 1: Configure
  decoder manifest](#configure-decoder-manifest-console "#configure-decoder-manifest-console")
- [Step 2: Map CAN
  interface](#map-can-interface "#map-can-interface")
- [Step 3: Review
  and create](#review-and-create-decoder-manifest-console "#review-and-create-decoder-manifest-console")

### Step 1: Configure

decoder manifest

In **General information**, do the following.

1. Enter a unique name for the decoder manifest.
2. (Optional) Enter a description.
3. Choose **Next**.

#### Add network interfaces

Each decoder manifest must have at least one network interface. You can
add multiple network interfaces to a decoder manifest.

###### To add a network interface

1. Upload a network interface file. You can upload a .dbc file for CAN protocols, or a .json file for ROS 2 or custom interfaces.
2. Enter a name for your network interface. If you uploaded a custom interface, the name is already provided.

#### Map missing signals

If there are signals in the vehicle model that are missing paired signal decoders in the uploaded network interfaces, you can create a default custom decoder that will map the missing signals. This is optional since you can manually map the signals in the next step.

###### To create a default custom decoder

1. Select **Create default custom decoder for missing signals**.
2. Choose **Next**.

### Step 2: Map CAN

interface

You can map the CAN signals with CAN signal decoders. If you selected the **Create default custom decoder for missing signals** checkbox, any signals that are missing a decoder signal are automatically mapped to default custom signal decoders.

###### To map CAN signals

1. In **CAN signal mapping**, select a signal decoder.
2. Choose **Next**.

###### Note

If you added a ROS 2 or a custom interface, you can verify the mappings before creating the decoder manifest.

### Step 3: Review

and create

Verify the configurations for the decoder manifest, and then choose
**Create**.

## Create a decoder manifest

(AWS CLI)

You can use the [CreateDecoderManifest](../APIReference/API_CreateDecoderManifest.md "../APIReference/API_CreateDecoderManifest.md") API operation to create decoder manifests.
The following example uses the AWS CLI.

###### Important

You must have a vehicle model before you can create a decoder manifest. Every
decoder manifest must be associated with a vehicle model. For more information,
see [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md "create-vehicle-model.md").

To create a decoder manifest, run the following command.

Replace `decoder-manifest-configuration` with the
name of the .json file that contains the configuration.

```
aws iotfleetwise create-decoder-manifest --cli-input-json file://`decoder-manifest-configuration`.json
```

- Replace `decoder-manifest-name`
  with the name of the decoder manifest that you're
  creating.
- Replace `vehicle-model-ARN` with
  the Amazon Resource Name (ARN) of the vehicle-model.
- (Optional) Replace `description`
  with a description to help you identify the decoder
  manifest.
  For more information about how to configure branches, attributes,
  sensors, and actuators, see [Configure AWS IoT FleetWise
  network interfaces and decoder signals](configure-network-interfaces-decoder-signals.md "configure-network-interfaces-decoder-signals.md").

```
{
    "name": "`decoder-manifest-name`",
    "modelManifestArn": "`vehicle-model-arn`",
    "description": "`description`",
    "networkInterfaces": [
        {
            "canInterface": {
                "name": "myNetworkInterface",
                "protocolName": "CAN",
                "protocolVersion": "2.0b"
            },
            "interfaceId": "Qq1acaenByOB3sSM39SYm",
            "type": "CAN_INTERFACE"
        }
    ],
    "signalDecoders": [
        {
            "canSignal": {
                "name": "Engine_Idle_Time",
                "factor": 1,
                "isBigEndian": true,
                "isSigned": false,
                "length": 24,
                "messageId": 271343712,
                "offset": 0,
                "startBit": 16
            },
            "fullyQualifiedName": "Vehicle.EngineIdleTime",
            "interfaceId": "Qq1acaenByOB3sSM39SYm",
            "type": "CAN_SIGNAL"
        },
        {
            "canSignal": {
                "name": "Engine_Run_Time",
                "factor": 1,
                "isBigEndian": true,
                "isSigned": false,
                "length": 24,
                "messageId": 271343712,
                "offset": 0,
                "startBit": 40
            },
            "fullyQualifiedName": "Vehicle.EngineRunTime",
            "interfaceId": "Qq1acaenByOB3sSM39SYm",
            "type": "CAN_SIGNAL"
        }
    ]
}
```

- Replace `decoder-manifest-name`
  with the name of the decoder manifest that you're
  creating.
- Replace `vehicle-model-ARN` with
  the Amazon Resource Name (ARN) of the vehicle-model.
- (Optional) Replace `description`
  with a description to help you identify the decoder
  manifest.
  The order of property nodes within a structure (struct) must
  remain consistent as defined in the signal catalog and vehicle model
  (model manifest). For more information about how to configure
  branches, attributes, sensors, and actuators, see [Configure AWS IoT FleetWise
  network interfaces and decoder signals](configure-network-interfaces-decoder-signals.md "configure-network-interfaces-decoder-signals.md").

```
{
	"name": "`decoder-manifest-name`",
	"modelManifestArn": "`vehicle-model-arn`",
	"description": "`description`",
	"networkInterfaces": [{
		"canInterface": {
			"name": "myNetworkInterface",
			"protocolName": "CAN",
			"protocolVersion": "2.0b"
		},
		"interfaceId": "Qq1acaenByOB3sSM39SYm",
		"type": "CAN_INTERFACE"
	}, {
		"type": "VEHICLE_MIDDLEWARE",
		"interfaceId": "G1KzxkdnmV5Hn7wkV3ZL9",
		"vehicleMiddleware": {
			"name": "ROS2_test",
			"protocolName": "ROS_2"
		}
	}],
	"signalDecoders": [{
			"canSignal": {
				"name": "Engine_Idle_Time",
				"factor": 1,
				"isBigEndian": true,
				"isSigned": false,
				"length": 24,
				"messageId": 271343712,
				"offset": 0,
				"startBit": 16
			},
			"fullyQualifiedName": "Vehicle.EngineIdleTime",
			"interfaceId": "Qq1acaenByOB3sSM39SYm",
			"type": "CAN_SIGNAL"
		},
		{
			"canSignal": {
				"name": "Engine_Run_Time",
				"factor": 1,
				"isBigEndian": true,
				"isSigned": false,
				"length": 24,
				"messageId": 271343712,
				"offset": 0,
				"startBit": 40
			},
			"fullyQualifiedName": "Vehicle.EngineRunTime",
			"interfaceId": "Qq1acaenByOB3sSM39SYm",
			"type": "CAN_SIGNAL"
		},
		{
			"fullyQualifiedName": "Vehicle.CompressedImageTopic",
			"type": "MESSAGE_SIGNAL",
			"interfaceId": "G1KzxkdnmV5Hn7wkV3ZL9",
			"messageSignal": {
				"topicName": "CompressedImageTopic:sensor_msgs/msg/CompressedImage",
				"structuredMessage": {
					"structuredMessageDefinition": [{
							"fieldName": "header",
							"dataType": {
								"structuredMessageDefinition": [{
										"fieldName": "stamp",
										"dataType": {
											"structuredMessageDefinition": [{
													"fieldName": "sec",
													"dataType": {
														"primitiveMessageDefinition": {
															"ros2PrimitiveMessageDefinition": {
																"primitiveType": "INT32"
															}
														}
													}
												},
												{
													"fieldName": "nanosec",
													"dataType": {
														"primitiveMessageDefinition": {
															"ros2PrimitiveMessageDefinition": {
																"primitiveType": "UINT32"
															}
														}
													}
												}
											]
										}
									},
									{
										"fieldName": "frame_id",
										"dataType": {
											"primitiveMessageDefinition": {
												"ros2PrimitiveMessageDefinition": {
													"primitiveType": "STRING"
												}
											}
										}
									}
								]
							}
						},
						{
							"fieldName": "format",
							"dataType": {
								"primitiveMessageDefinition": {
									"ros2PrimitiveMessageDefinition": {
										"primitiveType": "STRING"
									}
								}
							}
						},
						{
							"fieldName": "data",
							"dataType": {
								"structuredMessageListDefinition": {
									"name": "listType",
									"memberType": {
										"primitiveMessageDefinition": {
											"ros2PrimitiveMessageDefinition": {
												"primitiveType": "UINT8"
											}
										}
									},
									"capacity": 0,
									"listType": "DYNAMIC_UNBOUNDED_CAPACITY"
								}
							}
						}
					]
				}
			}
		}
	]
}
```

- Replace `decoder-manifest-name`
  with the name of the decoder manifest that you're
  creating.
- Replace `vehicle-model-ARN` with
  the Amazon Resource Name (ARN) of the vehicle-model.
- (Optional) Replace `description`
  with a description to help you identify the decoder
  manifest.
  For more information about how to configure branches, attributes,
  sensors, and actuators, see [Configure AWS IoT FleetWise
  network interfaces and decoder signals](configure-network-interfaces-decoder-signals.md "configure-network-interfaces-decoder-signals.md").

```
{
	"name": "`decoder-manifest-name`",
	"modelManifestArn": "`vehicle-model-arn`",
	"description": "`description`",
	"networkInterfaces": [
        {
		    "interfaceId": "`myCustomInterfaceId`",
		    "type": "CUSTOM_DECODING_INTERFACE",
            "customDecodingInterface": {
                "name": "`myCustomInterface`"
            }
        }
    ],
    "signalDecoders": [
        {
            "customDecodingSignal": {
                "fullyQualifiedName": "`Vehicle.actuator1`",
                "interfaceId": "`myCustomInterfaceId`",
                "type": "CUSTOM_DECODING_SIGNAL",
                "customDecodingSignal": {
                    "id": "`Vehicle.actuator1`"
                }
            }
        },
        {
            "customDecodingSignal": {
                "fullyQualifiedName": "`Vehicle.actuator2`",
                "interfaceId": "`myCustomInterfaceId`",
                "type": "CUSTOM_DECODING_SIGNAL",
                "customDecodingSignal": {
                    "id": "`Vehicle.actuator2`"
                }
            }
        }
    ]
}
```

###### Note

You can download a [demo script](https://raw.githubusercontent.com/aws/aws-iot-fleetwise-edge/main/tools/cloud/ros2-to-decoders.py "https://raw.githubusercontent.com/aws/aws-iot-fleetwise-edge/main/tools/cloud/ros2-to-decoders.py") to create a decoder manifest with vision system
signals. For more information, see the [_Vision System Data Developer
Guide_](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/vision-system-data/vision-system-data-demo.ipynb "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/vision-system-data/vision-system-data-demo.ipynb").

Vision system data is in preview release and is subject to change.

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `CreateDecoderManifest` API operation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS_KEY_ID`"
 ]
 }
 ]
}`

```
