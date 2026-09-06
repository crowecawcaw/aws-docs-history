

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Delete an AWS IoT FleetWise fleet
<a name="delete-fleet-cli"></a>

You can use the [DeleteFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteFleet.html) API operation to delete a fleet. The following example uses AWS CLI.

**Important**  
Before you delete a fleet, make sure it has no associated vehicles. For instructions on how to disassociate a vehicle from a fleet, see [Disassociate an AWS IoT FleetWise vehicle from a fleet](disassociate-vehicle-cli.md).

To delete a fleet, run the following command.

Replace {{fleet-id}} with the ID of the fleet that you're deleting.

```
aws iotfleetwise delete-fleet --fleet-id {{fleet-id}} 
```

## Verify fleet deletion
<a name="verify-fleet-deletion"></a>

You can use the [ListFleets](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleets.html) API operation to verify if a fleet was deleted. The following example uses the AWS CLI.

To retrieve a paginated list of summaries of all fleets, run the following command.

```
aws iotfleetwise list-fleets
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListFleets` API operation. 

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