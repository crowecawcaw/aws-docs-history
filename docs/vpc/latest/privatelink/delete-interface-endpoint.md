# Delete an interface endpoint

When you are finished with a VPC endpoint, you can delete it. Deleting an interface
endpoint also deletes its endpoint network interfaces.

###### To delete an interface endpoint using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Select the interface endpoint.
4. Choose **Actions**, **Delete VPC endpoints**.
5. When prompted for confirmation, enter `delete`.
6. Choose **Delete**.

###### To delete an interface endpoint using the command line

- [delete-vpc-endpoints](../../../cli/latest/reference/ec2/delete-vpc-endpoints.md "../../../cli/latest/reference/ec2/delete-vpc-endpoints.md")
  (AWS CLI)
- [Remove-EC2VpcEndpoint](../../../powershell/latest/reference/items/Remove-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/Remove-EC2VpcEndpoint.md") (Tools for Windows PowerShell)
