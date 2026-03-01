# Moving an image through its lifecycle in Amazon ECR

If you are using Amazon ECR for the first time, use the following steps with the Docker CLI and
the AWS CLI to create a sample image, authenticate to the default registry, and create a
private repository. Then push an image to and pull an image from the private repository.
When you are finished with the sample image, delete the sample image and the
repository.

To use the AWS Management Console instead of the AWS CLI, see [Creating an Amazon ECR private repository to store images](repository-create.md "repository-create.md").

For more information on the other tools available for managing your AWS resources,
including the different AWS SDKs, IDE toolkits, and the Windows PowerShell command line
tools, see [http://aws.amazon.com/tools/](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/").

## Prerequisites

If you do not have the latest AWS CLI and Docker installed and ready to use, use
the following steps to install both of these tools.

### Install the AWS CLI

To use the AWS CLI with Amazon ECR, install the latest AWS CLI version. For
information, see
[Installing the AWS Command Line Interface](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md") in the
_AWS Command Line Interface User Guide_.

### Install Docker

Docker is available on many different operating systems, including most modern
Linux distributions, like Ubuntu, and even macOS and Windows. For more information
about how to install Docker on your particular operating system, go to the [Docker
installation guide](https://docs.docker.com/engine/installation/#installation "https://docs.docker.com/engine/installation/#installation").

You do not need a local development system to use Docker. If you are using Amazon EC2
already, you can launch an Amazon Linux 2023 instance and install Docker to get
started.

If you already have Docker installed, skip to [Step 1: Create a Docker image](#cli-create-image "#cli-create-image").

###### To install Docker on an Amazon EC2 instance using an Amazon Linux 2023 AMI

1. Launch an instance with the latest Amazon Linux 2023 AMI. For more
   information, see [Launching an instance](../../../AWSEC2/latest/UserGuide/launching-instance.md "../../../AWSEC2/latest/UserGuide/launching-instance.md") in the
   _Amazon EC2 User Guide_.
2. Connect to your instance. For more information, see [Connect to Your Linux
   Instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the _Amazon EC2 User Guide_.
3. Update the installed packages and package cache on your instance.

```
`sudo yum update -y`
```

4. Install the most recent Docker Community Edition package.

```
`sudo yum install docker`
```

5. Start the Docker service.

```
`sudo service docker start`
```

6. Add the `ec2-user` to the `docker` group so you can
   execute Docker commands without using `sudo`.

```
`sudo usermod -a -G docker ec2-user`
```

7. Log out and log back in again to pick up the new `docker` group
   permissions. You can accomplish this by closing your current SSH terminal
   window and reconnecting to your instance in a new one. Your new SSH session
   will have the appropriate `docker` group permissions.
8. Verify that the `ec2-user` can run Docker commands without
   `sudo`.

```
`docker info`
```

###### Note

In some cases, you may need to reboot your instance to provide
permissions for the `ec2-user` to access the Docker daemon.
Try rebooting your instance if you see the following error:

```
Cannot connect to the Docker daemon. Is the docker daemon running on this host?
```

## Step 1: Create a Docker image

In this step, you create a Docker image of a simple web application, and test it on
your local system or Amazon EC2 instance.

###### To create a Docker image of a simple web application

1. Create a file called `Dockerfile`. A Dockerfile is a
   manifest that describes the base image to use for your Docker image and what you
   want installed and running on it. For more information about Dockerfiles, go to
   the [Dockerfile
   Reference](https://docs.docker.com/engine/reference/builder/ "https://docs.docker.com/engine/reference/builder/").

```
`touch Dockerfile`
```

2. Edit the `Dockerfile` you just created and add the
   following content.

```
FROM public.ecr.aws/amazonlinux/amazonlinux:latest

# Install dependencies
RUN yum update -y && \
 yum install -y httpd

# Install apache and write hello world message
RUN echo 'Hello World!' > /var/www/html/index.html

# Configure apache
RUN echo 'mkdir -p /var/run/httpd' >> /root/run_apache.sh && \
 echo 'mkdir -p /var/lock/httpd' >> /root/run_apache.sh && \
 echo '/usr/sbin/httpd -D FOREGROUND' >> /root/run_apache.sh && \
 chmod 755 /root/run_apache.sh

EXPOSE 80

CMD /root/run_apache.sh
```

This Dockerfile uses the public Amazon Linux 2 image hosted on Amazon ECR Public.
The `RUN` instructions update the package caches, installs some
software packages for the web server, and then write the "Hello World!" content
to the web servers document root. The `EXPOSE` instruction exposes
port 80 on the container, and the `CMD` instruction starts the web
server. 3. Build the Docker image from your Dockerfile.

###### Note

Some versions of Docker may require the full path to your Dockerfile in
the following command, instead of the relative path shown below.

```
`docker build -t hello-world .`
```

4. List your container image.

```
`docker images --filter reference=hello-world`
```

Output:

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              e9ffedc8c286        4 minutes ago       194MB
```

5. Run the newly built image. The `-p 80:80` option maps the exposed
   port 80 on the container to port 80 on the host system. For more information
   about **docker run**, go to the [Docker run
   reference](https://docs.docker.com/engine/reference/run/ "https://docs.docker.com/engine/reference/run/").

```
`docker run -t -i -p 80:80 hello-world`
```

###### Note

Output from the Apache web server is displayed in the terminal window. You
can ignore the "`Could not reliably determine the fully
 qualified domain name`" message. 6. Open a browser and point to the server that is running Docker and hosting your
container.

    * If you are using an EC2 instance, this is the **Public
     DNS** value for the server, which is the same address you
     use to connect to the instance with SSH. Make sure that the security
     group for your instance allows inbound traffic on port 80.
    * If you are running Docker locally, point your browser to [http://localhost/](http://localhost/ "http://localhost/").
    * If you are using **docker-machine** on a Windows or Mac
     computer, find the IP address of the VirtualBox VM that is hosting
     Docker with the **docker-machine ip** command,
     substituting `machine-name` with the name of
     the docker machine you are using.



    ```
    `docker-machine ip `machine-name``
    ```

You should see a web page with your "Hello World!" statement. 7. Stop the Docker container by typing **Ctrl + c**.

## Step 2: Create a repository

Now that you have an image to push to Amazon ECR, you must create a repository to hold it.
In this example, you create a repository called `hello-repository` to which
you later push the `hello-world:latest` image. To create a repository, run
the following command:

```
`aws ecr create-repository \
 --repository-name `hello-repository` \
 --region `region``
```

## Step 3: Authenticate to your default registry

After you have installed and configured the AWS CLI, authenticate the Docker CLI to your
default registry. That way, the **docker** command can push and pull
images with Amazon ECR. The AWS CLI provides a **get-login-password** command to
simplify the authentication process.

To authenticate Docker to an Amazon ECR registry with
get-login-password, run the **aws ecr get-login-password** command. When passing
the authentication token to the **docker login** command, use the value `AWS` for the username and specify the Amazon ECR registry URI you want to authenticate to. If authenticating to
multiple registries, you must repeat the command for each registry.

###### Important

If you receive an error, install or upgrade to the latest version of the
AWS CLI. For more information, see [Installing the AWS Command Line Interface](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md") in the
_AWS Command Line Interface User Guide_.

- [get-login-password](../../../cli/latest/reference/ecr/get-login-password.md "../../../cli/latest/reference/ecr/get-login-password.md") (AWS CLI)

```
`aws ecr get-login-password --region `region` | docker login --username AWS --password-stdin ``aws_account_id``.dkr.ecr.`region`.amazonaws.com`
```

- [Get-ECRLoginCommand](../../../powershell/latest/reference/items/Get-ECRLoginCommand.md "../../../powershell/latest/reference/items/Get-ECRLoginCommand.md") (AWS Tools for Windows PowerShell)

```
`(Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin ``aws_account_id``.dkr.ecr.`region`.amazonaws.com`
```

## Step 4: Push an image to Amazon ECR

Now you can push your image to the Amazon ECR repository you created in the previous
section. Use the **docker** CLI to push images after the following
prerequisites are met:

- The minimum version of **docker** is installed:
  1.7.
- The Amazon ECR authorization token was configured with **docker
  login**.
- The Amazon ECR repository exists and the user has access to push to the
  repository.

After those prerequisites are met, you can push your image to your newly created
repository in the default registry for your account.

###### To tag and push an image to Amazon ECR

1. List the images you have stored locally to identify the image to tag and
   push.

```
`docker images`
```

Output:

```
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
hello-world         latest              e9ffedc8c286        4 minutes ago       241MB
```

2. Tag the image to push to your repository.

```
`docker tag hello-world:latest `aws_account_id`.dkr.ecr.`region`.amazonaws.com/hello-repository`
```

3. Push the image.

```
`docker push `aws_account_id`.dkr.ecr.`region`.amazonaws.com/hello-repository:latest`
```

Output:

```
The push refers to a repository [aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository] (len: 1)
e9ae3c220b23: Pushed
a6785352b25c: Pushed
0998bf8fb9e9: Pushed
0a85502c06c9: Pushed
latest: digest: sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636EXAMPLE size: 6774
```

## Step 5: Pull an image from Amazon ECR

After your image is pushed to your Amazon ECR repository, you can pull it from other
locations. Use the **docker** CLI to pull images after the following
prerequisites are met:

- The minimum version of **docker** is installed:
  1.7.
- The Amazon ECR authorization token was configured with **docker
  login**.
- The Amazon ECR repository exists and the user has access to pull from the
  repository.

After those prerequisites are met, you can pull your image. To pull your example image
from Amazon ECR, run the following command:

```
`docker pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/hello-repository:latest`
```

Output:

```
latest: Pulling from hello-repository
0a85502c06c9: Pull complete
0998bf8fb9e9: Pull complete
a6785352b25c: Pull complete
e9ae3c220b23: Pull complete
Digest: sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636EXAMPLE
Status: Downloaded newer image for aws_account_id.dkr.region.amazonaws.com/hello-repository:latest
```

## Step 6: Delete an image

If you no longer need an image in one of your repositories, you can delete the image.
To delete an image, specify the repository that it's in and either an
`imageTag` or `imageDigest` value for the image. The following
example deletes an image in the `hello-repository` repository with the image
tag `latest`. To delete your example image from the repository, run the
following command:

```
`aws ecr batch-delete-image \
 --repository-name hello-repository \
 --image-ids imageTag=latest \
 --region `region``
```

## Step 7: Delete a repository

If you no longer need an entire repository of images, you can delete the repository.
The following example uses the `--force` flag to delete a repository that
contains images. To delete a repository that contains images (and all the images within
it), run the following command:

```
`aws ecr delete-repository \
 --repository-name hello-repository \
 --force \
 --region `region``
```
