# Delete an AWS IoT FleetWise signal catalog

You can use the [DeleteSignalCatalog](../APIReference/API_DeleteSignalCatalog.md "../APIReference/API_DeleteSignalCatalog.md") API operation to delete a signal catalog. The
following example uses AWS CLI.

###### Important

Before deleting a signal catalog, make sure it has no associated vehicle
models, decoder manifests, vehicles, fleets, or campaigns. For instructions, see
the following:

- [Delete an AWS IoT FleetWise vehicle model](delete-vehicle-model.md "delete-vehicle-model.md")
- [Delete an AWS IoT FleetWise decoder manifest](delete-decoder-manifest.md "delete-decoder-manifest.md")
- [Delete an AWS IoT FleetWise vehicle](delete-vehicle.md "delete-vehicle.md")
- [Delete an AWS IoT FleetWise fleet](delete-fleet-cli.md "delete-fleet-cli.md")
- [Delete an AWS IoT FleetWise campaign](delete-campaign.md "delete-campaign.md")
  To delete an existing signal catalog, run the following command. Replace
  `signal-catalog-name` with the name of the signal
  catalog that you're deleting.

```
aws iotfleetwise delete-signal-catalog --name `signal-catalog-name`
```

## Verify signal catalog

deletion

You can use the [ListSignalCatalogs](../APIReference/API_ListSignalCatalogs.md "../APIReference/API_ListSignalCatalogs.md") API operation to verify if a signal catalog has been
deleted. The following example uses AWS CLI.

To retrieve a paginated list of summaries of all signal catalogs, run the
following command.

```
aws iotfleetwise list-signal-catalogs
```

If you [enabled encryption](key-management.md "key-management.md")
using a customer managed AWS KMS key, include the following policy statement
so that your role can invoke the `ListSignalCatalogs`
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
