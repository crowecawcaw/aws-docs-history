# Customizing Docker images for Flink and FluentD

Take the following steps to customize Docker images for Amazon EMR on EKS with Apache Flink or FluentD images. These include technical guidance for getting a base
image, customizing it, publishing it, and submitting a workload.

###### Topics

- [Prerequisites](#jobruns-flink-docker-flink-fluentd-prereqs "#jobruns-flink-docker-flink-fluentd-prereqs")
- [Step 1: Retrieve a base image from Amazon Elastic Container Registry](#jobruns-flink-docker-flink-fluentd-retrieve-base "#jobruns-flink-docker-flink-fluentd-retrieve-base")
- [Step 2: Customize a base image](#jobruns-flink-docker-flink-fluentd-customize-image "#jobruns-flink-docker-flink-fluentd-customize-image")
- [Step 3: Publish your custom image](#jobruns-flink-docker-flink-fluentd-publish-image "#jobruns-flink-docker-flink-fluentd-publish-image")
- [Step 4: Submit a Flink workload in Amazon EMR using a custom image](#jobruns-flink-docker-flink-fluentd-submit-workload "#jobruns-flink-docker-flink-fluentd-submit-workload")

## Prerequisites

Before you customize your Docker image, make sure that you have completed the following prerequisites:

- Completed the [Setting up the Flink Kubernetes operator for Amazon EMR on EKS](jobruns-flink-kubernetes-operator-setup.md "jobruns-flink-kubernetes-operator-setup.md") steps.
- Installed Docker in your environment. For more information, see [Get Docker](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/").

## Step 1: Retrieve a base image from Amazon Elastic Container Registry

The base image contains the Amazon EMR runtime and connectors that you need to access other AWS services. If you're using
Amazon EMR on EKS with Flink version 6.14.0 or higher, you can get the base images from the Amazon ECR Public Gallery. Browse the
gallery to find the image link and pull the image to your local workspace. For example, for the Amazon EMR 6.14.0 release, the following
`docker pull` command returns the latest standard base image. Replace `emr-6.14.0:latest` with the
release version you want.

```
docker pull public.ecr.aws/emr-on-eks/flink/emr-6.14.0-flink:latest
```

The following are links to the Flink gallery image and Fluentd gallery image:

- [emr-on-eks/flink/emr-6.14.0-flink](https://gallery.ecr.aws/emr-on-eks/flink/emr-6.14.0-flink "https://gallery.ecr.aws/emr-on-eks/flink/emr-6.14.0-flink")
- [emr-on-eks/fluentd/emr-6.14.0(](https://gallery.ecr.aws/emr-on-eks/fluentd/emr-6.14.0 "https://gallery.ecr.aws/emr-on-eks/fluentd/emr-6.14.0")

## Step 2: Customize a base image

The following steps describe how to customize the base image you pulled from Amazon ECR.

1. Create a new `Dockerfile` on your local Workspace.
2. Edit the `Dockerfile` and add the following content. This `Dockerfile`
   uses the container image you pulled from `public.ecr.aws/emr-on-eks/flink/emr-7.12.0-flink:latest`.

```
FROM public.ecr.aws/emr-on-eks/flink/emr-7.12.0-flink:latest
USER root
### Add customization commands here ####
USER hadoop:hadoop
```

Use the following configuration if you're using `Fluentd`.

```
FROM public.ecr.aws/emr-on-eks/fluentd/emr-7.12.0:latest
USER root
### Add customization commands here ####
USER hadoop:hadoop
```

3. Add commands in the `Dockerfile` to customize the base image.
   The following command demonstrates how to install Python libraries.

```
FROM public.ecr.aws/emr-on-eks/flink/emr-7.12.0-flink:latest
USER root
RUN pip3 install --upgrade boto3 pandas numpy // For python 3
USER hadoop:hadoop
```

4. In the same directory of where you created `DockerFile`, run the following
   command to build the Docker image. The field you supply following the `-t` flag is your custom name for the image.

```
docker build -t <`YOUR_ACCOUNT_ID`>.dkr.ecr.<`YOUR_ECR_REGION`>.amazonaws.com/<`ECR_REPO`>:<`ECR_TAG`>
```

## Step 3: Publish your custom image

You can now publish the new Docker image to your Amazon ECR registry.

1. Run the following command to create an Amazon ECR repository to store your Docker image. Provide
   a name for your repository, such as `emr_custom_repo.` For more
   information, see [Create a repository](../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-create-repository "../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-create-repository") in the Amazon Elastic Container Registry User Guide.

```
aws ecr create-repository \
       --repository-name emr_custom_repo \
       --image-scanning-configuration scanOnPush=true \
       --region <AWS_REGION>
```

2. Run the following command to authenticate to your default registry. For more information, see
   [Authenticate to your default registry](../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-authenticate-registry "../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-authenticate-registry") in the Amazon Elastic Container Registry User Guide.

```
aws ecr get-login-password --region <`AWS_REGION`> | docker login --username AWS --password-stdin <`AWS_ACCOUNT_ID`>.dkr.ecr.<`YOUR_ECR_REGION`>.amazonaws.com
```

3. Push the image.
   For more information, see [Push an image to Amazon ECR](../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-push-image "../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-push-image") in the Amazon Elastic Container Registry User Guide.

```
docker push <`YOUR_ACCOUNT_ID`>.dkr.ecr.<`YOUR_ECR_REGION`>.amazonaws.com/<`ECR_REPO`>:<`ECR_TAG`>
```

## Step 4: Submit a Flink workload in Amazon EMR using a custom image

Make the following changes to your `FlinkDeployment` spec to use a custom image. To do so,
enter your own image in the `spec.image` line of your deployment spec.

```
apiVersion: flink.apache.org/v1beta1
   kind: FlinkDeployment
   metadata:
     name: basic-example
   spec:
     flinkVersion: v1_18
     image: <`YOUR_ACCOUNT_ID`>.dkr.ecr.<`YOUR_ECR_REGION`>.amazonaws.com/<`ECR_REPO`>:<`ECR_TAG`>
     imagePullPolicy: Always
     flinkConfiguration:
           taskmanager.numberOfTaskSlots: "1"
```

To use a custom image for your Fluentd job, enter your own image in the
`monitoringConfiguration.image` line of your deployment spec.

```
  monitoringConfiguration:
       image: <`YOUR_ACCOUNT_ID`>.dkr.ecr.<`YOUR_ECR_REGION`>.amazonaws.com/<`ECR_REPO`>:<`ECR_TAG`>
       cloudWatchMonitoringConfiguration:
         logGroupName: flink-log-group
         logStreamNamePrefix: custom-fluentd
```
