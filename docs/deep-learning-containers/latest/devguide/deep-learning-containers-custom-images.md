# Customize Deep Learning Containers

Deep Learning Containers are built for specific machine learning frameworks, infrastructures, and Amazon cloud services. The full list of available images and their respective tags are available [here](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md"). The containers come pre-configured with essential dependencies, eliminating the need for manual setup and optimization and they are readily available through Amazon Elastic Container Registry (ECR). Additionally, these containers are designed to work seamlessly with various Amazon cloud services, including Amazon SageMaker, Amazon EKS, Amazon EC2, and Amazon ECS.

## Tutorial

In the following tutorial, we explore how to customize a PyTorch training container, providing you with a practical example of container customization.

- Choose latest PyTorch Training image: the tag for 2.7 PyTorch Training GPU image is - 2.7.1-gpu-py312-cu128-ubuntu22.04-ec2
- This image includes stable versions of key components, including NVIDIA CUDA, cuDNN and EFA. If you are looking for detailed information about libraries, frameworks and components included in PyTorch 2.7 Training image, refer to our release notes [here](dlc-pytorch-2-7-training-ec2-ecs-eks.md "dlc-pytorch-2-7-training-ec2-ecs-eks.md").

Create a Dockerfile with this base image.

```
FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:2.7.1-gpu-py312-cu128-ubuntu22.04-ec2
# Add custom code and testing scripts required
```

Build the Docker image, pointing to your personal Docker registry (usually your username), with the image's custom name and custom tag.

```
$ docker build -t `<registry>`/`<any name>`:`<any tag>`
```

You can use the following command to run the container, and the "--gpus all" flag ensures GPU access when running the container.

```
$ docker run -it --gpus all `<registry>`/`<image-name>`:`<tag>`
```

Push to your personal Docker Registry:

```
$ docker push `<registry>`/`<any name>`:`<any tag>`
```

###### Important

You may need to login to access to the Deep Learning Containers image repository. Specify your region in the following command:

```
$ aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com
```

Remember to replace registry names and tag with your actual registry name when building and pushing the image.
