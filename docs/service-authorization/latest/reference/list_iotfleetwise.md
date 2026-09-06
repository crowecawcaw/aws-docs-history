

# Actions, resources, and condition keys for AWS IoT FleetWise
<a name="list_iotfleetwise"></a>

AWS IoT FleetWise (service prefix: `iotfleetwise`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotfleetwise/iotfleetwise.json) for this service.

**Topics**
+ [API operations defined by AWS IoT FleetWise](#list_iotfleetwise-operations)
+ [Actions defined by AWS IoT FleetWise](#list_iotfleetwise-actions-as-permissions)
+ [Permission-only actions for AWS IoT FleetWise](#list_iotfleetwise-permission-only-actions)
+ [Resource types defined by AWS IoT FleetWise](#list_iotfleetwise-resources-for-iam-policies)
+ [Condition keys for AWS IoT FleetWise](#list_iotfleetwise-policy-keys)

## API operations defined by AWS IoT FleetWise
<a name="list_iotfleetwise-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iotfleetwise-actions-as-permissions).




- **   AssociateVehicleFleet  **
  - **IAM action:**  [iotfleetwise:AssociateVehicleFleet](#list_iotfleetwise-action-AssociateVehicleFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchCreateVehicle  **
  - **IAM action:**  [iotfleetwise:CreateVehicle](#list_iotfleetwise-action-CreateVehicle)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCampaign  **
  - **IAM action:**  [iotfleetwise:CreateCampaign](#list_iotfleetwise-action-CreateCampaign)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotfleetwise.amazonaws.com / **Access level:** Write

- **   CreateDecoderManifest  **
  - **IAM action:**  [iotfleetwise:CreateDecoderManifest](#list_iotfleetwise-action-CreateDecoderManifest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFleet  **
  - **IAM action:**  [iotfleetwise:CreateFleet](#list_iotfleetwise-action-CreateFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateModelManifest  **
  - **IAM action:**  [iotfleetwise:CreateModelManifest](#list_iotfleetwise-action-CreateModelManifest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSignalCatalog  **
  - **IAM action:**  [iotfleetwise:CreateSignalCatalog](#list_iotfleetwise-action-CreateSignalCatalog)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStateTemplate  **
  - **IAM action:**  [iotfleetwise:CreateStateTemplate](#list_iotfleetwise-action-CreateStateTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVehicle  **
  - **IAM action:**  [iotfleetwise:CreateVehicle](#list_iotfleetwise-action-CreateVehicle)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCampaign  **
  - **IAM action:**  [iotfleetwise:DeleteCampaign](#list_iotfleetwise-action-DeleteCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDecoderManifest  **
  - **IAM action:**  [iotfleetwise:DeleteDecoderManifest](#list_iotfleetwise-action-DeleteDecoderManifest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFleet  **
  - **IAM action:**  [iotfleetwise:DeleteFleet](#list_iotfleetwise-action-DeleteFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModelManifest  **
  - **IAM action:**  [iotfleetwise:DeleteModelManifest](#list_iotfleetwise-action-DeleteModelManifest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSignalCatalog  **
  - **IAM action:**  [iotfleetwise:DeleteSignalCatalog](#list_iotfleetwise-action-DeleteSignalCatalog) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStateTemplate  **
  - **IAM action:**  [iotfleetwise:DeleteStateTemplate](#list_iotfleetwise-action-DeleteStateTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVehicle  **
  - **IAM action:**  [iotfleetwise:DeleteVehicle](#list_iotfleetwise-action-DeleteVehicle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateVehicleFleet  **
  - **IAM action:**  [iotfleetwise:DisassociateVehicleFleet](#list_iotfleetwise-action-DisassociateVehicleFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCampaign  **
  - **IAM action:**  [iotfleetwise:GetCampaign](#list_iotfleetwise-action-GetCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDecoderManifest  **
  - **IAM action:**  [iotfleetwise:GetDecoderManifest](#list_iotfleetwise-action-GetDecoderManifest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEncryptionConfiguration  **
  - **IAM action:**  [iotfleetwise:GetEncryptionConfiguration](#list_iotfleetwise-action-GetEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFleet  **
  - **IAM action:**  [iotfleetwise:GetFleet](#list_iotfleetwise-action-GetFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLoggingOptions  **
  - **IAM action:**  [iotfleetwise:GetLoggingOptions](#list_iotfleetwise-action-GetLoggingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetModelManifest  **
  - **IAM action:**  [iotfleetwise:GetModelManifest](#list_iotfleetwise-action-GetModelManifest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegisterAccountStatus  **
  - **IAM action:**  [iotfleetwise:GetRegisterAccountStatus](#list_iotfleetwise-action-GetRegisterAccountStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSignalCatalog  **
  - **IAM action:**  [iotfleetwise:GetSignalCatalog](#list_iotfleetwise-action-GetSignalCatalog) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStateTemplate  **
  - **IAM action:**  [iotfleetwise:GetStateTemplate](#list_iotfleetwise-action-GetStateTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVehicle  **
  - **IAM action:**  [iotfleetwise:GetVehicle](#list_iotfleetwise-action-GetVehicle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVehicleStatus  **
  - **IAM action:**  [iotfleetwise:GetVehicleStatus](#list_iotfleetwise-action-GetVehicleStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportDecoderManifest  **
  - **IAM action:**  [iotfleetwise:ImportDecoderManifest](#list_iotfleetwise-action-ImportDecoderManifest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ImportSignalCatalog  **
  - **IAM action:**  [iotfleetwise:ImportSignalCatalog](#list_iotfleetwise-action-ImportSignalCatalog)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListCampaigns  **
  - **IAM action:**  [iotfleetwise:ListCampaigns](#list_iotfleetwise-action-ListCampaigns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDecoderManifestNetworkInterfaces  **
  - **IAM action:**  [iotfleetwise:ListDecoderManifestNetworkInterfaces](#list_iotfleetwise-action-ListDecoderManifestNetworkInterfaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDecoderManifestSignals  **
  - **IAM action:**  [iotfleetwise:ListDecoderManifestSignals](#list_iotfleetwise-action-ListDecoderManifestSignals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDecoderManifests  **
  - **IAM action:**  [iotfleetwise:ListDecoderManifests](#list_iotfleetwise-action-ListDecoderManifests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFleets  **
  - **IAM action:**  [iotfleetwise:ListFleets](#list_iotfleetwise-action-ListFleets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFleetsForVehicle  **
  - **IAM action:**  [iotfleetwise:ListFleetsForVehicle](#list_iotfleetwise-action-ListFleetsForVehicle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListModelManifestNodes  **
  - **IAM action:**  [iotfleetwise:ListModelManifestNodes](#list_iotfleetwise-action-ListModelManifestNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelManifests  **
  - **IAM action:**  [iotfleetwise:ListModelManifests](#list_iotfleetwise-action-ListModelManifests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSignalCatalogNodes  **
  - **IAM action:**  [iotfleetwise:ListSignalCatalogNodes](#list_iotfleetwise-action-ListSignalCatalogNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSignalCatalogs  **
  - **IAM action:**  [iotfleetwise:ListSignalCatalogs](#list_iotfleetwise-action-ListSignalCatalogs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListStateTemplates  **
  - **IAM action:**  [iotfleetwise:ListStateTemplates](#list_iotfleetwise-action-ListStateTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [iotfleetwise:ListTagsForResource](#list_iotfleetwise-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVehicles  **
  - **IAM action:**  [iotfleetwise:ListVehicles](#list_iotfleetwise-action-ListVehicles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVehiclesInFleet  **
  - **IAM action:**  [iotfleetwise:ListVehiclesInFleet](#list_iotfleetwise-action-ListVehiclesInFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutEncryptionConfiguration  **
  - **IAM action:**  [iotfleetwise:PutEncryptionConfiguration](#list_iotfleetwise-action-PutEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutLoggingOptions  **
  - **IAM action:**  [iotfleetwise:PutLoggingOptions](#list_iotfleetwise-action-PutLoggingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterAccount  **
  - **IAM action:**  [iotfleetwise:RegisterAccount](#list_iotfleetwise-action-RegisterAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [iotfleetwise:TagResource](#list_iotfleetwise-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [iotfleetwise:UntagResource](#list_iotfleetwise-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCampaign  **
  - **IAM action:**  [iotfleetwise:UpdateCampaign](#list_iotfleetwise-action-UpdateCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDecoderManifest  **
  - **IAM action:**  [iotfleetwise:UpdateDecoderManifest](#list_iotfleetwise-action-UpdateDecoderManifest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFleet  **
  - **IAM action:**  [iotfleetwise:UpdateFleet](#list_iotfleetwise-action-UpdateFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateModelManifest  **
  - **IAM action:**  [iotfleetwise:UpdateModelManifest](#list_iotfleetwise-action-UpdateModelManifest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSignalCatalog  **
  - **IAM action:**  [iotfleetwise:UpdateSignalCatalog](#list_iotfleetwise-action-UpdateSignalCatalog) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStateTemplate  **
  - **IAM action:**  [iotfleetwise:UpdateStateTemplate](#list_iotfleetwise-action-UpdateStateTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVehicle  **
  - **IAM action:**  [iotfleetwise:UpdateVehicle](#list_iotfleetwise-action-UpdateVehicle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS IoT FleetWise
<a name="list_iotfleetwise-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateVehicleFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_AssociateVehicleFleet.html)  **
  - **Description:** Grants permission to associate the given vehicle to a fleet
  - **Resource types (\*required):** [fleet\*](#list_iotfleetwise-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCampaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateCampaign.html)  **
  - **Description:** Grants permission to create a campaign
  - **Resource types (\*required):** [campaign\*](#list_iotfleetwise-resource-campaign) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)<br />[iotfleetwise:DestinationArn](#list_iotfleetwise-iotfleetwise_DestinationArn)
  - **Resource types (\*required):** [fleet\*](#list_iotfleetwise-resource-fleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)<br />[iotfleetwise:DestinationArn](#list_iotfleetwise-iotfleetwise_DestinationArn)
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)<br />[iotfleetwise:DestinationArn](#list_iotfleetwise-iotfleetwise_DestinationArn)
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)<br />[iotfleetwise:DestinationArn](#list_iotfleetwise-iotfleetwise_DestinationArn)
  - **Access level:** Write

- **   [CreateDecoderManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateDecoderManifest.html)  **
  - **Description:** Grants permission to create a decoder manifest for an existing model
  - **Resource types (\*required):** [decodermanifest\*](#list_iotfleetwise-resource-decodermanifest) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [modelmanifest\*](#list_iotfleetwise-resource-modelmanifest) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateFleet.html)  **
  - **Description:** Grants permission to create a fleet
  - **Resource types (\*required):** [fleet\*](#list_iotfleetwise-resource-fleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateModelManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateModelManifest.html)  **
  - **Description:** Grants permission to create a model manifest definition
  - **Resource types (\*required):** [modelmanifest\*](#list_iotfleetwise-resource-modelmanifest) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateSignalCatalog.html)  **
  - **Description:** Grants permission to create a signal catalog
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStateTemplate](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateStateTemplate.html)  **
  - **Description:** Grants permission to create a state template
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [statetemplate\*](#list_iotfleetwise-resource-statetemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateVehicle.html)  **
  - **Description:** Grants permission to create a vehicle
  - **Resource types (\*required):** [decodermanifest\*](#list_iotfleetwise-resource-decodermanifest) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [modelmanifest\*](#list_iotfleetwise-resource-modelmanifest) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCampaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteCampaign.html)  **
  - **Description:** Grants permission to delete a campaign
  - **Resource types (\*required):** [campaign\*](#list_iotfleetwise-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDecoderManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteDecoderManifest.html)  **
  - **Description:** Grants permission to delete the given decoder manifest
  - **Resource types (\*required):** [decodermanifest\*](#list_iotfleetwise-resource-decodermanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteFleet.html)  **
  - **Description:** Grants permission to delete a fleet
  - **Resource types (\*required):** [fleet\*](#list_iotfleetwise-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteModelManifest.html)  **
  - **Description:** Grants permission to delete the given model manifest
  - **Resource types (\*required):** [modelmanifest\*](#list_iotfleetwise-resource-modelmanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteSignalCatalog.html)  **
  - **Description:** Grants permission to delete a specific signal catalog
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStateTemplate](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteStateTemplate.html)  **
  - **Description:** Grants permission to delete a state template
  - **Resource types (\*required):** [statetemplate\*](#list_iotfleetwise-resource-statetemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteVehicle.html)  **
  - **Description:** Grants permission to delete a vehicle
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateVehicleFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DisassociateVehicleFleet.html)  **
  - **Description:** Grants permission to disassociate a vehicle from an existing fleet
  - **Resource types (\*required):** [fleet\*](#list_iotfleetwise-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCampaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetCampaign.html)  **
  - **Description:** Grants permission to get summary information for a given campaign
  - **Resource types (\*required):** [campaign\*](#list_iotfleetwise-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDecoderManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetDecoderManifest.html)  **
  - **Description:** Grants permission to get summary information for a given decoder manifest definition
  - **Resource types (\*required):** [decodermanifest\*](#list_iotfleetwise-resource-decodermanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEncryptionConfiguration](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetEncryptionConfiguration.html)  **
  - **Description:** Grants permission to get KMS-based encryption status for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetFleet.html)  **
  - **Description:** Grants permission to get summary information for a fleet
  - **Resource types (\*required):** [fleet\*](#list_iotfleetwise-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLoggingOptions](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetLoggingOptions.html)  **
  - **Description:** Grants permission to get the logging options for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetModelManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetModelManifest.html)  **
  - **Description:** Grants permission to get summary information for a given model manifest definition
  - **Resource types (\*required):** [modelmanifest\*](#list_iotfleetwise-resource-modelmanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegisterAccountStatus](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetRegisterAccountStatus.html)  **
  - **Description:** Grants permission to get the account registration status with IoT FleetWise
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetSignalCatalog.html)  **
  - **Description:** Grants permission to get summary information for a specific signal catalog
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStateTemplate](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetStateTemplate.html)  **
  - **Description:** Grants permission to get summary information for a given state template
  - **Resource types (\*required):** [statetemplate\*](#list_iotfleetwise-resource-statetemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetVehicle.html)  **
  - **Description:** Grants permission to get summary information for a vehicle
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVehicleStatus](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetVehicleStatus.html)  **
  - **Description:** Grants permission to get the status of the campaigns running on a specific vehicle
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportDecoderManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ImportDecoderManifest.html)  **
  - **Description:** Grants permission to import an existing decoder manifest
  - **Resource types (\*required):** [decodermanifest\*](#list_iotfleetwise-resource-decodermanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ImportSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ImportSignalCatalog.html)  **
  - **Description:** Grants permission to create a signal catalog by importing existing definitions
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Access level:** Write

- **   [ListCampaigns](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListCampaigns.html)  **
  - **Description:** Grants permission to list campaigns
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDecoderManifestNetworkInterfaces](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifestNetworkInterfaces.html)  **
  - **Description:** Grants permission to list network interfaces associated to the existing decoder manifest
  - **Resource types (\*required):** [decodermanifest\*](#list_iotfleetwise-resource-decodermanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDecoderManifestSignals](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifestSignals.html)  **
  - **Description:** Grants permission to list decoder manifest signals
  - **Resource types (\*required):** [decodermanifest\*](#list_iotfleetwise-resource-decodermanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDecoderManifests](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifests.html)  **
  - **Description:** Grants permission to list all decoder manifests, with an optional filter on model manifest
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListFleets](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleets.html)  **
  - **Description:** Grants permission to list all fleets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListFleetsForVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleetsForVehicle.html)  **
  - **Description:** Grants permission to list all the fleets that the given vehicle is associated with
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListModelManifestNodes](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListModelManifestNodes.html)  **
  - **Description:** Grants permission to list all nodes for the given model manifest
  - **Resource types (\*required):** [modelmanifest\*](#list_iotfleetwise-resource-modelmanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListModelManifests](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListModelManifests.html)  **
  - **Description:** Grants permission to list all model manifests, with an optional filter on signal catalog
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSignalCatalogNodes](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListSignalCatalogNodes.html)  **
  - **Description:** Grants permission to list all nodes for a given signal catalog
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSignalCatalogs](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListSignalCatalogs.html)  **
  - **Description:** Grants permission to list all signal catalogs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListStateTemplates](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListStateTemplates.html)  **
  - **Description:** Grants permission to list state templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [campaign](#list_iotfleetwise-resource-campaign) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [decodermanifest](#list_iotfleetwise-resource-decodermanifest) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [fleet](#list_iotfleetwise-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [modelmanifest](#list_iotfleetwise-resource-modelmanifest) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [signalcatalog](#list_iotfleetwise-resource-signalcatalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [statetemplate](#list_iotfleetwise-resource-statetemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [vehicle](#list_iotfleetwise-resource-vehicle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListVehicles](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehicles.html)  **
  - **Description:** Grants permission to list all vehicles, with an optional filter on model manifest
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListVehiclesInFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehiclesInFleet.html)  **
  - **Description:** Grants permission to list vehicles in the given fleet
  - **Resource types (\*required):** [fleet\*](#list_iotfleetwise-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutEncryptionConfiguration](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_PutEncryptionConfiguration.html)  **
  - **Description:** Grants permission to enable or disable KMS-based encryption for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutLoggingOptions](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_PutLoggingOptions.html)  **
  - **Description:** Grants permission to put the logging options for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterAccount](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_RegisterAccount.html)  **
  - **Description:** Grants permission to register an AWS account to IoT FleetWise
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [campaign](#list_iotfleetwise-resource-campaign) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [decodermanifest](#list_iotfleetwise-resource-decodermanifest) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [fleet](#list_iotfleetwise-resource-fleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [modelmanifest](#list_iotfleetwise-resource-modelmanifest) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [signalcatalog](#list_iotfleetwise-resource-signalcatalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [statetemplate](#list_iotfleetwise-resource-statetemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [vehicle](#list_iotfleetwise-resource-vehicle) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleetwise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [campaign](#list_iotfleetwise-resource-campaign) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [decodermanifest](#list_iotfleetwise-resource-decodermanifest) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [fleet](#list_iotfleetwise-resource-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [modelmanifest](#list_iotfleetwise-resource-modelmanifest) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [signalcatalog](#list_iotfleetwise-resource-signalcatalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [statetemplate](#list_iotfleetwise-resource-statetemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Resource types (\*required):** [vehicle](#list_iotfleetwise-resource-vehicle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleetwise-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCampaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateCampaign.html)  **
  - **Description:** Grants permission to update the given campaign
  - **Resource types (\*required):** [campaign\*](#list_iotfleetwise-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDecoderManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateDecoderManifest.html)  **
  - **Description:** Grants permission to update a decoder manifest defnition
  - **Resource types (\*required):** [decodermanifest\*](#list_iotfleetwise-resource-decodermanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateFleet.html)  **
  - **Description:** Grants permission to update the fleet
  - **Resource types (\*required):** [fleet\*](#list_iotfleetwise-resource-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateModelManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateModelManifest.html)  **
  - **Description:** Grants permission to update the given model manifest definition
  - **Resource types (\*required):** [modelmanifest\*](#list_iotfleetwise-resource-modelmanifest)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateSignalCatalog.html)  **
  - **Description:** Grants permission to update a specific signal catalog definition
  - **Resource types (\*required):** [signalcatalog\*](#list_iotfleetwise-resource-signalcatalog)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStateTemplate](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateStateTemplate.html)  **
  - **Description:** Grants permission to update the given state template
  - **Resource types (\*required):** [statetemplate\*](#list_iotfleetwise-resource-statetemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateVehicle.html)  **
  - **Description:** Grants permission to update the vehicle
  - **Resource types (\*required):** [decodermanifest](#list_iotfleetwise-resource-decodermanifest) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[iotfleetwise:UpdateToDecoderManifestArn](#list_iotfleetwise-iotfleetwise_UpdateToDecoderManifestArn)<br />[iotfleetwise:UpdateToModelManifestArn](#list_iotfleetwise-iotfleetwise_UpdateToModelManifestArn)
  - **Resource types (\*required):** [modelmanifest](#list_iotfleetwise-resource-modelmanifest) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[iotfleetwise:UpdateToDecoderManifestArn](#list_iotfleetwise-iotfleetwise_UpdateToDecoderManifestArn)<br />[iotfleetwise:UpdateToModelManifestArn](#list_iotfleetwise-iotfleetwise_UpdateToModelManifestArn)
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[iotfleetwise:UpdateToDecoderManifestArn](#list_iotfleetwise-iotfleetwise_UpdateToDecoderManifestArn)<br />[iotfleetwise:UpdateToModelManifestArn](#list_iotfleetwise-iotfleetwise_UpdateToModelManifestArn)
  - **Access level:** Write



## Permission-only actions for AWS IoT FleetWise
<a name="list_iotfleetwise-permission-only-actions"></a>

The following actions are defined by AWS IoT FleetWise but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GenerateCommandPayload](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/controlling-access.html#generate-command-payload)  **
  - **Description:** Grants permission to generate the payload for running a command on a vehicle
  - **Resource types (\*required):** [statetemplate](#list_iotfleetwise-resource-statetemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[iotfleetwise:Signals](#list_iotfleetwise-iotfleetwise_Signals)
  - **Resource types (\*required):** [vehicle\*](#list_iotfleetwise-resource-vehicle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_)<br />[iotfleetwise:Signals](#list_iotfleetwise-iotfleetwise_Signals)
  - **Access level:** Permissions management, Write



## Resource types defined by AWS IoT FleetWise
<a name="list_iotfleetwise-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [campaign](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html)  | arn:${Partition}:iotfleetwise:${Region}:${Account}:campaign/${CampaignName} | [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_) | 
|  [decodermanifest](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/decoder-manifests.html)  | arn:${Partition}:iotfleetwise:${Region}:${Account}:decoder-manifest/${Name} | [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_) | 
|  [fleet](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html)  | arn:${Partition}:iotfleetwise:${Region}:${Account}:fleet/${FleetId} | [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_) | 
|  [modelmanifest](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicle-models.html)  | arn:${Partition}:iotfleetwise:${Region}:${Account}:model-manifest/${Name} | [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_) | 
|  [signalcatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/signal-catalogs.html)  | arn:${Partition}:iotfleetwise:${Region}:${Account}:signal-catalog/${Name} | [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_) | 
|  [statetemplate](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/last-known-state.html)  | arn:${Partition}:iotfleetwise:${Region}:${Account}:state-template/${StateTemplateId} | [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_) | 
|  [vehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicles.html)  | arn:${Partition}:iotfleetwise:${Region}:${Account}:vehicle/${VehicleId} | [aws:ResourceTag/${TagKey}](#list_iotfleetwise-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT FleetWise
<a name="list_iotfleetwise-policy-keys"></a>

AWS IoT FleetWise defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [iotfleetwise:DestinationArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleetwise.html)  | Filters access by campaign destination ARN, eg. an S3 bucket ARN or a Timestream ARN | ARN | 
|   [iotfleetwise:Signals](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleetwise.html)  | Filters access by fully qualified signal names | ArrayOfString | 
|   [iotfleetwise:UpdateToDecoderManifestArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleetwise.html)  | Filters access by a list of IoT FleetWise Decoder Manifest ARNs | ARN | 
|   [iotfleetwise:UpdateToModelManifestArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleetwise.html)  | Filters access by a list of IoT FleetWise Model Manifest ARNs | ARN | 