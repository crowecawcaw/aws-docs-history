# Create an interface

You can create interfaces using either the AWS IoT SiteWise console or the AWS CLI.

Console

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/") and choose **Models** from
   the navigation pane.
2. Choose **Create interface**.
3. Enter a unique **Name** and optional
   **Description** for your interface. You can also optionally add
   an **External ID** of you choosing.
4. Add properties to your interface. You can add attributes, measurements,
   transforms, and metrics just like with asset models. For more information, see [Create an asset model (console)](create-asset-models.md#create-asset-model-console "create-asset-models.md#create-asset-model-console").
5. Choose **Create interface** to create the interface.
6. If you have hierarchies to define parent-child relationships between interfaces,
   choose **Add hierarchy** and enter relevant details.

AWS CLI
To create an interface, use the `CreateAssetModel` operation with the
`assetModelType` parameter set to `INTERFACE`:

```
aws iotsitewise create-asset-model \
  --asset-model-name "CNC-INTERFACE" \
  --asset-model-description "Standard interface for CNC machines" \
  --asset-model-type "INTERFACE" \
  --asset-model-properties '[
    {
      "name": "Temperature-in-C",
      "dataType": "DOUBLE",
      "type": {
        "measurement": {}
      },
      "unit": "Celsius"
    },
    {
      "name": "Down-time",
      "dataType": "DOUBLE",
      "type": {
        "measurement": {}
      },
      "unit": "Minutes"
    },
    {
      "name": "Running-time",
      "dataType": "DOUBLE",
      "type": {
        "measurement": {}
      },
      "unit": "Minutes"
    },
    {
      "name": "Availability",
      "dataType": "DOUBLE",
      "type": {
        "metric": {
          "expression": "Running-time / (Running-time + Down-time) * 100",
          "variables": [
            {
              "name": "Running-time",
              "value": {
                "propertyId": "${Running-time}"
              }
            },
            {
              "name": "Down-time",
              "value": {
                "propertyId": "${Down-time}"
              }
            }
          ],
          "window": {
            "tumbling": {
              "interval": "1h"
            }
          }
        }
      },
      "unit": "Percent"
    }
  ]'
```
