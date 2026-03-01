# Deploying feature flags and configuration data in AWS AppConfig

After you [create
required artifacts](creating-feature-flags-and-configuration-data.md "creating-feature-flags-and-configuration-data.md") for working with feature flags and freeform configuration data, you
can create a new deployment. When you create a new deployment, you specify the following
information:

- An application ID
- A configuration profile ID
- A configuration version
- An environment ID where you want to deploy the configuration data
- A deployment strategy ID that defines how fast you want the changes to take
  effect
- An AWS Key Management Service (AWS KMS) key ID to encrypt the data using a customer managed key.
  When you call the [StartDeployment](../../2019-10-09/APIReference/API_StartDeployment.md "../../2019-10-09/APIReference/API_StartDeployment.md") API
  action, AWS AppConfig performs the following tasks:

1. Retrieves the configuration data from the underlying data store by using the location
   URI in the configuration profile.
2. Verifies the configuration data is syntactically and semantically correct by using the
   validators you specified when you created your configuration profile.
3. Caches a copy of the data so it is ready to be retrieved by your application. This
   cached copy is called the _deployed data_.
   You can mitigate situations where deploying configuration data causes errors in your
   application by using a combination of AWS AppConfig deployment strategies and automatic rollbacks based
   on Amazon CloudWatch alarms. A deployment strategy enables you to slowly release changes to production
   environments over minutes or hours. Once configured, if one or more CloudWatch alarms go into the
   alarm state during a deployment, AWS AppConfig automatically rolls back your configuration data to the
   previous version. For more information about deployment strategies, see [Working with deployment strategies](appconfig-creating-deployment-strategy.md "appconfig-creating-deployment-strategy.md"). For more information about automatic
   rollbacks, see [Monitoring deployments for automatic rollback](monitoring-deployments.md "monitoring-deployments.md").

###### Topics

- [Working with deployment strategies](appconfig-creating-deployment-strategy.md "appconfig-creating-deployment-strategy.md")
- [Deploying a configuration](appconfig-deploying.md "appconfig-deploying.md")
- [Deploying AWS AppConfig configurations using CodePipeline](appconfig-integration-codepipeline.md "appconfig-integration-codepipeline.md")
- [Reverting a configuration](appconfig-deploying-reverting.md "appconfig-deploying-reverting.md")
