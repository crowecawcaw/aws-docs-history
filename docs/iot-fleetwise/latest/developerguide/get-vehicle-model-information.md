AWS IoT FleetWise will no longer be open to new customers starting April 30, 2026. If you would like to use AWS IoT FleetWise, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](iotfleetwise-availability-change.md "iotfleetwise-availability-change.md").

# Get AWS IoT FleetWise vehicle model information

You can use the [GetModelManifest](../APIReference/API_GetModelManifest.md "../APIReference/API_GetModelManifest.md") API operation to retrieve information about a vehicle model. The following example uses AWS CLI.

To retrieve information about a vehicle model, run the following command.

Replace `vehicle-model` with the name of the vehicle
model that you want to retrieve.

```
aws iotfleetwise get-model-manifest --name `vehicle-model`
```

###### Note

This operation is [eventually consistent](https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf "https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf"). In other words, changes to the vehicle model might not be reflected immediately.

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `GetModelManifest` API operation.

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
