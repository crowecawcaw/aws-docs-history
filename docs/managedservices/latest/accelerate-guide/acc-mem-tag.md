# Accelerate Alarm Manager tags

By default, when you onboard with AMS Accelerate, your configuration is deployed to AWS AppConfig, defining an alarm baseline for your resources. The alarm definitions
are applied only to resources with the **ams:rt:\*** tags. We recommend that these tags be applied using the
[Accelerate Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md"): you set up a
basic Resource Tagger configuration in order to let AMS Accelerate know which resources you want managed.

Use Resource Tagger to apply the tag key **ams:rt:ams-managed** with tag value **true** to any resources you want AMS Accelerate
to monitor.

###### Topics

- [Accelerate tags using Resource Tagger](acc-mem-tag-alarms-use-rt.md "acc-mem-tag-alarms-use-rt.md")
- [Accelerate tags without Resource Tagger](acc-mem-tags-no-rt.md "acc-mem-tags-no-rt.md")
- [Accelerate tags using CloudFormation](acc-mem-tags-cfn.md "acc-mem-tags-cfn.md")
- [Accelerate tags using Terraform](acc-mem-tags-terraform.md "acc-mem-tags-terraform.md")
