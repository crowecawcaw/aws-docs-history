# Create multiple AWS IoT FleetWise vehicles

You can use the [BatchCreateVehicle](../APIReference/API_BatchCreateVehicle.md "../APIReference/API_BatchCreateVehicle.md") API operation to create multiple vehicles at one time.
The following example uses the AWS CLI.

To create multiple vehicles, run the following command.

Replace `file-name` with the name of the .json file that
contains the configurations of multiple vehicles.

```
aws iotfleetwise batch-create-vehicle --cli-input-json file://`file-name`.json
```

###### Example – vehicle configurations

```
{
    "vehicles": [
        {
                "associationBehavior": "`associationBehavior`",
                "vehicleName": "`vehicle-name`",
                "modelManifestArn": "`model-manifest-ARN`",
                "decoderManifestArn": "`decoder-manifest-ARN`",
                "attributes": {
                    "`key`": "`value`"
                }
        },
        {
                "associationBehavior": "`associationBehavior`",
                "vehicleName": "`vehicle-name`",
                "modelManifestArn": "`model-manifest-ARN`",
                "decoderManifestArn": "`decoder-manifest-ARN`",
                "attributes": {
                    "`key`": "`value`"
                }
        }
    ]
}
```

You can create up to 10 vehicles for each batch operation. For more information about
the vehicle configuration, see [Create an AWS IoT FleetWise vehicle](create-vehicle.md "create-vehicle.md").

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `BatchCreateVehicle` API operation.

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
