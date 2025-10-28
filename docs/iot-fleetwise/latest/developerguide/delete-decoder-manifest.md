# Delete an AWS IoT FleetWise decoder manifest

You can use the AWS IoT FleetWise console or API to delete a decoder manifest.

###### Important

Vehicles associated with the decoder manifest must be deleted first. For more
information, see [Delete an AWS IoT FleetWise vehicle](delete-vehicle.md "delete-vehicle.md").

###### Topics

- [Delete a decoder manifest
  (console)](#delete-decoder-manifest-console "#delete-decoder-manifest-console")
- [Delete a decoder manifest
  (AWS CLI)](#delete-decoder-manifest-cli "#delete-decoder-manifest-cli")

## Delete a decoder manifest

(console)

You can use the AWS IoT FleetWise console to delete a decoder manifest.

###### To delete a decoder manifest

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
2. On the navigation pane, choose **Vehicle models**.
3. Choose the target vehicle model.
4. On the vehicle model summary page, choose the **Decoder
   manifests** tab.
5. Choose the target decoder manifest, and then choose
   **Delete**.
6. In **Delete
   `decoder-manifest-name`?**, enter the
   name of the decoder manifest to delete, and then choose
   **Confirm**.

## Delete a decoder manifest

(AWS CLI)

You can use the [DeleteDecoderManifest](../APIReference/API_DeleteDecoderManifest.md "../APIReference/API_DeleteDecoderManifest.md") API operation to delete a decoder manifest.
The following example uses AWS CLI.

###### Important

Before you delete the decoder manifest, delete the associated vehicles
first. For more information, see [Delete an AWS IoT FleetWise vehicle](delete-vehicle.md "delete-vehicle.md").

To delete a decoder manifest, run the following command.

Replace `decoder-manifest-name` with the name of the
decoder manifest that you're deleting.

```
aws iotfleetwise delete-decoder-manifest --name `decoder-manifest-name`
```

### Verify decoder manifest deletion

You can use the [ListDecoderManifests](../APIReference/API_ListDecoderManifests.md "../APIReference/API_ListDecoderManifests.md") API operation to verify if a decoder manifest has
been deleted. The following example uses AWS CLI.

To retrieve a paginated list of summaries of all decoder manifests, run the
following command.

```
aws iotfleetwise list-decoder-manifests
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListDecoderManifests` API operation.

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
