# Athena engine versioning

Athena occasionally releases a new engine version to provide improved performance,
functionality, and code fixes. When a new engine version is available, Athena notifies you
through the Athena console and your [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/ "https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/"). Your AWS Health Dashboard notifies you about events that can affect your AWS
services or account. For more information about AWS Health Dashboard, see [Getting started with the
AWS Health Dashboard](../../../health/latest/ug/getting-started-phd.md "../../../health/latest/ug/getting-started-phd.md").

Engine versioning is configured per [workgroup](workgroups-manage-queries-control-costs.md "workgroups-manage-queries-control-costs.md"). You can
use workgroups to control which query engine your queries use and whether to let Athena
automatically upgrade your workgroups. The query engine that is in use is shown in the query
editor, on the workgroup details page, and is available through the Athena APIs.

- By default, workgroups are configured to auto upgrade. When a workgroup is set to
  auto upgrade, Athena upgrades the workgroup for you unless it finds
  incompatibilities.
- If you configure a workgroup to use a given version, Athena will not change the
  version of the workgroup.
  In both cases, Athena upgrades your workgroups when a version is no longer available. Athena
  notifies you through [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/ "https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/") regarding when an engine version will no longer be offered. Your
  Health Dashboard notifies you about events that can affect your AWS services or account. For more
  information about AWS Health Dashboard, see [Getting started with the
  AWS Health Dashboard](../../../health/latest/ug/getting-started-phd.md "../../../health/latest/ug/getting-started-phd.md").

When you start using a new engine version, a small subset of queries may break due to
incompatibilities. Breaking changes are announced when a new Athena version is released. You
should use workgroups to test your queries in advance of the upgrade by creating a test
workgroup that uses the new engine or by test upgrading an existing workgroup. For more
information, see [Test queries in advance of an engine version upgrade](engine-versions-changing.md#engine-versions-testing "engine-versions-changing.md#engine-versions-testing").

###### Topics

- [Change Athena engine versions](engine-versions-changing.md "engine-versions-changing.md")
- [Athena engine version 3](engine-versions-reference-0003.md "engine-versions-reference-0003.md")
