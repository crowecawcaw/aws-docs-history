# Resource Tagger use cases in AMS Accelerate

This section lists commonly performed actions with Resource Tagger.

## Viewing the tags applied by Resource Tagger

All tags applied by Resource Tagger have the key prefix **ams:rt:.**
For example, the following tag definition results in a tag with key **ams:rt:sampleKey** and value **sampleValue**. All tags
with this prefix are treated as being part of Resource Tagger.

```
{
	"Key": "sampleKey",
	"Value": "sampleValue"
}
```

###### Important

If you manually create your own tag with the **ams:rt:** prefix, it's
considered managed by Resource Tagger. This means that if the resource is managed by
Resource Tagger, but the configuration profiles do not indicate that the tag should be
applied, then Resource Tagger removes your manually added tag. If you do manually tag
resources managed by Resource Tagger, do not use the **ams:rt:** prefix for tag keys.

## Using Resource Tagger to create tags

The AMS Accelerate Resource Tagger is a component that is deployed in your account during AMS Accelerate onboarding.
Resource Tagger has a configurable set of rules that define how your resources should be tagged, then it enforces those
rules, automatically adding and removing tags on resources to ensure they comply with your rules.

If you want to use the Resource Tagger to tag your resources, see
[Accelerate Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md").

The following is an example Resource Tagger configuration snippet that adds the tag
**ams:rt:ams-managed** with the value **true** to all
Amazon EC2 instances. The **ams:rt:ams-managed** tag opts you in to having your resources monitored by AMS Accelerate.

```
{
    "AWS::EC2::Instance": {
        "SampleConfigurationBlock": {
            "Enabled": true,
            "Filter": {
                "Platform": "*"
            },
            "Tags": [
                {
                    "Key": "ams:rt:ams-managed",
                    "Value": "true"
                }
            ]
        }
    }
}

```

###### Warning

Be careful when specifying the name for your new configuration (`SampleConfigurationBlock` in the provided example) as you may inadvertently
override the AMS-managed configuration with the same name.

## Preventing Resource Tagger from modifying resources

Resource Tagger can be set to a read-only mode that prevents it from adding or removing any tags on your resources.
This is useful if you want to provide your own tagging mechanism.

When in read-only mode, Resource Tagger still examines the tagging rules that are being specified in the managed
and customer configuration profiles, and scans for resources that do not meet these tagging rules. Any non-compliant
resources are surfaced with AWS Config. The AWS Config Rules that you can look for have the `AMSResourceTagger-` prefix.
For example the `AMSResourceTagger-EC2Instance` AWS Config rule evaluates if appropriate tags are created for
`AWS::EC2::Instance` resources based on the configuration profile.

Resource Tagger stops at this point, and does not make any changes to your resources (does not add or remove tags).

You can enable the read-only mode by modifying the customer configuration profile to include the
**ReadOnly** key in the **Options** block. For example, the following configuration profile
snippet shows how this might look:

```
{
    "Options": {
        "ReadOnly": true
    },
    "AWS::EC2::Instance": {
        [... the rest of your configuration ...]
    }
}
```

Resource Tagger would react to this new configuration as soon as it has finished deploying, and stop adding and
removing tags on resources.

###### Note

To re-enable tag modification, change the **ReadOnly** value to **false**,
or remove the key altogether, since the default value is **false**.

For more on the **Options** setting, see
[Syntax and structure](acc-tag-tools-profiles.md#acc-rt-config-doc-format "acc-tag-tools-profiles.md#acc-rt-config-doc-format"), next.

## Example configuration profile

The following example profile document specifies that all Windows EC2 instances that
are part of a stack-\* CloudFormation stack be managed by AMS Accelerate; however, explicitly
excludes a particular EC2 instance with ID i-00000000000000001.

```
{
    "AWS::EC2::Instance": {
        "AMSMonitoringWindows": {
            "Enabled": true,
            "Filter": {
                "Fn::AND": [
                    {
                        "Platform": "Windows"
                    },
                    {
                        "Tag": {
                            "Key": "aws:cloudformation:stack-name",
                            "Value": "stack-*"
                        }
                    },
                    {
                        "Fn::NOT": {
                            "InstanceId": "i-00000000000000001"
                        }
                    }
                ]
            },
            "Tags": [
                {
                    "Key": "ams:rt:ams-managed",
                    "Value": "true"
                }
            ]
        }
    }
}
```

###### Warning

Be careful when specifying the name for your new configuration (`SampleConfigurationBlock` in the provided example) as you may inadvertently
override the AMS-managed configuration with the same name.

## Merging the default configuration

The default configuration profile is supplied by AMS Accelerate at the time of account
onboarding. This profile provides default rules that are deployed in your account.

While you can't modify the default configuration profile, you can provide overrides to
the defaults by specifying a configuration block in your customization configuration
profile with the same **ConfigurationID** as the default configuration
block. If you do this, your configuration block overwrites the default configuration block.

For example, consider the following default configuration document:

```
{
	"AWS::EC2::Instance": {
		"AMSManagedBlock1": {
			"Enabled": true,
			"Filter": {
				"Platform": "Windows"
			},
			"Tags": [{
				"Key": "my-tag",
				"Value": "SampleValueA"
			}]
		}
	}
}
```

To change the tag value applied here from `SampleValueA` to `SampleValueB`, and
have the tag applied to all instances, not just Windows instances, you would provide the following customization
configuration profile:

```
{
	"AWS::EC2::Instance": {
		"AMSManagedBlock1": {
			"Enabled": true,
			"Filter": {
				"Platform": "*"
			},
			"Tags": [{
				"Key": "my-tag",
				"Value": "SampleValueB"
			}]
		}
	}
}
```

###### Important

Remember to deploy your configuration changes after you have made them. For more
information, see [Deploying configuration changes](#acc-rt-deploy-changes "#acc-rt-deploy-changes"). In SSM AppConfig,
you must deploy a new version of the configuration after creating it.

## Disabling the default configuration

You can disable a default configuration rule by adding a configuration block with the
same **ConfigurationID** to your customization configuration profile and
giving the **Enabled** field for a value of
**false**.

For example, if the following configuration were present in the default configuration profile:

```
{
	"AWS::EC2::Instance": {
		"AMSManagedBlock1": {
			"Enabled": true,
			"Filter": {
				"Platform": "Windows"
			},
			"Tags": [{
				"Key": "my-tag",
				"Value": "SampleValueA"
			}]
		}
	}
}
```

You could disable this tagging rule by including the following in your customization configuration profile:

```
{
	"AWS::EC2::Instance": {
		"AMSManagedBlock1": {
			"Enabled": false
		}
	}
}
```

###### Important

Remember to deploy your configuration changes after you have made them; for
information, see [Deploying configuration changes](#acc-rt-deploy-changes "#acc-rt-deploy-changes"). In SSM AppConfig,
you must deploy a new version of the configuration after creating it.

## Removing tags applied by Resource Tagger

Any tags prefixed with **ams:rt** are removed by Resource Tagger if the
tags do not exist in the configuration profiles, or, if they do exist, where the filter
doesn't match. This means that you can remove tags applied by Resource Tagger by doing one
of the following:

- Modifying the customization configuration section that defines the tag.
- Adding an exception for the specific resources so they no longer match the filter.

For example: if a **Linux** instance has the following tags:

```
"Tags": [{
    "Key": "ams:rt:MyOwnTag",
    "Value": true
},{
    "Key": "myTag",
    "Value": true
}]
```

And you deploy the following Resource Tagger configuration profile:

```
{
    "AWS::EC2::Instance": {
        "AMSMonitoringWindows": {
            "Enabled": true,
            "Filter": {
                "Platform": "Windows"
            },
            "Tags": [{
                "Key": "ams:rt:ams-managed",
                "Value": "true"
            }]
        }
    }
}
```

Resource Tagger reacts to the new configuration changes, and the only tag on the instance becomes:

```
 "Tags": [{
     "Key": "myTag",
     "Value": true
 }]
```

###### Warning

Be careful when specifying the name for your new configuration (`SampleConfigurationBlock` in the provided example) as you may inadvertently
override the AMS-managed configuration with the same name.

###### Important

Remember to deploy your configuration changes after you have made them; for
information, see [Deploying configuration changes](#acc-rt-deploy-changes "#acc-rt-deploy-changes"). In SSM AppConfig,
you must deploy a new version of the configuration after creating it.

## Viewing or making changes to the Resource Tagger configuration

The two JSON configuration profiles, **AMSManagedTags** and
**CustomerManagedTags**, deployed to your account in [AWS
AppConfig](../../../appconfig/latest/userguide/what-is-appconfig.md "../../../appconfig/latest/userguide/what-is-appconfig.md") at onboarding and residing in the AMSResourceTagger application, and in
the **AMSInfrastructure** environment, can be reviewed through AppConfig’s [GetConfiguration](../../../appconfig/2019-10-09/APIReference/API_GetConfiguration.md "../../../appconfig/2019-10-09/APIReference/API_GetConfiguration.md") API.

The following is an example of this GetConfiguration call:

```
aws appconfig get-configuration
 --application AMSResourceTagger
 --environment AMSInfrastructure
 --configuration AMSManagedTags
 --client-id `ANY_STRING`
 outfile.json
```

**Application**: AppConfig logical unit to provide capabilities,
for the Resource Tagger, this is AMSResourceTagger.

- **Environment**: AMSInfrastructure.
- **Configuration**: To view AMS Accelerate default tag definitions, the value
  is AMSManagedTags, while to view customer tag definitions, the value is CustomerManagedTags.
- **Client ID**: The unique application instance identifier, this
  can be any string.
- The tag definitions can then be viewed in the specified output file, in this case,
  outfile.json.

The alarm definitions can then be viewed in the specified output file, in this case,
outfile.json.

You can see which version of configuration is deployed to your account by viewing the past deployments
in the **AMSInfrastructure** environment.

To override tag rules:

Any of the existing tag rules can be overridden by updating the customization profile
either with CloudFormation by [Deploying a configuration profile with CloudFormation for Accelerate](acc-tag-cf-ex-deploy-config.md "acc-tag-cf-ex-deploy-config.md") or, or directly using using AppConfig’s [**CreateHostedConfigurationVersion**](../../../appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.md "../../../appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.md") API. Using the same
**ConfigurationID** as a default configuration tag rule overrides the
default rule, and applies the custom rule in its place.

To deploy changes made to the **CustomerManagedTags** document:

After you make changes to the customization configuration profile, you must deploy the
changes for them. To deploy the new changes, AppConfig’s [StartDeployment](../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md "../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md")
API must be run using the AWS AppConfig Console or the CLI.

## Deploying configuration changes

Once the customization is completed, these changes must be deployed through the AWS AppConfig
[StartDeployment](../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md "../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md")
API. The following instructions show how to deploy using the AWS CLI. Additionally, you can
use the AWS Management Console to make these changes. For information, see [Step 5: Deploying a configuration](../../../appconfig/latest/userguide/appconfig-deploying.md "../../../appconfig/latest/userguide/appconfig-deploying.md").

```
aws appconfig start-deployment
--application-id <application_id>
--environment-id <environment_id>
--deployment-strategy-id <deployment_strategy_id>
--configuration-profile-id <configuration_profile_id>
--configuration-version 1
```

- **Application ID**: The application ID of the application AMSResourceTagger.
  Get this with the [ListApplications](../../../appconfig/2019-10-09/APIReference/API_ListApplications.md "../../../appconfig/2019-10-09/APIReference/API_ListApplications.md") API call.
- **Environment ID**: The environment ID; get this with the
  [ListEnvironments](../../../appconfig/2019-10-09/APIReference/API_ListEnvironments.md "../../../appconfig/2019-10-09/APIReference/API_ListEnvironments.md") API call.
- **Deployment Strategy ID**: The deployment strategy ID; get this with the
  [ListDeploymentStrategies](../../../appconfig/2019-10-09/APIReference/API_ListDeploymentStrategies.md "../../../appconfig/2019-10-09/APIReference/API_ListDeploymentStrategies.md") API call.
- **Configuration Profile ID**: The configuration profile ID of CustomerManagedTags; get this with the
  [ListConfigurationProfiles](../../../appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.md "../../../appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.md") API call.
- **Configuration Version**: The version of the configuration profile you intend to
  deploy.

###### Important

Resource Tagger applies the tags as specified in the configuration profiles. Any manual
modifications you make (with the AWS Management Console, or CloudWatch CLI/SDK) to the resource tags are automatically reverted back, so
ensure your changes are defined through Resource Tagger. To know which tags are created by the Resource
Tagger, look for tag keys prefixed with `ams:rt:`.

Restrict access to the deployment with the
[StartDeployment](../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md "../../../appconfig/2019-10-09/APIReference/API_StartDeployment.md")
and the
[StopDeployment](../../../appconfig/2019-10-09/APIReference/API_StopDeployment.md "../../../appconfig/2019-10-09/APIReference/API_StopDeployment.md")
API actions to trusted users who understand the responsibilities and consequences of deploying a new configuration to
your targets.

To learn more about how to use AWS AppConfig features to create and deploy a configuration, see the documentation at
[Working with AWS AppConfig](../../../appconfig/latest/userguide/appconfig-working.md "../../../appconfig/latest/userguide/appconfig-working.md").

## Configuring Terraform to ignore Resource Tagger tags

If you use Terraform to provision your resources, and you want to use Resource Tagger to tag your
resources, the Resource Tagger tags may be identified as drift by Terraform.

You can configure Terraform to ignore all Resource Tagger tags using the
**lifecycle** configuration block, or the
**ignore_tags** global configuration block. For more information, see the
Terraform documentation on Resource Tagging at [Resource Tagging](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/resource-tagging "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/resource-tagging").

The following example shows how to create a global configuration to ignore all tags that begin with the Resource Tagger tag prefix `ams:rt:`:

```
provider "aws" {
  # ... potentially other configuration ...

  ignore_tags {
    key_prefixes = ["ams:rt:"]
  }
}
```

## Viewing the number of resources managed by Resource Tagger

Resource Tagger sends metrics every hour to Amazon CloudWatch, in the
`AMS/ResourceTagger` namespace. Metrics are emitted only for resource types
supported by Resource Tagger.

| Metric Name                 | Dimensions                                | Description                                                                                                                                                                                                                                                         |
| --------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ResourceCount               | Component, ResourceType                   | Number of resources (of the specified resource type) deployed in this region.<br>Units: Count                                                                                                                                                                       |
| ResourcesMissingManagedTags | Component, ResourceType                   | Number of resources (of the specified resource type) that require managed tags,<br>according to the configuration profiles, but have not yet been tagged by Resource Tagger.<br>Units: Count                                                                        |
| UnmanagedResources          | Component, ResourceType                   | Number of resources (of the specified resource type) with no managed tags<br>applied by Resource Tagger. Typically, these resources did not match any Resource<br>Tagger configuration block, or are explicitly excluded from configuration blocks.<br>Units: Count |
| MatchingResourceCount       | Component, ResourceType, ConfigClauseName | Number of resources (of the specified resource type) that match the Resource<br>Tagger configuration block. For a resource to match the configuration block, the<br>block must be enabled and the resource must match the block's filter.<br>Units: Count           |

These metrics are also viewable as graphs, in the
**AMS-Resource-Tagger-Reporting-Dashboard**. To see the dashboard, from
the Amazon CloudWatch management console, select
**AMS-Resource-Tagger-Reporting-Dashboard**. By default, the graphs in
this dashboard display the data for the prior 12-hour period.

AMS Accelerate deploys CloudWatch alarms to your account to detect significant increases
in the number of unmanaged resources, for example, resources excluded from management by
AMS Resource Tagger. AMS Operations will investigate increases in unmanaged resources
that exceed: either three resources of the same type, or a 50% increase over all resources of
the same type. If the change does not appear to be deliberate, AMS Operations might contact
you to review the change.
