# Create component models

Use AWS IoT SiteWise component models to define subassemblies that you can reference from asset models
or other component models. In this way, you can re-use the definition of the component across
multiple other models, or multiple times within the same model.

The process of defining a component model is very similar to defining an asset model.
Like an asset model, a component model has a name, description, and asset properties.
However, component models can't include asset hierarchy definitions, since component models
themselves can't be used to create assets directly. Component models also can't define
alarms.

For example, you can define a component for a servo motor with motor temperature,
encoder temperature, and insulation resistance properties. Then, you can define an asset
model for equipment that contains servo motors, such as a CNC machine.

###### Note

- We recommend that you model your operation starting with the lowest-level nodes.
  For example, create your servo motor component before you create your CNC machine's
  asset model. Asset models contain references to existing component models.
- You can't create an asset directly from a component model. To create an asset that
  uses your component, you must create an asset model for your asset. Then, you create a
  custom composite model for it that references your component. For more information
  about creating asset models, see [Create asset models in AWS IoT SiteWise](create-asset-models.md "create-asset-models.md")

For more information about creating custom
composite models, see [Create custom composite models (components)](create-custom-composite-models.md "create-custom-composite-models.md").
The following sections describe how to use the AWS IoT SiteWise API to create component
models.

###### Topics

- [Create a component model (AWS CLI)](#create-component-model-cli "#create-component-model-cli")
- [Example component model](#component-model-example "#component-model-example")

## Create a component model (AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to create a component model.

Use the [CreateAssetModel](../APIReference/API_CreateAssetModel.md "../APIReference/API_CreateAssetModel.md") operation to create a component model with properties.
This operation expects a payload with the following structure:

```
{
  "assetModelType": "COMPONENT_MODEL",
  "assetModelName": "`String`",
  "assetModelDescription": "`String`",
  "assetModelProperties": `Array of AssetModelProperty`,
}
```

###### To create a component model (AWS CLI)

1. Create a file called `component-model-payload.json` and then
   copy the following JSON object into the file:

```
{
  "assetModelType": "COMPONENT_MODEL",
  "assetModelName": "",
  "assetModelDescription": "",
  "assetModelProperties": [

  ]
}
```

2. Use your preferred JSON text editor to edit the
   `component-model-payload.json` file for the following:
   1. Enter a name (`assetModelName`) for the component model, such as
      `Servo Motor` or `Servo Motor Model`.
      This name must be unique across all asset models and component models in your
      account in this AWS Region.
   2. (Optional) Enter an external ID (`assetModelExternalId`) for the
      component model. This is a user-defined ID. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.
   3. (Optional) Enter a description (`assetModelDescription`) for the
      asset model, or remove the `assetModelDescription` key-value
      pair.
   4. (Optional) Define asset properties (`assetModelProperties`) for the
      component model. For more information, see [Define data properties](asset-properties.md "asset-properties.md").
   5. (Optional) Add tags (`tags`) for the asset model. For more
      information, see [Tag your AWS IoT SiteWise resources](tag-resources.md "tag-resources.md").

3. Run the following command to create a component model from the definition in the
   JSON file.

```
aws iotsitewise create-asset-model --cli-input-json file://component-model-payload.json
```

The operation returns a response that contains the `assetModelId` that
you refer to when adding a reference to your component model in an asset model or
another component model. The response also contains the state of the model
(`assetModelStatus.state`), which is initially `CREATING`. The
component model's status is `CREATING` until the changes propagate.

###### Note

The component model creation process can take up to a few minutes for complex
models. To check the current status of your component model, use the [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md") operation by specifying the `assetModelId`.
After the component model status is `ACTIVE`, you can add references to
your component model in asset models or other component models.

For more information, see [Asset and model states](asset-and-model-states.md "asset-and-model-states.md"). 4. (Optional) Create custom composite models for your component model. With custom
composite models, you can group properties within the model, or to include a
subassembly by referencing another component model. For more information, see [Create custom composite models (components)](create-custom-composite-models.md "create-custom-composite-models.md").

## Example component model

This section contains an example component model definition that you can use to create
a component model with the AWS CLI and AWS IoT SiteWise SDKs. This component model represents a servo
motor that can be used within another piece of equipment, such as a
CNC
machine.

###### Topics

- [Servo motor component model](#example-servo-motor "#example-servo-motor")

### Servo motor component model

The following component model represents a servo motor that can be used within
equipment such as CNC machines. The servo motor provides various measurements, such as
temperatures and electrical resistance. These measurements are available as properties
on assets created from asset models that reference the servo motor component
model.

```
{
    "assetModelName": "ServoMotor",
    "assetModelType": "COMPONENT_MODEL",
    "assetModelProperties": [
        {
            "dataType": "DOUBLE",
            "name": "Servo Motor Temperature",
            "type": {
            "measurement": {}
            },
            "unit": "Celsius"
        },
        {
            "dataType": "DOUBLE",
            "name": "Spindle speed",
            "type": {
            "measurement": {}
            },
            "unit": "rpm"
        }
    ]
}
```
