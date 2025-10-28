# Resolve drift with Reset and Re-register

Drift often occurs as you and your organization members use the landing zone.

Drift detection is automatic in AWS Control Tower. Automated scans of your SCPs help you identify
resources that need changes or configuration updates that must be made to resolve the drift.

To repair many types of drift, choose **Reset** on the **Landing
zone settings** page in the console. Also, you can resolve some types of drift by
choosing to **Re-register** an OU in the console. For controls, you can
resolve drift programmatically by calling the **ResetEnabledControl** API.
For more information about types of drift and how to resolve them, see [Types of governance drift](governance-drift.md "governance-drift.md") and [Detect and resolve drift in AWS Control Tower](drift.md "drift.md").

One special case of drift resolution occurs for _role
drift_. If a required role is not available, the console shows a warning page and
some instructions on how to restore the role. Your landing zone is unavailable until the role
drift is resolved. This drift reset is not the same as a full landing zone reset. For more
information, see _Don't delete required roles_ in the section
called [Types of drift to resolve right away](drift.md#types-of-drift "drift.md#types-of-drift").

###### When you take action to resolve drift on a landing zone version, two behaviors are

possible.

- If you are on the latest landing zone version, when you choose
  **Reset** and then choose **Confirm**, your drifted
  landing zone resources are reset to the saved AWS Control Tower configuration. The landing zone
  version stays the same.
- If you are not on the latest version, you must choose **Update**.
  The landing zone is upgraded to the latest landing zone version. Drift is resolved as
  part of this process.
