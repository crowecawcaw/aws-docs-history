# Accelerate Resource Tagger

With Resource Tagger, you can specify rules to govern how AWS resources are tagged in your
account. While onboarding an account, AMS Accelerate deploys your tagging policy to ensure resources
within your managed accounts are tagged.

###### Contents

- [What is Resource Tagger?](acc-resource-tagger.md#acc-rt-what-is "acc-resource-tagger.md#acc-rt-what-is")
- [How Resource Tagger works](acc-resource-tagger.md#acc-rt-how-works "acc-resource-tagger.md#acc-rt-how-works")
- [Resource Tagger Configuration Profiles in AMS Accelerate](acc-tag-tools-profiles.md "acc-tag-tools-profiles.md")
  - [Syntax and structure](acc-tag-tools-profiles.md#acc-rt-config-doc-format "acc-tag-tools-profiles.md#acc-rt-config-doc-format")

- [Resource Tagger use cases in AMS Accelerate](acc-rt-using.md "acc-rt-using.md")
  - [Viewing the tags applied by Resource Tagger](acc-rt-using.md#acc-rt-using-view-tags "acc-rt-using.md#acc-rt-using-view-tags")
  - [Using Resource Tagger to create tags](acc-rt-using.md#acc-tag-how-works-rt "acc-rt-using.md#acc-tag-how-works-rt")
  - [Preventing Resource Tagger from modifying resources](acc-rt-using.md#acc-rt-preventing-rt-changes "acc-rt-using.md#acc-rt-preventing-rt-changes")
  - [Example configuration profile](acc-rt-using.md#acc-rt-using-ex-config-doc "acc-rt-using.md#acc-rt-using-ex-config-doc")
  - [Merging the default configuration](acc-rt-using.md#acc-rt-using-merge-default-config "acc-rt-using.md#acc-rt-using-merge-default-config")
  - [Disabling the default configuration](acc-rt-using.md#acc-rt-using-disable-default-config "acc-rt-using.md#acc-rt-using-disable-default-config")
  - [Removing tags applied by Resource Tagger](acc-rt-using.md#acc-rt-remove-tags "acc-rt-using.md#acc-rt-remove-tags")
  - [Viewing or making changes to the Resource Tagger configuration](acc-rt-using.md#acc-rt-make-changes "acc-rt-using.md#acc-rt-make-changes")
  - [Deploying configuration changes](acc-rt-using.md#acc-rt-deploy-changes "acc-rt-using.md#acc-rt-deploy-changes")
  - [Configuring Terraform to ignore Resource Tagger tags](acc-rt-using.md#acc-rt-ignore-tags "acc-rt-using.md#acc-rt-ignore-tags")
  - [Viewing the number of resources managed by Resource Tagger](acc-rt-using.md#acc-rt-number-of-resources "acc-rt-using.md#acc-rt-number-of-resources")

## What is Resource Tagger?

Resource Tagger is an AMS Accelerate service offering you use to specify rules to govern how AWS resources are tagged
in your account. It aims to provide you with complete visibility into how your tags are applied to your AWS
resources.

Resource Tagger automatically creates, updates, and deletes tags on supported AWS
resources, based on the tagging rules you specify in your configuration profiles. For
example, you can specify a rule that applies a tag to a collection of Amazon EC2 instances,
indicating that they should be managed by AMS Accelerate, which results in the instances being
monitored or backed up. You can use tags like this to identify compliance status for the AWS
resources based on the defined policy in your AWS AppConfig configuration profiles. For more
information, see [AWS AppConfig](../../../appconfig/latest/userguide/what-is-appconfig.md "../../../appconfig/latest/userguide/what-is-appconfig.md").

AMS Accelerate provides a default managed tagging configuration so you can have your resources
monitored by AMS Accelerate. You define which resources should be managed by AMS Accelerate, and the managed tagging
rules ensure that the resources having the appropriate tags are monitored by AMS Accelerate.

With Resource Tagger, if you choose, you can override or deactivate the default
AMS Accelerate managed tags, provide your own tagging rules to meet your policies, and use
other mechanisms, such as Terraform, to avoid drift. You can define the exceptions to scale,
based on your operations. For example, you could define policy to apply tags for all Amazon EC2
instances with supported platforms (such as Windows and Linux), and exclude from tagging
specific instance IDs.

###### Important

Resource Tagger controls all tags in your account that have the **ams:rt:** prefix.
Any tags that begin with this prefix are deleted unless they are present in Resource
Tagger's configuration rules. To summarize, any tag on supported resources that starts
with **ams:rt:** is considered owned by Resource Tagger. If you manually tag
something with, for example, **ams:rt:**, that tag would automatically be
removed if it wasn't specified in one of the Resource Tagger configuration profiles.

## How Resource Tagger works

When your account is onboarded to AMS Accelerate, two JSON configuration documents are
deployed to your account in AWS AppConfig. The two documents, called _Configuration profiles_,
are **AMSManagedTags**, referred to as the **default
configuration profile**, and **CustomerManagedTags**, referred to as the
**customization configuration profile**. You use the customization configuration profile to
define your own policies and rules for your accounts, and those are not overwritten by AMS Accelerate.

Both profiles reside in the **AMSResourceTagger** application, and in the **AMSInfrastructure**
environment. All tags applied by the resource tagger have the key prefix **ams:rt:**.

**Customization configuration profile**:

The customization configuration profile is initially empty at the time of account
onboarding; however, any rules placed in the profile document are enforced, in addition to the rules
in the default configuration profile. Any configuration in the customization configuration
profile is entirely managed by you, and is not overwritten by AMS Accelerate, except by your request.

You can specify any custom tagging rules you want in the custom configuration profile for
the supported AWS resources, and you can also specify modifications to the AMS Accelerate-managed
default configuration here, see [Resource Tagger use cases in AMS Accelerate](acc-rt-using.md "acc-rt-using.md").

###### Important

If you update this profile, the Resource Tagger automatically enforces the changes across all
relevant resources in your AWS account. The changes are enacted automatically, but they
may take up to 60 minutes to take effect.

You can update this profile by using the AWS Management Console, or through AWS CLI/SDK tools. For
information about updating a customization configuration profile, see the AWS AppConfig user guide:
[What Is AWS AppConfig?](../../../appconfig/latest/userguide/what-is-appconfig.md "../../../appconfig/latest/userguide/what-is-appconfig.md")

**Default configuration profile**:

The default configuration profile document is internal to AMS Accelerate and it contains AMS Accelerate-supplied
default rules that you can't modify or delete permanently. This profile can be updated at any time by
AMS Accelerate and made available to you for review; any changes you have made to it are automatically
deleted. If you want to modify or disable any of the default configuration rules you use the
customization configuration profile, see [Resource Tagger use cases in AMS Accelerate](acc-rt-using.md "acc-rt-using.md").
