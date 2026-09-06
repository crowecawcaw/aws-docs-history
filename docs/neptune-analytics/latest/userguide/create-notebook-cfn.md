

# Creating a new Neptune Analytics notebook using a CloudFormation template
<a name="create-notebook-cfn"></a>

[Amazon SageMaker AI Notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) provide a fully managed Jupyter environment for running graph notebooks that are connected to a Neptune Analytics graph. SageMaker AI Notebooks run natively on Amazon Linux 2, and support use of the Jupyter Classic Notebook or JupyterLab 3 interface on the same instance.

You can use one of the following CloudFormation templates to set up a new Neptune Analytics notebook to use with your Neptune Analytics graph:

**To use an CloudFormation stack to create a new Neptune Analytics notebook**

1. Choose one of the **Launch Stack** buttons in the following table to launch the CloudFormation stack on the CloudFormation console.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/neptune-analytics/latest/userguide/create-notebook-cfn.html)

1.  On the **Select Template** page, choose **Next**.

1. In the **Stack Details** page, under **GraphEndpoint**, enter the public or private endpoint of your Neptune Analytics graph.

1. Under **Notebook Name** enter a name for the new notebook that is unique for your account and region in SageMaker AI.

1. On the **Options** page, choose **Next**.

1. If you're using a private endpoint for your Neptune Analytics graph, enter the following under **Network Options**:

   1. Under **GraphVPC** enter the ID of a VPC associated with the private graph endpoint.

   1. Under **GraphSubnetId** enter the ID of any subnet associated with your private graph endpoint.

   1. Under **GraphSecurityGroup** enter the ID of a security group associated with the VPC. This is optional; if not provided, a new security group is automatically created for this purpose.

1. Click through the rest of the stack creation steps, leaving everything as default, and submit for creation.

In around 5 minutes, you should see the new Neptune Analytics notebook appear in the SageMaker AI and Neptune consoles.