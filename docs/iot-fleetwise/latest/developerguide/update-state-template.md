

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Update an AWS IoT FleetWise state template
<a name="update-state-template"></a>

**Important**  
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

You can use the [UpdateStateTemplate](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateStateTemplate.html) API operation or AWS IoT FleetWise console to update an existing state template.

## Update a state template (console)
<a name="update-template-console"></a>

To update a state template from the console, go to the [State templates](https://console.aws.amazon.com/iotfleetwise/home#/stateTemplates) page of the AWS IoT FleetWise console and perform the following steps.

1. Choose the state template that you want to update, and then choose **Edit**.

1. Edit the state template details, and then choose **Save changes**.

## Update a state template (AWS CLI)
<a name="update-template-cli"></a>

To update a state template, run the following command.

Replace {{update-state-template}} with the name of the .json file that contains the configuration of the state template.

```
aws iotfleetwise update-state-template \
    --cli-input-json file://{{update-state-template}}.json
```

**Example state template configuration**  
The `stateTemplateProperties` should contain the fully qualified names of the signals.  
The `dataExtraDimensions` and `metadataExtraDimensions` should contain the fully qualified names of the vehicle attributes.  

```
{
    "identifier": "{{state-template-name}}",
    "stateTemplatePropertiesToAdd": [
        "Vehicle.Signal.Three"
    ],
    "stateTemplatePropertiesToRemove": [
        "Vehicle.Signal.One"
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