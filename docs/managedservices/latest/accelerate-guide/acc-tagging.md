# Tagging in AMS Accelerate

Most Accelerate features (patching, backup, monitoring) use _tags_ and
_configuration profiles_ to decide which of your resources to manage,
what actions to apply, and when to apply them.
Tags are labels that you apply to resources.
Configuration profiles contain rules based on those tags.

Each Accelerate feature has its own tagging requirements. Some features require you to
use specific tags, while others allow you to use any of your own.

For information about required tags, see [Customer-managed tags in Accelerate](acc-tag-req.md "acc-tag-req.md").

For information about tags that can be defined customers, see [Customer-provided tags in Accelerate](acc-tag-cust-provided.md "acc-tag-cust-provided.md")

###### Contents

- [Tags](acc-tag-intro.md "acc-tag-intro.md")
  - [What are tags?](acc-tag-intro.md#acc-tag-what-is "acc-tag-intro.md#acc-tag-what-is")
  - [How tagging works](acc-tag-intro.md#acc-tag-how-works "acc-tag-intro.md#acc-tag-how-works")
  - [Customer-managed tags](acc-tag-req.md "acc-tag-req.md")
    - [Monitoring](acc-tag-req-mon.md "acc-tag-req-mon.md")
    - [Configuring EC2 instances](acc-tag-req-ins-config.md "acc-tag-req-ins-config.md")
    - [Backups](acc-tag-req-backup.md "acc-tag-req-backup.md")

  - [Accelerate-managed tags](acc-tag-infra.md "acc-tag-infra.md")
  - [Customer-provided tags](acc-tag-cust-provided.md "acc-tag-cust-provided.md")

- [Tag management tools](acc-tag-tools.md "acc-tag-tools.md")
  - [Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md")
    - [What is Resource Tagger?](acc-resource-tagger.md#acc-rt-what-is "acc-resource-tagger.md#acc-rt-what-is")
    - [How Resource Tagger works](acc-resource-tagger.md#acc-rt-how-works "acc-resource-tagger.md#acc-rt-how-works")
    - [Configuration Profiles](acc-tag-tools-profiles.md "acc-tag-tools-profiles.md")
      - [Syntax and structure](acc-tag-tools-profiles.md#acc-rt-config-doc-format "acc-tag-tools-profiles.md#acc-rt-config-doc-format")

    - [Use cases](acc-rt-using.md "acc-rt-using.md")
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

  - [CloudFormation](acc-tag-how-works-cfn.md "acc-tag-how-works-cfn.md")
    - [Use cases](acc-tag-tools-cf-ex.md "acc-tag-tools-cf-ex.md")
      - [Tag EC2](acc-tag-cf-ex-tag-ec2.md "acc-tag-cf-ex-tag-ec2.md")
      - [Tag ASG](acc-tag-cf-ex-tag-asg.md "acc-tag-cf-ex-tag-asg.md")
      - [Deploy config profile](acc-tag-cf-ex-deploy-config.md "acc-tag-cf-ex-deploy-config.md")

  - [Terraform](acc-tag-tools-terraform.md "acc-tag-tools-terraform.md")
