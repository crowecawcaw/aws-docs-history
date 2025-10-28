# Use inference endpoints to deploy models

Endpoint are locations where you send inference requests to your deployed machine learning
models. After you create an endpoint, you can add models to it, test it, and change its
settings as needed. By using endpoints, you don't have to manage the underlying
infrastructure for configuring and deploying a model.

For more information about using endpoints for real-time inference, see [Deploy models for real-time inference](../../../sagemaker/latest/dg/realtime-endpoints-deploy-models.md "../../../sagemaker/latest/dg/realtime-endpoints-deploy-models.md") in the _Amazon SageMaker AI Developer Guide_. Also see the [Getting started with deploying real time models on SageMaker AI](https://aws.amazon.com/blogs/machine-learning/part-2-model-hosting-patterns-in-amazon-sagemaker-getting-started-with-deploying-real-time-models-on-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/part-2-model-hosting-patterns-in-amazon-sagemaker-getting-started-with-deploying-real-time-models-on-sagemaker/") blog post.

###### Topics

- [Create an endpoint and deploy a
  model](#sagemaker-create-endpoint "#sagemaker-create-endpoint")
- [View your endpoints](#sagemaker-view-endpoints "#sagemaker-view-endpoints")

## Create an endpoint and deploy a

model

To create an endpoint, follow these steps:

1.  Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2.  From the main menu, choose **Build**.
3.  From the drop-down menu, choose **Inference endpoints**.
4.  From the **Endpoints** page, choose **Create endpoint**.
5.  From the **Create endpoint** page, configure these values:
    - For **Endpoint name**, enter a name for the endpoint.
    - For **Instance type**, choose an instance for the endpoint.
    - For **Initial instance count**, enter the number of instances for
      the endpoint to provision initially.
    - For **Maximum instance count**, enter the maximum number of instances that
      the endpoint can provision, when it scales up.

6.  Under **Models**, choose **Add model**. In the **Add model**
    modal form, follow these steps:
    1. Select the model type (JumpStart foundation models or Deployable models that you created).

    The form lists the models that are compatible with the instance type you selected. 2. Choose one of the models. 3. Under **Model settings**, enter these values:

        * Number of CPU cores – Number of accelerators to deploy.
        * Minimum number of copies – minimum number of model copies to deploy.
        * Min CPU memory – Minimum amount of CPU memory.
        * Max CPU memory – Maximum amount of CPU memory.

    4. Choose **Add model**.

7.  Choose **Deploy** to deploy the endpoint.

## View your endpoints

To view your endpoints in the **Endpoints** table, follow these steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the main menu, choose **Build**.
3. From the drop-down menu, choose **Inference endpoints**.
4. (Optional) To search for specific endpoints, enter text in **Search by endpoint name**.
