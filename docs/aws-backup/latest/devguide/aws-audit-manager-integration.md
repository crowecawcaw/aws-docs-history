# Using AWS Backup Audit Manager with

AWS Audit Manager

AWS Backup Audit Manager controls map to prebuilt, standard controls in AWS Audit Manager, allowing you
to import your AWS Backup Audit Manager compliance findings to your AWS Audit Manager reports. You might
want to do so to help a compliance officer, audit manager, or other colleague who reports on
backup activity as part of your organization’s overall compliance posture.

You can import the compliance results of your AWS Backup Audit Manager controls to your
AWS Audit Manager frameworks. To enable AWS Audit Manager to automatically collect data from your AWS Backup Audit
Manager controls, create a custom control in AWS Audit Manager using the instructions for [Customizing an
existing control](../../../audit-manager/latest/userguide/customize-control-from-existing.md "../../../audit-manager/latest/userguide/customize-control-from-existing.md") in the _AWS Audit Manager User Guide_. As you follow
those instructions, note that the **Data source** for AWS Backup controls is
**AWS Config**.

For a list of AWS Backup controls, see [Choosing your
controls](choosing-controls.md "choosing-controls.md").
