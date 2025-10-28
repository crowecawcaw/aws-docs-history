AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Deleting managed views

Managed views can only be deleted by the AWS service that manages them. Before the
managing service can delete the view, you may need to perform service-specific tasks to remove
a managed view from your account.

Resource Explorer managed views use the AWS Systems Manager `AWSManagedViewForSSM` unified console
resource, which allows Systems Manager to access resource information indexed by Resource Explorer for your
organization. If you want to delete the managed view, you must disable the unified console in
Systems Manager. For instructions, see [Disabling the Systems Manager unified console](../../../systems-manager/latest/userguide/systems-manager-disable-integrated-console.md "../../../systems-manager/latest/userguide/systems-manager-disable-integrated-console.md") in the _AWS Systems Manager User
Guide_.
