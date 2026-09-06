

# Creating an Amazon Neptune cluster using AWS CloudFormation
<a name="get-started-cfn-create"></a>

You can use an CloudFormation template to set up a Neptune DB Cluster.

1. To launch the CloudFormation stack on the CloudFormation console, choose one of the **Launch Stack** buttons in the following table.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/neptune/latest/userguide/get-started-cfn-create.html)

1.  On the **Select Template** page, choose **Next**.

1. On the **Specify Details** page, choose a key pair for the **EC2SSHKeyPairName**.

   This key pair is required to access the EC2 instance. Ensure that you have the PEM file for the key pair that you choose.

1. Choose **Next**.

1. On the **Options** page, choose **Next**.

1. On the **Review** page, select the first check box to acknowledge that CloudFormation will create IAM resources. Select the second check box to acknowledge `CAPABILITY_AUTO_EXPAND` for the new stack. 
**Note**  
`CAPABILITY_AUTO_EXPAND` explicitly acknowledges that macros will be expanded when creating the stack, without prior review. Users often create a change set from a processed template so that the changes made by macros can be reviewed before actually creating the stack. For more information, see the CloudFormation [CreateStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html) API.

   Then choose **Create**.

**Note**  
You can also use your CloudFormation template to [upgrade your DB cluster's engine version.](cfn-engine-update.md)