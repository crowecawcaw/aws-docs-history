# Manage your geofence collection

resources

Manage your geofence collections using the Amazon Location console, the AWS CLI, or the Amazon Location
APIs.

## List your geofence collection

resources

You can view your geofence collection list using the Amazon Location console, the AWS CLI,
or the Amazon Location APIs:

Console
**To view a list of geofence collections using the
Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Geofence collections** from the left
   navigation pane.
3. View a list of your geofence collections under **My
   geofence collections**.

API
Use the `ListGeofenceCollections` operation from the
Amazon Location Geofences APIs.

The following example is an API request to get a list of geofence
collections in the AWS account.

```
POST /geofencing/v0/list-collections
```

The following is an example response for
`ListGeofenceCollections`:

```
{
    "Entries": [
    {
        "CollectionName": "`ExampleCollection`",
        "CreateTime": 2020-09-30T22:59:34.142Z,
        "Description": "string",
        "UpdateTime": 2020-09-30T23:59:34.142Z
    },
    "NextToken": "1234-5678-9012"
}
```

CLI
Use the `list-geofence-collections` command.

The following example is an AWS CLI to get a list of geofence collections in
the AWS account.

```
aws location list-geofence-collections
```

## Get geofence collection details

You can get details about any geofence collection resource in your AWS account using
the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

Console
**To view the details of a geofence collection
using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Geofence collections** from the left
   navigation pane.
3. Under **My geofence collections**, select the
   name link of the target geofence collection.

API
Use the `DescribeGeofenceCollection` operation from the
Amazon Location Geofences APIs.

The following example is an API request to get the geofence collection
details for `ExampleCollection`.

```
GET /geofencing/v0/collections/`ExampleCollection`
```

The following is an example response for
`DescribeGeofenceCollection`:

```
{
    "CollectionArn": "arn:aws:geo:us-west-2:123456789012:geofence-collection/GeofenceCollection",
    "CollectionName": "`ExampleCollection`",
    "CreateTime": 2020-09-30T22:59:34.142Z,
    "Description": "string",
    "KmsKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "Tags": {
        "Tag1" : "Value1"
    },
    "UpdateTime": 2020-09-30T23:59:34.142Z
}
```

CLI
Use the `describe-geofence-collection` command.

The following example is an AWS CLI to get the geofence collection
details for `ExampleCollection`.

```
aws location describe-geofence-collection \
    --collection-name "`ExampleCollection`"
```

## Delete a geofence collection

You can delete a geofence collection from your AWS account using the Amazon Location
console, the AWS CLI, or the Amazon Location APIs.

Console
**To delete a geofence collection using the
Amazon Location console**

###### Warning

This operation deletes the resource permanently.

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Geofence collections** from the left
   navigation pane.
3. Under **My geofence collection**, select the
   target geofence collection.
4. Choose **Delete geofence collection**.

API
Use the `DeleteGeofenceCollection` operation from the
Amazon Location APIs.

The following example is an API request to delete the geofence
collection `ExampleCollection`.

```
DELETE /geofencing/v0/collections/`ExampleCollection`
```

The following is an example response for
`DeleteGeofenceCollection`:

```
HTTP/1.1 200
```

CLI
Use the `delete-geofence-collection` command.

The following example is an AWS CLI command to delete the geofence
collection `ExampleCollection`.

```
aws location delete-geofence-collection \
    --collection-name "`ExampleCollection`"
```

## List stored geofences

You can list geofences stored in a specified geofence collection using the Amazon Location
console, the AWS CLI, or the Amazon Location APIs.

Console
**To view a list of geofences using the Amazon Location
console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Geofence collections** from the left
   navigation pane.
3. Under **My geofence collection**, select the
   name link of the target geofence collection.
4. View geofences in the geofence collection under
   **Geofences**

API
Use the `ListGeofences` operation from the Amazon Location
Geofences APIs.

The following example is an API request to get a list of geofences
stored in the geofence collection
`ExampleCollection`.

```
POST /geofencing/v0/collections/`ExampleCollection`/list-geofences
```

The following is an example response for `ListGeofences`:

```
{
   "Entries": [
      {
         "CreateTime": 2020-09-30T22:59:34.142Z,
         "GeofenceId": "geofence-1",
         "Geometry": {
             "Polygon": [
                 [-5.716667, -15.933333,
                 [-14.416667, -7.933333],
                 [-12.316667, -37.066667],
                 [-5.716667, -15.933333]
             ]
         },
         "Status": "ACTIVE",
         "UpdateTime": 2020-09-30T23:59:34.142Z
      }
   ],
   "NextToken": "1234-5678-9012"
}
```

CLI
Use the `list-geofences` command.

The following example is an AWS CLI to get a list of geofences stored in
the geofence collection `ExampleCollection`.

```
aws location list-geofences \
    --collection-name "`ExampleCollection`"
```

## Get geofence details

You can get the details of a specific geofence, such as the create time, update time,
geometry, and status, from a geofence collection using the Amazon Location console, AWS CLI, or
the Amazon Location APIs.

Console
**To view the status of a geofence using the
Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Geofence collections** from the left
   navigation pane.
3. Under **My geofence collection**, select the
   name link of the target geofence collection.
4. Under **Geofences**, you’ll be able to view
   the status of your geofences.

API
Use the `GetGeofence` operation from the Amazon Location
Geofences APIs.

The following example is an API request to get the geofence details
from a geofence collection
`ExampleCollection`.

```
GET /geofencing/v0/collections/`ExampleCollection`/geofences/`ExampleGeofence1`
```

The following is an example response for `GetGeofence`:

```
{
   "CreateTime": 2020-09-30T22:59:34.142Z,
   "GeofenceId": "`ExampleGeofence1`",
   "Geometry": {
      "Polygon": [
          [-1,-1],
          [1,-1],
          [0,1],
          [-1,-1]
      ]
   },
   "Status": "ACTIVE",
   "UpdateTime": 2020-09-30T23:59:34.142Z
}
```

CLI
Use the `get-geofence` command.

The following example is an AWS CLI to get the geofence collection
details for `ExampleCollection`.

```
aws location get-geofence \
    --collection-name "`ExampleCollection`" \
    --geofence-id "`ExampleGeofence1`"
```

## Delete geofences

You can delete geofences from a geofence collection using the Amazon Location console, the
AWS CLI, or the Amazon Location APIs.

Console
**To delete a geofence using the Amazon Location
console**

###### Warning

This operation deletes the resource permanently.

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. Choose **Geofence collections** from the left
   navigation pane.
3. Under **My geofence collection**, select the
   name link of the target geofence collection.
4. Under **Geofences**, select the target
   geofence.
5. Choose **Delete geofence**.

API
Use the `BatchDeleteGeofence` operation from the Amazon Location
Geofences APIs.

The following example is an API request to delete geofences from the
geofence collection `ExampleCollection`.

```
POST /geofencing/v0/collections/`ExampleCollection`/delete-geofences
Content-type: application/json

{
   "GeofenceIds": [ "`ExampleGeofence11`" ]
}
```

The following is an example success response for `BatchDeleteGeofence`.

```
HTTP/1.1 200
```

CLI
Use the `batch-delete-geofence` command.

The following example is an AWS CLI command to delete geofences from the
geofence collection `ExampleCollection`.

```
aws location `batch-delete-geofence` \
    --collection-name "`ExampleCollection`" \
    --geofence-ids "`ExampleGeofence11`"
```
