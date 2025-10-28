# Accelerate Alarm Manager

###### Important

AMS Accelerate doesn't support monitoring of Amazon EFS FileSystem, Amazon EC2 NatGateway,
or Amazon EKS Cluster resources in the Asia Pacific (Malaysia) Region.

AMS Accelerate applies alarms to your AWS resources using the tag-based Alarm Manager to implement a baseline monitoring strategy and ensure that
all your AWS resources are monitored and protected. By integrating with the tag-based Alarm Manager, you can customize the configuration of your AWS
resources based on their type, platform, and other tags, to ensure the resources are monitored. Alarm Manager is deployed to your Accelerate account during onboarding.

## How Alarm Manager works

When your account is onboarded to AMS Accelerate, two JSON documents, called configuration profiles, are deployed in your account in
[AWS AppConfig](../../../appconfig/latest/userguide/what-is-appconfig.md "../../../appconfig/latest/userguide/what-is-appconfig.md"). Both
profile documents reside in the Alarm Manager application and in the AMS Accelerate infrastructure environment.

The two configuration profiles are named **AMSManagedAlarms** (the default configuration profile) and **CustomerManagedAlarms**
(the customization configuration profile).

- Default configuration profile:
  - The configuration found in this profile contains the default configuration that AMS Accelerate deploys in all customer accounts. This configuration
    contains the default AMS Accelerate monitoring policy, which you should not modify because AMS Accelerate can update this profile at any time, erasing any changes
    you have made.
  - If you want to modify or disable any of these definitions, see
    [Modifying the Accelerate alarm default configuration](acc-mem-modify-default.md "acc-mem-modify-default.md") and
    [Disabling the default Accelerate alarm configuration](acc-mem-disable-default-config.md "acc-mem-disable-default-config.md").

- Customization configuration profile:
  - Any configuration in this profile is entirely managed by you; AMS Accelerate does not overwrite this profile, unless you explicitly request it.
  - You can specify any custom alarm definitions you want in this profile, and you can also specify modifications to the AMS Accelerate-managed default
    configuration. For more information, see [Modifying the Accelerate alarm default configuration](acc-mem-modify-default.md "acc-mem-modify-default.md") and
    [Disabling the default Accelerate alarm configuration](acc-mem-disable-default-config.md "acc-mem-disable-default-config.md").
  - If you update this profile, Alarm Manager automatically enforces your changes across all relevant resources in your AWS account. Note that while your changes
    are enacted automatically, they may take up to 60 minutes to take effect.
  - You can update this profile using the AWS Management Console or AWS CLI/SDK tools. See the
    [AWS AppConfig User Guide](../../../appconfig/latest/userguide/what-is-appconfig.md "../../../appconfig/latest/userguide/what-is-appconfig.md") for instructions about updating a configuration.
  - The customization profile is initially empty; however, any alarm definitions placed in the
    profile document are enforced, in addition to the default configuration.

All CloudWatch alarms created by the Alarm Manager contain the tag key **ams:alarm-manager:managed** and tag value **true**. This is to ensure
that the Alarm Manager manages only those alarms that it creates, and won’t interfere with any of your own alarms. You can see these tags using the Amazon CloudWatch
[ListTagsForResource](../../../AmazonCloudWatch/latest/APIReference/API_ListTagsForResource.md "../../../AmazonCloudWatch/latest/APIReference/API_ListTagsForResource.md") API.

###### Important

If custom alarm definitions and default alarm definitions are specified with the same ConfigurationID (see
[Accelerate Configuration profile: monitoring](acc-mem-config-doc-format.md "acc-mem-config-doc-format.md")), the custom definitions take priority over default rules.
