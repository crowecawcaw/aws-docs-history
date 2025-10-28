# Service-managed standards in Security Hub CSPM

A service-managed standard is a security standard that another AWS service manages but that you can view in Security Hub CSPM. For example,
[Service-Managed Standard: AWS Control Tower](service-managed-standard-aws-control-tower.md "service-managed-standard-aws-control-tower.md") is a
service-managed standard that AWS Control Tower manages. A service-managed standard differs from a security standard that
AWS Security Hub CSPM manages in the following ways:

- **Standard creation and deletion** – You
  create and delete a service-managed standard with the managing service's console or API, or with
  the AWS CLI. Until you create the standard in the managing service in one of those
  ways, the standard doesn't appear in the Security Hub CSPM console and isn't accessible by the
  Security Hub CSPM API or AWS CLI.
- **No automatic enablement of controls** – When
  you create a service-managed standard, Security Hub CSPM and the managing service don't automatically enable
  the controls that apply to the standard. In addition, when Security Hub CSPM releases new
  controls for the standard, they're not automatically enabled. This is a departure
  from standards that Security Hub CSPM manages. For more information about the usual way of
  configuring controls in Security Hub CSPM, see [Understanding security controls in Security Hub CSPM](controls-view-manage.md "controls-view-manage.md").
- **Enabling and disabling controls** – We
  recommend enabling and disabling controls in the managing service to avoid
  drift.
- **Availability of controls** – The managing
  service chooses which controls are available as part of the service-managed
  standard. Available controls may include all, or a subset of, the existing Security Hub CSPM
  controls.
  After the managing service creates the service-managed standard and makes controls available for it,
  you can access your control findings, control statuses, and standard security score in the
  Security Hub CSPM console, Security Hub CSPM API, or AWS CLI. Some or all of this information may also be available in
  the managing service.

Select a service-managed standard from the following list to view more details about it.

###### Service-managed standards

- [Service-Managed Standard: AWS Control Tower](service-managed-standard-aws-control-tower.md "service-managed-standard-aws-control-tower.md")
