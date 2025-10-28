# Delete an AWS IoT FleetWise fleet

You can use the [DeleteFleet](../APIReference/API_DeleteFleet.md "../APIReference/API_DeleteFleet.md") API
operation to delete a fleet. The following example uses AWS CLI.

###### Important

Before you delete a fleet, make sure it has no associated vehicles. For instructions on how to disassociate a vehicle from a fleet, see [Disassociate an AWS IoT FleetWise vehicle from a
fleet](disassociate-vehicle-cli.md "disassociate-vehicle-cli.md").

To delete a fleet, run the following command.

Replace `fleet-id` with the ID of the fleet that you're
deleting.

```
aws iotfleetwise delete-fleet --fleet-id `fleet-id`
```

## Verify fleet deletion

You can use the [ListFleets](../APIReference/API_ListFleets.md "../APIReference/API_ListFleets.md") API
operation to verify if a fleet was deleted. The following example uses the
AWS CLI.

To retrieve a paginated list of summaries of all fleets, run the following
command.

```
aws iotfleetwise list-fleets
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListFleets` API operation.

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
