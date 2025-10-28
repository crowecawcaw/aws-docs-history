# Update an AWS IoT FleetWise fleet

You can use the [UpdateFleet](../APIReference/API_UpdateFleet.md "../APIReference/API_UpdateFleet.md") API
operation to update the description for a fleet. The following example uses
AWS CLI.

To update a fleet, run the following command.

- Replace `fleet-id` with the ID of the fleet that
  you're updating.
- Replace `description` with a new description.

The description can have 1-2048 characters.

```
aws iotfleetwise update-fleet --fleet-id `fleet-id` --description `description`
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `UpdateFleet` API operation.

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
