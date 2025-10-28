# Create asset models in AWS IoT SiteWise

AWS IoT SiteWise asset models drive standardization of your industrial data. An asset model
contains a name, description, asset properties, and asset hierarchy definitions. For
example, you can define a wind turbine model with temperature, rotations per minute (RPM),
and power properties. Then, you can define a wind farm model with a net power output
property and a wind turbine hierarchy definition.

###### Note

- We recommend that you model your operation starting with the lowest-level nodes.
  For example, create your wind turbine model before you create your wind farm model.
  Asset hierarchy definitions contain references to existing asset models. With this
  approach, you can define asset hierarchies as you create your models.
- Asset models can't contain other asset models. If you must define a model that you
  can reference as a subassembly within another model, you should create a component-->
  model instead. For more information, see [Create component models](create-component-models.md "create-component-models.md").
  The following sections describe how to use the AWS IoT SiteWise console or API to create asset
  models. The following sections also describe the different types of asset properties and
  asset hierarchies that you can use to create models.

###### Topics

- [Create an asset model (console)](#create-asset-model-console "#create-asset-model-console")
- [Create an asset model (AWS CLI)](#create-asset-model-cli "#create-asset-model-cli")
- [Example asset models](#asset-model-examples "#asset-model-examples")
- [Define asset model hierarchies](define-asset-hierarchies.md "define-asset-hierarchies.md")

## Create an asset model (console)

You can use the AWS IoT SiteWise console to create an asset model. The AWS IoT SiteWise console provides
various features, such as formula auto completion, that can help you define valid asset
models.

###### To create an asset model (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models**.
3. Choose **Create asset model**.
4. On the **Create model** page, do the following:
   1. Enter a **Name** for the asset model, such as `Wind
Turbine` or `Wind Turbine Model`. This name must
      be unique across all models in your account in this Region.
   2. (Optional) Add an **External ID** for the model. This is a
      user-defined ID. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.
   3. (Optional) Add **Measurement definitions** for the model.
      Measurements represent data streams from your equipment. For more information, see
      [Define data streams from equipment (measurements)](measurements.md "measurements.md").
   4. (Optional) Add **Transform definitions** for the model.
      Transforms are formulas that map data from one form to another. For more
      information, see [Transform data (transforms)](transforms.md "transforms.md").
   5. (Optional) Add **Metric definitions** for the model. Metrics
      are formulas that aggregate data over time intervals. Metrics can input data from
      associated assets, so that you can calculate values that represent your operation
      or a subset of your operation. For more information, see [Aggregate data from properties and other assets (metrics)](metrics.md "metrics.md").
   6. (Optional) Add **Hierarchy definitions** for the model.
      Hierarchies are relationships between assets. For more information, see [Define asset model hierarchies](define-asset-hierarchies.md "define-asset-hierarchies.md").
   7. (Optional) Add tags for the asset model. For more information, see [Tag your AWS IoT SiteWise resources](tag-resources.md "tag-resources.md").
   8. Choose **Create model**.When you create an asset model, the AWS IoT SiteWise console navigates to the new model's
      page. On this page, you can see the model's **Status**, which is
      initially **CREATING**. This page automatically updates, so you can
      wait for the model's status to update.

###### Note

The asset model creation process can take up to a few minutes for complex
models. After the asset model status is **ACTIVE**, you can use the
asset model to create assets. For more information, see [Asset and model states](asset-and-model-states.md "asset-and-model-states.md"). 5. (Optional) After you create your asset model, you can configure your asset model
for the edge. For more information about SiteWise Edge, see [Configure edge capabilities on
AWS IoT SiteWise Edge](edge-data-collection-and-processing.md "edge-data-collection-and-processing.md").

    1. On the model page, choose **Configure for Edge**.


    ###### Note

    The data processing pack (DPP) feature will no longer be open to new customers starting November 7, 2025 . If you would like to use DPP,
     sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
    [Data processing pack availability change](../appguide/iotsitewise-dpp-availability-change.md "../appguide/iotsitewise-dpp-availability-change.md").
    2. On the model configuration page, choose the edge configuration for your model.
     This controls where AWS IoT SiteWise can compute and store properties associated with this
     asset model. For more information about configuring your model for the edge, see
     [Set up an OPC UA source in
     SiteWise Edge](configure-opcua-source.md "configure-opcua-source.md").
    3. For **Custom edge configuration**, choose the location that
     you want AWS IoT SiteWise to compute and store each of your asset model properties.


    ###### Note

    Transforms and metrics that are associated must be configured for the same
     location. For more information about configuring your model for the edge, see
     [Set up an OPC UA source in
     SiteWise Edge](configure-opcua-source.md "configure-opcua-source.md").
    4. Choose **Save**. On the model page, your **Edge
     configuration** should now be **Configured**.

## Create an asset model (AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to create an asset model.

Use the [CreateAssetModel](../APIReference/API_CreateAssetModel.md "../APIReference/API_CreateAssetModel.md") operation to create an asset model with properties and
hierarchies. This operation expects a payload with the following structure.

```
{
  "assetModelType": "ASSET_MODEL",
  "assetModelName": "`String`",
  "assetModelDescription": "`String`",
  "assetModelProperties": `Array of AssetModelProperty`,
  "assetModelHierarchies": `Array of AssetModelHierarchyDefinition`
}
```

###### To create an asset model (AWS CLI)

1. Create a file called `asset-model-payload.json` and then copy
   the following JSON object into the file.

```
{
  "assetModelType": "ASSET_MODEL",
  "assetModelName": "",
  "assetModelDescription": "",
  "assetModelProperties": [

  ],
  "assetModelHierarchies": [

  ],
  "assetModelCompositeModels": [

  ]
}
```

2. Use your preferred JSON text editor to edit the
   `asset-model-payload.json` file for the following:
   1. Enter a name (`assetModelName`) for the asset model, such as
      `Wind Turbine` or `Wind Turbine
Model`. This name must be unique across all asset models and component
      models in your account in this AWS Region.
   2. (Optional) Enter an external ID (`assetModelExternalId`) for the asset
      model. This is a user-defined ID. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.
   3. (Optional) Enter a description (`assetModelDescription`) for the
      asset model, or remove the `assetModelDescription` key-value
      pair.
   4. (Optional) Define asset properties (`assetModelProperties`) for the
      model. For more information, see [Define data properties](asset-properties.md "asset-properties.md").
   5. (Optional) Define asset hierarchies (`assetModelHierarchies`) for
      the model. For more information, see [Define asset model hierarchies](define-asset-hierarchies.md "define-asset-hierarchies.md").
   6. (Optional) Define alarms for the model. Alarms monitor other properties so
      that you can identify when equipment or processes require attention. Each alarm

   definition is a composite model (`assetModelCompositeModels`) that
   standardizes the set of properties that the alarm uses. For more information, see
   [Monitor data with alarms in AWS IoT SiteWise](industrial-alarms.md "industrial-alarms.md") and [Define alarms on asset models in AWS IoT SiteWise](define-alarms.md "define-alarms.md"). 7. (Optional) Add tags (`tags`) for the asset model. For more
   information, see [Tag your AWS IoT SiteWise resources](tag-resources.md "tag-resources.md").

3. Run the following command to create an asset model from the definition in the JSON
   file.

```
aws iotsitewise create-asset-model --cli-input-json file://asset-model-payload.json
```

The operation returns a response that contains the `assetModelId` that
you refer to when creating an asset. The response also contains the state of the model
(`assetModelStatus.state`), which is initially `CREATING`. The
asset model's status is `CREATING` until the changes propagate.

###### Note

The asset model creation process can take up to a few minutes for complex
models. To check the current status of your asset model, use the [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md") operation by specifying the `assetModelId`.
After the asset model status is `ACTIVE`, you can use the asset model to
create assets. For more information, see [Asset and model states](asset-and-model-states.md "asset-and-model-states.md"). 4. (Optional) Create custom composite models for your asset model. With custom
composite models, you can group properties within the model, or include a subassembly
by referencing a component model. For more information, see [Create custom composite models (components)](create-custom-composite-models.md "create-custom-composite-models.md").

## Example asset models

This section contains example asset models definitions that you can use to create
asset models with the AWS CLI and AWS IoT SiteWise SDKs. These asset models represent a wind turbine
and a wind farm. Wind turbine assets ingest raw sensor data and calculate values such as
power and average wind speed. Wind farm assets calculate values such as total power for
all wind turbines in the wind farm.

###### Topics

- [Wind turbine asset model](#example-wind-turbine "#example-wind-turbine")
- [Wind farm asset model](#example-wind-farm "#example-wind-farm")

### Wind turbine asset model

The following asset model represents a turbine in a wind farm. The wind turbine
ingests sensor data to calculate values such as power and average wind speed.

###### Note

This example model resembles the wind turbine model from the AWS IoT SiteWise demo. For more
information, see [Use the AWS IoT SiteWise demo](getting-started-demo.md "getting-started-demo.md").

```
{
  "assetModelType": "ASSET_MODEL",
  "assetModelName": "Wind Turbine Asset Model",
  "assetModelDescription": "Represents a turbine in a wind farm.",
  "assetModelProperties": [
    {
      "name": "Location",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "Renton"
        }
      }
    },
    {
      "name": "Make",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "Amazon"
        }
      }
    },
    {
      "name": "Model",
      "dataType": "INTEGER",
      "type": {
        "attribute": {
          "defaultValue": "500"
        }
      }
    },
    {
      "name": "Torque (KiloNewton Meter)",
      "dataType": "DOUBLE",
      "unit": "kNm",
      "type": {
        "measurement": {}
      }
    },
    {
      "name": "Wind Direction",
      "dataType": "DOUBLE",
      "unit": "Degrees",
      "type": {
        "measurement": {}
      }
    },
    {
      "name": "RotationsPerMinute",
      "dataType": "DOUBLE",
      "unit": "RPM",
      "type": {
        "measurement": {}
      }
    },
    {
      "name": "Wind Speed",
      "dataType": "DOUBLE",
      "unit": "m/s",
      "type": {
        "measurement": {}
      }
    },
    {
      "name": "RotationsPerSecond",
      "dataType": "DOUBLE",
      "unit": "RPS",
      "type": {
        "transform": {
          "expression": "rpm / 60",
          "variables": [
            {
              "name": "rpm",
              "value": {
                "propertyId": "RotationsPerMinute"
              }
            }
          ]
        }
      }
    },
    {
      "name": "Overdrive State",
      "dataType": "DOUBLE",
      "type": {
        "transform": {
          "expression": "gte(torque, 3)",
          "variables": [
            {
              "name": "torque",
              "value": {
                "propertyId": "Torque (KiloNewton Meter)"
              }
            }
          ]
        }
      }
    },
    {
      "name": "Average Power",
      "dataType": "DOUBLE",
      "unit": "Watts",
      "type": {
        "metric": {
          "expression": "avg(torque) * avg(rps) * 2 * 3.14",
          "variables": [
            {
              "name": "torque",
              "value": {
                "propertyId": "Torque (Newton Meter)"
              }
            },
            {
              "name": "rps",
              "value": {
                "propertyId": "RotationsPerSecond"
              }
            }
          ],
          "window": {
            "tumbling": {
              "interval": "5m"
            }
          }
        }
      }
    },
    {
      "name": "Average Wind Speed",
      "dataType": "DOUBLE",
      "unit": "m/s",
      "type": {
        "metric": {
          "expression": "avg(windspeed)",
          "variables": [
            {
              "name": "windspeed",
              "value": {
                "propertyId": "Wind Speed"
              }
            }
          ],
          "window": {
            "tumbling": {
              "interval": "5m"
            }
          }
        }
      }
    },
    {
      "name": "Torque (Newton Meter)",
      "dataType": "DOUBLE",
      "unit": "Nm",
      "type": {
        "transform": {
          "expression": "knm * 1000",
          "variables": [
            {
              "name": "knm",
              "value": {
                "propertyId": "Torque (KiloNewton Meter)"
              }
            }
          ]
        }
      }
    },
    {
      "name": "Overdrive State Time",
      "dataType": "DOUBLE",
      "unit": "Seconds",
      "type": {
        "metric": {
          "expression": "statetime(overdrive_state)",
          "variables": [
            {
              "name": "overdrive_state",
              "value": {
                "propertyId": "Overdrive State"
              }
            }
          ],
          "window": {
            "tumbling": {
              "interval": "5m"
            }
          }
        }
      }
    }
  ],
  "assetModelHierarchies": []
}
```

### Wind farm asset model

The following asset model represents a wind farm that comprises multiple wind
turbines. This asset model defines a [hierarchy](define-asset-hierarchies.md "define-asset-hierarchies.md")
to the wind turbine model. This lets the wind farm calculate values (such as average
power) from data for all wind turbines in the wind farm.

###### Note

This example model resembles the wind farm model from the AWS IoT SiteWise demo. For more
information, see [Use the AWS IoT SiteWise demo](getting-started-demo.md "getting-started-demo.md").

This asset model depends on the [Wind turbine asset model](#example-wind-turbine "#example-wind-turbine"). Replace the `propertyId` and
`childAssetModelId` values with those from an existing wind turbine asset
model.

```
{
  "assetModelName": "Wind Farm Asset Model",
  "assetModelDescription": "Represents a wind farm.",
  "assetModelProperties": [
    {
      "name": "Code",
      "dataType": "INTEGER",
      "type": {
        "attribute": {
          "defaultValue": "300"
        }
      }
    },
    {
      "name": "Location",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "Renton"
        }
      }
    },
    {
      "name": "Reliability Manager",
      "dataType": "STRING",
      "type": {
        "attribute": {
          "defaultValue": "Mary Major"
        }
      }
    },
    {
      "name": "Total Overdrive State Time",
      "dataType": "DOUBLE",
      "unit": "seconds",
      "type": {
        "metric": {
          "expression": "sum(overdrive_state_time)",
          "variables": [
            {
              "name": "overdrive_state_time",
              "value": {
                "propertyId": "`ID of Overdrive State Time property in Wind Turbine Asset Model`",
                "hierarchyId": "Turbine Asset Model"
              }
            }
          ],
          "window": {
            "tumbling": {
              "interval": "5m"
            }
          }
        }
      }
    },
    {
      "name": "Total Average Power",
      "dataType": "DOUBLE",
      "unit": "Watts",
      "type": {
        "metric": {
          "expression": "sum(turbine_avg_power)",
          "variables": [
            {
              "name": "turbine_avg_power",
              "value": {
                "propertyId": "`ID of Average Power property in Wind Turbine Asset Model`",
                "hierarchyId": "Turbine Asset Model"
              }
            }
          ],
          "window": {
            "tumbling": {
              "interval": "5m"
            }
          }
        }
      }
    }
  ],
  "assetModelHierarchies": [
    {
      "name": "Turbine Asset Model",
      "childAssetModelId": "`ID of Wind Turbine Asset Model`"
    }
  ]
}
```
