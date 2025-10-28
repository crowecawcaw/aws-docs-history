# Update an AWS IoT FleetWise signal catalog

You can use the [UpdateSignalCatalog](../APIReference/API_UpdateSignalCatalog.md "../APIReference/API_UpdateSignalCatalog.md") API operation to update an existing signal catalog.
The following example uses AWS CLI.

To update an existing signal catalog, run the following command.

Replace `signal-catalog-configuration` with the name of
the .json file that contains the configuration.

```
aws iotfleetwise update-signal-catalog --cli-input-json file://`signal-catalog-configuration`.json
```

Replace `signal-catalog-name` with the name
of the signal catalog that you're updating.

For more information about how to configure branches, attributes,
sensors, and actuators, see [Configure AWS IoT FleetWise signals](define-signal.md "define-signal.md").

###### Important

Custom structures are immutable. If you need to re-order or insert
properties to an existing custom structure (struct), delete the
structure and create a brand-new structure with the desired order of
properties.

To delete a custom structure, add the structure's fully qualified
name in `nodesToRemove`. A structure can't be deleted if
it's referred to by any signals. Any signals that refer to the
structure (their data type is defined as the target structure) must
be updated or deleted before the request to update the signal
catalog.

```
{
    	"name": "signal-catalog-name",
    	"nodesToAdd": [{
    			"branch": {
    				"description": "Front left of vehicle specific data.",
    				"fullyQualifiedName": "Vehicle.Front.Left"
    			}
    		},
    		{
    			"branch": {
    				"description": "Door-specific data for the front left of vehicle.",
    				"fullyQualifiedName": "Vehicle.Front.Left.Door"
    			}
    		},
    		{
    			"actuator": {
    				"fullyQualifiedName": "Vehicle.Front.Left.Door.Lock",
    				"description": "Whether the front left door is locked.",
    				"dataType": "BOOLEAN"
    			}
    		},
    		{
    			"branch": {
    				"fullyQualifiedName": "Vehicle.Camera"
    			}
    		},
    		{
    			"struct": {
    				"fullyQualifiedName": "Vehicle.Camera.SVMCamera"
    			}
    		},
    		{
    			"property": {
    				"fullyQualifiedName": "Vehicle.Camera.SVMCamera.ISO",
    				"dataType": "STRING"
    			}
    		}
    	],
    	"nodesToRemove": ["Vehicle.Chassis.SteeringWheel.HandsOffSteeringState"],
    	"nodesToUpdate": [{
    		"attribute": {
    			"dataType": "FLOAT",
    			"fullyQualifiedName": "Vehicle.Chassis.SteeringWheel.Diameter",
    			"max": 55
    		}
    	}]
    }
```

If you [enabled encryption](key-management.md "key-management.md") using
a customer managed AWS KMS key, include the following policy statement so
that your role can invoke the `UpdateSignalCatalog` API
operation.

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

## Verify signal catalog

update

You can use the [ListSignalCatalogNodes](../APIReference/API_ListSignalCatalogNodes.md "../APIReference/API_ListSignalCatalogNodes.md") API operation to verify if a
signal catalog was updated. The following example uses AWS CLI.

To retrieve a paginated list of summaries of all signals (nodes)
in a given signal catalog, run the following command.

Replace `signal-catalog-name` with the
name of the signal catalog that you're checking.

```
aws iotfleetwise list-signal-catalog-nodes --name `signal-catalog-name`
```

If you [enabled encryption](key-management.md "key-management.md")
using a customer managed AWS KMS key, include the following policy statement
so that your role can invoke the `ListSignalCatalogNodes`
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
