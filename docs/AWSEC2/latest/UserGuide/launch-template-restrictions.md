# Restrictions for Amazon EC2 launch

templates

The following restrictions apply to launch templates and launch template
versions:

- Quotas – To view the
  quotas for your launch templates and launch template versions, open the [Service Quotas](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") console or use
  the [list-service-quotas](../../../cli/latest/reference/service-quotas/list-service-quotas.md "../../../cli/latest/reference/service-quotas/list-service-quotas.md") AWS CLI command. Each AWS account can have up to
  a maximum of 5,000 launch templates per Region and up to 10,000 versions per
  launch template. Your accounts might have different quotas based on their age
  and usage history.
- Parameters are optional – Launch
  template parameters are optional. However, you must ensure that your instance
  launch request includes all required parameters. For example, if your launch
  template does not include an AMI ID, you must specify an AMI ID when launching
  an instance with this launch template.
- Parameters not validated – Launch
  template parameters are not fully validated when you create the launch template.
  If you specify incorrect values or use unsupported parameter combinations,
  instances will fail to launch using this launch template. To avoid issues, make
  sure to specify correct values and use supported parameter combinations. For
  example, to launch an instance in a placement group, you must specify a
  supported instance type.
- Tags – You can tag a launch template,
  but you can't tag a launch template version.
- Immutable – Launch templates are
  immutable. To modify a launch template, you must create a new version of the
  launch template.
- Version numbers – Launch template
  versions are numbered in the order in which they are created. When you create a
  launch template version, you can't specify the version number yourself.
