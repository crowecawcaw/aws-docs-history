# Disassociate an AWS IoT FleetWise vehicle from a

fleet

You can use the [DisassociateVehicleFleet](../APIReference/API_DisassociateVehicle.md "../APIReference/API_DisassociateVehicle.md") API operation to disassociate a vehicle from a fleet.
The following example uses AWS CLI.

To disassociate a vehicle with a fleet, run the following command.

- Replace `fleet-id` with the ID of the fleet.
- Replace `vehicle-name` with the ID of the
  vehicle.

```
aws iotfleetwise disassociate-vehicle-fleet --fleet-id `fleet-id` --vehicle-name `vehicle-name`
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `DisassociateVehicleFleet` API operation.

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
