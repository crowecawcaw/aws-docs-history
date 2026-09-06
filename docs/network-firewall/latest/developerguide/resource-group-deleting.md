

# Deleting a resource group in AWS Network Firewall
<a name="resource-group-deleting"></a>

You can delete your resource group in the Network Firewall console or the AWS Resource Groups [DeleteGroup](https://docs.aws.amazon.com/ARG/latest/APIReference/API_DeleteGroup.html) API. To delete a resource group in the Network Firewall console, perform the following procedure.

**Deleting a resource group**  
You can't delete a resource group that's referenced in a rule group. When you try to delete a resource group, AWS Network Firewall checks to see if it's currently being referenced. A resource group can be referenced by a rule group. If Network Firewall determines that the resource is being referenced, it warns you. Network Firewall is almost always able to determine whether a resource is being referenced. However, in rare cases, it might not be able to do so. If you need to be sure that the resource that you want to delete isn't in use, check all of your rule groups before deleting it. Note that policies that have associations can't be deleted.

**To delete a resource group**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Network Firewall resource groups**.

1. In the **Resource group** page, select the resource group that you want to delete. 

1. Choose **Delete**, and confirm your request.

Your resource group is removed from the list in the **Resource group** page.