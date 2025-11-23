# Using a CloudFormation template to update the engine

version of your Neptune DB Cluster

You can re-use the Neptune CloudFormation template that you used to create your
Neptune DB Cluster to update its engine version.

Neptune engine version upgrades can be minor or major. Using an CloudFormation template
can help with major version upgrades, which often contain significant changes. Since
major version upgrades can contain database changes that are not backward-compatible
with existing applications, you may also need to make changes to your applications
when upgrading. Always [test
before upgrading](engine-maintenance-management.md#always-test-before-upgrading "engine-maintenance-management.md#always-test-before-upgrading"), and we strongly recommend that you always create a manual
snapshot of your DB cluster before upgrading.

Note that you have to do a separate engine upgrade for each major version.
You can't skip a major version and upgrade directly to the major version following.

Prior to May 17, 2023, if you used the Neptune CloudFormation stack to upgrade your engine
version, it simply created a new, empty DB cluster in place your current one. As of
May 17, 2023, however, the Neptune CloudFormation stack now supports in-place engine
upgrades that preserve your existing data.

###### Note

If you are using the AWS Cloud Development Kit (AWS CDK), ensure that the AWS CDK version being used is 2.82.0 or later. Versions prior to
2.82.0 do not support in-place Neptune engine upgrades.

For a major version upgrade, your template should set the following properties in
`DBCluster`:

- `DBClusterParameterGroup` (Custom or Default)
- `DBInstanceParameterGroupName`
- `EngineVersion`
  Similarly, for DBInstances attached to DBCluster you should set:

- `DBParameterGroup` (Custom/Default)
  Make sure that all your parameter groups are defined in the template, whether
  they are default or custom.

In the case of a custom parameter group, make sure that the family of your existing
custom parameter group is compatible with the new engine version. Engine versions earlier
than [1.2.0.0](engine-releases-1.2.0.md "engine-releases-1.2.0.md") used parameter group family
`neptune1`, whereas engine releases from 1.2.0.0 forward require parameter
group family `neptune1.2`. See [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md") for more information.

For major engine version upgrades, specify a parameter group with the appropriate
family in the `DBCluster` `DBInstanceParameterGroupName` field.

A default parameter group should be upgraded to one that is compatible with the new
engine version.

Note that Neptune automatically reboots DB instances after an engine upgrade.

###### Topics

- [Example: Minor engine upgrade from 1.2.0.1 to 1.2.0.2](cfn-engine-update-1201-1202.md "cfn-engine-update-1201-1202.md")
- [Example: Major version upgrade
  from 1.1.1.0 to 1.2.0.2 with default parameter groups](cfn-engine-update-1110-1202-default.md "cfn-engine-update-1110-1202-default.md")
- [Example: Major version upgrade
  from 1.1.1.0 to 1.2.0.2 with custom parameter groups](cfn-engine-update-1110-1202-custom.md "cfn-engine-update-1110-1202-custom.md")
- [Example: Major version upgrade
  from 1.1.1.0 to 1.2.0.2 with a mix of default and custom parameter groups](cfn-engine-update-1110-1202-mixed.md "cfn-engine-update-1110-1202-mixed.md")
