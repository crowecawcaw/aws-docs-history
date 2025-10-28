# AWS Config Process Checks Within a Conformance Pack for AWS Config

Process checks is a type of AWS Config rule that allows you to track your external and internal
tasks that require verification as part of the conformance packs. These checks can be added
to an existing conformance pack or a new conformance pack. You can track all compliance that
includes AWS Configurations and manual checks in a single location.

With process checks, you can list the compliance of requirements and actions at a single
location. These process checks help increase the coverage of compliance regimes-based
conformance packs. You can further expand the conformance pack by adding new process checks
that track processes and actions needing manual verification and tracking. This enables
conformance pack to become the template that provides details about AWS Configurations and manual
processes for a compliance regime.

You can track and manage the compliance of
processes not associated with resource configuration changes within a conformance packs as
process checks. For example, you can add a process check to track the PCI-DSS compliance
requirement to store media backup at an offsite location. You will manually evaluate the
compliance of this according to PCI-DSS guidelines, or according to your organization's
guidance.

**Region availability**: Process checks with the conformance packs are
available in all AWS Regions where AWS Config conformance packs are available. For more
information, see [Region Support](conformance-packs.md#conformance-packs-regions "conformance-packs.md#conformance-packs-regions").

###### Topics

- [Sample Template](Sample-CPack-Template-for-Creating-Process-Check-Rule.md "Sample-CPack-Template-for-Creating-Process-Check-Rule.md")
- [Creating Process Checks](How-to-create-a-Process-Check-Rule.md "How-to-create-a-Process-Check-Rule.md")
- [Changing Compliance Status](change-compliance-status.md "change-compliance-status.md")
- [View and Edit](view-a-process-check-console.md "view-a-process-check-console.md")
