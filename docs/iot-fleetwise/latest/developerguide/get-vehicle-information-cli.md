# Get AWS IoT FleetWise vehicle information

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can use the [GetVehicle](../APIReference/API_GetVehicle.md "../APIReference/API_GetVehicle.md") API
operation to retrieve vehicle information. The following example uses the AWS CLI.

To retrieve the metadata of a vehicle, run the following command.

Replace `vehicle-name` with the ID of the vehicle that you
want to retrieve.

```
aws iotfleetwise get-vehicle --vehicle-name `vehicle-name`
```

###### Note

This operation is [eventually
consistent](https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf "https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf"). In other words, changes to the vehicle might not be reflected
immediately.

You can use the [GetVehicleStatus](../APIReference/API_GetVehicleStatus.md "../APIReference/API_GetVehicleStatus.md")
API operation to retrieve the status of resources associated with a vehicle. The following
example uses the AWS CLI.

To retrieve the status of resources associated with a vehicle, run the following
command.

- Replace `vehicle-name` with the ID of the vehicle which the
  resources are associated with.
- Replace `type` with the type of the
  resource whose status you want to retrieve. Valid values for `type` are
  `CAMPAIGN`, `STATE_TEMPLATE`, and `DECODER`.

```
aws iotfleetwise get-vehicle-status --vehicle-name `vehicle-name` --type `type`
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `GetVehicle` or `GetVehicleStatus` API operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS_KEY_ID`"
 ]
 }
 ]
}`

```
