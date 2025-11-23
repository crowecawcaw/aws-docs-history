# Updating provisioned products

When you want to use a new version of a product or configure a provisioned product with
updated parameter values, you must update it. You can also change tags or take other actions
on a provisioned product if your administrator has enabled these features.

You can only update provisioned products if they are in the **Available**
or **Tainted** state.

You cannot update failed provisioned products or provisioned products that are in the
process of starting, updating, or terminating. See [Viewing Provisioned Product Status](enduser-viewstack.md#enduser-viewstack-status "enduser-viewstack.md#enduser-viewstack-status") for more information on provisioned product
status.

###### Note

If the provisioned product you launch is a stack set, you own the stack set.
Ownership of individual stacks depends whether or not you have access to the accounts
where the stacks were deployed. For more information, see [Working with CloudFormation StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md").

###### To update a provisioned product

1. From the Provisioned products list, choose the provisioned product, and then
   choose **Actions**.
2. To update, choose **Update** and enter your
   parameters.
3. If your administrator allows you to update tags on this provisioned product, you
   see a **Tag Updates** section.
4. Choose **Update**. The provisioned product status
   changes to an **Under change** status.

To see the output from the update operation, view the **Events** tab.
