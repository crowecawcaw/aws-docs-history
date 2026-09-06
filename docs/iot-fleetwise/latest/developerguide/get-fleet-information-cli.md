

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Get AWS IoT FleetWise fleet information
<a name="get-fleet-information-cli"></a>

You can use the [ListFleetsForVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleetsForVehicle.html) API operation to retrieve a paginated list of IDs of all fleets that the vehicle belongs to. The following example uses the AWS CLI.

To retrieve a paginated list of IDs of all fleets that the vehicle belongs to, run the following command.

Replace {{vehicle-name}} with the ID of the vehicle.

```
aws iotfleetwise list-fleets-for-vehicle \
            --vehicle-name {{vehicle-name}}
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListFleetsForVehicle` API operation. 

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

You can use the [ListVehiclesInFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehiclesInFleet.html) API operation to retrieve a paginated list of summaries of all vehicles in a fleet. The following example uses the AWS CLI.

To retrieve a paginated list of summaries of all vehicles in a fleet, run the following command.

Replace {{fleet-id}} with the ID of the fleet.

```
aws iotfleetwise list-vehicles-in-fleet \
            --fleet-id {{fleet-id}}
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListVehiclesInFleet` API operation. 

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

You can use the [GetFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetFleet.html) API operation to retrieve fleet information. The following example uses the AWS CLI.

To retrieve the metadata of a fleet, run the following command.

Replace {{fleet-id}} with the ID of the fleet.

```
aws iotfleetwise get-fleet \
            --fleet-id {{fleet-id}}
```

**Note**  
This operation is [eventually consistent](https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf). In other words, changes to the fleet might not be reflected immediately.

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `GetFleet` API operation. 

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