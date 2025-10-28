# Get AWS IoT FleetWise fleet information

You can use the [ListFleetsForVehicle](../APIReference/API_ListFleetsForVehicle.md "../APIReference/API_ListFleetsForVehicle.md") API operation to retrieve a paginated list of IDs of
all fleets that the vehicle belongs to. The following example uses the AWS CLI.

To retrieve a paginated list of IDs of all fleets that the vehicle belongs to, run the
following command.

Replace `vehicle-name` with the ID of the vehicle.

```
aws iotfleetwise list-fleets-for-vehicle \
            --vehicle-name `vehicle-name`
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListFleetsForVehicle` API operation.

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

You can use the [ListVehiclesInFleet](../APIReference/API_ListVehiclesInFleet.md "../APIReference/API_ListVehiclesInFleet.md") API operation to retrieve a paginated list of summaries
of all vehicles in a fleet. The following example uses the AWS CLI.

To retrieve a paginated list of summaries of all vehicles in a fleet, run the
following command.

Replace `fleet-id` with the ID of the fleet.

```
aws iotfleetwise list-vehicles-in-fleet \
            --fleet-id `fleet-id`
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListVehiclesInFleet` API operation.

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

You can use the [GetFleet](../APIReference/API_GetFleet.md "../APIReference/API_GetFleet.md") API
operation to retrieve fleet information. The following example uses the AWS CLI.

To retrieve the metadata of a fleet, run the following command.

Replace `fleet-id` with the ID of the fleet.

```
aws iotfleetwise get-fleet \
            --fleet-id `fleet-id`
```

###### Note

This operation is [eventually consistent](https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf "https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf"). In other words, changes to the fleet might not be reflected immediately.

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `GetFleet` API operation.

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
