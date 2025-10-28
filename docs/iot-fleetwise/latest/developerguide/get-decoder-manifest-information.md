# Get AWS IoT FleetWise decoder manifest

information

You can use the [GetDecoderManifest](../APIReference/API_GetDecoderManifest.md "../APIReference/API_GetDecoderManifest.md") API operation to verify if network interfaces and
signal decoders in the decoder manifest have been updated. The following example
uses AWS CLI.

To retrieve information about a decoder manifest, run the following
command.

Replace `decoder-manifest` with the name of the decoder
manifest that you want to retrieve.

```
aws iotfleetwise get-decoder-manifest --name `decoder-manifest`
```

###### Note

This operation is [eventually consistent](https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf "https://web.stanford.edu/class/cs345d-01/rl/eventually-consistent.pdf"). In other words, changes to the decoder
manifest might not be reflected immediately.

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `GetDecoderManifest` API operation.

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
