# Update an AWS IoT FleetWise decoder manifest

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can use the [UpdateDecoderManifest](../APIReference/API_UpdateDecoderManifest.md "../APIReference/API_UpdateDecoderManifest.md") API operation to update a decoder manifest. You
can add, remove, and update network interfaces and signal decoders. You can also
change the status of the decoder manifest. The following example uses the
AWS CLI.

To update a decoder manifest, run the following command.

Replace `decoder-manifest-name` with the name of the
decoder manifest that you're updating.

```
aws iotfleetwise update-decoder-manifest /
                --name `decoder-manifest-name` /
                --status ACTIVE
```

If the signals don't have specified decoding rules, you can create default decoding rules. The signals are added to a custom decoded interface with the `CustomDecodingSignal$id` set to the fully qualified name of the signal. To update a decoder manifest with default decoding rules, run the following command.

Replace `decoder-manifest-name` with the name of the
decoder manifest that you're updating.

```
aws iotfleetwise update-decoder-manifest /
                --name `decoder-manifest-name` /
                --status ACTIVE
                --default-for-unmapped-signals CUSTOM_DECODING
```

###### Important

After you activate the decoder manifest, you can't edit it.

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `UpdateDecoderManifest` API operation.

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

## Verify decoder manifest update

You can use the [ListDecoderManifestSignals](../APIReference/API_ListDecoderManifestSignals.md "../APIReference/API_ListDecoderManifestSignals.md") API operation to verify if decoder signals
in the decoder manifest were updated. The following example uses AWS CLI.

To retrieve a paginated list of summaries of all decoder signals (nodes) in a
given decoder manifest, run the following command.

Replace `decoder-manifest-name` with the name of the
decoder manifest that you're checking.

```
aws iotfleetwise list-decoder-manifest-signals /
                 --name `decoder-manifest-name`
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListDecoderManifestSignals` API operation.

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

You can use the [ListDecoderManifestNetworkInterfaces](../APIReference/API_ListDecoderManifestNetworkInterfaces.md "../APIReference/API_ListDecoderManifestNetworkInterfaces.md") API operation to verify if network
interfaces in the decoder manifest were updated. The following example uses
AWS CLI.

To retrieve a paginated list of summaries of all network interfaces in a given
decoder manifest, run the following command.

Replace `decoder-manifest-name` with the name of the
decoder manifest that you're checking.

```
aws iotfleetwise list-decoder-manifest-network-interfaces /
                 --name `decoder-manifest-name`
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListDecoderManifestNetworkInterfaces` API operation.

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
