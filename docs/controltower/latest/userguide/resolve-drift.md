

# Resolve drift with Reset and Re-register
<a name="resolve-drift"></a>

Drift often occurs as you and your organization members use the landing zone.

Drift detection is automatic in AWS Control Tower. Automated scans of your SCPs help you identify resources that need changes or configuration updates that must be made to resolve the drift. 

To repair many types of drift, choose **Reset** on the **Landing zone settings** page in the console. Also, you can resolve some types of drift by choosing to ** Re-register** an OU in the console. For controls, you can resolve drift programmatically by calling the **ResetEnabledControl** API. For more information about types of drift and how to resolve them, see [Types of governance drift](governance-drift.md) and [Detect and resolve drift in AWS Control Tower](drift.md).

One special case of drift resolution occurs for *role drift*. If a required role is not available, the console shows a warning page and some instructions on how to restore the role. Your landing zone is unavailable until the role drift is resolved. This drift reset is not the same as a full landing zone reset. For more information, see *Don't delete required roles* in the section called [Types of drift to resolve right away](drift.md#types-of-drift).

**When you take action to resolve drift on a landing zone version, the behavior depends on your current version.**  
If you are on landing zone version 3.1 or above, you can choose **Update** to change your landing zone configuration without upgrading versions, or choose **Reset** to reapply your saved configurations to your drifted landing zone resources. Drift is resolved as part of the update process.
If you are on a landing zone version earlier than 3.1, you cannot choose **Reset**. You must choose **Update** and upgrade your landing zone to at least version 3.1.