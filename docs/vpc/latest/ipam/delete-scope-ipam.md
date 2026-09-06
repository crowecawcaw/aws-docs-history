

# Delete a scope
<a name="delete-scope-ipam"></a>

You may want to delete an IPAM scope if it no longer serves its intended purpose, such as when you restructure your network, consolidate regions, or adjust your IP address allocation. Deleting unused scopes can help streamline your IPAM configuration and optimize your IP address management within AWS. 

**Note**  
You can't delete a scope if either of the following is true:  
The scope is a default scope. When you create an IPAM, two default scopes (one public, one private) are created automatically, and cannot be deleted. To see if a scope is a default scope, view the **Scope type** in the details of the scope.
There are one or more pools in the scope. You must first [Delete a pool](delete-pool-ipam.md) before you can delete the scope.

------
#### [ AWS Management Console ]

**To delete a scope**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Scopes**.

1. In the content pane, choose the scope that you want to delete.

1. Choose **Actions** > **Delete scope**.

1. Enter **delete** and then choose **Delete**.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

Use the following AWS CLI commands to delete a scope:

1. View scopes: [describe-ipam-scopes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-scopes.html)

1. Delete a scope: [delete-ipam-scope](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-ipam-scope.html)

1. View updated scopes: [describe-ipam-scopes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-scopes.html)

------

To create a new scope, see [Create additional scopes](add-scope-ipam.md). To delete the IPAM, see [Delete an IPAM](delete-ipam.md).