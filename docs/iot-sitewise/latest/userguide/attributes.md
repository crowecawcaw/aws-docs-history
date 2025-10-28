# Define static data (attributes)

_Asset attributes_ represent information that is
generally static, such as device manufacturer or geographic location. Each asset that you
create from an asset model contains the attributes of that model.

###### Topics

- [Define attributes (console)](#define-attributes-console "#define-attributes-console")
- [Define attributes (AWS CLI)](#define-attributes-cli "#define-attributes-cli")

## Define attributes (console)

When you define an attribute for an asset model in the AWS IoT SiteWise console, you specify
the following parameters:

- **Name** – The property's name.
- **Default value** – (Optional) The default value for
  this attribute. Assets created from the model have this value for the attribute. For
  more information about how to override the default value in an asset created from a
  model, see [Update attribute values](update-attribute-values.md "update-attribute-values.md").
- **Data type** – The property's data type, which is one of the
  following:
  - **String** – A string with up to 1024 bytes.
  - **Integer** – A signed 32-bit integer with range [-2,147,483,648, 2,147,483,647].
  - **Double** – A floating point number with range [-10^100, 10^100] and IEEE 754 double precision.
  - **Boolean** – `true` or `false`.

- **External ID** – (Optional) This is a user-defined ID.
  For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.

For more information, see [Create an asset model (console)](create-asset-models.md#create-asset-model-console "create-asset-models.md#create-asset-model-console").

## Define attributes (AWS CLI)

When you define an attribute for an asset model with the AWS IoT SiteWise API, you specify the
following parameters:

- `name` – The property's name.
- `defaultValue` – (Optional) The default value for
  this attribute. Assets created from the model have this value for the attribute. For
  more information about how to override the default value in an asset created from a
  model, see [Update attribute values](update-attribute-values.md "update-attribute-values.md").
- `dataType` – The property's data type, which is one of the
  following:
  - `STRING` – A string with up to 1024 bytes.
  - `INTEGER` – A signed 32-bit integer with range [-2,147,483,648, 2,147,483,647].
  - `DOUBLE` – A floating point number with range [-10^100, 10^100] and IEEE 754 double precision.
  - `BOOLEAN` – `true` or `false`.

- `externalId` – (Optional) This is a user-defined ID. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.

###### Example attribute definition

The following example demonstrates an attribute that represents an asset's model
number with a default value. This object is an example of an [AssetModelProperty](../APIReference/API_AssetModelProperty.md "../APIReference/API_AssetModelProperty.md") that
contains an [Attribute](../APIReference/API_Attribute.md "../APIReference/API_Attribute.md"). You can specify this object as a part of the
[CreateAssetModel](../APIReference/API_CreateAssetModel.md "../APIReference/API_CreateAssetModel.md") request payload to create an attribute property. For more
information, see [Create an asset model (AWS CLI)](create-asset-models.md#create-asset-model-cli "create-asset-models.md#create-asset-model-cli").

```
{
`...`
"assetModelProperties": [
{
  "name": "Model number",
  "dataType": "STRING",
  "type": {
    "attribute": {
      "defaultValue": "BLT123"
    }
  }
}
],
`...`
}
```
