# How to customize Docker images

Follow these steps to customize Docker images for Amazon EMR on EKS. The steps show you how to get a base image, customize and
publish it, and submit a workload using the image.

- [Prerequisites](#docker-custom-images-prereq "#docker-custom-images-prereq")
- [Step 1: Retrieve a base image from Amazon Elastic Container Registry
  (Amazon ECR)](#docker-custom-images-retrieve "#docker-custom-images-retrieve")
- [Step 2: Customize a base image](#docker-custom-images-customize "#docker-custom-images-customize")
- [Step 3: (Optional but recommended) Validate
  a custom image](#docker-custom-images-validate "#docker-custom-images-validate")
- [Step 4: Publish a custom image](#docker-custom-images-publish "#docker-custom-images-publish")
- [Step 5: Submit a Spark workload in Amazon EMR using
  a custom image](#docker-custom-images-submit "#docker-custom-images-submit")

###### Note

Other options you may want to consider when customizing Docker images are customizing for interactive endpoints, which you do to ensure you have your required dependencies, or
using multi-architectural container images:

- [Customize Docker images for interactive
  endpoints](docker-custom-images-managed-endpoint.md "docker-custom-images-managed-endpoint.md")
- [Work with multi-architecture
  images](docker-custom-images-multi-architecture.md "docker-custom-images-multi-architecture.md")

## Prerequisites

- Complete the [Setting up Amazon EMR on EKS](setting-up.md "setting-up.md") steps for
  Amazon EMR on EKS.
- Install Docker in your environment. For more information, see [Get Docker](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/").

## Step 1: Retrieve a base image from Amazon Elastic Container Registry

(Amazon ECR)

The base image contains the Amazon EMR runtime and connectors that are used to access other
AWS services. For Amazon EMR 6.9.0 and higher, you can get the base images from the
Amazon ECR Public Gallery. Browse the gallery to find the image link and pull the image to your
local workspace. For example, for Amazon EMR 7.9.0 release, the following
`docker pull` command gets you the lastest standard base image. You can replace
`emr-7.9.0:latest` with
`emr-7.9.0-spark-rapids:latest` to retrieve the image that has
Nvidia RAPIDS accelerator. You can also replace `emr-7.9.0:latest`
with `emr-7.9.0-java11:latest` to retrieve the image with Java 11
runtime.

```
docker pull public.ecr.aws/emr-on-eks/spark/`emr-7.9.0:latest`
```

If you would like to retrieve the base image for a Amazon EMR 6.9.0 or ealier releases, or if
you prefer to retrieve from Amazon ECR registry accounts in each Region, use the following
steps:

1. Choose a base image URI. The image URI follows this format,
   ``ECR-registry-account`.dkr.ecr.`Region`.amazonaws.com/spark/`container-image-tag``,
   as the following example demonstrates.

```
`895885662937`.dkr.ecr.`us-west-2`.amazonaws.com/spark/`emr-6.6.0:latest`
```

To choose a base image in your Region, see [Details for selecting a base image URI](docker-custom-images-tag.md "docker-custom-images-tag.md"). 2. Log in to the Amazon ECR repository where the base image is stored. Replace
`895885662937` and `us-west-2` with
the Amazon ECR registry account and the AWS Region you have selected.

```
aws ecr get-login-password --region `us-west-2` | docker login --username AWS --password-stdin `895885662937`.dkr.ecr.`us-west-2`.amazonaws.com
```

3. Pull the base image into your local Workspace. Replace
   `emr-6.6.0:latest` with the container image tag you have
   selected.

```
docker pull `895885662937`.dkr.ecr.`us-west-2`.amazonaws.com/spark/`emr-6.6.0:latest`
```

## Step 2: Customize a base image

Follow these steps to customize the base image you have pulled from Amazon ECR.

1. Create a new `Dockerfile` on your local Workspace.
2. Edit the `Dockerfile` you just created and add the following content.
   This `Dockerfile` uses the container image you have pulled from
   `895885662937.dkr.ecr.us-west-2.amazonaws.com/spark/emr-6.6.0:latest`.

```
FROM 895885662937.dkr.ecr.us-west-2.amazonaws.com/spark/emr-6.6.0:latest
USER root
### Add customization commands here ####
USER hadoop:hadoop
```

3. Add commands in the `Dockerfile` to customize the base image. For
   example, add a command to install Python libraries, as the following
   `Dockerfile` demonstrates.

```
FROM 895885662937.dkr.ecr.us-west-2.amazonaws.com/spark/emr-6.6.0:latest
USER root
RUN pip3 install --upgrade boto3 pandas numpy // For python 3
USER hadoop:hadoop
```

4. From the same directory where the `Dockerfile` is created, run the
   following command to build the Docker image. Provide a name for the Docker image, for
   example, `emr6.6_custom`.

```
docker build -t `emr6.6_custom` .
```

## Step 3: (Optional but recommended) Validate

a custom image

We recommend that you test the compatibility of your custom image before publishing it.
You can use the [Amazon EMR on EKS custom image CLI](https://github.com/awslabs/amazon-emr-on-eks-custom-image-cli "https://github.com/awslabs/amazon-emr-on-eks-custom-image-cli") to check if your image has the required file
structures and correct configurations for running on Amazon EMR on EKS.

###### Note

The Amazon EMR on EKS custom image CLI cannot confirm that your image is free of error. Use
caution when removing dependencies from the base images.

Take the following steps to validate your custom image.

1. Download and install Amazon EMR on EKS custom image CLI. For more information, see [Amazon EMR on EKS custom image CLI Installation Guide](https://github.com/awslabs/amazon-emr-on-eks-custom-image-cli/blob/main/installer/assets/INSTALLATION_GUIDE.md "https://github.com/awslabs/amazon-emr-on-eks-custom-image-cli/blob/main/installer/assets/INSTALLATION_GUIDE.md").
2. Run the following command to test the installation.

```
emr-on-eks-custom-image --version
```

The following shows an example of the output.

```
Amazon EMR on EKS Custom Image CLI
Version: x.xx
```

3. Run the following command to validate your custom image.

```
emr-on-eks-custom-image validate-image -i `image_name` -r `release_version` [-t `image_type`]
```

    * `-i` specifies the local image URI that needs to be validated. This
     can be the image URI, any name or tag that you defined for your image.
    * `-r` specifies the exact release version for the base image, for
     example, `emr-6.6.0-latest`.
    * `-t` specifies the image type. If this is a Spark image, input
     `spark`. The default value is `spark`. The current Amazon EMR on EKS
     custom image CLI version only supports Spark runtime images.

If you run the command successfully and the custom image meets all the required
configurations and file structures, the returned output displays the results of all of
the tests, as the following example demonstrates.

```
Amazon EMR on EKS Custom Image Test
Version: x.xx
... Checking if docker cli is installed
... Checking Image Manifest
[INFO] Image ID: xxx
[INFO] Created On: 2021-05-17T20:50:07.986662904Z
[INFO] Default User Set to hadoop:hadoop : PASS
[INFO] Working Directory Set to /home/hadoop : PASS
[INFO] Entrypoint Set to /usr/bin/entrypoint.sh : PASS
[INFO] SPARK_HOME is set with value: /usr/lib/spark : PASS
[INFO] JAVA_HOME is set with value: /etc/alternatives/jre : PASS
[INFO] File Structure Test for spark-jars in /usr/lib/spark/jars: PASS
[INFO] File Structure Test for hadoop-files in /usr/lib/hadoop: PASS
[INFO] File Structure Test for hadoop-jars in /usr/lib/hadoop/lib: PASS
[INFO] File Structure Test for bin-files in /usr/bin: PASS
... Start Running Sample Spark Job
[INFO] Sample Spark Job Test with local:///usr/lib/spark/examples/jars/spark-examples.jar : PASS
-----------------------------------------------------------------
Overall Custom Image Validation Succeeded.
-----------------------------------------------------------------
```

If the custom image doesn't meet the required configurations or file structures,
error messages occur. The returned output provides information about the incorrect
configurations or file structures.

## Step 4: Publish a custom image

Publish the new Docker image to your Amazon ECR registry.

1. Run the following command to create an Amazon ECR repository for storing your Docker
   image. Provide a name for your repository, for example,
   `emr6.6_custom_repo`. Replace
   `us-west-2` with your Region.

```
aws ecr create-repository \
    --repository-name `emr6.6_custom_repo` \
    --image-scanning-configuration scanOnPush=true \
    --region `us-west-2`
```

For more information, see [Create
a repository](../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-create-repository "../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-create-repository") in the _Amazon ECR User Guide_. 2. Run the following command to authenticate to your default registry.

```
aws ecr get-login-password --region `us-west-2` | docker login --username AWS --password-stdin `aws_account_id`.dkr.ecr.`us-west-2`.amazonaws.com
```

For more information, see [Authenticate to your default registry](../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-authenticate-registry "../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-authenticate-registry") in the _Amazon ECR User
Guide_. 3. Tag and publish an image to the Amazon ECR repository you created.

Tag the image.

```
docker tag `emr6.6_custom` `aws_account_id`.dkr.ecr.`us-west-2`.amazonaws.com/`emr6.6_custom_repo`
```

Push the image.

```
docker push `aws_account_id`.dkr.ecr.us-west-2.amazonaws.com/`emr6.6_custom_repo`
```

For more information, see [Push an image
to Amazon ECR](../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-push-image "../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-push-image") in the _Amazon ECR User Guide_.

## Step 5: Submit a Spark workload in Amazon EMR using

a custom image

After a custom image is built and published, you can submit an Amazon EMR on EKS job using a
custom image.

First, create a start-job-run-request.json file and specify the
`spark.kubernetes.container.image` parameter to reference the custom image, as
the following example JSON file demonstrates.

###### Note

You can use `local://` scheme to refer to files available in the custom
image as shown with `entryPoint` argument in the JSON snippet below. You can
also use the `local://` scheme to refer to application dependencies. All files
and dependencies that are referred using `local://` scheme must already be
present at the specified path in the custom image.

```

{
    "name": "spark-custom-image",
    "virtualClusterId": "`virtual-cluster-id`",
    "executionRoleArn": "`execution-role-arn`",
    "releaseLabel": "`emr-6.6.0-latest`",
    "jobDriver": {
      "sparkSubmitJobDriver": {
        "entryPoint": "local:///usr/lib/spark/examples/jars/spark-examples.jar",
        "entryPointArguments": [
                  "10"
              ],
         "sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi --conf spark.kubernetes.container.image=`123456789012.dkr.ecr.us-west-2.amazonaws.com/emr6.6_custom_repo`"
       }
    }
}

```

You can also reference the custom image with `applicationConfiguration`
properties as the following example demonstrates.

```

{
    "name": "spark-custom-image",
    "virtualClusterId": "`virtual-cluster-id`",
    "executionRoleArn": "`execution-role-arn`",
    "releaseLabel": "`emr-6.6.0-latest`",
    "jobDriver": {
      "sparkSubmitJobDriver": {
        "entryPoint": "local:///usr/lib/spark/examples/jars/spark-examples.jar",
        "entryPointArguments": [
                  "10"
              ],
         "sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi"
       }
    },
    "configurationOverrides": {
        "applicationConfiguration": [
            {
                "classification": "spark-defaults",
                "properties": {
                    "spark.kubernetes.container.image": "`123456789012.dkr.ecr.us-west-2.amazonaws.com/emr6.6_custom_repo`"
                }
            }
        ]
    }
}
```

Then run the `start-job-run` command to submit the job.

```

aws emr-containers start-job-run --cli-input-json file://./start-job-run-request.json
```

In the JSON examples above, replace `emr-6.6.0-latest` with
your Amazon EMR release version. We strongly recommend that you use the `-latest`
release version to ensure that the selected version contains the latest security updates.
For more information about Amazon EMR release versions and their image tags, see [Details for selecting a base image URI](docker-custom-images-tag.md "docker-custom-images-tag.md").

###### Note

You can use `spark.kubernetes.driver.container.image` and
`spark.kubernetes.executor.container.image` to specify a different image for
driver and executor pods.
