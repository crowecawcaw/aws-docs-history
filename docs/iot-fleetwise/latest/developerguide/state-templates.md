

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Create an AWS IoT FleetWise state template
<a name="state-templates"></a>

**Important**  
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

You can use the AWS IoT FleetWise API or console to create a state template. State templates provide a mechanism to track the state of your vehicles. The Edge Agent for AWS IoT FleetWise software that runs on the vehicle collects and sends signal updates to the cloud.

## Create a state template (console)
<a name="create-state-template-console"></a>

You can use the AWS IoT FleetWise console to create a state template.

**To create a state template**

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. On the navigation pane, choose **State templates**.

1. On the **State templates** page, choose **Create state template**.

1. In **State template details**, enter a name for the state template and optionally enter a description.

1. In **Choose signals**, add signals that you want to fetch vehicle status information from.

1. Choose **Create state template**.

After you successfully create a state template, you will see it listed on the **State templates** page. You can now associate it with a vehicle.

## Create a state template (AWS CLI)
<a name="create-state-templates-cli"></a>

You can use the [CreateStateTemplate](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateStateTemplate.html) API operation to create a state template. The following example uses the AWS CLI.

To create a state template, run the following command.

Replace {{create-state-template}} with the name of the .json file that contains the state template configuration.

```
aws iotfleetwise create-state-template \
    --cli-input-json file://{{create-state-template}}.json
```

**Example state template configuration**  
`stateTemplateProperties` should contain the fully qualified names of the signals.  
`dataExtraDimensions` and `metadataExtraDimensions` should contain the fully qualified names of the vehicle attributes. The dimensions specified replace any existing dimension values in the state template.  

```
{
    "name": "{{state-template-name}}",
    "signalCatalogArn": "arn:aws:iotfleetwise:{{us-east-1}}:{{account}}:signal-catalog/{{catalog-name}}",
    "stateTemplateProperties": [
        "Vehicle.Signal.One",
        "Vehicle.Signal.Two"
    ],
    "dataExtraDimensions": [
        "Vehicle.Attribute.One",
        "Vehicle.Attribute.Two"
    ],
    "metadataExtraDimensions": [
        "Vehicle.Attribute.Three",
        "Vehicle.Attribute.Four"
    ]
}
```

## Associate an AWS IoT FleetWise state template with a vehicle
<a name="apply-state-templates"></a>

### Associate a state template with a vehicle (console)
<a name="add-template-console"></a>

You can use the AWS IoT FleetWise console to add associated state templates to a vehicle.

**To associate a state template**

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. On the navigation pane, choose **Vehicles**.

1. Choose a vehicle from the list to open its details page.

1. On the **State templates** tab, choose **Manage state templates**.

1. Choose **Add state template**.

1. Select a state template and choose its reporting method.

   1. **On change** – The state template will report changes to the vehicle's state.

   1. **Periodic** – The state template will report updates on the specified time interval.

1. Choose **Save changes**.

### Associate an AWS IoT FleetWise state template with a vehicle (AWS CLI)
<a name="add-state-templates-cli"></a>

Associate the created state template with a vehicle to allow the collection of state updates from the vehicle to the cloud. To do this, use:
+ When creating a vehicle, use the `stateTemplates` field of the `create-vehicle` command. For more information, see [Create an AWS IoT FleetWise vehicle](create-vehicle.md#create-vehicle-cli).
+ When updating a vehicle, use the `stateTemplatesToAdd` or `stateTemplatesToRemove` fields of the `update-vehicle` command. For more information, see [Update an AWS IoT FleetWise vehicle](update-vehicle-cli.md).