

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Manage AWS IoT FleetWise vehicles
<a name="vehicles"></a>

Vehicles are instances of vehicle models. Vehicles must be created from a vehicle model and associated with a decoder manifest. Vehicles uploads one or more data streams to the cloud. For example, a vehicle can send mileage, engine temperature, and state of heater data to the cloud. Every vehicle contains the following information: 

`vehicleName`  
An ID that identifies the vehicle.  
Do not add personally identifiable information (PII) or other confidential or sensitive information in your vehicle name. Vehicle names are accessible by other AWS services, including Amazon CloudWatch. Vehicle names aren't intended to be used for private or sensitive data.

`modelManifestARN`  
The Amazon Resource Name (ARN) of a vehicle model (model manifest). Every vehicle is created from a vehicle model. Vehicles created from the same vehicle model consist of the same group of signals inherited from the vehicle model. These signals are defined and standardized in the signal catalog.

`decoderManifestArn`  
The ARN of the decoder manifest. A decoder manifest provides decoding information that AWS IoT FleetWise can use to transform raw signal data (binary data) into human-readable values. A decoder manifest must be associated with a vehicle model. AWS IoT FleetWise uses the same decoder manifest to decode raw data from vehicles created based on the same vehicle model.

`attributes`  
Attributes are key-value pairs that contain static information. Vehicles can contain attributes inherited from the vehicle model. You can add additional attributes to distinguish an individual vehicle from other vehicles created from the same vehicle model. For example, if you have a black car, you can specify the following value for an attribute: `{"color": "black"}`.  
Attributes must be defined in the associated vehicle model before you can add them to individual vehicles.

For more information about vehicle models, decoder manifests, and attributes, see [Model AWS IoT FleetWise vehicles](vehicle-modeling.md).

AWS IoT FleetWise provides the following API operations that you can use to create and manage vehicles.
+ [CreateVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateVehicle.html) – Creates a new vehicle.
+ [BatchCreateVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_BatchCreateVehicle.html) – Creates one or more new vehicles.
+ [UpdateVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateVehicle.html) – Updates an existing vehicle.
+ [BatchUpdateVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_BatchUpdateVehicle.html) – Updates one or more existing vehicles.
+ [DeleteVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteVehicle.html) – Deletes an existing vehicle.
+ [ListVehicles](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehicles.html) – Retrieves a paginated list of summaries of all vehicles.
+ [GetVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetVehicle.html) – Retrieves information about a vehicle.

**Topics**
+ [Provision AWS IoT FleetWise vehicles](provision-vehicles.md)
+ [Reserved topics in AWS IoT FleetWise](reserved-topics.md)
+ [Create an AWS IoT FleetWise vehicle](create-vehicle.md)
+ [Create multiple AWS IoT FleetWise vehicles](create-vehicles-cli.md)
+ [Update an AWS IoT FleetWise vehicle](update-vehicle-cli.md)
+ [Update multiple AWS IoT FleetWise vehicles](update-vehicles-cli.md)
+ [Delete an AWS IoT FleetWise vehicle](delete-vehicle.md)
+ [Get AWS IoT FleetWise vehicle information](get-vehicle-information-cli.md)