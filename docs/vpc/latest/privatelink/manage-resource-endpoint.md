# Manage resource endpoints

After you create a resource endpoint, you can manage its security groups or tags.

###### Tasks

- [Delete an endpoint](#delete-resource-endpoint "#delete-resource-endpoint")
- [Update an endpoint](#update-resource-endpoint "#update-resource-endpoint")

## Delete an endpoint

When you are finished with a VPC endpoint, you can delete it.

###### To delete an endpoint using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Select the endpoint.
4. Choose **Actions**, **Delete VPC endpoints**.
5. When prompted for confirmation, enter `delete`.
6. Choose **Delete**.

###### To delete an endpoint using the command line

- [delete-vpc-endpoints](../../../cli/latest/reference/ec2/delete-vpc-endpoints.md "../../../cli/latest/reference/ec2/delete-vpc-endpoints.md")
  (AWS CLI)
- [Remove-EC2VpcEndpoint](../../../powershell/latest/reference/items/Remove-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/Remove-EC2VpcEndpoint.md")
  (Tools for Windows PowerShell)

## Update an endpoint

You can update a VPC endpoint.

###### To update an endpoint using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Select the endpoint.
4. Choose **Actions**, and the appropriate option.
5. Follow the console steps to submit the update.

###### To update an endpoint using the command line

- [modify-vpc-endpoint](../../../cli/latest/reference/ec2/modify-vpc-endpoint.md "../../../cli/latest/reference/ec2/modify-vpc-endpoint.md")
  (AWS CLI)
- [Edit-EC2VpcEndpoint](../../../powershell/latest/reference/items/Edit-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/Edit-EC2VpcEndpoint.md") (Tools for Windows PowerShell)
