

# Create a custom image and push to Amazon ECR
<a name="studio-updated-byoi-how-to-prepare-image"></a>

This page provides instructions on how to create a local Dockerfile, build the container image, and add it to Amazon Elastic Container Registry (Amazon ECR).

**Note**  
In the following examples, the tags are not specified, and the tag `latest` is applied by default. If you would like to specify a tag, you will need to append `:{{tag}}` to end of the image names. For more information, see [docker image tag](https://docs.docker.com/reference/cli/docker/image/tag/) in the *Docker documentation*.

**Topics**
+ [Create a local Dockerfile and build the container image](#studio-updated-byoi-how-to-create-local-dockerfile)
+ [Add a Docker image to Amazon ECR](#studio-updated-byoi-add-container-image)

## Create a local Dockerfile and build the container image
<a name="studio-updated-byoi-how-to-create-local-dockerfile"></a>

Use the following instructions to create a Dockerfile with your desired software and dependencies.

**To create your Dockerfile**

1. First set your variables for the AWS CLI commands that follow.

   ```
   LOCAL_IMAGE_NAME={{local-image-name}}
   ```

   `{{local-image-name}}` is the name of the container image on your local device, that you define here.

1. Create a text-based document, named `Dockerfile`, that meet the specifications in [Custom image specifications](studio-updated-byoi-specs.md).

   `Dockerfile` examples for supported applications can be found in [Dockerfile samples](studio-updated-byoi-specs.md#studio-updated-byoi-specs-dockerfile-templates).
**Note**  
If you are bringing your own image to SageMaker Unified Studio, you will need to follow the [Dockerfile specifications](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/byoi-specifications.html) in the *Amazon SageMaker Unified Studio User Guide*.  
`Dockerfile` examples for SageMaker Unified Studio can be found in [Dockerfile example](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/byoi-specifications.html#byoi-specifications-example) in the *Amazon SageMaker Unified Studio User Guide*.

1. In the directory containing your `Dockerfile`, build the Docker image using the following command. The period (`.`) specifies that the `Dockerfile` should be in the context of the build command.

   ```
   docker build -t ${LOCAL_IMAGE_NAME} .
   ```

   After the build completes, you can list your container image information with the following command.

   ```
   docker images
   ```

1. (Optional) You can test your image by using the following command.

   ```
   docker run -it ${LOCAL_IMAGE_NAME}
   ```

   In the output you will find that your server is running at a URL, like `http://127.0.0.1:8888/...`. You can test the image by copying the URL into the browser. 

   If this does not work, you may need to include `-p {{port}}:{{port}}` in the docker run command. This option maps the exposed port on the container to a port on the host system. For more information about docker run, see the [Running containers](https://docs.docker.com/engine/containers/run/) in the *Docker documentation*.

   Once you have verified that the server is working, you can stop the server and shut down all kernels before continuing. The instructions are viewable the output.

## Add a Docker image to Amazon ECR
<a name="studio-updated-byoi-add-container-image"></a>

To add a container image to Amazon ECR, you will need to do the following.
+ Create an Amazon ECR repository.
+ Log in to your default registry.
+ Push the image to the Amazon ECR repository.

**Note**  
The Amazon ECR repository must be in the same AWS Region as the domain you are attaching the image to.

**To build and push the container image to Amazon ECR**

1. First set your variables for the AWS CLI commands that follow.

   ```
   ACCOUNT_ID={{account-id}}
   REGION={{aws-region}}
   ECR_REPO_NAME={{ecr-repository-name}}
   ```
   + `{{account-id}}` is your account ID. You can find this at the top right of any AWS console page. For example, the [SageMaker AI console](https://console.aws.amazon.com/sagemaker).
   + `{{aws-region}}` is the AWS Region of your Amazon SageMaker AI domain. You can find this at the top right of any AWS console page. 
   + `{{ecr-repository-name}}` is the name of your Amazon Elastic Container Registry repository, that you define here. To view your Amazon ECR repositories, see the [Amazon ECR console](https://console.aws.amazon.com/ecr).

1. Log in to Amazon ECR and sign in to Docker.

   ```
   aws ecr get-login-password \
       --region ${REGION} | \
       docker login \
       --username AWS \
       --password-stdin ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com
   ```

   On a successful authentication, you will receive a succeeded log in message.
**Important**  
If you receive an error, you may need to install or upgrade to the latest version of the AWS CLI. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

1. Tag the image in a format compatible with Amazon ECR, to push to your repository.

   ```
   docker tag \
       ${LOCAL_IMAGE_NAME} \
       ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO_NAME}
   ```

1. Create an Amazon ECR repository using the AWS CLI. To create the repository using the Amazon ECR console, see [Creating an Amazon ECR private repository to store images](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html).

   ```
   aws ecr create-repository \
       --region ${REGION} \
       --repository-name ${ECR_REPO_NAME}
   ```

1. Push the image to your Amazon ECR repository. You can also tag the Docker image.

   ```
   docker push ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${ECR_REPO_NAME}
   ```

Once the image has been successfully added to your Amazon ECR repository, you can view it in the [Amazon ECR console](https://console.aws.amazon.com/ecr).