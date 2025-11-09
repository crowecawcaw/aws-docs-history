# Compatibility of OU baselines and landing zone

versions

AWS Control Tower baselines allow you to set a governance standard at the OU level, rather than at
the landing zone level, if your business requires it. The baseline called
`AWSControlTowerBaseline` is available to help register your OUs with
AWS Control Tower.

###### Note

A _baseline_ is a group of controls and resources that work
together to establish a stable governance environment within your landing zone.

When you enable a baseline on an OU, by callling the `EnableBaseline` API
in AWS Control Tower, you must specify a
baseline version that's compatible with your current AWS Control Tower landing zone version. After
you specify a baseline, all member accounts in an OU follow the baseline given for the OU.
In other words, new accounts are provisioned with the updated baseline, and existing member
accounts become governed according to the new baseline.

If you do not select a baseline for your existing OUs and accounts, the landing zone
version determines the entire governance posture, by default. However, each registered OU in
your landing zone is assigned a baseline version, which is the latest baseline compatible
with your current landing zone version. Therefore, each OU and enrolled member account has
an associated baseline, even if you never assign a baseline specifically.

For the OU-level baseline, `AWSControlTowerBaseline`, the table that follows
shows the compatibility of baselines with AWS Control Tower landing zone versions.

| **Baseline version** | **Landing zone versions** | **Included blueprints**                                                                                                                                    | **Included controls**  | **Change from previous baseline**                                                                                |
| -------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 1.0                  | 2.0 to 2.7                | BP_BASELINE_CLOUDTRAIL, BP_BASELINE_CLOUDWATCH, BP_BASELINE_CONFIG,<br>BP_BASELINE_ROLES, BP_BASELINE_SERVICE_ROLES, IAM<br>Resources                      | All mandatory controls | None                                                                                                             |
| 2.0                  | 2.8 to 2.9                | BP_BASELINE_CLOUDTRAIL, BP_BASELINE_CLOUDWATCH, BP_BASELINE_CONFIG,<br>BP_BASELINE_ROLES, BP_BASELINE_SERVICE_ROLES, Config SLR, IAM<br>resources          | All mandatory controls | Added AWS Config service-linked role (SLR) and new Config blueprint to<br>use the SLR                            |
| 3.0                  | 3.0 to 3.1                | BP_BASELINE_CLOUDWATCH, BP_BASELINE_CONFIG, BP_BASELINE_ROLES,<br>BP_BASELINE_SERVICE_ROLES, Config SLR, IAM resources                                     | All mandatory controls | New AWS Config blueprint. Change to record global resources only in home<br>Region. Removed CloudTrail blueprint |
| 4.0                  | 3.2 to 3.3                | BP_BASELINE_CLOUDWATCH, BP_BASELINE_CONFIG, BP_BASELINE_ROLES,<br>BP_BASELINE_SERVICE_LINKED_ROLE, BP_BASELINE_SERVICE_ROLES, Config SLR,<br>IAM resources | All mandatory controls | New SLR blueprint                                                                                                |

For more information about specific resources created in accounts when you set up your
landing zone, see [Resources created in
the shared accounts](shared-account-resources.md "shared-account-resources.md").

If you update your landing zone to a version that supports a newer
`AWSControlTowerBaseline` baseline version, and the new landing zone version
is compatible with your existing baseline version, your OU state changes to **Update
available**.

- You can continue to use account factory and other features without updating the OU
  baseline immediately, except in the case of a landing zone update from 2.x to
  3.x.
- New accounts enrolled in this OU receive resources based on the existing baseline
  version until the baseline version is updated (with the **Extend
  governance** feature in the console, or by means of the
  `UpdateEnabledBaseline` API).
- After you update the baseline version, all accounts within that OU receive
  resources based on the new baseline version.

###### Note

If you update your AWS Control Tower landing zone from any version 2.X to any version 3.X, you
also must update the baseline version on your OUs, due to the change from account-level
to organization-level AWS CloudTrail trails. In the console, your OU will show a status of
**Update required**.

**Considerations for baselines**

- If your OU requires a baseline update, you cannot provision new accounts or enroll
  existing accounts into that OU.
- After a landing zone update, if you also plan to update an OU baseline, you must
  re-register the OU or update your OU baseline version programmatically.
- We recommend that you update to the highest compatible baseline for the landing
  zone version you're using, so that you gain all the benefits of the landing zone and
  the baseline combined. For example, if you update to landing zone version 3.3, you
  can keep using baseline 3.0, but you do not get every benefit of landing zone
  version 3.3 unless you also update to baseline 4.0.
- Baseline updates cannot be rolled back.
- Baseline enablement targets one OU at a time. Therefore, nested OUs are not
  updated automatically when the parent OU is updated. We recommend that you update
  the parent OU before you update the nested OUs.
- When you call the `UpdateEnabledBaseline` API or re-register an OU
  from the console, the OU retains all controls that were enabled before the baseline
  update.
- When multiple baseline versions are compatible with your landing zone version, you
  must use the latest baseline version if you enable a baseline on an unmanaged
  OU.
