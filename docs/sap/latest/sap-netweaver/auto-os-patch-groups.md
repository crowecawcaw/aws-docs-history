

# Create patch groups
<a name="auto-os-patch-groups"></a>

You can use patch groups to organize instances for patching. This can help you ensure that you only deploy patches to the correct set of instances and that the patches have been adequately tested before they are deployed. After you create the patch group, you can tag your Amazon EC2 instances to add them to the patch group and then add the patch group to a patch baseline.

You might want to organize patch groups by:
+ Operating system – such as Linux and Windows
+ Environment – such as development, test, and production
+ Server function – such as SAP database servers and SAP application servers

**Note**  
An Amazon EC2 instance can only be in one patch group at a time.

For more information about patch groups, see [About patch groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-patchgroups.html) in the * AWS Systems Manager User Guide*.

 **Tag Amazon EC2 instances to add to the patch group** 

After you create the patch group, use tags to add Amazon EC2 instances to the patch group. For detailed steps on how to do this, see [Working with patch groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html) in the * AWS Systems Manager User Guide*.

 **Add the patch group to a patch baseline** 

To ensure that the correct patches are installed during the patching execution, you must register the patch group with a patch baseline. When the system applies a patch baseline to an instance, the service checks to see if a patch group is defined for the instance. For detailed steps on how to add a patch group to a patch baseline, see [Add a patch group to a patch baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html#sysman-patch-group-patchbaseline) in the * AWS Systems Manager User Guide*.

**Note**  
Patch groups are not used in patching operations that are based on patch policies. For more information, see the following:  
 [Using Quick Setup patch policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-policies.html) 
 [Configure the home AWS Region](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-getting-started.html#quick-setup-getting-started-home) 
 [Creating a patch policy](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-patch-manager.html#create-patch-policy) 