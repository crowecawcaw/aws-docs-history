

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Step 2: Create a project
<a name="gsg-projects"></a>

Now that you've signed in to the AWS Management Console, you can use the Amazon Monitron console to create your project.

**To create a project**

1. Choose the AWS Region that you want to use in the Region selector. Amazon Monitron is available only in the US East (N. Virginia), Europe (Ireland), and Asia Pacific (Sydney) Regions.  
![Dropdown menu showing AWS region options including US East, US West, and their corresponding codes.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gs-project-select-region.png)

1. Open the Amazon Monitron console at [https://console.aws.amazon.com/monitron](https://console.aws.amazon.com/monitron/). 

1. Choose **Create project**.  
![Getting started dialog box with a link to documentation and a Create project button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gs-project-monitron-create-project.png)

1. Under **Project Details**, for **Project name**, enter a name for the project. 

1. (Optional) Under **Data encryption**, you can check **Custom encryption settings (advanced) ** if you have an AWS KMS key in AWS Key Management Service. Amazon Monitron encrypts all data at rest and in transit. If you don't provide your own CMK, your data is encrypted by a CMK that Amazon Monitron owns and manages.

   For more information about encryption for your project, see [KMS and Data Encryption in Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-protection.html#data-encryption).

1.  (Optional) To add a tag to the project, enter a key-value pair under **Tags** and then choose **Add tag**.

   For more information about tags, see [Tags in Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/tagging.html). 

1. Choose **Next** to create the project.  
![](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/gs-project-monitron-project-details.png)

When you create your first project, the owner of the AWS account will get an email from *AWS Organizations*. No action needs to be taken based on this email.