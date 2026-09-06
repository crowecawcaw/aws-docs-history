

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Delete an AWS IoT FleetWise vehicle
<a name="delete-vehicle"></a>

You can use the AWS IoT FleetWise console or API to delete vehicles.

**Important**  
After a vehicle is deleted, AWS IoT FleetWise automatically removes the vehicle from the associated fleets and campaigns. For more information, see [Manage fleets in AWS IoT FleetWise](fleets.md) and [Collect AWS IoT FleetWise data with campaigns](campaigns.md). However, the vehicle still exists as a thing or is still associated with a thing in AWS IoT Core. For instructions on deleting a thing, see [Delete a thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html#delete-thing) in the *AWS IoT Core Developer Guide*.

## Delete a vehicle (console)
<a name="delete-vehicle-console"></a>

You can use the AWS IoT FleetWise console to delete a vehicle.

**To delete a vehicle**

1. <a name="fleetwise-open-console"></a>Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. On the navigation pane, choose **Vehicles**.

1. On the **Vehicles** page, select the button next to the vehicle you want to delete.

1. Choose **Delete**.

1. In **Delete **vehicle-name****, enter the name of the vehicle, and then choose **Delete**.

## Delete a vehicle (AWS CLI)
<a name="delete-vehicle-cli"></a>

You can use the [DeleteVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteVehicle.html) API operation to delete a vehicle. The following example uses AWS CLI.

To delete a vehicle, run the following command.

Replace {{vehicle-name}} with the ID of the vehicle that you want to delete.

```
aws iotfleetwise delete-vehicle --vehicle-name {{vehicle-name}}
```

### Verify vehicle deletion
<a name="verify-vehicle-deletion"></a>

You can use the [ListVehicles](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehicles.html) API operation to verify if a vehicle was deleted. The following example uses the AWS CLI.

To retrieve a paginated list of summaries of all vehicles, run the following command.

```
aws iotfleetwise list-vehicles
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListVehicles` API operation. 

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