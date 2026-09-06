

# Creating a container image for use on Amazon ECS
<a name="create-container-image"></a>

Amazon ECS uses Docker images in task definitions to launch containers. Docker is a technology that provides the tools for you to build, run, test, and deploy distributed applications in containers. 

Amazon ECS schedules containerized applications on to container instances or on to AWS Fargate. Containerized applications are packaged as container images. This example creates a container image for a web server.

You can create your first Docker image, and then push that image to Amazon ECR, which is a container registry, for use in your Amazon ECS task definitions. This walkthrough assumes that you possess a basic understanding of what Docker is and how it works. For more information about Docker, see [What is Docker?](http://aws.amazon.com/docker/) and the [Docker documentation](https://docs.docker.com/get-started/docker-overview/).

## Prerequisites
<a name="create-container-image-prerequisites"></a>

Before you begin, ensure the following prerequisites are met.
+ Ensure you have completed the Amazon ECR setup steps. For more information, see [Moving an image through its lifecycle in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html) in the *Amazon Elastic Container Registry User Guide*.
+ Your user has the required IAM permissions to access and use the Amazon ECR service. For more information, see [Amazon ECR managed policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security-iam-awsmanpol.html).
+ You have Docker installed. For Docker installation steps for Amazon Linux 2023, see [Installing Docker on AL2023](#create-container-image-install-docker). For all other operating systems, see the Docker documentation at [Docker Desktop overview](https://docs.docker.com/desktop/).
+ You have the AWS CLI installed and configured. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

If you don't have or need a local development environment and you prefer to use an Amazon EC2 instance to use Docker, we provide the following steps to launch an Amazon EC2 instance using Amazon Linux 2023 and install Docker Engine and the Docker CLI.

### Installing Docker on AL2023
<a name="create-container-image-install-docker"></a>

Docker is available on many different operating systems, including most modern Linux distributions, like Ubuntu, and even macOS and Windows. For more information about how to install Docker on your particular operating system, go to the [Docker installation guide](https://docs.docker.com/engine/installation/#installation).

You do not need a local development system to use Docker. If you are using Amazon EC2 already, you can launch an Amazon Linux 2023 instance and install Docker to get started.

If you already have Docker installed, skip to [Create a Docker image](#create-container-image-create-image).

**To install Docker on an Amazon EC2 instance using an Amazon Linux 2023 AMI**

1. Launch an instance with the latest Amazon Linux 2023 AMI. For more information, see [Launch an EC2 instance using the launch instance wizard in the console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html) in the *Amazon EC2 User Guide*.

1. Connect to your instance. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the *Amazon EC2 User Guide*.

1. Update the installed packages and package cache on your instance.

   ```
   sudo yum update -y
   ```

1. Install the most recent Docker Community Edition package.

   ```
   sudo yum install docker
   ```

1. Start the Docker service.

   ```
   sudo service docker start
   ```

1. Add the `ec2-user` to the `docker` group so you can execute Docker commands without using `sudo`.

   ```
   sudo usermod -a -G docker ec2-user
   ```

1. Log out and log back in again to pick up the new `docker` group permissions. You can accomplish this by closing your current SSH terminal window and reconnecting to your instance in a new one. Your new SSH session will have the appropriate `docker` group permissions.

1. Verify that the `ec2-user` can run Docker commands without `sudo`.

   ```
   docker info
   ```
**Note**  
In some cases, you may need to reboot your instance to provide permissions for the `ec2-user` to access the Docker daemon. Try rebooting your instance if you see the following error:  

   ```
   Cannot connect to the Docker daemon. Is the docker daemon running on this host?
   ```

## Create a Docker image
<a name="create-container-image-create-image"></a>

Amazon ECS task definitions use container images to launch containers on the container instances in your clusters. In this section, you create a Docker image of a simple web application, and test it on your local system or Amazon EC2 instance, and then push the image to the Amazon ECR container registry so you can use it in an Amazon ECS task definition.

**To create a Docker image of a simple web application**

1. Create a file called `Dockerfile`. A Dockerfile is a manifest that describes the base image to use for your Docker image and what you want installed and running on it. For more information about Dockerfiles, go to the [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/).

   ```
   touch Dockerfile
   ```

1. Edit the `Dockerfile` you just created and add the following content.

   ```
   FROM public.ecr.aws/amazonlinux/amazonlinux:latest
   
   # Update installed packages and install Apache
   RUN yum update -y && \
    yum install -y httpd
   
   # Write hello world message
   RUN echo 'Hello World!' > /var/www/html/index.html
   
   # Configure Apache
   RUN echo 'mkdir -p /var/run/httpd' >> /root/run_apache.sh && \
    echo 'mkdir -p /var/lock/httpd' >> /root/run_apache.sh && \
    echo '/usr/sbin/httpd -D FOREGROUND' >> /root/run_apache.sh && \
    chmod 755 /root/run_apache.sh
   
   EXPOSE 80
   
   CMD /root/run_apache.sh
   ```

   This Dockerfile uses the public Amazon Linux 2023 image hosted on Amazon ECR Public. The `RUN` instructions update the package caches, installs some software packages for the web server, and then write the "Hello World\!" content to the web servers document root. The `EXPOSE` instruction means that port 80 on the container is the one that is listening, and the `CMD` instruction starts the web server.

1. <a name="sample-docker-build-step"></a>Build the Docker image from your Dockerfile.
**Note**  
Some versions of Docker may require the full path to your Dockerfile in the following command, instead of the relative path shown in the following example.  
If you run the command an ARM based system, such as [Apple Silicon](https://support.apple.com/en-gb/116943), use the --platform option "--platform linux/amd64".

   ```
   docker build -t hello-world .
   ```

1. List your container image.

   ```
   docker images --filter reference=hello-world
   ```

   Output:

   ```
   REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
   hello-world         latest              e9ffedc8c286        4 minutes ago       194MB
   ```

1. Run the newly built image. The `-p 80:80` option maps the exposed port 80 on the container to port 80 on the host system. 

   ```
   docker run -t -i -p 80:80 hello-world
   ```
**Note**  
Output from the Apache web server is displayed in the terminal window. You can ignore the "`Could not reliably determine the fully qualified domain name`" message.

1. Open a browser and point to the server that is running Docker and hosting your container.
   + If you are using an EC2 instance, this is the **Public DNS** value for the server, which is the same address you use to connect to the instance with SSH. Make sure that the security group for your instance allows inbound traffic on port 80.
   + If you are running Docker locally, point your browser to [http://localhost/](http://localhost/).

   You should see a web page with your "Hello World\!" statement.

1. Stop the Docker container by typing **Ctrl \+ c**.

## Push your image to Amazon Elastic Container Registry
<a name="create-container-image-push-ecr"></a>

Amazon ECR is a managed AWS managed image registry service. You can use the Docker CLI to push, pull, and manage images in your Amazon ECR repositories. For Amazon ECR product details, featured customer case studies, and FAQs, see the [Amazon Elastic Container Registry product detail pages](http://aws.amazon.com/ecr).

**To tag your image and push it to Amazon ECR**

1. Create an Amazon ECR repository to store your `hello-world` image. Note the `repositoryUri` in the output.

   Substitute `region`, with your AWS Region, for example, `us-east-1`.

   ```
   aws ecr create-repository --repository-name {{hello-repository}} --region {{region}}
   ```

   Output:

   ```
   {
       "repository": {
           "registryId": "{{aws_account_id}}",
           "repositoryName": "hello-repository",
           "repositoryArn": "arn:aws:ecr:{{region}}:{{aws_account_id}}:repository/hello-repository",
           "createdAt": 1505337806.0,
           "repositoryUri": "{{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/hello-repository"
       }
   }
   ```

1. Tag the `hello-world` image with the `repositoryUri` value from the previous step.

   ```
   docker tag hello-world {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{hello-repository}}
   ```

1. Run the **aws ecr get-login-password** command. Specify the registry URI you want to authenticate to. For more information, see [Registry Authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth) in the *Amazon Elastic Container Registry User Guide*.

   ```
   aws ecr get-login-password --region {{region}} | docker login --username AWS --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com
   ```

   Output:

   ```
   Login Succeeded
   ```
**Important**  
If you receive an error, install or upgrade to the latest version of the AWS CLI. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

1. Push the image to Amazon ECR with the `repositoryUri` value from the earlier step.

   ```
   docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{hello-repository}}
   ```

## Clean up
<a name="create-container-image-cleanup"></a>

To continue on with creating an Amazon ECS task definition and launching a task with your container image, skip to the [Next steps](#create-container-image-next-steps). When you are done experimenting with your Amazon ECR image, you can delete the repository so you are not charged for image storage.

```
aws ecr delete-repository --repository-name {{hello-repository}} --region {{region}} --force
```

## Next steps
<a name="create-container-image-next-steps"></a>

Your task definitions require a task execution role. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md).

After you have created and pushed your container image to Amazon ECR, you can use that image in a task definition. For more information, see one of the following:
+ [Learn how to create an Amazon ECS Linux task for Fargate](getting-started-fargate.md)
+ [Learn how to create an Amazon ECS Windows task for Fargate](Windows_fargate-getting_started.md)
+ [Creating an Amazon ECS Linux task for the Fargate with the AWS CLI](ECS_AWSCLI_Fargate.md)