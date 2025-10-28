AWS Blockchain Templates was discontinued on April 30, 2019. No further updates to this
service or this supporting documentation will be made. For the best Managed Blockchain experience on AWS,
we recommend that you use [Amazon Managed Blockchain
(AMB)](https://aws.amazon.com/managed-blockchain/ "https://aws.amazon.com/managed-blockchain/"). To learn more about getting started with Amazon Managed Blockchain, see our
[workshop on Hyperledger Fabric](https://catalog.us-east-1.prod.workshops.aws/workshops/008da2cb-8454-42d0-877b-bc290bff7fcf/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/008da2cb-8454-42d0-877b-bc290bff7fcf/en-US"), or our [blog on deploying an Ethereum node](https://aws.amazon.com/blogs/database/deploy-an-ethereum-node-on-amazon-managed-blockchain/ "https://aws.amazon.com/blogs/database/deploy-an-ethereum-node-on-amazon-managed-blockchain/").
If you have questions about AMB or require further support, [contact Support](https://console.aws.amazon.com/support/home#/case/create?issueType=technical "https://console.aws.amazon.com/support/home#/case/create?issueType=technical") or your AWS account team.

# Clean Up Resources

AWS CloudFormation makes it easy to clean up resources that the stack created. When you delete the stack, all resources that the stack created are deleted.

###### To delete resources that the template created

- Open the AWS CloudFormation console, select the root stack that you created earlier, choose **Actions**, **Delete**.

The **Status** of the root stack you created earlier and the associated nested stacks update to **DELETE_IN_PROGRESS**.
You may choose to delete the prerequisites you created for the Ethereum network.

###### Delete the VPC

- Open the Amazon VPC console, select the VPC you created earlier and then choose **Actions**, **Delete VPC**. This also deletes the subnets, security groups, and the NAT gateway associated with the VPC.

###### Delete the IAM role and EC2 instance profile

- Open the IAM console and choose **Roles**. Select the role for ECS and the role for EC2 that you created earlier and choose **Delete**.

###### Terminate the EC2 instance for the bastion host

- Open the Amazon EC2 dashboard, choose **Running instances**, select the EC2 instance that you created for the bastion host, choose **Actions**, **Instance State**, **Terminate**.
