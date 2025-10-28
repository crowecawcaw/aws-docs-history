**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Deleting a custom managed list in Firewall Manager

You can delete custom managed lists. You can't edit or delete lists that Firewall Manager manages.

###### Note

Currently, Firewall Manager doesn’t check references to a custom managed list when you delete
it. This means that you can delete a custom managed application list or protocol
list even when it is in use by an active policy. This can cause the policy to stop
functioning. Only delete an application list or protocol list after you have
verified that it isn't referenced by any active polices.

###### To delete a custom managed application or protocol list

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
   [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").

###### Note

For information about setting up a Firewall Manager administrator account, see
[AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md"). 2. Make sure that the list that you want to delete isn't in use in any of your audit
security group policies by doing the following:

    1. In the navigation pane, choose **Security policies**.
    2. In the **AWS Firewall Manager policies** page, select and edit your
     audit security groups, and remove any references to the custom list
     that you want to delete.


    If you delete a custom managed list that's in use in an audit security group policy,
     the policy that's using it can stop functioning.

3. In the navigation pane, choose **Application lists** or **Protocol lists**, depending on the type of list you want to delete.
4. In the list page, select the custom list that you want to delete and choose
   **Delete**.
