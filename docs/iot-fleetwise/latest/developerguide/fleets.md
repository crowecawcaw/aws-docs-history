

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Manage fleets in AWS IoT FleetWise
<a name="fleets"></a>

A fleet represents a group of vehicles. A fleet without associated vehicles is an empty entity. Before you can use the fleet to manage multiple vehicles at the same time, you must associate vehicles with the fleet. A vehicle can belong to multiple fleets. You can control what data to collect from a fleet of vehicles and when to collect data by deploying a campaign. For more information, see [Collect AWS IoT FleetWise data with campaigns](campaigns.md).

A fleet contains the following information.

`fleetId`  
The ID of the fleet.

(Optional) `description`  
A description that helps you find the fleet.

`signalCatalogArn`  
The Amazon Resource Name (ARN) of the signal catalog.

AWS IoT FleetWise provides the following API operations that you can use to create and manage fleets.
+ [CreateFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateFleet.html) – Creates a group of vehicles that contain the same group of signals.
+ [AssociateVehicleFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_AssociateVehicle.html) – Associates a vehicle to a fleet.
+ [DisassociateVehicleFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DisassociateVehicle.html) – Disassociates a vehicle from a fleet.
+ [UpdateFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateFleet.html) – Updates the description for an existing fleet.
+ [DeleteFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteFleet.html) – Deletes an existing fleet.
+ [ListFleets](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleets.html) – Retrieves a paginated list of summaries of all fleets.
+ [ListFleetsForVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleetsForVehicle.html) – Retrieves a paginated list of IDs of all fleets that the vehicle belongs to.
+ [ListVehiclesInFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehiclesInFleet.html) – Retrieves a paginated list of summaries of all vehicles in a fleet.
+ [GetFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetFleet.html) – Retrieves information about a fleet.

**Topics**
+ [Create an AWS IoT FleetWise fleet](create-fleet-cli.md)
+ [Associate an AWS IoT FleetWise vehicle with a fleet](associate-vehicle-cli.md)
+ [Disassociate an AWS IoT FleetWise vehicle from a fleet](disassociate-vehicle-cli.md)
+ [Update an AWS IoT FleetWise fleet](update-fleet-cli.md)
+ [Delete an AWS IoT FleetWise fleet](delete-fleet-cli.md)
+ [Get AWS IoT FleetWise fleet information](get-fleet-information-cli.md)