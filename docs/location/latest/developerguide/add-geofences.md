# Add geofences with Amazon Location

Geofences contain points and vertices that form a closed boundary, which defines an area
of interest. Geofence collections store and manage one or multiple geofences.

Amazon Location geofence collections store geofences defined by using a standard geospatial data
format called [GeoJSON (RFC 7946)](https://geojson.org/ "https://geojson.org/"). You can use
tools, such as [geojson.io](http://geojson.io/ "http://geojson.io/"), at no charge to draw your
geofences graphically and save the output GeoJSON file.

###### Note

Amazon Location doesn't support clockwise polygons (use counter-clockwise winding order as
required by [RFC 7946
§3.1.6](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6 "https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6")) and geofences that cross the antimeridian (the 180° line of
longitude).

###### Topics

- [Create a geofence collection](#create-geofence-collection "#create-geofence-collection")
- [Draw geofences](#draw-geofences "#draw-geofences")
- [Add polygon geofences](#draw-polygon-geofences "#draw-polygon-geofences")
- [Add circular geofences](#draw-circle-geofences "#draw-circle-geofences")

## Create a geofence collection

Create a geofence collection to store and manage geofences by using the Amazon Location
console, the AWS CLI, or the Amazon Location APIs.

Console

###### To create a geofence collection using the Amazon Location

console

1. Open the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. In the left navigation pane, choose **Geofence
   collections**.
3. Choose **Create geofence
   collection**.
4. Fill out the following boxes:

   - **Name** – Enter a unique name. For
     example,
     `ExampleGeofenceCollection`.
     Maximum 100 characters. Valid entries include alphanumeric
     characters, hyphens, periods, and underscores.
   - **Description** – Enter an
     optional description to differentiate your resources.

5. Under **EventBridge rule with CloudWatch as a
   target**, you can create an optional EventBridge rule to
   get started [reacting to geofence
   events](location-events.md "location-events.md"). This enables Amazon Location to publish events to
   Amazon CloudWatch Logs.
6. (Optional) Under **Tags**, enter a tag
   **Key** and **Value**. This
   adds a tag to your new geofence collection. For more information,
   see [Manage resources with
   Tags](manage-resources.md "manage-resources.md").
7. (Optional) Under **Customer managed key
   encryption**, you can choose to **Add a
   customer managed key**. This adds a symmetric customer
   managed key that you create, own, and manage over the default AWS
   owned encryption. For more information, see [Encrypting data at
   rest](encryption-at-rest.md "encryption-at-rest.md").
8. Choose **Create geofence
   collection**.

API

###### To create a geofence collection using the Amazon Location

APIs

Use the `CreateGeofenceCollection` operation from the
Amazon Location Geofences APIs.

The following example uses an API request to create a geofence collection
called `ExampleGeofenceCollection`. The geofence
collection is associated with a [customer
managed AWS KMS key to encrypt customer data](encryption-at-rest.md "encryption-at-rest.md").

```
POST /geofencing/v0/collections
Content-type: application/json

{
   "CollectionName": "`ExampleGeofenceCollection`",
   "Description": "Geofence collection 1 for shopping center",
   "KmsKeyId": "`1234abcd-12ab-34cd-56ef-1234567890ab`",
   "Tags": {
      "Tag1" : "Value1"
   }
}
```

AWS CLI

###### To create a geofence collection using AWS CLI

commands

Use the `create-geofence-collection` command.

The following example uses the AWS CLI to create a geofence collection
called `ExampleGeofenceCollection`. The geofence
collection is associated with a [customer
managed AWS KMS key to encrypt customer data](encryption-at-rest.md "encryption-at-rest.md").

```
aws location \
  create-geofence-collection \
  --collection-name "`ExampleGeofenceCollection`" \
  --description "Shopping center geofence collection" \
  --kms-key-id "`1234abcd-12ab-34cd-56ef-1234567890ab`" \
  --tags Tag1=Value1
```

###### Note

Billing depends on your usage. You might incur fees for the use of other AWS
services. For more information, see [Amazon Location Service pricing](https://aws.amazon.com/location/pricing/ "https://aws.amazon.com/location/pricing/").

## Draw geofences

Now that you've created your geofence collection, you can define your geofences.
Geofences are defined either as a polygon or as a circle. To draw a polygon geofence you
can use a GeoJSON editing tool, such as [geojson.io](http://geojson.io/ "http://geojson.io/").

To create a circular geofence, define the center point using the latitude and
longitude of the location and set the radius in meters. For more information, see
[Add circular geofences](#draw-circle-geofences "#draw-circle-geofences").

Using the Amazon Location Service APIs, you can also add metadata to your geofence in the form of
key-value pairs. These can be useful for storing information about the geofence, such as
its type, or other information that is specific to your application. You can use this
metadata when [React to Amazon Location Service events with Amazon EventBridge](location-events.md "location-events.md").

## Add polygon geofences

Polygon geofences use GeoJSON coordinate arrays to define an area. Use this format
when you need to track entries into or exits from an irregularly shaped geographic
boundary.

### Draw geofences using a GeoJSON tool

###### To create a GeoJSON file

1. Open a GeoJSON editing tool, such as [geojson.io](http://geojson.io/ "http://geojson.io/").
2. Choose the **Draw a polygon** icon and draw your area of
   interest.
3. Choose **Save**, then choose **GeoJSON**
   from the dropdown menu.

### Put GeoJSON geofences in a geofence collection

You can use the resulting GeoJSON file to upload your geofences using the Amazon Location Service
console, the AWS CLI, or the Amazon Location APIs.

Console

###### To add a geofence to a geofence collection using

the Amazon Location Service console

1. Open the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. In the left navigation pane, choose **Geofence
   collections**.
3. From the **Geofence collections** list,
   select the name link for the target geofence collection.
4. Under **Geofences**, choose
   **Create geofences**.
5. In the **Add geofences** window, drag and
   drop your GeoJSON into the window.
6. Choose **Add geofences**.

API

###### To add geofences using the Amazon Location

APIs

Use the `PutGeofence` operation from the Amazon Location
Geofences APIs.

The following example uses an API request to add a geofence with the
ID `GEOFENCE-EXAMPLE1` to a geofence collection
called `ExampleGeofenceCollection`. It also
specifies a geofence metadata property with the key `Type`
and value `loadingArea`.

```
PUT /geofencing/v0/collections/`ExampleGeofenceCollection`/geofences/`GEOFENCE-EXAMPLE1`
Content-type: application/json

{
   "GeofenceProperties": {
      "Type" : "loadingArea"
   },
   "Geometry": {
      "Polygon": [
        [
            [-5.716667, -15.933333],
            [-14.416667, -7.933333],
            [-12.316667, -37.066667],
            [-5.716667, -15.933333]
        ]
      ]
   }
}
```

Alternatively, you can add more than one geofence using the
`BatchPutGeofence` operation.

```
POST /geofencing/v0/collections/`ExampleGeofenceCollection`/put-geofences
Content-type: application/json

{
   "Entries": [
      {
         "GeofenceProperties": {
            "Type" : "loadingArea"
         },
         "GeofenceId": "`GEOFENCE-EXAMPLE1`",
         "Geometry": {
            "Polygon": [
               [
                  [-5.716667, -15.933333],
                  [-14.416667, -7.933333],
                  [-12.316667, -37.066667],
                  [-5.716667, -15.933333]
               ]
            ]
         }
      }
   ]
}
```

AWS CLI

###### To add a geofence to a geofence collection using

AWS CLI commands

Use the `put-geofence` command.

The following example uses the AWS CLI to add a geofence to a geofence
collection called
`ExampleGeofenceCollection`.

```
aws location \
    put-geofence \
        --collection-name `ExampleGeofenceCollection` \
        --geofence-id `ExampleGeofenceTriangle` \
        --geofence-properties '{"Type": "loadingArea"}' \
        --geometry 'Polygon=[[[-5.716667, -15.933333],[-14.416667, -7.933333],[-12.316667, -37.066667],[-5.716667, -15.933333]]]'
```

## Add circular geofences

To create a circular geofence, you must know the latitude and longitude of the center
point and the radius in meters. Use circular geofences when you need to trigger events
based on proximity to a specific point, such as a store, warehouse, or landmark. You can
create circular geofences with the Amazon Location console, the Amazon Location APIs, or the
AWS CLI.

Console

###### To add a circular geofence to a geofence collection

using the Amazon Location Service console

1. Open the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. In the left navigation pane, choose **Geofence
   collections**.
3. From the **Geofence collections** list, select
   the name link for the target geofence collection.
4. Under **Geofences**, choose **Create
   geofences**.
5. In the **Add geofences** window, choose
   **Circle**, then enter the center
   **Latitude**, **Longitude**,
   and **Radius** in meters.
6. Choose **Add geofences**.

API

###### To add circular geofences using the Amazon Location

APIs

Use the `PutGeofence` operation from the Amazon Location Geofences
APIs.

The following example uses an API request to add a geofence with the ID
`GEOFENCE-EXAMPLE2` to a geofence collection
called `ExampleGeofenceCollection`.

```
PUT /geofencing/v0/collections/`ExampleGeofenceCollection`/geofences/`GEOFENCE-EXAMPLE2`
Content-type: application/json

{
   "Geometry": {
      "Circle": {
        "Center": [-5.716667, -15.933333],
        "Radius": 50
      }
   }
}
```

AWS CLI

###### To add a circular geofence to a geofence collection

using AWS CLI commands

Use the `put-geofence` command.

The following example uses the AWS CLI to add a circular geofence to a
geofence collection called
`ExampleGeofenceCollection`.

```
aws location \
    put-geofence \
        --collection-name `ExampleGeofenceCollection` \
        --geofence-id `ExampleGeofenceCircle` \
        --geometry 'Circle={Center=[-5.716667, -15.933333], Radius=50}'
```

###### Note

You can also put JSON for complex geometry into its own file, as in
the following example.

```
aws location \
    put-geofence \
        --collection-name `ExampleGeofenceCollection` \
        --geofence-id `ExampleGeofenceCircle` \
        --geometry file://circle.json
```

Where `circle.json` contains the circle geometry.

```
{
    "Circle": {
        "Center": [-74.006975, 40.717127],
        "Radius": 287.7897969218057
    }
}
```
