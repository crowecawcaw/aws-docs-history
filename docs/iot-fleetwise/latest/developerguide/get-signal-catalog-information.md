AWS IoT FleetWise will no longer be open to new customers starting April 30, 2026. If you would like to use AWS IoT FleetWise, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](iotfleetwise-availability-change.md "iotfleetwise-availability-change.md").

# Get AWS IoT FleetWise signal catalog information

You can use the [GetSignalCatalog](../APIReference/API_GetSignalCatalog.md "../APIReference/API_GetSignalCatalog.md") API operation to retrieve signal catalog information.
The following example uses AWS CLI.

To retrieve information about a signal catalog, run the following command.

Replace `signal-catalog-name` with the name of the signal
catalog that you want to retrieve.

```
aws iotfleetwise get-signal-catalog --name `signal-catalog-name`
```

If you [enabled encryption](key-management.md "key-management.md")
using a customer managed AWS KMS key, include the following policy statement
so that your role can invoke the `GetSignalCatalog`
API operation.

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

###### Note

This operation is [eventually consistent](https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf "https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf"). In other words, changes to the signal
catalog might not be reflected immediately.
