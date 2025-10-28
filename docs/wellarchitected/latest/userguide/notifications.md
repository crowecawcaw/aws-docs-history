# Notifications

The **Notifications** page displays version differences for workloads and
review templates that have lenses and profiles associated with them. You can upgrade to the
newest version of a lens or profile for a workload from the Notifications page.

## Lens notifications

When a new version of a lens is available, a banner appears at the top of the
**Workloads** or **Review templates** page to
notify you. If you view a specific workload or review template using an outdated lens,
you will also see a banner indicating that a new lens version is available.

Choose **View available upgrades** for a list of workloads or review
templates that can be upgraded.

See [Upgrading a lens in AWS WA Tool](lenses-upgrading.md "lenses-upgrading.md") for instructions on upgrading a lens for a
workload or a review template.

When the owner of a shared lens deletes it, if you have a workload associated with the
deleted lens, you will receive a notification that you can still use the lens in your
existing workload, but you will not be able to add it to new workloads.

## Profile notifications

There are two types of **Profile notifications**:

- Profile upgrade
- Profile deletion

When a profile associated with a workload has been
edited (for more information, see [Editing a profile in AWS WA Tool](editing-profiles.md "editing-profiles.md")), a notification
that there is a new version of the profile is displayed in **Profile
notifications**.

When the owner of a shared profile deletes it, if
you have a workload associated with the deleted profile, you will receive a notification
that you can still use the profile in your existing workload, but you will not be able
to add it to new workloads.

###### To upgrade a profile version

1. In the left navigation pane, select **Notifications**.
2. Select the name of the workload from the list on the **Profile notifications** tab, or use the search bar to search by workload name.
3. Choose **upgrade profile version**.
4. In the **Acknowledgment** section, select the confirmation box for **I understand and accept these changes**.
5. (Optional) If choosing to save a milestone, select the **Save a milestone** box and provide a **Milestone name**.
6. Select **Save**.

Once the profile is upgraded, the latest version number and updated date is displayed in the **Profile** section of the workload.

See [Using profiles in AWS WA Tool](profiles.md "profiles.md") for more information.
