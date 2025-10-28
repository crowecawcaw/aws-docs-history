# Update an AWS IoT FleetWise vehicle

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can use the [UpdateVehicle](../APIReference/API_UpdateVehicle.md "../APIReference/API_UpdateVehicle.md")
API operation to update an existing vehicle. The following example uses the
AWS CLI.

To update a vehicle, run the following command.

Replace `file-name` with the name of the .json file that
contains the configuration of your vehicle.

```
aws iotfleetwise update-vehicle --cli-input-json file://`file-name`.json
```

###### Example – vehicle configuration

- Replace `vehicle-name` with the ID of the vehicle
  that you want to update.
- (Optional) Replace `model-manifest-ARN` with the
  ARN of the vehicle model (model manifest) that you use to replace the
  vehicle model in use.
- (Optional) Replace `decoder-manifest-ARN` with
  the ARN of your decoder manifest associated with the new vehicle model that
  you specified.
- (Optional) Replace `attribute-update-mode` with vehicle attributes.

      + `Merge` – Merge new attributes into existing
       attributes by updating existing attributes with new values and
       adding new attributes if they don't exist.


      For example, if a vehicle has the following attributes:
       `{"color": "black", "fuelType": "electric"}`, and you
       update the vehicle with the following attributes: `{"color":
       "", "fuelType": "gasoline", "model": "x"}`, the updated
       vehicle has the following attributes: `{"fuelType": "gasoline",
       "model": "x"}`.
      + `Overwrite` – Replace existing attributes with new
       attributes.


      For example, if a vehicle has the following attributes:
       `{"color": "black", "fuelType": "electric"}`, and you
       update the vehicle with the `{"model": "x"}` attribute,
       the updated vehicle has the `{"model": "x"}`
       attribute.

  This is required if attributes are present in the input.

- (Optional) To add new attributes or update existing ones with new values,
  configure `attributes`. For example, if you have an electric car,
  you can specify the following value for an attribute: `{"fuelType":
"electric"}`.

To delete attributes, configure `attributeUpdateMode` to
`Merge`.

###### Important

Attributes must be defined in the associated vehicle model before you can add them to
individual vehicles.

```
 {
         "vehicleName": "`vehicle-name`",
         "modelManifestArn": "`model-manifest-arn`",
         "decoderManifestArn": "`decoder-manifest-arn`",
         "attributeUpdateMode": "`attribute-update-mode`"
         }
}
```

###### Example – add or remove state templates associated with the vehicle

You can associate additional state templates or remove existing associations from the
vehicle using the following fields:

- `stateTemplatesToAdd`
- `stateTemplatesToRemove`

```
aws iotfleetwise update-vehicle --cli-input-json file://`update-vehicle.json`
```

Where the `update-vehicle.json` file contains
(for example):

```
{
    "vehicleName": "`vehicle-name`",
    "modelManifestArn": "`model-manifest-arn`",
    "decoderManifestArn": "`decoder-manifest-arn`",
    "attributeUpdateMode": "`attribute-update-mode`",
    "stateTemplatesToAdd": [
        {
            "identifier": "`state-template-name`",
            "stateTemplateUpdateStrategy": {
                "onChange": {}
            }
        }
    ],
    "stateTemplatesToRemove": ["`state-template-name`"]
}
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `UpdateVehicle` API operation.

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
