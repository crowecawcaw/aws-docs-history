

AWS Blockchain Templates was discontinued on April 30, 2019. No further updates to this service or this supporting documentation will be made. For the best Managed Blockchain experience on AWS, we recommend that you use [ Amazon Managed Blockchain (AMB)](https://aws.amazon.com/managed-blockchain/). To learn more about getting started with Amazon Managed Blockchain, see our [ workshop on Hyperledger Fabric](https://catalog.us-east-1.prod.workshops.aws/workshops/008da2cb-8454-42d0-877b-bc290bff7fcf/en-US), or our [blog on deploying an Ethereum node](https://aws.amazon.com/blogs/database/deploy-an-ethereum-node-on-amazon-managed-blockchain/). If you have questions about AMB or require further support, [contact Support](https://console.aws.amazon.com/support/home#/case/create?issueType=technical) or your AWS account team.

# Setting Up AWS Blockchain Templates
<a name="blockchain-templates-setting-up"></a>

Before you start with AWS Blockchain Templates, complete the following tasks:
+ [Create a Key Pair](#blockchain-templates-create-a-key-pair)

These are fundamental prerequisites for all blockchain configurations. In addition, the blockchain network that you choose may have prerequisites, which vary according to your desired environment and configuration choices. For more information, see the relevant section for your blockchain template in [AWS Blockchain Templates and Features](blockchain-template-features.md).

For step-by-step instructions to set up prerequisites for a private Ethereum network using an Amazon ECS cluster, see [Getting Started with AWS Blockchain Templates](blockchain-templates-getting-started.md).

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Create a Key Pair
<a name="blockchain-templates-create-a-key-pair"></a>

AWS uses public-key cryptography to secure the login information for the instances in a blockchain network. You specify the name of the key pair when you use each AWS Blockchain Template. You can then use the key pair to access instances directly, for example, to log in using SSH. 

If you already have a key pair in the right Region, you can skip this step. If you haven't created a key pair already, you can create one using the Amazon EC2 console. Create the key pair in the same Region that you use to launch the Ethereum network. For more information, see [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) in the *Amazon EC2 User Guide*. 

**To create a key pair**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation bar, select a Region for the key pair. You can select any Region that's available to you, regardless of your location, but key pairs are specific to a Region. For example, if you plan to launch an instance in the US East (Ohio) region, you must create a key pair for the instance in the same Region.

1. In the navigation pane, choose **Key Pairs**, **Create Key Pair**.

1. For **Key pair name**, enter a name for the new key pair. Choose a name that is easy for you to remember, such as your IAM user name, followed by `-key-pair`, plus the region name. For example, *me*-key-pair-*useast2*. Choose **Create**.

1. The private key file is automatically downloaded by your browser. The base file name is the name that you specified as the name of your key pair, and the file name extension is `.pem`. Save the private key file in a safe place.
**Important**  
This is the only chance for you to save the private key file. You provide the name of your key pair when you launch the Ethereum network.

For more information, see [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon EC2 User Guide*. For more information about connecting to EC2 instances using the key pair, see [Connect to Your Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the *Amazon EC2 User Guide*.