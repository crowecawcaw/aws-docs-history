# Update an AWS IoT FleetWise state template

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can use the [UpdateStateTemplate](../APIReference/API_UpdateStateTemplate.md "../APIReference/API_UpdateStateTemplate.md") API operation or AWS IoT FleetWise console to update an existing state
template.

To update a state template from the console, go to the [State templates](https://console.aws.amazon.com/iotfleetwise/home#/stateTemplates "https://console.aws.amazon.com/iotfleetwise/home#/stateTemplates") page of the AWS IoT FleetWise console and
perform the following steps.

1. Choose the state template that you want to update, and then choose **Edit**.
2. Edit the state template details, and then choose **Save changes**.
   To update a state template, run the following command.

Replace `update-state-template` with the name of the
.json file that contains the configuration of the state template.

```
aws iotfleetwise update-state-template \
    --cli-input-json file://`update-state-template`.json
```

###### Example state template configuration

The `stateTemplateProperties` should contain the fully qualified
names of the signals.

The `dataExtraDimensions` and `metadataExtraDimensions` should
contain the fully qualified names of the vehicle attributes.

```
{
    "identifier": "`state-template-name`",
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
