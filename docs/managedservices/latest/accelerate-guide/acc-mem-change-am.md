# Changing the Accelerate alarm configuration

To add or update new alarm definitions, you can either deploy configuration document
[Using AWS CloudFormation to deploy Accelerate configuration changes](acc-mem-deploy-change-cfn.md "acc-mem-deploy-change-cfn.md"), or invoke the
[CreateHostedConfigurationVersion](../../../appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.md "../../../appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.md") API.

This is a Linux command line command that generates the parameter value in base64, which is what the AppConfig CLI command expects. For information, see the
AWS CLI documentation,
[Binary/Blob (binary large object)](../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-blob "../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-blob").

As an example:

```
aws appconfig create-hosted-configuration-version --application-id `application-id` --configuration-profile-id `configuration-profile-id` --content `base64-string`
      --content-type application/json
```

- **Application ID:** ID of the application AMS AlarmManager; you can find this out with the
  [ListApplications](../../../appconfig/2019-10-09/APIReference/API_ListApplications.md "../../../appconfig/2019-10-09/APIReference/API_ListApplications.md") API call.
- **Configuration Profile ID**: ID of the configuration CustomerManagedAlarms; you can find this out with the
  [ListConfigurationProfiles](../../../appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.md "../../../appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.md") API call.
- **Content**: Base64 string of the content, to be created by
  creating a document and encoding it in base64: cat alarms-v2.json | base64 (see
  [Binary/Blob (binary large object)](../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-blob "../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-blob")).

**Content Type**: MIME type, `application/json` because alarm definitions are written in JSON.

###### Important

Restrict access to the
[StartDeployment](../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md "../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md") and
[StopDeployment](../../../appconfig/2019-10-09/APIReference/API_StopDeployment.md "../../../appconfig/2019-10-09/APIReference/API_StopDeployment.md")
API actions to trusted users who understand the responsibilities and consequences of deploying a new configuration to your targets.

To learn more about how to use AWS AppConfig features to create and deploy a configuration, see
[Working with AWS AppConfig](../../../appconfig/latest/userguide/appconfig-working.md "../../../appconfig/latest/userguide/appconfig-working.md").
