

# Delete an interface endpoint
<a name="delete-interface-endpoint"></a>

When you are finished with a VPC endpoint, you can delete it. Deleting an interface endpoint also deletes its endpoint network interfaces.

**To delete an interface endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the interface endpoint.

1. Choose **Actions**, **Delete VPC endpoints**. 

1. When prompted for confirmation, enter **delete**.

1. Choose **Delete**.

**To delete an interface endpoint using the command line**
+ [delete-vpc-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpc-endpoints.html) (AWS CLI)
+ [Remove-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2VpcEndpoint.html) (Tools for Windows PowerShell)