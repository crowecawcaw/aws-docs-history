# Determining which lens to upgrade in AWS WA Tool

You can find which workloads aren't using the most current lens version by viewing
the **Notifications** page.

The following information is displayed on the **Notifications** page for each workload:

**Resource**

The name of the workload or review template.

**Resource type**

The type of resource. This can be either **Workload**
or **Review template**.

**Associated resource**

The name of the lens.

**Notification type**

The type of upgrade notification.

- **Not current** – The workload is using a
  version of the lens that is no longer current. Upgrade to the
  current lens version for better guidance.
- **Deprecated** – The workload is using a
  version of the lens that no longer reflects best practices.
  Upgrade to the current lens version.
- **Deleted** – The workload is using a lens
  that has been deleted by its owner.

**Version in use**

The lens version currently used for the workload.

**Current available version**

The lens version available for upgrade, or **None**
if the lens has been deleted.

To upgrade the lens associated with a workload, select the workload and choose
**Upgrade lens version**.
