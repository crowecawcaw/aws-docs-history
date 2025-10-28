# Create custom composite models (components)

Custom composite models, or components if you're using the console, provide another level of organization
for your asset models and component models. You can use them to structure your models by grouping properties or
referencing other models. For more information about working with custom composite models, see [Custom composite models (components)](custom-composite-models.md "custom-composite-models.md").

You create a custom composite model within an existing asset model or component model.
There are two types of custom composite models. To group related properties within
a model, you can create an **inline** custom composite model. To
reference a component model within your asset model or component model, you can create
a **component-model-based** custom composite model.

The following sections describe how to use the AWS IoT SiteWise API to create custom composite models.

###### Topics

- [Create an inline component (console)](#create-inline-component-console "#create-inline-component-console")
- [Create an inline custom composite model
  (AWS CLI)](#create-inline-composite-models-cli "#create-inline-composite-models-cli")
- [Create a component-model-based component
  (console)](#create-component-console "#create-component-console")
- [Create a component-model-based
  custom composite model (AWS CLI)](#create-component-based-composite-model-cli "#create-component-based-composite-model-cli")

## Create an inline component (console)

You can use the AWS IoT SiteWise console to create an inline component that defines its own properties.

###### Note

Because this is an _inline_ component, these properties only apply to the current
asset model and aren't shared anywhere else.

If you need to produce a reusable model (for example, to share among multiple asset models, or to include
multiple instances within one asset model), you should create a component based on a component model instead. See the following section for details.

###### To create a component (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models**.
3. Choose the asset model to which you want to add a component.
4. On the **Properties** tab, choose **Components**.
5. Choose **Create component**.
6. On the **Create component** page, do the following:
   1. Enter a **Name** for the component, such as `ServoMotor` or `ServoMotor Model`. This name must
      be unique across all components in your account in this Region.
   2. (Optional) Add **Attribute definitions** for the model.
      Attributes represent information that rarely changes. For more information, see
      [Define static data (attributes)](attributes.md "attributes.md").
   3. (Optional) Add **Measurement definitions** for the model.
      Measurements represent data streams from your equipment. For more information, see
      [Define data streams from equipment (measurements)](measurements.md "measurements.md").
   4. (Optional) Add **Transform definitions** for the model.
      Transforms are formulas that map data from one form to another. For more
      information, see [Transform data (transforms)](transforms.md "transforms.md").
   5. (Optional) Add **Metric definitions** for the model. Metrics
      are formulas that aggregate data over time intervals. Metrics can input data from
      associated assets, so that you can calculate values that represent your operation or
      a subset of your operation. For more information, see [Aggregate data from properties and other assets (metrics)](metrics.md "metrics.md").
   6. Choose **Create component**.

## Create an inline custom composite model

(AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to create an inline custom composite model that defines its own properties.

Use the [CreateAssetModelCompositeModel](../APIReference/API_CreateAssetModelCompositeModel.md "../APIReference/API_CreateAssetModelCompositeModel.md") operation to create an inline model with properties. This
operation expects a payload with the following structure.

###### Note

Because this is an _inline_ composite model, these properties only apply to the current
asset model and aren't shared anywhere else. What makes it "inline" is that it doesn't provide a value
for the `composedAssetModelId` field.

If you need to produce a reusable model (for example, to share among multiple asset models, or to include
multiple instances within one asset model), you should create a _component-model-based_
composite model instead. See the following section for details.

```
{
    "assetModelCompositeModelName": "CNCLathe_ServoMotorA",
    "assetModelCompositeModelType": "CUSTOM",
    "assetModelCompositeModelProperties": [
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

## Create a component-model-based component

(console)

You can use the AWS IoT SiteWise console to create a component based on a component model.

###### To create a component-model-based component (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models**.
3. Choose the asset model to which you want to add a component.
4. On the **Properties** tab, choose **Components**.
5. Choose **Create component**.
6. On the **Create component** page, do the following:
   1. Select the component model you want to based the component on.
   2. Enter a **Name** for the component, such as `ServoMotor` or `ServoMotor Model`. This name must
      be unique across all components in your account in this Region.
   3. Choose **Create component**.

## Create a component-model-based

custom composite model (AWS CLI)

You can use the AWS CLI to create a component-model-based custom composite model within your asset model.
A component-model-based custom composite model is a reference to a component model that you've already
defined elsewhere.

Use the [CreateAssetModelCompositeModel](../APIReference/API_CreateAssetModelCompositeModel.md "../APIReference/API_CreateAssetModelCompositeModel.md") operation to create a component-model-based custom composite model. This
operation expects a payload with the following structure.

###### Note

In this example, the value of `composedAssetModelId` is the asset model ID or external ID of an existing
component model. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_. For an example of how to create a component model, see [Create a component model (AWS CLI)](create-component-models.md#create-component-model-cli "create-component-models.md#create-component-model-cli").

```
{
    "assetModelCompositeModelName": "CNCLathe_ServoMotorA",
    "assetModelCompositeModelType": "CUSTOM",
    "composedAssetModelId": `component model ID`
]
```

Since it's just a reference, a component-model-based custom composite model has
no properties of its own, other than a name.

If you want to add multiple instances of the same component to your asset model (for example, a CNC
machine that has multiple servo motors), you can add multiple component-model-based custom composite models that each
have their own name but which all reference the same `composedAssetModelId`.

You can nest components within other components. To do so, you can add a component-model-based composite
model, as shown in this example, to one of your component models.
