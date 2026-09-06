

# Compatibility of OU baselines and landing zone versions
<a name="table-of-baselines"></a>

AWS Control Tower baselines allow you to set a governance standard at the OU level, rather than at the landing zone level, if your business requires it. The baseline called `AWSControlTowerBaseline` is available to help register your OUs with AWS Control Tower.

**Note**  
A *baseline* is a group of controls and resources that work together to establish a stable governance environment within your landing zone.

When you enable a baseline on an OU, by callling the `EnableBaseline` API in AWS Control Tower, you must specify a baseline version that's compatible with your current AWS Control Tower landing zone version. After you specify a baseline, all member accounts in an OU follow the baseline given for the OU. In other words, new accounts are provisioned with the updated baseline, and existing member accounts become governed according to the new baseline.

If you do not select a baseline for your existing OUs and accounts, the landing zone version determines the entire governance posture, by default. However, each registered OU in your landing zone is assigned a baseline version, which is the latest baseline compatible with your current landing zone version. Therefore, each OU and enrolled member account has an associated baseline, even if you never assign a baseline specifically.

For the OU-level baseline, `AWSControlTowerBaseline`, the table that follows shows the compatibility of baselines with AWS Control Tower landing zone versions.


| **Baseline version** | **Landing zone versions** | **Included blueprints** | **Change from previous baseline** | 
| --- | --- | --- | --- | 
| 1.0 | 2.0 to 2.7 | BP\_BASELINE\_CLOUDTRAIL, BP\_BASELINE\_CLOUDWATCH, BP\_BASELINE\_CONFIG, BP\_BASELINE\_ROLES, BP\_BASELINE\_SERVICE\_ROLES, IAM Resources | None | 
| 2.0 | 2.8 to 2.9 | BP\_BASELINE\_CLOUDTRAIL, BP\_BASELINE\_CLOUDWATCH, BP\_BASELINE\_CONFIG, BP\_BASELINE\_ROLES, BP\_BASELINE\_SERVICE\_ROLES, Config SLR, IAM resources | Added AWS Config service-linked role (SLR) and new Config blueprint to use the SLR | 
| 3.0 | 3.0 to 3.1 | BP\_BASELINE\_CLOUDWATCH, BP\_BASELINE\_CONFIG, BP\_BASELINE\_ROLES, BP\_BASELINE\_SERVICE\_ROLES, Config SLR, IAM resources | New AWS Config blueprint. Change to record global resources only in home Region. Removed CloudTrail blueprint | 
| 4.0 | 3.2 to 3.3 | BP\_BASELINE\_CLOUDWATCH, BP\_BASELINE\_CONFIG, BP\_BASELINE\_ROLES, BP\_BASELINE\_SERVICE\_LINKED\_ROLE, BP\_BASELINE\_SERVICE\_ROLES, Config SLR, IAM resources | New SLR blueprint | 
| 5.0 | 4.0 | BP\_BASELINE\_CLOUDWATCH, BP\_BASELINE\_CONFIG, BP\_BASELINE\_ROLES, BP\_BASELINE\_SERVICE\_LINKED\_ROLE, BP\_BASELINE\_SERVICE\_ROLES, Config SLR, IAM resources | Removed AWS Config Aggregation Authorization(s). AWS Config Aggregation Authorization from each member account is not needed since LandingZone version 4.0 adopted AWS Organizations Config Aggregator which has access to all member accounts within the Organization. | 

For more information about specific resources created in accounts when you set up your landing zone, see [Resources created in the shared accounts](https://docs.aws.amazon.com/controltower/latest/userguide/shared-account-resources.html).

If you update your landing zone to a version that supports a newer `AWSControlTowerBaseline` baseline version, and the new landing zone version is compatible with your existing baseline version, your OU state changes to **Update available**.
+ You can continue to use Account Factory and other features without updating the organizational unit (OU) baseline immediately.
+ New accounts enrolled in this OU receive resources based on the existing baseline version until the baseline version is updated (with the **Extend governance** feature in the console, or by means of the `UpdateEnabledBaseline` API).
+ After you update the baseline version, all accounts within that OU receive resources based on the new baseline version.

**Note**  
If you update your AWS Control Tower landing zone from any version 2.X to any version 3.X, you also must update the baseline version on your OUs, due to the change from account-level to organization-level AWS CloudTrail trails. In the console, your OU will show a status of **Update required**.

 **Considerations for baselines**
+ If your OU requires a baseline update, you cannot provision new accounts or enroll existing accounts into that OU.
+ After a landing zone update, if you also plan to update an OU baseline, you must re-register the OU or update your OU baseline version programmatically.
+ We recommend that you update to the highest compatible baseline for the landing zone version you're using, so that you gain all the benefits of the landing zone and the baseline combined. For example, if you update to landing zone version 3.3, you can keep using baseline 3.0, but you do not get every benefit of landing zone version 3.3 unless you also update to baseline 4.0.
+ Baseline updates cannot be rolled back.
+ Baseline enablement targets one OU at a time. Therefore, nested OUs are not updated automatically when the parent OU is updated. We recommend that you update the parent OU before you update the nested OUs.
+  When you call the `UpdateEnabledBaseline` API or re-register an OU from the console, the OU retains all controls that were enabled before the baseline update.
+ When multiple baseline versions are compatible with your landing zone version, you must use the latest baseline version if you enable a baseline on an unmanaged OU.