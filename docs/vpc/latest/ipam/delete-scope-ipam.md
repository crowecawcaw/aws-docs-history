# Delete a scope

You may want to delete an IPAM scope if it no longer serves its intended purpose, such as when you restructure your network, consolidate regions, or adjust your IP address allocation. Deleting unused scopes can help streamline your IPAM configuration and optimize your IP address management within AWS.

###### Note

You can't delete a scope if either of the following is true:

- The scope is a default scope. When you create an IPAM, two default scopes (one public, one
  private) are created automatically, and cannot be deleted. To see if a scope is
  a default scope, view the **Scope type** in the details of the
  scope.
- There are one or more pools in the scope.
  You must first [Delete a pool](delete-pool-ipam.md "delete-pool-ipam.md")
  before you can delete the scope.

AWS Management Console

###### To delete a scope

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Scopes**.
3. In the content pane, choose the scope that you want to delete.
4. Choose **Actions** > **Delete scope**.
5. Enter `delete` and then choose
   **Delete**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to delete a scope:

1. View scopes: [describe-ipam-scopes](../../../cli/latest/reference/ec2/describe-ipam-scopes.md "../../../cli/latest/reference/ec2/describe-ipam-scopes.md")
2. Delete a scope: [delete-ipam-scope](../../../cli/latest/reference/ec2/delete-ipam-scope.md "../../../cli/latest/reference/ec2/delete-ipam-scope.md")
3. View updated scopes: [describe-ipam-scopes](../../../cli/latest/reference/ec2/describe-ipam-scopes.md "../../../cli/latest/reference/ec2/describe-ipam-scopes.md")

To create a new scope, see [Create additional scopes](add-scope-ipam.md "add-scope-ipam.md"). To delete the IPAM, see [Delete an IPAM](delete-ipam.md "delete-ipam.md").
