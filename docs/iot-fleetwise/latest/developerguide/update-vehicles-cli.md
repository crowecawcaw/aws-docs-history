# Update multiple AWS IoT FleetWise vehicles

You can use the [BatchUpdateVehicle](../APIReference/API_BatchUpdateVehicle.md "../APIReference/API_BatchUpdateVehicle.md") API operation to update multiple existing vehicles at
one time. The following example uses the AWS CLI.

To update multiple vehicles, run the following command.

Replace `file-name` with the name of the .json file that
contains the configurations of multiple vehicles.

```
aws iotfleetwise batch-update-vehicle --cli-input-json file://`file-name`.json
```

###### Example – vehicle configurations

```
{
   "vehicles": [
      {
         "vehicleName": "vehicle-name",
         "modelManifestArn": "model-manifest-arn",
         "decoderManifestArn": "decoder-manifest-arn",
         "mergeAttributes": true,
         "attributes": {
         "key": "value"
         }
      },
      {
         "vehicleName": "vehicle-name",
         "modelManifestArn": "model-manifest-arn",
         "decoderManifestArn": "decoder-manifest-arn",
         "mergeAttributes": true,
         "attributes": {
         "key": "value"
         }
      }
   ]
}
```

You can update up to 10 vehicles for each batch operation. For more information about
the configuration of each vehicle, see [Update an AWS IoT FleetWise vehicle](update-vehicle-cli.md "update-vehicle-cli.md").

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `BatchUpdateVehicle` API operation.

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
