# Using AppConfig to deploy Accelerate alarm configuration changes

Once the customization is completed, use AppConfig to deploy your changes with
[StartDeployment](../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md "../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md").

```
  aws appconfig start-deployment --application-id `application_id`
   --environment-id `environment`_id Vdeployment-strategy-id
   `deployment_strategy_id` --configuration-profile-id `configuration_profile_id` --configuration-version `1`
```

- **Application ID**: ID of the application `AMSAlarmManager`, you can find this with the
  [ListApplications](../../../appconfig/2019-10-09/APIReference/API_ListApplications.md "../../../appconfig/2019-10-09/APIReference/API_ListApplications.md") API call.
- **Environment ID**: You can find this with the
  [ListEnvironments](../../../appconfig/2019-10-09/APIReference/API_ListEnvironments.md "../../../appconfig/2019-10-09/APIReference/API_ListEnvironments.md") API call.
- **Deployment Strategy ID**: You can find this with the
  [ListDeploymentStrategies](../../../appconfig/2019-10-09/APIReference/API_ListDeploymentStrategies.md "../../../appconfig/2019-10-09/APIReference/API_ListDeploymentStrategies.md") API call.
- **Configuration Profile ID**: ID of `CustomerManagedAlarms`; you can find this with the
  [ListConfigurationProfiles](../../../appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.md "../../../appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.md") API call.
- **Configuration Version**: The version of the configuration profile to be deployed.

###### Important

Alarm Manager applies the alarm definitions as specified in the configuration profiles. Any manual modifications you make with the AWS Management Console
or CloudWatch CLI/SDK to the CloudWatch alarms is automatically reverted back, so make sure your changes are defined through Alarm Manager. To understand which alarms
are created by the Alarm Manager, you can look for the `ams:alarm-manager:managed` tag with value `true`.

Restrict access to the
[StartDeployment](../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md "../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md") and
[StopDeployment](../../../appconfig/2019-10-09/APIReference/API_StopDeployment.md "../../../appconfig/2019-10-09/APIReference/API_StopDeployment.md")
API actions to trusted users who understand the responsibilities and consequences of deploying a new configuration to your targets.

To learn more about how to use AWS AppConfig features to create and deploy a configuration, see the
[AWS AppConfig documentation.](../../../appconfig/latest/userguide/appconfig-working.md "../../../appconfig/latest/userguide/appconfig-working.md")
