

# Actions, resources, and condition keys for Alexa for Business
<a name="list_a4b"></a>

Alexa for Business (service prefix: `a4b`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/a4b/latest/APIReference/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/a4b/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/a4b/latest/APIReference/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/a4b/a4b.json) for this service.

**Topics**
+ [Actions defined by Alexa for Business](#list_a4b-actions-as-permissions)
+ [Permission-only actions for Alexa for Business](#list_a4b-permission-only-actions)
+ [Resource types defined by Alexa for Business](#list_a4b-resources-for-iam-policies)
+ [Condition keys for Alexa for Business](#list_a4b-policy-keys)

## Actions defined by Alexa for Business
<a name="list_a4b-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ApproveSkill](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ApproveSkill.html)  **
  - **Description:** Grants permission to associate a skill with the organization under the customer's AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateContactWithAddressBook](https://docs.aws.amazon.com/a4b/latest/APIReference/API_AssociateContactWithAddressBook.html)  **
  - **Description:** Grants permission to associate a contact with a given address book
  - **Resource types (\*required):** [addressbook\*](#list_a4b-resource-addressbook) / **Condition keys:**  
  - **Resource types (\*required):** [contact\*](#list_a4b-resource-contact) / **Condition keys:**  
  - **Access level:** Write

- **   [AssociateDeviceWithNetworkProfile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_AssociateDeviceWithNetworkProfile.html)  **
  - **Description:** Grants permission to associate a device with the specified network profile
  - **Resource types (\*required):** [device\*](#list_a4b-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [networkprofile\*](#list_a4b-resource-networkprofile) / **Condition keys:**  
  - **Access level:** Write

- **   [AssociateDeviceWithRoom](https://docs.aws.amazon.com/a4b/latest/APIReference/API_AssociateDeviceWithRoom.html)  **
  - **Description:** Grants permission to associate device with given room
  - **Resource types (\*required):** [device\*](#list_a4b-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateSkillGroupWithRoom](https://docs.aws.amazon.com/a4b/latest/APIReference/API_AssociateSkillGroupWithRoom.html)  **
  - **Description:** Grants permission to associate the skill group with given room
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [skillgroup\*](#list_a4b-resource-skillgroup) / **Condition keys:**  
  - **Access level:** Write

- **   [AssociateSkillWithSkillGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_AssociateSkillWithSkillGroup.html)  **
  - **Description:** Grants permission to associate a skill with a skill group
  - **Resource types (\*required):** [skillgroup\*](#list_a4b-resource-skillgroup)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateSkillWithUsers](https://docs.aws.amazon.com/a4b/latest/APIReference/API_AssociateSkillWithUsers.html)  **
  - **Description:** Grants permission to make a private skill available for enrolled users to enable on their devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAddressBook](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateAddressBook.html)  **
  - **Description:** Grants permission to create an address book with the specified details
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBusinessReportSchedule](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateBusinessReportSchedule.html)  **
  - **Description:** Grants permission to create a recurring schedule for usage reports to deliver to the specified S3 location with a specified daily or weekly interval
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConferenceProvider](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateConferenceProvider.html)  **
  - **Description:** Grants permission to add a new conference provider under the user's AWS account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [CreateContact](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateContact.html)  **
  - **Description:** Grants permission to create a contact with the specified details
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGatewayGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateGatewayGroup.html)  **
  - **Description:** Grants permission to create a gateway group with the specified details
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNetworkProfile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateNetworkProfile.html)  **
  - **Description:** Grants permission to create a network profile with the specified details
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProfile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateProfile.html)  **
  - **Description:** Grants permission to create a new profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRoom](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateRoom.html)  **
  - **Description:** Grants permission to create room with the specified details
  - **Resource types (\*required):** [profile\*](#list_a4b-resource-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSkillGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateSkillGroup.html)  **
  - **Description:** Grants permission to create a skill group with given name and description
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/a4b/latest/APIReference/API_CreateUser.html)  **
  - **Description:** Grants permission to create a user
  - **Resource types (\*required):** [user\*](#list_a4b-resource-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAddressBook](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteAddressBook.html)  **
  - **Description:** Grants permission to delete an address book by the address book ARN
  - **Resource types (\*required):** [addressbook\*](#list_a4b-resource-addressbook)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteBusinessReportSchedule](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteBusinessReportSchedule.html)  **
  - **Description:** Grants permission to delete the recurring report delivery schedule with the specified schedule ARN
  - **Resource types (\*required):** [schedule\*](#list_a4b-resource-schedule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConferenceProvider](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteConferenceProvider.html)  **
  - **Description:** Grants permission to delete a conference provider
  - **Resource types (\*required):** [conferenceprovider\*](#list_a4b-resource-conferenceprovider)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteContact](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteContact.html)  **
  - **Description:** Grants permission to delete a contact by the contact ARN
  - **Resource types (\*required):** [contact\*](#list_a4b-resource-contact)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDevice](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteDevice.html)  **
  - **Description:** Grants permission to remove a device from Alexa For Business
  - **Resource types (\*required):** [device\*](#list_a4b-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeviceUsageData](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteDeviceUsageData.html)  **
  - **Description:** Grants permission to delete the device's entire previous history of voice input data and associated response data
  - **Resource types (\*required):** [device\*](#list_a4b-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGatewayGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteGatewayGroup.html)  **
  - **Description:** Grants permission to delete a gateway group
  - **Resource types (\*required):** [gatewaygroup\*](#list_a4b-resource-gatewaygroup)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteNetworkProfile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteNetworkProfile.html)  **
  - **Description:** Grants permission to delete a network profile by the network profile ARN
  - **Resource types (\*required):** [networkprofile\*](#list_a4b-resource-networkprofile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteProfile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteProfile.html)  **
  - **Description:** Grants permission to delete profile by profile ARN
  - **Resource types (\*required):** [profile\*](#list_a4b-resource-profile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRoom](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteRoom.html)  **
  - **Description:** Grants permission to delete room
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRoomSkillParameter](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteRoomSkillParameter.html)  **
  - **Description:** Grants permission to delete a parameter from a skill and room
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSkillAuthorization](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteSkillAuthorization.html)  **
  - **Description:** Grants permission to unlink a third-party account from a skill
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSkillGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteSkillGroup.html)  **
  - **Description:** Grants permission to delete skill group with skill group ARN
  - **Resource types (\*required):** [skillgroup\*](#list_a4b-resource-skillgroup)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete a user
  - **Resource types (\*required):** [user\*](#list_a4b-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateContactFromAddressBook](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DisassociateContactFromAddressBook.html)  **
  - **Description:** Grants permission to disassociate a contact from a given address book
  - **Resource types (\*required):** [addressbook\*](#list_a4b-resource-addressbook) / **Condition keys:**  
  - **Resource types (\*required):** [contact\*](#list_a4b-resource-contact) / **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateDeviceFromRoom](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DisassociateDeviceFromRoom.html)  **
  - **Description:** Grants permission to disassociate device from its current room
  - **Resource types (\*required):** [device\*](#list_a4b-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateSkillFromSkillGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DisassociateSkillFromSkillGroup.html)  **
  - **Description:** Grants permission to disassociate a skill from a skill group
  - **Resource types (\*required):** [skillgroup\*](#list_a4b-resource-skillgroup)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateSkillFromUsers](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DisassociateSkillFromUsers.html)  **
  - **Description:** Grants permission to make a private skill unavailable for enrolled users and prevent them from enabling it on their devices
  - **Resource types (\*required):** [user\*](#list_a4b-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateSkillGroupFromRoom](https://docs.aws.amazon.com/a4b/latest/APIReference/API_DisassociateSkillGroupFromRoom.html)  **
  - **Description:** Grants permission to disassociate the skill group from given room
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [skillgroup\*](#list_a4b-resource-skillgroup) / **Condition keys:**  
  - **Access level:** Write

- **   [ForgetSmartHomeAppliances](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ForgetSmartHomeAppliances.html)  **
  - **Description:** Grants permission to forget smart home appliances associated to a room
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAddressBook](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetAddressBook.html)  **
  - **Description:** Grants permission to get the address book details by the address book ARN
  - **Resource types (\*required):** [addressbook\*](#list_a4b-resource-addressbook)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConferencePreference](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetConferencePreference.html)  **
  - **Description:** Grants permission to retrieve the existing conference preferences
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConferenceProvider](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetConferenceProvider.html)  **
  - **Description:** Grants permission to get details about a specific conference provider
  - **Resource types (\*required):** [conferenceprovider\*](#list_a4b-resource-conferenceprovider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetContact](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetContact.html)  **
  - **Description:** Grants permission to get the contact details by the contact ARN
  - **Resource types (\*required):** [contact\*](#list_a4b-resource-contact)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDevice](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetDevice.html)  **
  - **Description:** Grants permission to get device details
  - **Resource types (\*required):** [device\*](#list_a4b-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGateway](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetGateway.html)  **
  - **Description:** Grants permission to retrieve the details of a gateway
  - **Resource types (\*required):** [gateway\*](#list_a4b-resource-gateway)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGatewayGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetGatewayGroup.html)  **
  - **Description:** Grants permission to retrieve the details of a gateway group
  - **Resource types (\*required):** [gatewaygroup\*](#list_a4b-resource-gatewaygroup)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInvitationConfiguration](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetInvitationConfiguration.html)  **
  - **Description:** Grants permission to retrieve the configured values for the user enrollment invitation email template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNetworkProfile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetNetworkProfile.html)  **
  - **Description:** Grants permission to get the network profile details by the network profile ARN
  - **Resource types (\*required):** [networkprofile\*](#list_a4b-resource-networkprofile)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProfile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetProfile.html)  **
  - **Description:** Grants permission to get profile when provided with Profile ARN
  - **Resource types (\*required):** [profile\*](#list_a4b-resource-profile)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRoom](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetRoom.html)  **
  - **Description:** Grants permission to get room details
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRoomSkillParameter](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetRoomSkillParameter.html)  **
  - **Description:** Grants permission to get an existing parameter that has been set for a skill and room
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSkillGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GetSkillGroup.html)  **
  - **Description:** Grants permission to get skill group details with skill group ARN
  - **Resource types (\*required):** [skillgroup\*](#list_a4b-resource-skillgroup)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListBusinessReportSchedules](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListBusinessReportSchedules.html)  **
  - **Description:** Grants permission to list the details of the schedules that a user configured
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConferenceProviders](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListConferenceProviders.html)  **
  - **Description:** Grants permission to list conference providers under a specific AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeviceEvents](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListDeviceEvents.html)  **
  - **Description:** Grants permission to list the device event history, including device connection status, for up to 30 days
  - **Resource types (\*required):** [device\*](#list_a4b-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGatewayGroups](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListGatewayGroups.html)  **
  - **Description:** Grants permission to list gateway group summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGateways](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListGateways.html)  **
  - **Description:** Grants permission to list gateway summaries
  - **Resource types (\*required):** [gatewaygroup\*](#list_a4b-resource-gatewaygroup)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSkills](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSkills.html)  **
  - **Description:** Grants permission to list skills
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSkillsStoreCategories](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSkillsStoreCategories.html)  **
  - **Description:** Grants permission to list all categories in the Alexa skill store
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSkillsStoreSkillsByCategory](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSkillsStoreSkillsByCategory.html)  **
  - **Description:** Grants permission to list all skills in the Alexa skill store by category
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSmartHomeAppliances](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListSmartHomeAppliances.html)  **
  - **Description:** Grants permission to list all of the smart home appliances associated with a room
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTags](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ListTags.html)  **
  - **Description:** Grants permission to list all tags on a resource
  - **Resource types (\*required):** [device](#list_a4b-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [room](#list_a4b-resource-room) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user](#list_a4b-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutConferencePreference](https://docs.aws.amazon.com/a4b/latest/APIReference/API_PutConferencePreference.html)  **
  - **Description:** Grants permission to set the conference preferences on a specific conference provider at the account level
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutInvitationConfiguration](https://docs.aws.amazon.com/a4b/latest/APIReference/API_PutInvitationConfiguration.html)  **
  - **Description:** Grants permission to configure the email template for the user enrollment invitation with the specified attributes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutRoomSkillParameter](https://docs.aws.amazon.com/a4b/latest/APIReference/API_PutRoomSkillParameter.html)  **
  - **Description:** Grants permission to put a room specific parameter for a skill
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutSkillAuthorization](https://docs.aws.amazon.com/a4b/latest/APIReference/API_PutSkillAuthorization.html)  **
  - **Description:** Grants permission to link a user's account to a third-party skill provider
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterAVSDevice](https://docs.aws.amazon.com/a4b/latest/APIReference/API_RegisterAVSDevice.html)  **
  - **Description:** Grants permission to register an Alexa-enabled device built by an Original Equipment Manufacturer (OEM) using Alexa Voice Service (AVS)
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Write

- **   [RejectSkill](https://docs.aws.amazon.com/a4b/latest/APIReference/API_RejectSkill.html)  **
  - **Description:** Grants permission to disassociate a skill from the organization under a user's AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ResolveRoom](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ResolveRoom.html)  **
  - **Description:** Grants permission to resolve room information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [RevokeInvitation](https://docs.aws.amazon.com/a4b/latest/APIReference/API_RevokeInvitation.html)  **
  - **Description:** Grants permission to revoke an invitation
  - **Resource types (\*required):** [user\*](#list_a4b-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchAddressBooks](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchAddressBooks.html)  **
  - **Description:** Grants permission to search address books and list the ones that meet a set of filter and sort criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchContacts](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchContacts.html)  **
  - **Description:** Grants permission to search contacts and list the ones that meet a set of filter and sort criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchDevices](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchDevices.html)  **
  - **Description:** Grants permission to search for devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchNetworkProfiles](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchNetworkProfiles.html)  **
  - **Description:** Grants permission to search network profiles and list the ones that meet a set of filter and sort criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchProfiles](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchProfiles.html)  **
  - **Description:** Grants permission to search for profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchRooms](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchRooms.html)  **
  - **Description:** Grants permission to search for rooms
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchSkillGroups](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchSkillGroups.html)  **
  - **Description:** Grants permission to search for skill groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchUsers](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchUsers.html)  **
  - **Description:** Grants permission to search for users
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SendAnnouncement](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SendAnnouncement.html)  **
  - **Description:** Grants permission to trigger an asynchronous flow to send text, SSML, or audio announcements to rooms that are identified by a search or filter
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendInvitation](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SendInvitation.html)  **
  - **Description:** Grants permission to send an invitation to a user
  - **Resource types (\*required):** [user\*](#list_a4b-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDeviceSync](https://docs.aws.amazon.com/a4b/latest/APIReference/API_StartDeviceSync.html)  **
  - **Description:** Grants permission to restore the device and its account to its known, default settings by clearing all information and settings set by its previous users
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartSmartHomeApplianceDiscovery](https://docs.aws.amazon.com/a4b/latest/APIReference/API_StartSmartHomeApplianceDiscovery.html)  **
  - **Description:** Grants permission to initiate the discovery of any smart home appliances associated with the room
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/a4b/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add metadata tags to a resource
  - **Resource types (\*required):** [device](#list_a4b-resource-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Resource types (\*required):** [room](#list_a4b-resource-room) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_a4b-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_a4b-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_a4b-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove metadata tags from a resource
  - **Resource types (\*required):** [device](#list_a4b-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [room](#list_a4b-resource-room) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user](#list_a4b-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UpdateAddressBook](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateAddressBook.html)  **
  - **Description:** Grants permission to update address book details by the address book ARN
  - **Resource types (\*required):** [addressbook\*](#list_a4b-resource-addressbook)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateBusinessReportSchedule](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateBusinessReportSchedule.html)  **
  - **Description:** Grants permission to update the configuration of the report delivery schedule with the specified schedule ARN
  - **Resource types (\*required):** [schedule\*](#list_a4b-resource-schedule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConferenceProvider](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateConferenceProvider.html)  **
  - **Description:** Grants permission to update an existing conference provider's settings
  - **Resource types (\*required):** [conferenceprovider\*](#list_a4b-resource-conferenceprovider)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateContact](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateContact.html)  **
  - **Description:** Grants permission to update the contact details by the contact ARN
  - **Resource types (\*required):** [contact\*](#list_a4b-resource-contact)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDevice](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateDevice.html)  **
  - **Description:** Grants permission to update device name
  - **Resource types (\*required):** [device\*](#list_a4b-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGateway](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateGateway.html)  **
  - **Description:** Grants permission to update the details of a gateway
  - **Resource types (\*required):** [gateway\*](#list_a4b-resource-gateway)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGatewayGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateGatewayGroup.html)  **
  - **Description:** Grants permission to update the details of a gateway group
  - **Resource types (\*required):** [gatewaygroup\*](#list_a4b-resource-gatewaygroup)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateNetworkProfile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateNetworkProfile.html)  **
  - **Description:** Grants permission to update a network profile by the network profile ARN
  - **Resource types (\*required):** [networkprofile\*](#list_a4b-resource-networkprofile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateProfile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateProfile.html)  **
  - **Description:** Grants permission to update an existing profile
  - **Resource types (\*required):** [profile\*](#list_a4b-resource-profile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRoom](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateRoom.html)  **
  - **Description:** Grants permission to update room details
  - **Resource types (\*required):** [room\*](#list_a4b-resource-room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSkillGroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UpdateSkillGroup.html)  **
  - **Description:** Grants permission to update skill group details with skill group ARN
  - **Resource types (\*required):** [skillgroup\*](#list_a4b-resource-skillgroup)
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for Alexa for Business
<a name="list_a4b-permission-only-actions"></a>

The following actions are defined by Alexa for Business but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CompleteRegistration](https://docs.aws.amazon.com/a4b/latest/ag/manage-devices.html)  | Grants permission to complete the operation of registering an Alexa device |  |   | Write | 
|   [PutDeviceSetupEvents](https://docs.aws.amazon.com/a4b/latest/ag/manage-devices.html)  | Grants permission to publish Alexa device setup events |  |   | Write | 
|   [RegisterDevice](https://docs.aws.amazon.com/a4b/latest/ag/manage-devices.html)  | Grants permission to register an Alexa device |  |   | Write | 

## Resource types defined by Alexa for Business
<a name="list_a4b-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [addressbook](https://docs.aws.amazon.com/a4b/latest/APIReference/API_AddressBook.html)  | arn:${Partition}:a4b:${Region}:${Account}:address-book/${ResourceId} |   | 
|  [conferenceprovider](https://docs.aws.amazon.com/a4b/latest/APIReference/API_ConferenceProvider.html)  | arn:${Partition}:a4b:${Region}:${Account}:conference-provider/${ResourceId} |   | 
|  [contact](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Contact.html)  | arn:${Partition}:a4b:${Region}:${Account}:contact/${ResourceId} |   | 
|  [device](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Device.html)  | arn:${Partition}:a4b:${Region}:${Account}:device/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_) | 
|  [gateway](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Gateway.html)  | arn:${Partition}:a4b:${Region}:${Account}:gateway/${ResourceId} |   | 
|  [gatewaygroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_GatewayGroup.html)  | arn:${Partition}:a4b:${Region}:${Account}:gateway-group/${ResourceId} |   | 
|  [networkprofile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_NetworkProfile.html)  | arn:${Partition}:a4b:${Region}:${Account}:network-profile/${ResourceId} |   | 
|  [profile](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Profile.html)  | arn:${Partition}:a4b:${Region}:${Account}:profile/${ResourceId} |   | 
|  [room](https://docs.aws.amazon.com/a4b/latest/APIReference/API_Room.html)  | arn:${Partition}:a4b:${Region}:${Account}:room/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_) | 
|  [schedule](https://docs.aws.amazon.com/a4b/latest/APIReference/API_BusinessReportSchedule.html)  | arn:${Partition}:a4b:${Region}:${Account}:schedule/${ResourceId} |   | 
|  [skillgroup](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SkillGroup.html)  | arn:${Partition}:a4b:${Region}:${Account}:skill-group/${ResourceId} |   | 
|  [user](https://docs.aws.amazon.com/a4b/latest/APIReference/API_UserData.html)  | arn:${Partition}:a4b:${Region}:${Account}:user/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_a4b-aws_ResourceTag___TagKey_) | 

## Condition keys for Alexa for Business
<a name="list_a4b-policy-keys"></a>

Alexa for Business defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [a4b:amazonId](https://docs.aws.amazon.com/a4b/latest/APIReference/API_RegisterAVSDevice.html)  | Filters actions based on the Amazon Id in the request | String | 
|   [a4b:filters\_deviceType](https://docs.aws.amazon.com/a4b/latest/APIReference/API_SearchDevices.html)  | Filters actions based on the device type in the request | ArrayOfString | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag-value assoicated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of mandatory tags in the request | ArrayOfString | 