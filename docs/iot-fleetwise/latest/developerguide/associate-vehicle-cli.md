# Associate an AWS IoT FleetWise vehicle with a fleet

You can use the [AssociateVehicleFleet](../APIReference/API_AssociateVehicle.md "../APIReference/API_AssociateVehicle.md") API operation to associate a vehicle with a fleet. The
following example uses AWS CLI.

###### Important

- You must have a vehicle and a fleet before you can associate a vehicle
  with a fleet. For more information, see [Manage AWS IoT FleetWise vehicles](vehicles.md "vehicles.md").
- If you associate a vehicle with a fleet that is targeted by a campaign,
  AWS IoT FleetWise automatically deploys the campaign to the vehicle.
  To associate a vehicle with a fleet, run the following command.

- Replace `fleet-id` with the ID of the fleet.
- Replace `vehicle-name` with the ID of the
  vehicle.

```
aws iotfleetwise associate-vehicle-fleet --fleet-id `fleet-id` --vehicle-name `vehicle-name`
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `AssociateVehicleFleet` API operation.

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
