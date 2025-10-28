# Select a landing zone version

If you are running AWS Control Tower landing zone version 3.1 and above, you can choose to stay on
the current version, or you can upgrade to a newer version, when you perform an
**Update** or **Reset** operation on your landing zone
configurations. The **Reset** operation is the best way to repair drift, in
most situations.

You can choose a landing zone version in the AWS Control Tower console, or by means of the AWS Control Tower
APIs.

###### Note

If you choose to deploy a landing zone version that skips over an intermediate
version, for example if you move from 3.1 to 3.3, AWS Control Tower automatically deploys the
intermediate version as part of the update operation.

In conversation, moving to a newer version is often referred to as an
_upgrade_, not just an update. These two concepts are distinct,
because you can _update_ your landing zone settings without upgrading
to a new version, for example, by changing the Regions that you govern. In the console,
the **Update** button performs an in-place update or an upgrade
operation, based on your current landing zone version and the one you select to
deploy.

**Choose your landing zone version – console
procedure**

1. From the AWS Control Tower console, navigate to the **Landing zone
   settings** page. In the table of available landing zones, select the
   new version. Remember that you can select versions 3.1 or later. Versions previous
   to 3.1 are not compatible with this feature.
2. When you select a version from the table, you can see the available actions.
   **Update** is available if your current version is earlier than
   the selected version. **Reset** is available if your current
   version is 3.1 or newer.
3. After you choose the version, select the **Update** button or the
   **Reset** button, in the upper right area of the screen.
4. You will see a confirmation display showing the landing zone version that you've
   selected for deployment. To continue, choose **Next** at the lower
   right. Your update operation may take a few minutes or more.
5. After the landing zone is updated, you may need to update your accounts. The
   easiest way to do the account updates is by a **Re-register OU**
   process for each of your registered OUs.

## Account updates, landing zone versions,

and baselines

AWS Control Tower landing zones are AWS resources that correspond to a set of baseline
configurations. There is not a one-to-one mapping of baselines and landing zone
versions. You can view a table that shows [Compatibility of OU baselines and landing zone
versions](table-of-baselines.md "table-of-baselines.md").

When you jump a baseline version, you must update accounts after your landing zone
update. For example, when upgrading from 3.1 to 3.2, you would not need to update your
accounts, because these landing zone versions share the same baseline.

In contrast, if you upgrade from 3.1 to 3.3, you would have to update accounts,
because the baseline version is 4.0, which encompasses 3.2 to 3.3.

For more information about the relationship between landing zone versions and
baselines, see [Compatibility of OU baselines and landing zone
versions](table-of-baselines.md "table-of-baselines.md").
