# Get AWS IoT FleetWise signal catalog

information

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
