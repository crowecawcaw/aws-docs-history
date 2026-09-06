

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Delete an AWS IoT FleetWise state template
<a name="delete-state-template"></a>

**Important**  
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

You can use the [DeleteStateTemplate](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteStateTemplate.html) API operation or AWS IoT FleetWise console to delete a state template.

## Delete a state template (console)
<a name="delete-template-console"></a>

To delete a state template from the console, go to the [State templates](https://console.aws.amazon.com/iotfleetwise/home#/stateTemplates) page of the AWS IoT FleetWise console and perform the following steps.

1. Choose the state template that you want to delete, and then choose **Delete**.

1. Confirm that you want to delete the state template, and then choose **Delete**.

## Delete a state template (AWS CLI)
<a name="delete-template-cli"></a>

To delete a state template, run the following command.

Replace {{identifier}} with the name or ID of the state template.

```
aws iotfleetwise delete-state-template \
    --identifier {{idenitfier}}
```