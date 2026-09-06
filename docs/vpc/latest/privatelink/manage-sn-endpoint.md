

# Manage service-network endpoints
<a name="manage-sn-endpoint"></a>

After you create a service-network endpoint, you can update its security groups or tags.

**Topics**
+ [Delete an endpoint](#delete-sn-endpoint)
+ [Update a service-network endpoint](#update-sn-endpoint)

## Delete an endpoint
<a name="delete-sn-endpoint"></a>

When you are finished with a VPC endpoint, you can delete it.

**To delete an endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the service-network endpoint.

1. Choose **Actions**, **Delete VPC endpoints**.

1. When prompted for confirmation, enter **delete**.

1. Choose **Delete**.

**To delete an endpoint using the command line**
+ [delete-vpc-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpc-endpoints.html) (AWS CLI)
+ [Remove-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2VpcEndpoint.html) (Tools for Windows PowerShell)

## Update a service-network endpoint
<a name="update-sn-endpoint"></a>

You can update a VPC endpoint.

**To update an endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the endpoint.

1. Choose **Actions**, and the appropriate option.

1. Follow the console steps to submit the update.

**To update an endpoint using the command line**
+ [modify-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-endpoint.html) (AWS CLI)
+ [Edit-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpoint.html) (Tools for Windows PowerShell)