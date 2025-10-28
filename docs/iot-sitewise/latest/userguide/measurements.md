# Define data streams from equipment (measurements)

A _measurement_ represents a device's raw sensor data
stream, such as timestamped temperature values or timestamped rotations per minute (RPM)
values.

###### Topics

- [Define measurements (console)](#define-measurements-console "#define-measurements-console")
- [Define measurements (AWS CLI)](#define-measurements-cli "#define-measurements-cli")

## Define measurements (console)

When you define a measurement for an asset model in the AWS IoT SiteWise console, you specify
following parameters:

- **Name** – The property's name.
- **Unit** – (Optional) The scientific unit for the property, such as mm or Celsius.
- **Data type** – The property's data type, which is one of the
  following:
  - **String** – A string with up to 1024 bytes.
  - **Integer** – A signed 32-bit integer with range [-2,147,483,648, 2,147,483,647].
  - **Double** – A floating point number with range [-10^100, 10^100] and IEEE 754 double precision.
  - **Boolean** – `true` or `false`.

- **External ID** – (Optional) This is a user-defined ID.
  For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.

For more information, see [Create an asset model (console)](create-asset-models.md#create-asset-model-console "create-asset-models.md#create-asset-model-console").

## Define measurements (AWS CLI)

When you define a measurement for an asset model with the AWS IoT SiteWise API, you specify
the following parameters:

- `name` – The property's name.
- `dataType` – The property's data type, which is one of the
  following:
  - `STRING` – A string with up to 1024 bytes.
  - `INTEGER` – A signed 32-bit integer with range [-2,147,483,648, 2,147,483,647].
  - `DOUBLE` – A floating point number with range [-10^100, 10^100] and IEEE 754 double precision.
  - `BOOLEAN` – `true` or `false`.

- `unit` – (Optional) The scientific unit for the property, such as mm or Celsius.
- `externalId` – (Optional) This is a user-defined ID. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.

###### Example measurement definition

The following example demonstrates a measurement that represents an asset's
temperature sensor readings. This object is an example of an [AssetModelProperty](../APIReference/API_AssetModelProperty.md "../APIReference/API_AssetModelProperty.md") that
contains a [Measurement](../APIReference/API_Measurement.md "../APIReference/API_Measurement.md"). You can specify this object as a part of the
[CreateAssetModel](../APIReference/API_CreateAssetModel.md "../APIReference/API_CreateAssetModel.md") request payload to create a measurement property. For more
information, see [Create an asset model (AWS CLI)](create-asset-models.md#create-asset-model-cli "create-asset-models.md#create-asset-model-cli").

The [Measurement](../APIReference/API_Measurement.md "../APIReference/API_Measurement.md") structure is an empty structure when you define an
asset model because you later configure each asset to use unique device data streams.
For more information about how to connect an asset's measurement property to a
device's sensor data stream, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").

```
{
      `...`
      "assetModelProperties": [
      {
          "name": "Temperature C",
          "dataType": "DOUBLE",
          "type": {
              "measurement": {}
          },
          "unit": "Celsius"
      }
  ],
      `...`
}
```
