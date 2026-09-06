

# Actions, resources, and condition keys for AWS Ground Station
<a name="list_groundstation"></a>

AWS Ground Station (service prefix: `groundstation`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ground-station/latest/ug/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ground-station/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ground-station/latest/ug/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/groundstation/groundstation.json) for this service.

**Topics**
+ [API operations defined by AWS Ground Station](#list_groundstation-operations)
+ [Actions defined by AWS Ground Station](#list_groundstation-actions-as-permissions)
+ [Resource types defined by AWS Ground Station](#list_groundstation-resources-for-iam-policies)
+ [Condition keys for AWS Ground Station](#list_groundstation-policy-keys)

## API operations defined by AWS Ground Station
<a name="list_groundstation-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_groundstation-actions-as-permissions).




- **   CancelContact  **
  - **IAM action:**  [groundstation:CancelContact](#list_groundstation-action-CancelContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConfig  **
  - **IAM action:**  [groundstation:CreateConfig](#list_groundstation-action-CreateConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [groundstation:TagResource](#list_groundstation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** groundstation.amazonaws.com / **Access level:** Write

- **   CreateDataflowEndpointGroup  **
  - **IAM action:**  [groundstation:CreateDataflowEndpointGroup](#list_groundstation-action-CreateDataflowEndpointGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [groundstation:TagResource](#list_groundstation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** groundstation.amazonaws.com / **Access level:** Write

- **   CreateDataflowEndpointGroupV2  **
  - **IAM action:**  [groundstation:CreateDataflowEndpointGroupV2](#list_groundstation-action-CreateDataflowEndpointGroupV2)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [groundstation:TagResource](#list_groundstation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEphemeris  **
  - **IAM action:**  [groundstation:CreateEphemeris](#list_groundstation-action-CreateEphemeris)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [groundstation:TagResource](#list_groundstation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMissionProfile  **
  - **IAM action:**  [groundstation:CreateMissionProfile](#list_groundstation-action-CreateMissionProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [groundstation:TagResource](#list_groundstation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** groundstation.amazonaws.com / **Access level:** Write

- **   DeleteConfig  **
  - **IAM action:**  [groundstation:DeleteConfig](#list_groundstation-action-DeleteConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataflowEndpointGroup  **
  - **IAM action:**  [groundstation:DeleteDataflowEndpointGroup](#list_groundstation-action-DeleteDataflowEndpointGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEphemeris  **
  - **IAM action:**  [groundstation:DeleteEphemeris](#list_groundstation-action-DeleteEphemeris) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMissionProfile  **
  - **IAM action:**  [groundstation:DeleteMissionProfile](#list_groundstation-action-DeleteMissionProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeContact  **
  - **IAM action:**  [groundstation:DescribeContact](#list_groundstation-action-DescribeContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeContactVersion  **
  - **IAM action:**  [groundstation:DescribeContactVersion](#list_groundstation-action-DescribeContactVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEphemeris  **
  - **IAM action:**  [groundstation:DescribeEphemeris](#list_groundstation-action-DescribeEphemeris) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentConfiguration  **
  - **IAM action:**  [groundstation:GetAgentConfiguration](#list_groundstation-action-GetAgentConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentTaskResponseUrl  **
  - **IAM action:**  [groundstation:GetAgentTaskResponseUrl](#list_groundstation-action-GetAgentTaskResponseUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfig  **
  - **IAM action:**  [groundstation:GetConfig](#list_groundstation-action-GetConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataflowEndpointGroup  **
  - **IAM action:**  [groundstation:GetDataflowEndpointGroup](#list_groundstation-action-GetDataflowEndpointGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMinuteUsage  **
  - **IAM action:**  [groundstation:GetMinuteUsage](#list_groundstation-action-GetMinuteUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMissionProfile  **
  - **IAM action:**  [groundstation:GetMissionProfile](#list_groundstation-action-GetMissionProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSatellite  **
  - **IAM action:**  [groundstation:GetSatellite](#list_groundstation-action-GetSatellite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAntennas  **
  - **IAM action:**  [groundstation:ListAntennas](#list_groundstation-action-ListAntennas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigs  **
  - **IAM action:**  [groundstation:ListConfigs](#list_groundstation-action-ListConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContactVersions  **
  - **IAM action:**  [groundstation:ListContactVersions](#list_groundstation-action-ListContactVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContacts  **
  - **IAM action:**  [groundstation:ListContacts](#list_groundstation-action-ListContacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataflowEndpointGroups  **
  - **IAM action:**  [groundstation:ListDataflowEndpointGroups](#list_groundstation-action-ListDataflowEndpointGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEphemerides  **
  - **IAM action:**  [groundstation:ListEphemerides](#list_groundstation-action-ListEphemerides) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroundStationReservations  **
  - **IAM action:**  [groundstation:ListGroundStationReservations](#list_groundstation-action-ListGroundStationReservations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroundStations  **
  - **IAM action:**  [groundstation:ListGroundStations](#list_groundstation-action-ListGroundStations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMissionProfiles  **
  - **IAM action:**  [groundstation:ListMissionProfiles](#list_groundstation-action-ListMissionProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSatellites  **
  - **IAM action:**  [groundstation:ListSatellites](#list_groundstation-action-ListSatellites) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [groundstation:ListTagsForResource](#list_groundstation-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterAgent  **
  - **IAM action:**  [groundstation:RegisterAgent](#list_groundstation-action-RegisterAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReserveContact  **
  - **IAM action:**  [groundstation:ReserveContact](#list_groundstation-action-ReserveContact)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [groundstation:TagResource](#list_groundstation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   TagResource  **
  - **IAM action:**  [groundstation:TagResource](#list_groundstation-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [groundstation:UntagResource](#list_groundstation-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAgentStatus  **
  - **IAM action:**  [groundstation:UpdateAgentStatus](#list_groundstation-action-UpdateAgentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfig  **
  - **IAM action:**  [groundstation:UpdateConfig](#list_groundstation-action-UpdateConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** groundstation.amazonaws.com / **Access level:** Write

- **   UpdateContact  **
  - **IAM action:**  [groundstation:UpdateContact](#list_groundstation-action-UpdateContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEphemeris  **
  - **IAM action:**  [groundstation:UpdateEphemeris](#list_groundstation-action-UpdateEphemeris) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMissionProfile  **
  - **IAM action:**  [groundstation:UpdateMissionProfile](#list_groundstation-action-UpdateMissionProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** groundstation.amazonaws.com / **Access level:** Write



## Actions defined by AWS Ground Station
<a name="list_groundstation-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CancelContact.html)  **
  - **Description:** Grants permission to cancel a contact
  - **Resource types (\*required):** [Contact\*](#list_groundstation-resource-Contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ContactId](#list_groundstation-groundstation_ContactId)
  - **Access level:** Write

- **   [CreateConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateConfig.html)  **
  - **Description:** Grants permission to create a configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataflowEndpointGroup](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateDataflowEndpointGroup.html)  **
  - **Description:** Grants permission to create a data flow endpoint group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataflowEndpointGroupV2](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateDataflowEndpointGroupV2.html)  **
  - **Description:** Grants permission to create a data flow endpoint group using the V2 operation
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEphemeris.html)  **
  - **Description:** Grants permission to create an ephemeris item
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateMissionProfile.html)  **
  - **Description:** Grants permission to create a mission profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteConfig.html)  **
  - **Description:** Grants permission to delete a config
  - **Resource types (\*required):** [Config\*](#list_groundstation-resource-Config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ConfigId](#list_groundstation-groundstation_ConfigId)<br />[groundstation:ConfigType](#list_groundstation-groundstation_ConfigType)
  - **Access level:** Write

- **   [DeleteDataflowEndpointGroup](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteDataflowEndpointGroup.html)  **
  - **Description:** Grants permission to delete a data flow endpoint group
  - **Resource types (\*required):** [DataflowEndpointGroup\*](#list_groundstation-resource-DataflowEndpointGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:DataflowEndpointGroupId](#list_groundstation-groundstation_DataflowEndpointGroupId)
  - **Access level:** Write

- **   [DeleteEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteEphemeris.html)  **
  - **Description:** Grants permission to delete an ephemeris item
  - **Resource types (\*required):** [EphemerisItem\*](#list_groundstation-resource-EphemerisItem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:EphemerisId](#list_groundstation-groundstation_EphemerisId)
  - **Access level:** Write

- **   [DeleteMissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteMissionProfile.html)  **
  - **Description:** Grants permission to delete a mission profile
  - **Resource types (\*required):** [MissionProfile\*](#list_groundstation-resource-MissionProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:MissionProfileId](#list_groundstation-groundstation_MissionProfileId)
  - **Access level:** Write

- **   [DescribeContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContact.html)  **
  - **Description:** Grants permission to describe a contact
  - **Resource types (\*required):** [Contact\*](#list_groundstation-resource-Contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ContactId](#list_groundstation-groundstation_ContactId)
  - **Access level:** Read

- **   [DescribeContactVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContactVersion.html)  **
  - **Description:** Grants permission to describe a specific version of a contact
  - **Resource types (\*required):** [Contact\*](#list_groundstation-resource-Contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ContactId](#list_groundstation-groundstation_ContactId)
  - **Access level:** Read

- **   [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html)  **
  - **Description:** Grants permission to describe an ephemeris item
  - **Resource types (\*required):** [EphemerisItem\*](#list_groundstation-resource-EphemerisItem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:EphemerisId](#list_groundstation-groundstation_EphemerisId)
  - **Access level:** Read

- **   [GetAgentConfiguration](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetAgentConfiguration.html)  **
  - **Description:** Grants permission to get the configuration of an agent
  - **Resource types (\*required):** [Agent\*](#list_groundstation-resource-Agent)
  - **Condition keys:** [groundstation:AgentId](#list_groundstation-groundstation_AgentId)
  - **Access level:** Read

- **   [GetAgentTaskResponseUrl](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetAgentTaskResponseUrl.html)  **
  - **Description:** Grants permission to retrieve presigned S3 logging URLs
  - **Resource types (\*required):** [Agent\*](#list_groundstation-resource-Agent)
  - **Condition keys:** [groundstation:AgentId](#list_groundstation-groundstation_AgentId)
  - **Access level:** Read

- **   [GetConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetConfig.html)  **
  - **Description:** Grants permission to return a configuration
  - **Resource types (\*required):** [Config\*](#list_groundstation-resource-Config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ConfigId](#list_groundstation-groundstation_ConfigId)<br />[groundstation:ConfigType](#list_groundstation-groundstation_ConfigType)
  - **Access level:** Read

- **   [GetDataflowEndpointGroup](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetDataflowEndpointGroup.html)  **
  - **Description:** Grants permission to return a data flow endpoint group
  - **Resource types (\*required):** [DataflowEndpointGroup\*](#list_groundstation-resource-DataflowEndpointGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:DataflowEndpointGroupId](#list_groundstation-groundstation_DataflowEndpointGroupId)
  - **Access level:** Read

- **   [GetMinuteUsage](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetMinuteUsage.html)  **
  - **Description:** Grants permission to return minutes usage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetMissionProfile.html)  **
  - **Description:** Grants permission to retrieve a mission profile
  - **Resource types (\*required):** [MissionProfile\*](#list_groundstation-resource-MissionProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:MissionProfileId](#list_groundstation-groundstation_MissionProfileId)
  - **Access level:** Read

- **   [GetSatellite](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetSatellite.html)  **
  - **Description:** Grants permission to return information about a satellite
  - **Resource types (\*required):** [Satellite\*](#list_groundstation-resource-Satellite)
  - **Condition keys:** [groundstation:SatelliteId](#list_groundstation-groundstation_SatelliteId)
  - **Access level:** Read

- **   [ListAntennas](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListAntennas.html)  **
  - **Description:** Grants permission to list antennas for a ground station
  - **Resource types (\*required):** [GroundStationResource\*](#list_groundstation-resource-GroundStationResource)
  - **Condition keys:** [groundstation:GroundStationId](#list_groundstation-groundstation_GroundStationId)
  - **Access level:** List

- **   [ListConfigs](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListConfigs.html)  **
  - **Description:** Grants permission to return a list of past configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListContactVersions](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContactVersions.html)  **
  - **Description:** Grants permission to list versions of a contact
  - **Resource types (\*required):** [Contact\*](#list_groundstation-resource-Contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ContactId](#list_groundstation-groundstation_ContactId)
  - **Access level:** List

- **   [ListContacts](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContacts.html)  **
  - **Description:** Grants permission to return a list of contacts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataflowEndpointGroups](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListDataflowEndpointGroups.html)  **
  - **Description:** Grants permission to list data flow endpoint groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEphemerides](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListEphemerides.html)  **
  - **Description:** Grants permission to list ephemerides
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGroundStationReservations](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStationReservations.html)  **
  - **Description:** Grants permission to list reservations for a ground station
  - **Resource types (\*required):** [GroundStationResource\*](#list_groundstation-resource-GroundStationResource)
  - **Condition keys:** [groundstation:GroundStationId](#list_groundstation-groundstation_GroundStationId)
  - **Access level:** List

- **   [ListGroundStations](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStations.html)  **
  - **Description:** Grants permission to list ground stations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMissionProfiles](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListMissionProfiles.html)  **
  - **Description:** Grants permission to return a list of mission profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSatellites](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListSatellites.html)  **
  - **Description:** Grants permission to list satellites
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [Config](#list_groundstation-resource-Config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ConfigId](#list_groundstation-groundstation_ConfigId)<br />[groundstation:ConfigType](#list_groundstation-groundstation_ConfigType)
  - **Resource types (\*required):** [Contact](#list_groundstation-resource-Contact) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ContactId](#list_groundstation-groundstation_ContactId)
  - **Resource types (\*required):** [DataflowEndpointGroup](#list_groundstation-resource-DataflowEndpointGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:DataflowEndpointGroupId](#list_groundstation-groundstation_DataflowEndpointGroupId)
  - **Resource types (\*required):** [MissionProfile](#list_groundstation-resource-MissionProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:MissionProfileId](#list_groundstation-groundstation_MissionProfileId)
  - **Access level:** Read

- **   [RegisterAgent](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_RegisterAgent.html)  **
  - **Description:** Grants permission to register an agent
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ReserveContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReserveContact.html)  **
  - **Description:** Grants permission to reserve a contact
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to assign a resource tag
  - **Resource types (\*required):** [Config](#list_groundstation-resource-Config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:ConfigId](#list_groundstation-groundstation_ConfigId)<br />[groundstation:ConfigType](#list_groundstation-groundstation_ConfigType)
  - **Resource types (\*required):** [Contact](#list_groundstation-resource-Contact) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:ContactId](#list_groundstation-groundstation_ContactId)
  - **Resource types (\*required):** [DataflowEndpointGroup](#list_groundstation-resource-DataflowEndpointGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:DataflowEndpointGroupId](#list_groundstation-groundstation_DataflowEndpointGroupId)
  - **Resource types (\*required):** [EphemerisItem](#list_groundstation-resource-EphemerisItem) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:EphemerisId](#list_groundstation-groundstation_EphemerisId)
  - **Resource types (\*required):** [MissionProfile](#list_groundstation-resource-MissionProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_groundstation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:MissionProfileId](#list_groundstation-groundstation_MissionProfileId)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to unassign a resource tag
  - **Resource types (\*required):** [Config](#list_groundstation-resource-Config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:ConfigId](#list_groundstation-groundstation_ConfigId)<br />[groundstation:ConfigType](#list_groundstation-groundstation_ConfigType)
  - **Resource types (\*required):** [Contact](#list_groundstation-resource-Contact) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:ContactId](#list_groundstation-groundstation_ContactId)
  - **Resource types (\*required):** [DataflowEndpointGroup](#list_groundstation-resource-DataflowEndpointGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:DataflowEndpointGroupId](#list_groundstation-groundstation_DataflowEndpointGroupId)
  - **Resource types (\*required):** [EphemerisItem](#list_groundstation-resource-EphemerisItem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:EphemerisId](#list_groundstation-groundstation_EphemerisId)
  - **Resource types (\*required):** [MissionProfile](#list_groundstation-resource-MissionProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_groundstation-aws_TagKeys)<br />[groundstation:MissionProfileId](#list_groundstation-groundstation_MissionProfileId)
  - **Access level:** Tagging, Write

- **   [UpdateAgentStatus](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateAgentStatus.html)  **
  - **Description:** Grants permission to update the status of an agent
  - **Resource types (\*required):** [Agent\*](#list_groundstation-resource-Agent)
  - **Condition keys:** [groundstation:AgentId](#list_groundstation-groundstation_AgentId)
  - **Access level:** Write

- **   [UpdateConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateConfig.html)  **
  - **Description:** Grants permission to update a configuration
  - **Resource types (\*required):** [Config\*](#list_groundstation-resource-Config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ConfigId](#list_groundstation-groundstation_ConfigId)<br />[groundstation:ConfigType](#list_groundstation-groundstation_ConfigType)
  - **Access level:** Write

- **   [UpdateContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateContact.html)  **
  - **Description:** Grants permission to update a contact
  - **Resource types (\*required):** [Contact\*](#list_groundstation-resource-Contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ContactId](#list_groundstation-groundstation_ContactId)
  - **Access level:** Write

- **   [UpdateEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateEphemeris.html)  **
  - **Description:** Grants permission to update an ephemeris item
  - **Resource types (\*required):** [EphemerisItem\*](#list_groundstation-resource-EphemerisItem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:EphemerisId](#list_groundstation-groundstation_EphemerisId)
  - **Access level:** Write

- **   [UpdateMissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateMissionProfile.html)  **
  - **Description:** Grants permission to update a mission profile
  - **Resource types (\*required):** [MissionProfile\*](#list_groundstation-resource-MissionProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:MissionProfileId](#list_groundstation-groundstation_MissionProfileId)
  - **Access level:** Write



## Resource types defined by AWS Ground Station
<a name="list_groundstation-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Agent](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AgentDetails.html)  | arn:${Partition}:groundstation:${Region}:${Account}:agent/${AgentId} | [groundstation:AgentId](#list_groundstation-groundstation_AgentId) | 
|  [Config](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConfigListItem.html)  | arn:${Partition}:groundstation:${Region}:${Account}:config/${ConfigType}/${ConfigId} | [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ConfigId](#list_groundstation-groundstation_ConfigId)<br />[groundstation:ConfigType](#list_groundstation-groundstation_ConfigType) | 
|  [Contact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ContactData.html)  | arn:${Partition}:groundstation:${Region}:${Account}:contact/${ContactId} | [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:ContactId](#list_groundstation-groundstation_ContactId) | 
|  [DataflowEndpointGroup](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html)  | arn:${Partition}:groundstation:${Region}:${Account}:dataflow-endpoint-group/${DataflowEndpointGroupId} | [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:DataflowEndpointGroupId](#list_groundstation-groundstation_DataflowEndpointGroupId) | 
|  [EphemerisItem](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisItem.html)  | arn:${Partition}:groundstation:${Region}:${Account}:ephemeris/${EphemerisId} | [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:EphemerisId](#list_groundstation-groundstation_EphemerisId) | 
|  [GroundStationResource](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GroundStationData.html)  | arn:${Partition}:groundstation:${Region}:${Account}:groundstation:${GroundStationId} | [groundstation:GroundStationId](#list_groundstation-groundstation_GroundStationId) | 
|  [MissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_MissionProfileListItem.html)  | arn:${Partition}:groundstation:${Region}:${Account}:mission-profile/${MissionProfileId} | [aws:ResourceTag/${TagKey}](#list_groundstation-aws_ResourceTag___TagKey_)<br />[groundstation:MissionProfileId](#list_groundstation-groundstation_MissionProfileId) | 
|  [Satellite](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SatelliteListItem.html)  | arn:${Partition}:groundstation:${Region}:${Account}:satellite/${SatelliteId} | [groundstation:SatelliteId](#list_groundstation-groundstation_SatelliteId) | 

## Condition keys for AWS Ground Station
<a name="list_groundstation-policy-keys"></a>

AWS Ground Station defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [groundstation:AgentId](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_RegisterAgent.html#groundstation-RegisterAgent-response-agentId)  | Filters access by the ID of an agent | String | 
|   [groundstation:ConfigId](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateConfig.html#groundstation-CreateConfig-response-configId)  | Filters access by the ID of a config | String | 
|   [groundstation:ConfigType](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateConfig.html#groundstation-CreateConfig-response-configType)  | Filters access by the type of a config | String | 
|   [groundstation:ContactId](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReserveContact.html#groundstation-ReserveContact-response-contactId)  | Filters access by the ID of a contact | String | 
|   [groundstation:DataflowEndpointGroupId](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateDataflowEndpointGroup.html#groundstation-CreateDataflowEndpointGroup-response-dataflowEndpointGroupId)  | Filters access by the ID of a dataflow endpoint group | String | 
|   [groundstation:EphemerisId](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEphemeris.html#groundstation-CreateEphemeris-response-ephemerisId)  | Filters access by the ID of an ephemeris | String | 
|   [groundstation:GroundStationId](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GroundStationData.html#groundstation-Type-GroundStationData-groundStationId)  | Filters access by the ID of a ground station | String | 
|   [groundstation:MissionProfileId](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateMissionProfile.html#groundstation-CreateMissionProfile-response-missionProfileId)  | Filters access by the ID of a mission profile | String | 
|   [groundstation:SatelliteId](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SatelliteListItem.html#groundstation-Type-SatelliteListItem-satelliteId)  | Filters access by the ID of a satellite | String | 