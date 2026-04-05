AWS IoT FleetWise will no longer be open to new customers starting April 30, 2026. If you would like to use AWS IoT FleetWise, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](iotfleetwise-availability-change.md "iotfleetwise-availability-change.md").

# Delete an AWS IoT FleetWise state template

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can use the [DeleteStateTemplate](../APIReference/API_DeleteStateTemplate.md "../APIReference/API_DeleteStateTemplate.md") API operation or AWS IoT FleetWise console to delete a state
template.

To delete a state template from the console, go to the [State templates](https://console.aws.amazon.com/iotfleetwise/home#/stateTemplates "https://console.aws.amazon.com/iotfleetwise/home#/stateTemplates") page of the AWS IoT FleetWise console and
perform the following steps.

1. Choose the state template that you want to delete, and then choose **Delete**.
2. Confirm that you want to delete the state template, and then choose **Delete**.
   To delete a state template, run the following command.

Replace `identifier` with the name or ID of the state
template.

```
aws iotfleetwise delete-state-template \
    --identifier `idenitfier`
```
