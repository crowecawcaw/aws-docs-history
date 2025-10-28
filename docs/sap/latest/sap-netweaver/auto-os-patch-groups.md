# Create patch groups

You can use patch groups to organize instances for patching. This can help you ensure that you only deploy patches to the correct set of instances and that the patches have been adequately tested before they are deployed. After you create the patch group, you can tag your Amazon EC2 instances to add them to the patch group and then add the patch group to a patch baseline.

You might want to organize patch groups by:

- Operating system – such as Linux and Windows
- Environment – such as development, test, and production
- Server function – such as SAP database servers and SAP application servers

###### Note

An Amazon EC2 instance can only be in one patch group at a time.

For more information about patch groups, see [About patch groups](../../../systems-manager/latest/userguide/sysman-patch-patchgroups.md "../../../systems-manager/latest/userguide/sysman-patch-patchgroups.md") in the _AWS Systems Manager User Guide_.

**Tag Amazon EC2 instances to add to the patch group**

After you create the patch group, use tags to add Amazon EC2 instances to the patch group. For detailed steps on how to do this, see [Working with patch groups](../../../systems-manager/latest/userguide/sysman-patch-group-tagging.md "../../../systems-manager/latest/userguide/sysman-patch-group-tagging.md") in the _AWS Systems Manager User Guide_.

**Add the patch group to a patch baseline**

To ensure that the correct patches are installed during the patching execution, you must register the patch group with a patch baseline. When the system applies a patch baseline to an instance, the service checks to see if a patch group is defined for the instance. For detailed steps on how to add a patch group to a patch baseline, see [Add a patch group to a patch baseline](../../../systems-manager/latest/userguide/sysman-patch-group-tagging.md#sysman-patch-group-patchbaseline "../../../systems-manager/latest/userguide/sysman-patch-group-tagging.md#sysman-patch-group-patchbaseline") in the _AWS Systems Manager User Guide_.

###### Note

Patch groups are not used in patching operations that are based on patch policies. For more information, see the following:

- [Using Quick Setup patch policies](../../../systems-manager/latest/userguide/patch-manager-policies.md "../../../systems-manager/latest/userguide/patch-manager-policies.md")
- [Configure the home AWS Region](../../../systems-manager/latest/userguide/quick-setup-getting-started.md#quick-setup-getting-started-home "../../../systems-manager/latest/userguide/quick-setup-getting-started.md#quick-setup-getting-started-home")
- [Creating a patch policy](../../../systems-manager/latest/userguide/quick-setup-patch-manager.md#create-patch-policy "../../../systems-manager/latest/userguide/quick-setup-patch-manager.md#create-patch-policy")
