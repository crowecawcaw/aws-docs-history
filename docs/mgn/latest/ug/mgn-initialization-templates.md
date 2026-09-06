

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Configuring the templates
<a name="mgn-initialization-templates"></a>

As part of the initialization of AWS Transform MGN, you have the opportunity to configure three templates.
+ Replication template (mandatory)
+ Launch template (optional)
+ Post-launch template (optional)

## Configuring your replication template
<a name="mgn-initialization-replication-template"></a>

To initialize AWS Transform MGN, you must first create and configure a replication template. If you initialize MGN with the console, the initialization process creates the template for you. If you initialize MGN with the API, you create the template. For more information, see [Initializing AWS Transform MGN with the API](mgn-initialize-api.md)

The replication template determines how data replication will work for each new server you add. The settings configured in this template will be applied to each newly added source server. [Learn more about the replication template](replication-settings-template.md#template-vs-server). 

## Configuring your launch template
<a name="mgn-initializing-launch-template"></a>

As part of the AWS MGN initialization process, you can configure your launch template. Every source server added to AWS MGN has launch settings that control actions performed after the server is launched in AWS. These settings are created automatically based on this default launch template, which can be modified at any time. You can also choose to modify the launch template for an individual source server.

[Learn more about the launch template](launch-template.md).

## Configuring a post-launch template
<a name="mgn-initialization-post-launch-template"></a>

 As part of the AWS MGN initialization process, you can configure your post-launch template. The post-launch template controls which post-launch actions will be executed when launching new instances. These settings are created automatically for each server based on the post-launch template and can be modified at any time. You can also modify the post-launch settings for any individual source server. 

To configure the post-launch actions, complete the following steps:

1. [Activate post-launch actions](post-launch-settings.md#post-launch-settings-activation).

1. [Configure predefined post-launch actions](predefined-post-launch-actions.md) according to your preferences.

1. [Create custom post-launch actions](post-launch-settings.md#post-launch-settings-custom-actions-add) according to your preferences.