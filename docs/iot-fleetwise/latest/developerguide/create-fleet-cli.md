# Create an AWS IoT FleetWise fleet

You can use the [CreateFleet](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md") API
operation to create a vehicle fleet. The following example uses AWS CLI.

###### Important

You must have a signal catalog before you can create a fleet. For more
information, see [Create an AWS IoT FleetWise signal catalog](create-signal-catalog.md "create-signal-catalog.md").

To create a fleet, run the following command.

- Replace `fleet-id` with the ID of the fleet that
  you're creating.

The fleet ID must be unique and have 1-100 characters. Valid characters:
letters (A-Z and a-z), numbers (0-9), colons (:), dashes (-), and underscores
(\_).

- (Optional) Replace `description` with a
  description.

The description can have 1-2048 characters.

- Replace `signal-catalog-arn` with the ARN of the
  signal catalog.

```
aws iotfleetwise create-fleet \
   --fleet-id `fleet-id` \
   --description `description` \
   --signal-catalog-arn `signal-catalog-arn`
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `CreateFleet` API operation.

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
