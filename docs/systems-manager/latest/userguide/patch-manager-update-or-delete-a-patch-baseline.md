• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Updating

or deleting a custom patch baseline

You can update or delete a custom patch baseline that you have created in
Patch Manager, a tool in AWS Systems Manager. When you update a patch baseline, you can
change its name or description, its approval rules, and its exceptions for
approved and rejected patches. You can also update the tags that are applied
to the patch baseline. You can't change the operating system type that a
patch baseline has been created for, and you can't make changes to a
predefined patch baseline provided by AWS.

## Updating or deleting a

patch baseline

Follow these steps to update or delete a patch baseline.

###### Important

Use caution when deleting a custom patch baseline that might be
used by a patch policy configuration in Quick Setup.

If you are using a [patch policy
configuration](patch-manager-policies.md "patch-manager-policies.md") in Quick Setup, updates you make to custom patch baselines are
synchronized with Quick Setup once an hour.

If a custom patch baseline that was referenced in a patch policy is deleted, a banner
displays on the Quick Setup **Configuration details** page for your patch
policy. The banner informs you that the patch policy references a patch baseline that no
longer exists, and that subsequent patching operations will fail. In this case, return to
the Quick Setup **Configurations** page, select the Patch Manager configuration ,
and choose **Actions**, **Edit configuration**. The
deleted patch baseline name is highlighted, and you must select a new patch baseline for the
affected operating system.

###### To update or delete a patch baseline

1.  Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2.  In the navigation pane, choose **Patch Manager**.
3.  Choose the patch baseline that you want to update or delete,
    and then do one of the following:

        * To remove the patch baseline from your AWS account,
         choose **Delete**. The system prompts
         you to confirm your actions.
        * To make changes to the patch baseline name or
         description, approval rules, or patch exceptions, choose
         **Edit**. On the **Edit
         patch baseline** page, change the values
         and options that you want, and then choose
         **Save changes**.
        * To add, change, or delete tags applied to the patch
         baseline, choose the **Tags** tab, and
         then choose **Edit tags**. On the
         **Edit patch baseline tags** page,
         make updates to the patch baseline tags, and then choose
         **Save changes**.

    For information about the configuration choices you can make,
    see [Working with custom patch
    baselines](patch-manager-manage-patch-baselines.md "patch-manager-manage-patch-baselines.md").
