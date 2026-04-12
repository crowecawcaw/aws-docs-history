AWS IoT FleetWise will no longer be open to new customers as of April 30, 2026. Existing
AWS IoT FleetWise customers can continue using the service. The
[Guidance
for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/ "https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/") provides guidance on how to develop and deploy modular
services for connected mobility solutions that can be used to achieve equivalent capabilities
as AWS IoT FleetWise.

# Manage fleets in AWS IoT FleetWise

A fleet represents a group of vehicles. A fleet without associated vehicles is an empty
entity. Before you can use the fleet to manage multiple vehicles at the same time, you must
associate vehicles with the fleet. A vehicle can belong to multiple fleets. You can control
what data to collect from a fleet of vehicles and when to collect data by deploying a
campaign. For more information, see [Collect AWS IoT FleetWise data with campaigns](campaigns.md "campaigns.md").

A fleet contains the following information.

`fleetId`

The ID of the fleet.

(Optional) `description`

A description that helps you find the fleet.

`signalCatalogArn`

The Amazon Resource Name (ARN) of the signal catalog.

AWS IoT FleetWise provides the following API operations that you can use to create and manage
fleets.

- [CreateFleet](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md")
  – Creates a group of vehicles that contain the same group of signals.
- [AssociateVehicleFleet](../APIReference/API_AssociateVehicle.md "../APIReference/API_AssociateVehicle.md") – Associates a vehicle to a fleet.
- [DisassociateVehicleFleet](../APIReference/API_DisassociateVehicle.md "../APIReference/API_DisassociateVehicle.md") – Disassociates a vehicle from a
  fleet.
- [UpdateFleet](../APIReference/API_UpdateFleet.md "../APIReference/API_UpdateFleet.md")
  – Updates the description for an existing fleet.
- [DeleteFleet](../APIReference/API_DeleteFleet.md "../APIReference/API_DeleteFleet.md")
  – Deletes an existing fleet.
- [ListFleets](../APIReference/API_ListFleets.md "../APIReference/API_ListFleets.md")
  – Retrieves a paginated list of summaries of all fleets.
- [ListFleetsForVehicle](../APIReference/API_ListFleetsForVehicle.md "../APIReference/API_ListFleetsForVehicle.md") – Retrieves a paginated list of IDs of all
  fleets that the vehicle belongs to.
- [ListVehiclesInFleet](../APIReference/API_ListVehiclesInFleet.md "../APIReference/API_ListVehiclesInFleet.md") – Retrieves a paginated list of summaries of
  all vehicles in a fleet.
- [GetFleet](../APIReference/API_GetFleet.md "../APIReference/API_GetFleet.md")
  – Retrieves information about a fleet.

###### Topics

- [Create an AWS IoT FleetWise fleet](create-fleet-cli.md "create-fleet-cli.md")
- [Associate an AWS IoT FleetWise vehicle with a fleet](associate-vehicle-cli.md "associate-vehicle-cli.md")
- [Disassociate an AWS IoT FleetWise vehicle from a fleet](disassociate-vehicle-cli.md "disassociate-vehicle-cli.md")
- [Update an AWS IoT FleetWise fleet](update-fleet-cli.md "update-fleet-cli.md")
- [Delete an AWS IoT FleetWise fleet](delete-fleet-cli.md "delete-fleet-cli.md")
- [Get AWS IoT FleetWise fleet information](get-fleet-information-cli.md "get-fleet-information-cli.md")
