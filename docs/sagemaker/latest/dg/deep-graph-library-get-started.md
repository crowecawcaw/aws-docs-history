# Getting started with training a deep graph network

DGL is available as a deep learning container in Amazon ECR. You can select deep learning
containers when you write your estimator function in an Amazon SageMaker notebook. You can also craft
your own custom container with DGL by following the [Bring Your Own
Container](your-algorithms.md "your-algorithms.md") guide. The easiest way to get started with a deep graph network uses one
of the DGL containers in Amazon Elastic Container Registry. 

###### Note

Backend framework support is limited to PyTorch and MXNet.

###### Setup

If you are using Amazon SageMaker Studio, you need to clone the examples repository first. If
you are using a notebook instance, you can find the examples by choosing the SageMaker AI icon at
bottom of the left toolbar.

###### To clone the Amazon SageMaker SDK and notebook examples repository

1. From the **JupyterLab** view in Amazon SageMaker AI, go to the **File
   Browser** at the top of the left toolbar. From the **File Browser
   panel**, you can see a
   new
   navigation at the top of the panel.
2. Choose the
   icon
   on the far right to clone a Git repository.
3. Add the repository URL: [https://github.com/awslabs/amazon-sagemaker-examples.git](https://github.com/awslabs/amazon-sagemaker-examples.git "https://github.com/awslabs/amazon-sagemaker-examples.git")
4. Browse the newly added folder and its contents. The DGL examples are stored in the
   **sagemaker-python-sdk** folder.

###### Train

After you've set up, you can train the deep graph network.
