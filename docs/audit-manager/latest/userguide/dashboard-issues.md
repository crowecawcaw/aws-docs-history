# Troubleshooting dashboard issues

You can use the information on this page to resolve common dashboard issues in
Audit Manager.

###### Topics

- [There isn't any data on my dashboard](#dashboard-no-data "#dashboard-no-data")
- [The CSV download option
  isn't available](#dashboard-download-option-unavailable "#dashboard-download-option-unavailable")
- [I don't see the downloaded
  file when trying to download a CSV file](#dashboard-cant-find-downloaded-file "#dashboard-cant-find-downloaded-file")
- [A specific control or control domain
  is missing from the dashboard](#dashboard-no-control-domain "#dashboard-no-control-domain")
- [I see similar or duplicate controls appearing under the same control
  domain](#dashboard-similar-or-duplicate-controls-in-the-same-control-domain "#dashboard-similar-or-duplicate-controls-in-the-same-control-domain")
- [The daily snapshot shows varying
  amounts of evidence each day. Is this normal?](#dashboard-varying-evidence "#dashboard-varying-evidence")

## There isn't any data on my dashboard

If the numbers in the [Daily snapshot](dashboard.md#dashboard-daily-snapshot "dashboard.md#dashboard-daily-snapshot") widget display a hyphen (-), this
indicates that no data is available. You must have at least one active assessment to
see data in the dashboard. To get started, [create an
assessment](create-assessments.md "create-assessments.md"). After a 24-hour period, your assessment data will start to
appear in the dashboard.

###### Note

If the numbers in the daily snapshot widget display a zero (0), this indicates
that your active assessments (or your selected assessment) have no non-compliant
evidence.

## The CSV download option

isn't available

This option is available for individual assessments only. Make sure that you
applied an [Assessment filter](dashboard.md#dashboard-assessment-filters "dashboard.md#dashboard-assessment-filters") to the dashboard, then try again.
Keep in mind that you can only download one CSV file at a time.

## I don't see the downloaded

file when trying to download a CSV file

If a control domain contains a large number of controls, there might be a short
delay while Audit Manager generates the CSV file. After the file is generated, it downloads
automatically.

If you still don’t see the downloaded file, make sure that your internet
connection is working normally and you're using the most current version of your web
browser. In addition, check your recent downloads folder. Files download into the
default location that's determined by your browser. If this doesn't resolve your
issue, try downloading the file using a different browser.

## A specific control or control domain

is missing from the dashboard

This likely means that your active assessments (or specified assessment) don't
have any relevant data for that control or control domain.

A control domain is displayed on the dashboard only if both of the following two
criteria are met:

- Your active assessments (or specified assessment) contain at least one
  control that's related to that domain
- At least one control within that domain collected evidence on the date at
  the top of the dashboard

A control is displayed within a domain only if it collected evidence on the date
at the top of the dashboard.

## I see similar or duplicate controls appearing under the same control

domain

This issue can occur if your assessments collect evidence from different versions
of the same standard control.

This happens in the following scenarios:

**Scenario 1: You have two assessments created from
the same standard framework**

- You created an assessment from a standard framework before the
  launch of the common controls library.

This assessment collects evidence using outdated standard
controls.

- You also created an assessment from the same standard
  framework after the launch of the common controls library.

This assessment collects evidence using the new versions of
the standard controls.

- As a result, your assessments collect evidence from different
  versions of the same standard controls.

**Scenario 2: You have two assessments created from a
custom framework that uses standard controls**

- You created an assessment from your custom framework before
  the launch of the common controls library.

This assessment collects evidence using outdated standard
controls.

- You also created an assessment from the same custom framework
  after the launch of the common controls library.

This assessment collects evidence using the new versions of
the standard controls.

- As a result, your assessments collect evidence from different
  versions of the same standard controls.

**Example:** Let’s say you have a pre-existing
assessment that you created from the PCI DSS standard framework before June 6th, 2024. Additionally, you created a new assessment from the PCI DSS standard framework
after June 6th, 2024. As a result, the first assessment collects evidence using the
outdated version of the standard controls for PCI DSS. The second assessment
collects evidence using the new version of the standard controls for PCI DSS.
Because both versions of the PCI DSS controls are actively collecting evidence in
your assessments, you’ll likely see both of sets of controls appear in the dashboard
under the same control domain. However, in rare cases, the outdated control and the
new control might appear under different control domains on the dashboard.

You can continue to collect evidence and view dashboard insights for outdated
standard controls and frameworks. However, we encourage you to use the new controls
and frameworks that Audit Manager provides following the launch of the common controls
library on June 6, 2024. The new standard controls can collect evidence from [AWS managed source](concepts.md#aws-managed-source "concepts.md#aws-managed-source")s. This means
that whenever there’s an update to the underlying data sources for a common or core
control, Audit Manager automatically applies the same update to all related standard
controls.

## The daily snapshot shows varying

amounts of evidence each day. Is this normal?

Not all evidence is collected on a daily basis. The controls in Audit Manager assessments
are mapped to different data sources, and each one can have a different evidence
collection schedule. As a result, it's expected that the daily snapshot displays a
varying amount of evidence each day. For more information, see [Evidence collection frequency](how-evidence-is-collected.md#frequency "how-evidence-is-collected.md#frequency").
