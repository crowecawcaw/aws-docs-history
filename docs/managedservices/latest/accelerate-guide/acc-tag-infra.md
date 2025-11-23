# Accelerate-managed tags

During onboarding to AMS Accelerate, several AWS resources are deployed to your account. So you can
identify them, these resources are tagged with the following:

| Key                      | Value                                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ams:resourceOwner        | AMS                                                                                                                                                                  |
| ams:resourceOwnerService | A description of which AMS Accelerate service offering this resource comes from, for instance, AMS<br>Deployment, Backup, Controls, Monitoring, Patch, and so forth. |
| AppId                    | AMSInfrastructure                                                                                                                                                    |
| AppName                  |
| Environment              |

###### Note

These tags are applied using CloudFormation stack-level tags, and rely on CloudFormation propagating the tags to created
resources. For more information, see
[Resource tag](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md").
