# Import an AWS IoT FleetWise signal catalog

You can use the AWS IoT FleetWise console or API to import a signal catalog.

###### Topics

- [Import a signal catalog
  (console)](#import-signal-catalog-console "#import-signal-catalog-console")
- [Import a signal catalog (AWS CLI)](#import-signal-catalog "#import-signal-catalog")

## Import a signal catalog

(console)

You can use the AWS IoT FleetWise console to import a signal catalog.

###### Important

You can have a maximum of one signal catalog. If you already have a signal
catalog, you won't see the option to import a signal catalog in the
console.

###### To import a signal catalog

1. Open the [AWS IoT FleetWise
   console](https://console.aws.amazon.com/iotfleetwise/ "https://console.aws.amazon.com/iotfleetwise/").
2. On the navigation pane, choose **Signal
   catalog**.
3. On the signal catalog summary page, choose **Import signal
   catalog**.
4. Import the file containing the signals.
   - To upload a file from an S3 bucket:
     1. Choose **Import from S3**.
     2. Choose **Browse S3**.
     3. For **Buckets**, enter the bucket
        name or object, choose it from the list, and then choose
        the file from the list. Choose the **Choose
        file** button.Or, for **S3 URI**, enter an Amazon Simple
        Storage Service URI. For more information, see [Methods for accessing a bucket](../../../AmazonS3/latest/userguide/access-bucket-intro.md "../../../AmazonS3/latest/userguide/access-bucket-intro.md") in the
        _Amazon S3 User Guide_.

   - To upload a file from your computer:
     1. Choose **Import from file**.
     2. Upload a .json file in a [Vehicle Signal Specification (VSS)](<https://www.w3.org/auto/wg/wiki/Vehicle_Signal_Specification_(VSS)/Vehicle_Data_Spec> "https://www.w3.org/auto/wg/wiki/Vehicle_Signal_Specification_(VSS)/Vehicle_Data_Spec")
        format.

5. Verify the signal catalog, and then choose **Import
   file**.

## Import a signal catalog (AWS CLI)

You can use the [ImportSignalCatalog](../APIReference/API_ImportSignalCatalog.md "../APIReference/API_ImportSignalCatalog.md") API operation to upload a JSON file that helps
create a signal catalog. You must follow the [Vehicle Signal Specification (VSS)](<https://www.w3.org/auto/wg/wiki/Vehicle_Signal_Specification_(VSS)/Vehicle_Data_Spec> "https://www.w3.org/auto/wg/wiki/Vehicle_Signal_Specification_(VSS)/Vehicle_Data_Spec") to save signals in the JSON
file. The following example uses AWS CLI.

To import a signal catalog, run the following command.

- Replace `signal-catalog-name` with the name
  of the signal catalog that you're creating.
- (Optional) Replace description with a
  `description` to help you identify the
  signal catalog.
- Replace `signal-catalog-configuration-vss`
  with the name of the JSON string file that contains signals defined in
  VSS.

For more information about how to configure branches, attributes, sensors, and
actuators, see [Configure AWS IoT FleetWise signals](define-signal.md "define-signal.md").

```
aws iotfleetwise import-signal-catalog \
                 --name `signal-catalog-name` \
                 --description  `description` \
                 --vss file://`signal-catalog-configuration-vss`.json
```

The JSON must be stringified and passed through the
`vssJson` field. The following is an example of
signals defined in VSS.

```
{
	"Vehicle": {
		"type": "branch",
		"children": {
			"Chassis": {
				"type": "branch",
				"description": "All data concerning steering, suspension, wheels, and brakes.",
				"children": {
					"SteeringWheel": {
						"type": "branch",
						"description": "Steering wheel signals",
						"children": {
							"Diameter": {
								"type": "attribute",
								"description": "The diameter of the steering wheel",
								"datatype": "float",
								"unit": "cm",
								"min": 1,
								"max": 50
							},
							"HandsOff": {
								"type": "branch",
								"children": {
									"HandsOffSteeringState": {
										"type": "actuator",
										"description": "HndsOffStrWhlDtSt. Hands Off Steering State",
										"datatype": "boolean"
									},
									"HandsOffSteeringMode": {
										"type": "actuator",
										"description": "HndsOffStrWhlDtMd. Hands Off Steering Mode",
										"datatype": "int8",
										"min": 0,
										"max": 2
									}
								}
							}
						}
					},
					"Accelerator": {
						"type": "branch",
						"description": "",
						"children": {
							"AcceleratorPedalPosition": {
								"type": "sensor",
								"description": "Throttle__Position. Accelerator pedal position as percent. 0 = Not depressed. 100 = Fully depressed.",
								"datatype": "uint8",
								"unit": "%",
								"min": 0,
								"max": 100.000035
							}
						}
					}
				}
			},
			"Powertrain": {
				"type": "branch",
				"description": "Powertrain data for battery management, etc.",
				"children": {
					"Transmission": {
						"type": "branch",
						"description": "Transmission-specific data, stopping at the drive shafts.",
						"children": {
							"VehicleOdometer": {
								"type": "sensor",
								"description": "Vehicle_Odometer",
								"datatype": "float",
								"unit": "km",
								"min": 0,
								"max": 67108863.984375
							}
						}
					},
					"CombustionEngine": {
						"type": "branch",
						"description": "Engine-specific data, stopping at the bell housing.",
						"children": {
							"Engine": {
								"type": "branch",
								"description": "Engine description",
								"children": {
									"timing": {
										"type": "branch",
										"description": "timing description",
										"children": {
											"run_time": {
												"type": "sensor",
												"description": "Engine run time",
												"datatype": "int16",
												"unit": "ms",
												"min": 0,
												"max": 10000
											},
											"idle_time": {
												"type": "sensor",
												"description": "Engine idle time",
												"datatype": "int16",
												"min": 0,
												"unit": "ms",
												"max": 10000
											}
										}
									}
								}
							}
						}
					}
				}
			},
			"Axle": {
				"type": "branch",
				"description": "Axle signals",
				"children": {
					"TireRRPrs": {
						"type": "sensor",
						"description": "TireRRPrs. Right rear Tire pressure in kilo-Pascal",
						"datatype": "float",
						"unit": "kPaG",
						"min": 0,
						"max": 1020
					}
				}
			}
		}
	},
	"Cameras": {
		"type": "branch",
		"description": "Branch to aggregate all cameras in the vehicle",
		"children": {
			"FrontViewCamera": {
				"type": "sensor",
				"datatype": "VehicleDataTypes.SVMCamera",
				"description": "Front view camera"
			},
			"RearViewCamera": {
				"type": "sensor",
				"datatype": "VehicleDataTypes.SVMCamera",
				"description": "Rear view camera"
			},
			"LeftSideViewCamera": {
				"type": "sensor",
				"datatype": "VehicleDataTypes.SVMCamera",
				"description": "Left side view camera"
			},
			"RightSideViewCamera": {
				"type": "sensor",
				"datatype": "VehicleDataTypes.SVMCamera",
				"description": "Right side view camera"
			}
		}
	},
	"ComplexDataTypes": {
		"VehicleDataTypes": {
			"type": "branch",
			"description": "Branch to aggregate all camera related higher order data types",
			"children": {
				"SVMCamera": {
					"type": "struct",
					"description": "This data type represents Surround View Monitor (SVM) camera system in a vehicle",
					"comment": "Test comment",
					"deprecation": "Test deprecation message",
					"children": {
						"Make": {
							"type": "property",
							"description": "Make of the SVM camera",
							"datatype": "string",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						},
						"Description": {
							"type": "property",
							"description": "Description of the SVM camera",
							"datatype": "string",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						},
						"FPS": {
							"type": "property",
							"description": "FPS of the SVM camera",
							"datatype": "double",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						},
						"Orientation": {
							"type": "property",
							"description": "Orientation of the SVM camera",
							"datatype": "VehicleDataTypes.Orientation",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						},
						"Range": {
							"type": "property",
							"description": "Range of the SVM camera",
							"datatype": "VehicleDataTypes.Range",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						},
						"RawData": {
							"type": "property",
							"description": "Represents binary data of the SVM camera",
							"datatype": "uint8[]",
							"dataencoding": "binary",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						},
						"CapturedFrames": {
							"type": "property",
							"description": "Represents selected frames captured by the SVM camera",
							"datatype": "VehicleDataTypes.Frame[]",
							"dataencoding": "typed",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						}
					}
				},
				"Range": {
					"type": "struct",
					"description": "Range of a camera in centimeters",
					"comment": "Test comment",
					"deprecation": "Test deprecation message",
					"children": {
						"Min": {
							"type": "property",
							"description": "Minimum range of a camera in centimeters",
							"datatype": "uint32",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						},
						"Max": {
							"type": "property",
							"description": "Maximum range of a camera in centimeters",
							"datatype": "uint32",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						}
					}
				},
				"Orientation": {
					"type": "struct",
					"description": "Orientation of a camera",
					"comment": "Test comment",
					"deprecation": "Test deprecation message",
					"children": {
						"Front": {
							"type": "property",
							"description": "Indicates whether the camera is oriented to the front of the vehicle",
							"datatype": "boolean",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						},
						"Rear": {
							"type": "property",
							"description": "Indicates whether the camera is oriented to the rear of the vehicle",
							"datatype": "boolean",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						},
						"Side": {
							"type": "property",
							"description": "Indicates whether the camera is oriented to the side of the vehicle",
							"datatype": "boolean",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						}
					}
				},
				"Frame": {
					"type": "struct",
					"description": "Represents a camera frame",
					"comment": "Test comment",
					"deprecation": "Test deprecation message",
					"children": {
						"Data": {
							"type": "property",
							"datatype": "string",
							"dataencoding": "binary",
							"comment": "Test comment",
							"deprecation": "Test deprecation message"
						}
					}
				}
			}
		}
	}

}
```

The following example shows the same signals defined in VSS in a
JSON string.

```
{
   "vssJson": "{\"Vehicle\":{\"type\":\"branch\",\"children\":{\"Chassis\":{\"type\":\"branch\",\"description\":\"All data concerning steering, suspension, wheels, and brakes.\",\"children\":{\"SteeringWheel\":{\"type\":\"branch\",\"description\":\"Steering wheel signals\",\"children\":{\"Diameter\":{\"type\":\"attribute\",\"description\":\"The diameter of the steering wheel\",\"datatype\":\"float\",\"unit\":\"cm\",\"min\":1,\"max\":50},\"HandsOff\":{\"type\":\"branch\",\"children\":{\"HandsOffSteeringState\":{\"type\":\"actuator\",\"description\":\"HndsOffStrWhlDtSt. Hands Off Steering State\",\"datatype\":\"boolean\"},\"HandsOffSteeringMode\":{\"type\":\"actuator\",\"description\":\"HndsOffStrWhlDtMd. Hands Off Steering Mode\",\"datatype\":\"int8\",\"min\":0,\"max\":2}}}}},\"Accelerator\":{\"type\":\"branch\",\"description\":\"\",\"children\":{\"AcceleratorPedalPosition\":{\"type\":\"sensor\",\"description\":\"Throttle__Position. Accelerator pedal position as percent. 0 = Not depressed. 100 = Fully depressed.\",\"datatype\":\"uint8\",\"unit\":\"%\",\"min\":0,\"max\":100.000035}}}}},\"Powertrain\":{\"type\":\"branch\",\"description\":\"Powertrain data for battery management, etc.\",\"children\":{\"Transmission\":{\"type\":\"branch\",\"description\":\"Transmission-specific data, stopping at the drive shafts.\",\"children\":{\"VehicleOdometer\":{\"type\":\"sensor\",\"description\":\"Vehicle_Odometer\",\"datatype\":\"float\",\"unit\":\"km\",\"min\":0,\"max\":67108863.984375}}},\"CombustionEngine\":{\"type\":\"branch\",\"description\":\"Engine-specific data, stopping at the bell housing.\",\"children\":{\"Engine\":{\"type\":\"branch\",\"description\":\"Engine description\",\"children\":{\"timing\":{\"type\":\"branch\",\"description\":\"timing description\",\"children\":{\"run_time\":{\"type\":\"sensor\",\"description\":\"Engine run time\",\"datatype\":\"int16\",\"unit\":\"ms\",\"min\":0,\"max\":10000},\"idle_time\":{\"type\":\"sensor\",\"description\":\"Engine idle time\",\"datatype\":\"int16\",\"min\":0,\"unit\":\"ms\",\"max\":10000}}}}}}}}},\"Axle\":{\"type\":\"branch\",\"description\":\"Axle signals\",\"children\":{\"TireRRPrs\":{\"type\":\"sensor\",\"description\":\"TireRRPrs. Right rear Tire pressure in kilo-Pascal\",\"datatype\":\"float\",\"unit\":\"kPaG\",\"min\":0,\"max\":1020}}}}}}"
}
```

###### Note

You can download a [demo script](https://raw.githubusercontent.com/aws/aws-iot-fleetwise-edge/main/tools/cloud/ros2-to-nodes.py "https://raw.githubusercontent.com/aws/aws-iot-fleetwise-edge/main/tools/cloud/ros2-to-nodes.py") to convert ROS 2 messages to VSS JSON files that
are compatible with the signal catalog. For more information, see the [_Vision System Data Developer
Guide_](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/vision-system-data/vision-system-data-demo.ipynb "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/vision-system-data/vision-system-data-demo.ipynb").

Vision system data is in preview release and is subject to change.

If you [enabled encryption](key-management.md "key-management.md") using a
customer managed AWS KMS key, include the following policy statement so that your
role can invoke the `ImportSignalCatalog` API operation.

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
