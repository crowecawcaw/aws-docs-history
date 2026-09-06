

# Getting started with training a deep graph network
<a name="deep-graph-library-get-started"></a>

DGL is available as a deep learning container in Amazon ECR. You can select deep learning containers when you write your ModelTrainer function in an Amazon SageMaker notebook. You can also craft your own custom container with DGL by following the [Bring Your Own Container](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) guide. The easiest way to get started with a deep graph network uses one of the DGL containers in Amazon Elastic Container Registry.  

**Note**  
 Backend framework support is limited to PyTorch and MXNet. 

**Setup**  
If you are using Amazon SageMaker Studio, you need to clone the examples repository first. If you are using a notebook instance, you can find the examples by choosing the SageMaker AI icon at bottom of the left toolbar. 

**To clone the Amazon SageMaker SDK and notebook examples repository**

1. From the **JupyterLab** view in Amazon SageMaker AI, go to the **File Browser** at the top of the left toolbar. From the **File Browser panel**, you can see a new navigation at the top of the panel. 

1. Choose the icon on the far right to clone a Git repository. 

1. Add the repository URL: [https://github.com/awslabs/amazon-sagemaker-examples.git](https://github.com/awslabs/amazon-sagemaker-examples.git) 

1. Browse the newly added folder and its contents. The DGL examples are stored in the **sagemaker-python-sdk** folder. 

**Train**  
After you've set up, you can train the deep graph network.