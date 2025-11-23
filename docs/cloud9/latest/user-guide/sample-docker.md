AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Docker tutorial for AWS Cloud9

This tutorial shows you how to connect an AWS Cloud9 SSH development environment to a running Docker container inside of an Amazon Linux instance in Amazon EC2.
This enables you to use the AWS Cloud9 IDE to work with code and files inside of a Docker container and to run commands on that container.
For information about Docker, see [What is Docker](https://www.docker.com/what-docker "https://www.docker.com/what-docker") on the Docker website.

Following this tutorial and creating this sample might result in charges to your AWS account. These include possible charges for services such as Amazon EC2. For more information, see
[Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").

###### Topics

- [Prerequisites](#sample-docker-prereqs "#sample-docker-prereqs")
- [Step 1: Install and run Docker](#sample-docker-install "#sample-docker-install")
- [Step 2: Build the image](#sample-docker-build "#sample-docker-build")
- [Step 3: Run the container](#sample-docker-run "#sample-docker-run")
- [Step 4: Create the environment](#sample-docker-env "#sample-docker-env")
- [Step 5: Run the code](#sample-docker-code "#sample-docker-code")
- [Step 6: Clean up](#sample-docker-clean-up "#sample-docker-clean-up")

## Prerequisites

- **You should have an Amazon EC2 instance running Amazon Linux or Ubuntu
  Server.** This sample assumes you already have an Amazon EC2 instance running
  Amazon Linux or Ubuntu Server in your AWS account. To launch an Amazon EC2 instance, see [Launch a
  Linux Virtual Machine](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/ "https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/"). In the **Choose an Amazon Machine Image
  (AMI)** page of the wizard, choose an AMI whose display name starts with
  **Amazon Linux AMI** or **Ubuntu Server**.
- **If the Amazon EC2 instance runs within an Amazon VPC, there are additional requirements.** See [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md "vpc-settings.md").
- **The Amazon EC2 instance should have at least 8 to 16 GB of free disk space available.** This sample uses Docker images that are over 3 GB in size and can use additional
  increments of 3 GB or more of disk space to build images. If you try to run this sample on
  a disk that has 8 GB of free space or less, we've found that the Docker image might not build or the Docker container might not run. To check the instance's
  free disk space, you can run a command such as **`df -h`** (for "disk filesystem information in human-readable format") on the instance.
  To increase an existing instance's disk size, see [Modifying a Volume](../../../ebs/latest/userguide/ebs-modify-volume.md "../../../ebs/latest/userguide/ebs-modify-volume.md") in the _Amazon EC2 User Guide_.

## Step 1: Install and run Docker

In this step, you check if Docker is installed on the Amazon EC2 instance, and install Docker if it isn't already installed. After you install Docker, you run it on
the instance.

1. Connect to the running Amazon EC2 instance by using an SSH client such as the **`ssh`** utility or PuTTY. To do this, see
   "Step 3: Connect to Your Instance" in [Launch a Linux Virtual Machine](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/ "https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/").
2. Check if Docker is installed on the instance. To do this, run the **`docker`** command on the instance with the **`--version`** option.

```
docker --version
```

If Docker is installed, the Docker version and build number are displayed. In this case, skip ahead to step 5 later in this procedure. 3. Install Docker. To do this, run the **`yum`** or **`apt`** command with the **`install`** action, specifying the **`docker`** or **`docker.io`** package to install.

For Amazon Linux:

```
sudo yum install -y docker
```

For Ubuntu Server:

```
sudo apt install -y docker.io
```

4. Confirm that Docker is installed. To do this, run the **`docker --version`** command again. The Docker version and build number are displayed.
5. Run Docker. To do this, run the **`service`** command with the **`docker`** service and the **`start`** action.

```
sudo service docker start
```

6. Confirm Docker is running. To do this, run the **`docker`** command with the **`info`** action.

```
sudo docker info
```

If Docker is running, information about Docker is displayed.

## Step 2: Build the image

In this step, you use a Dockerfile to build a Docker image onto the instance. This sample uses an image that includes Node.js and a sample chat server application.

1. On the instance, create the Dockerfile. To do this, with the SSH client still connected to the instance,
   in the `/tmp` directory on the instance, create a file named `Dockerfile`. For example, run the **`touch`** command as follows.

```
sudo touch /tmp/Dockerfile
```

2. Add the following contents to the `Dockerfile` file.

```

# Build a Docker image based on the Amazon Linux 2 Docker image.
FROM amazonlinux:2

# install common tools
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum update -y
RUN yum install -y sudo bash curl wget git man-db nano vim bash-completion tmux  gcc gcc-c++ make tar

# Enable the Docker container to communicate with AWS Cloud9 by
# installing SSH.
RUN yum install -y openssh-server

# Ensure that Node.js is installed.
RUN yum install -y nodejs

# Create user and enable root access
RUN useradd --uid 1000 --shell /bin/bash -m --home-dir /home/ubuntu ubuntu && \
    sed -i 's/%wheel\s.*/%wheel ALL=NOPASSWD:ALL/' /etc/sudoers && \
    usermod -a -G wheel ubuntu

# Add the AWS Cloud9 SSH public key to the Docker container.
# This assumes a file named authorized_keys containing the
# AWS Cloud9 SSH public key already exists in the same
# directory as the Dockerfile.
RUN mkdir -p /home/ubuntu/.ssh
ADD ./authorized_keys /home/ubuntu/.ssh/authorized_keys
RUN chown -R ubuntu /home/ubuntu/.ssh /home/ubuntu/.ssh/authorized_keys && \
chmod 700 /home/ubuntu/.ssh && \
chmod 600 /home/ubuntu/.ssh/authorized_keys

# Update the password to a random one for the user ubuntu.
RUN echo "ubuntu:$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)" | chpasswd

# pre-install Cloud9 dependencies
USER ubuntu
RUN curl https://d2j6vhu5uywtq3.cloudfront.net/static/c9-install.sh | bash

USER root
# Start SSH in the Docker container.
CMD ssh-keygen -A && /usr/sbin/sshd -D

```

To add the preceding contents to the `Dockerfile` file, you could use the **`vi`** utility on the instance as follows.

    1. Use the AWS Cloud9 to open and edit the `/tmp/Dockerfile` file.



    ```
    sudo vi /tmp/Dockerfile
    ```
    2. Paste the preceding contents into the `Dockerfile` file. If you're not sure how to do this, see your SSH client's documentation.
    3. Switch to command mode. To do this, press the `Esc` key. (`-- INSERT --` disappears from the bottom of the window.)
    4. Type `:wq` (to write to the `/tmp/Dockerfile` file, save the file, and then exit **`vi`**), and then press `Enter`.###### Note

You can access a frequently updated list of Docker images from AWS CodeBuild. For
more information, see [Docker images provided by CodeBuild](../../../codebuild/latest/userguide/build-env-ref-available.md "../../../codebuild/latest/userguide/build-env-ref-available.md") in the
_AWS CodeBuild User Guide_. 3. On the instance, create a file that contains the AWS Cloud9 SSH public key for the Docker container to use. To do this, in the same directory as the `Dockerfile` file,
create a file named `authorized_keys`, for example, by running the **`touch`** command.

```
sudo touch /tmp/authorized_keys
```

4. Add the AWS Cloud9 SSH public key to the `authorized_keys` file. To get the AWS Cloud9 SSH public key, do the following:
   1. Open the AWS Cloud9 console at [https://console.aws.amazon.com/cloud9/](https://console.aws.amazon.com/cloud9/ "https://console.aws.amazon.com/cloud9/").
   2. In the AWS navigation bar, in the AWS Region selector, choose the AWS Region where you'll want to create the AWS Cloud9 development environment later in this topic.
   3. If a welcome page is displayed, for **New AWS Cloud9 environment**, choose **Create environment**. Otherwise, choose **Create environment**.
   4. On the **Name environment** page, for **Name**, type a name for the environment. (The name doesn't matter here. You'll choose a different name later.)
   5. Choose **Next step**.
   6. For **Environment type**, choose **Connect and run in remote server (SSH)**.
   7. Expand **View public SSH key**.
   8. Choose **Copy key to clipboard**. (This is between **View public SSH key** and **Advanced settings**.)
   9. Choose **Cancel**.
   10. Paste the contents of the clipboard into the `authorized_keys` file, and then save the file. For example, you can use the **`vi`** utility, as described earlier in this step.

5. Build the image by running the **`docker`** command with the **`build`** action, adding the tag `cloud9-image:latest` to the image and
   specifying the path to the `Dockerfile` file to use.

```
sudo docker build -t cloud9-image:latest /tmp
```

If successful, the last two lines of the build output display `Successfully built` and `Successfully tagged`.

To confirm that Docker successfully built the image, run the **`docker`** command with the `image ls` action.

```
sudo docker image ls
```

If successful, the output displays an entry where the `REPOSITORY` field is set to `cloud9-image` and the `TAG` field is set to `latest`. 6. Make a note of the Amazon EC2 instance's public IP address. You'll need it for [Step 4: Create the environment](#sample-docker-env "#sample-docker-env"). If you're not sure what the public IP address of the instance is,
you can run the following command on the instance to get it.

```
curl http://169.254.169.254/latest/meta-data/public-ipv4
```

## Step 3: Run the container

In this step, you run a Docker container on the instance. This container is based on the image you built in the previous step.

1. To run the Docker container, run the **`docker`** command on the instance with the **`run`** action and the following options.

```
sudo docker run -d -it --expose 9090 -p 0.0.0.0:9090:22 --name cloud9 cloud9-image:latest
```

    * `-d` runs the container in detached mode, exiting whenever the root process that is used to run the container (in this sample, the SSH client) exits.
    * `-it` runs the container with an allocated pseudo-TTY and keeps STDIN open, even if the container is not attached.
    * `--expose` makes the specified port (in this sample, port `9090`) available from the container.
    * `-p` makes the specified port available internally to the Amazon EC2 instance over the specified IP address and port. In this sample, port `9090` on the container can be accessed
    internally through port `22` on the Amazon EC2 instance.
    * `--name` is a human-readable name for the container (in this sample, `cloud9`).
    * `cloud9-image:latest` is the human-readable name of the built image to use to run the container.

To confirm that Docker is successfully running the container, run the **`docker`** command with the `container ls` action.

```
sudo docker container ls
```

If successful, the output displays an entry where the `IMAGE` field is set to `cloud9-image:latest` and the `NAMES` field is set to `cloud9`. 2. Log in to the running container. To do this, run the **`docker`** command with the **`exec`** action and the following options.

```
sudo docker exec -it cloud9 bash
```

    * `-it` runs the container with an allocated pseudo-TTY and keeps STDIN open, even if the container isn't attached.
    * `cloud9` is the human-readable name of the running container.
    * `bash` starts the standard shell in the running container.

If successful, the terminal prompt changes to display the logged-in user's name for the container and the ID of the container.

###### Note

If you ever want to log out of the running container, run the **`exit`** command. The terminal prompt changes back to display the logged-in user's name for the instance and
the private DNS of the instance. The container should still be running. 3. For the directory on the running container that you want AWS Cloud9 to start from after it logs in, set its access permissions to
**`rwxr-xr-x`**. This means read-write-execute permissions for the owner, read-execute permissions for the group, and read-execute permissions for others. For example,
if the directory's path is `~`, you can set these permissions on the directory by running the **`chmod`** command in the running container as follows.

```
sudo chmod u=rwx,g=rx,o=rx ~
```

4. Make a note of the path to the directory on the running container that contains the Node.js binary, as you'll need it for [Step 4: Create the environment](#sample-docker-env "#sample-docker-env").
   If you're not sure what this path is, run the following command on the running container to get it.

```
which node
```

## Step 4: Create the environment

In this step, you use AWS Cloud9 to create an AWS Cloud9 SSH development environment and connect it to the running Docker container. After AWS Cloud9 creates the
environment, it displays the AWS Cloud9 IDE so that you can start working with the files and code in the container.

You create an AWS Cloud9 SSH development environment with the AWS Cloud9 console. You can't create an SSH environment using
the CLI.

### Prerequisites

- Make sure that you completed the steps in [Setting up AWS Cloud9](setting-up.md "setting-up.md") first. That way, you can sign in to the AWS Cloud9
  console and create environments.
- Identify an existing cloud compute instance (for example, an Amazon EC2 instance in
  your AWS account) or your own server that you want AWS Cloud9 to connect to the
  environment.
- Make sure that the existing instance or your own server meets all of the [SSH host requirements](ssh-settings.md#ssh-settings-requirements "ssh-settings.md#ssh-settings-requirements"). This includes having specific versions of Python, Node.js, and other
  components installed, setting specific permissions on the directory that you want
  AWS Cloud9 to start from after login, and setting up any associated Amazon Virtual Private Cloud.

### Create the SSH Environment

1. Make sure that you completed the preceding prerequisites.
2. Connect to your existing instance or your own server by using an SSH client, if
   you aren't already connected to it. This ensures that you can add the necessary
   public SSH key value to the instance or server. This is described later in this
   procedure.

###### Note

To connect to an existing AWS Cloud compute instance, see one or more of
the following resources:

    * For Amazon EC2, see [Connect to Your Linux Instance](../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md "../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md") in the
     *Amazon EC2 User Guide*.
    * For Amazon Lightsail, see [Connect to your Linux/Unix-based Lightsail instance](https://lightsail.aws.amazon.com/ls/docs/how-to/article/lightsail-how-to-connect-to-your-instance-virtual-private-server "https://lightsail.aws.amazon.com/ls/docs/how-to/article/lightsail-how-to-connect-to-your-instance-virtual-private-server") in the
     *Amazon Lightsail Documentation*.
    * For AWS Elastic Beanstalk, see [Listing and
     Connecting to Server Instances](../../../elasticbeanstalk/latest/dg/using-features.md "../../../elasticbeanstalk/latest/dg/using-features.md") in the
     *AWS Elastic Beanstalk Developer Guide*.
    * For AWS OpsWorks, see [Using SSH to Log In to a
     Linux Instance](../../../opsworks/latest/userguide/workinginstances-ssh.md "../../../opsworks/latest/userguide/workinginstances-ssh.md") in the
     *AWS OpsWorks User Guide*.
    * For other AWS services, see the documentation for that specific
     service.To connect to your own server, use SSH. SSH is already installed on the

macOS and Linux operating systems. To connect to your server by using SSH on
Windows, you must install [PuTTY](https://www.putty.org/ "https://www.putty.org/"). 3. Sign in to the AWS Cloud9 console, at [https://console.aws.amazon.com/cloud9/](https://console.aws.amazon.com/cloud9/ "https://console.aws.amazon.com/cloud9/"). 4. After you sign in to the AWS Cloud9 console, in the top navigation bar choose an
AWS Region to create the environment in. For a list of available AWS Regions, see
[AWS Cloud9](../../../general/latest/gr/rande.md#cloud9_region "../../../general/latest/gr/rande.md#cloud9_region") in the
_AWS General Reference_.

![Region selector in the AWS Cloud9 console](images/consolas_region_new_UX.png) 5. If this is the first time that you're creating a development environment, a
welcome page is displayed. In the **New AWS Cloud9 environment** panel,
choose **Create environment**.

If you've previously created development environments, you can also expand the
pane on the left of the screen. Choose **Your environments**, and
then choose **Create environment**.

In the **welcome** page:

![Choose the Create environment button if the welcome page is displayed](images/create_welcome_env_new_UX.png)

Or in the **Your environments** page:

![Choose the Create environment button if the welcome page isn't displayed](images/console_create_env_new_UX.png) 6. On the **Create environment** page, enter a name for your
environment. 7. For **Description**, enter something about your environment. For
this tutorial, use `This environment is for the AWS Cloud9 tutorial.` 8. For **Environment type**, choose **Existing
Compute** from the following options:

    * **New EC2 instance**
     – Launches an Amazon EC2 instance that AWS Cloud9 can connect to directly over SSH.


    * **Existing compute**  – Launches an Amazon EC2 instance that doesn't require any open
     inbound ports. AWS Cloud9 connects to the instance through [AWS Systems Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md").




    	+ If you select the **Existing compute** option, a
    	 service role and an IAM instance profile are created to allow Systems Manager
    	 to interact with the EC2 instance on your behalf. You can view the
    	 names of both in the **Service role and instance profile for
    	 Systems Manager access** section further down the interface. For
    	 more information, see [Accessing no-ingress EC2 instances with AWS Systems Manager](ec2-ssm.md "ec2-ssm.md").

###### Warning

Creating an EC2 instance for your environment might result in possible
charges to your AWS account for Amazon EC2. There's no additional cost to use
Systems Manager to manage connections to your EC2 instance.

###### Warning

AWS Cloud9 uses SSH public key to connect securely to your server. To establish
the secure connection, add our public key to your
`~/.ssh/authorized_keys` file and provide your login
credentials in the following steps. Choose **Copy key to clipboard** to copy the
SSH key, or **View public SSH key to display it.** 9. On the **Existing compute** panel, for
**User**, enter the login name that you used to connect to the
instance or server earlier in this procedure. For example, for an AWS Cloud
compute instance, it might be `ec2-user`, `ubuntu`, or
`root`.

###### Note

We recommend that the login name is associated with administrative
permissions or an administrator user on the instance or server. More
specifically, we recommend that this login name owns the Node.js installation
on the instance or server. To check this, from the terminal of your instance or
server, run the command **`ls -l $(which node)`** (or **`ls -l $(nvm which node)`** if you're using `nvm`). This command displays the owner
name of the Node.js installation. It also displays the installation's
permissions, group name, and location. 10. For **Host**, enter the public IP address (preferred) or the
hostname of the instance or server. 11. For **Port**, enter the port that you want AWS Cloud9 to use to try
to connect to the instance or server. Alternatively, keep the default port. 12. Choose **Additional details - optional** to display the environment path, path to node.js binary and SSH jump host information. 13. For **Environment path**, enter the path to the directory on
the instance or server that you want AWS Cloud9 to start from. You identified this
earlier in the prerequisites to this procedure. If you leave this blank, AWS Cloud9
uses the directory that your instance or server typically starts with after login.
This is usually a home or default directory. 14. For **Path to Node.js binary path**, enter the path
information to specify the path to the Node.js binary on the instance or server.
To get the path, you can run the command **`which
 node`** (or **`nvm which node`** if you're using `nvm`) on your instance or server. For
example, the path might be `/usr/bin/node`. If you leave this blank,
AWS Cloud9 attempts to guess where the Node.js binary is when it tries to
connect. 15. For **SSH jump host**, enter information about the jump host
that the instance or server uses. Use the format
`USER_NAME@HOSTNAME:PORT_NUMBER` (for example,
`ec2-user@:ip-192-0-2-0:22`).

The jump host must meet the following requirements:

    * It must be reachable over the public internet using SSH.
    * It must allow inbound access by any IP address over the specified
     port.
    * The public SSH key value that was copied into the
     `~/.ssh/authorized_keys` file on the existing instance
     or server must also be copied into the
     `~/.ssh/authorized_keys` file on the jump host.
    * Netcat must be installed.

16. Add up to 50 tags by supplying a **Key** and a
    **Value** for each tag. Do so by selecting **Add new
    tag**. The tags are attached to the AWS Cloud9 environment as resource
    tags, and are propagated to the following underlying resources: the CloudFormation stack,
    the Amazon EC2 instance, and Amazon EC2 security groups. To learn more about tags, see
    [Control Access Using AWS Resource
    Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _[IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")_ and the [advanced information](tags.md "tags.md") about tags in this guide.

###### Warning

If you update these tags after you create them, the changes aren't
propagated to the underlying resources. For more information, see [Propagating tag updates to underlying resources](tags.md#tags-propagate "tags.md#tags-propagate") in the advanced
information about [tags](tags.md "tags.md"). 17. Choose **Create** to create your environment, and you're then
redirected to the home page. When the account is created successfully, a green
flash bar appears at the top of the AWS Cloud9 console. You can select the new
environment and choose **Open in Cloud9** to launch the IDE.

![AWS Cloud9 IDE selector in the AWS Cloud9 console](images/cloud9-ide-open.png)

If the account fails to create, a red flash bar appears at the top of the AWS Cloud9
console. Your account might fail to create due to a problem with your web browser,
your AWS access permissions, the instance, or the associated network. You can
find information about possible fixes to issues that might cause the account to
fail in the [AWS Cloud9 Troubleshooting
section.](troubleshooting.md#troubleshooting-env-loading "troubleshooting.md#troubleshooting-env-loading")

###### Note

If your environment is using a proxy to access the internet, you must provide
proxy details to AWS Cloud9 so it can install dependencies. For more information, see
[Failed to install dependencies](troubleshooting.md#proxy-failed-dependencies "troubleshooting.md#proxy-failed-dependencies").

## Step 5: Run the code

In this step, you use the AWS Cloud9 IDE to run a sample application inside the running Docker container.

1. With the AWS Cloud9 IDE displayed for the running container, start the sample chat server. To do this,
   in the **Environment** window, right-click the sample `workspace/server.js` file, and then choose **Run**.
2. Preview the sample application. To do this, in the **Environment** window, open the
   the `workspace/client/index.html` file. Then, on the menu bar, choose **Tools, Preview, Preview Running Application**.
3. On the application preview tab, for **Your Name**, type your name. For **Message**, type a message.
   Then choose **Send**. The chat server adds your name and message to the list.

## Step 6: Clean up

In this step, you delete the environment and remove AWS Cloud9 and Docker support files from the Amazon EC2 instance.
Also, to prevent ongoing charges to your AWS account after you're done using this sample, you should terminate the Amazon EC2 instance that is running Docker.

### Step 6.1: Delete the environment

To delete the environment, see [Deleting an environment in AWS Cloud9](delete-environment.md "delete-environment.md").

### Step 6.2: Remove

AWS Cloud9 support files from the container

After you delete the environment, some AWS Cloud9 support files still remain in the container. If you want to keep using the container but no longer
need these support files, delete the `.c9` folder from the directory on the container that you specified AWS Cloud9 to start from after it logs in.
For example, if the directory is `~`, run the **`rm`** command with the **`-r`** option as follows.

```
sudo rm -r ~/.c9
```

### Step 6.3:

Remove Docker support files from the instance

If you no longer want to keep the Docker container, the Docker image, and Docker on the Amazon EC2 instance, but you want to keep the instance, you
can remove these Docker support files as follows.

1. Remove the Docker container from the instance. To do this, run the **`docker`** command on the instance
   with the **`stop`** and **`rm`** stop actions and the human-readable name of the container.

```
sudo docker stop cloud9
sudo docker rm cloud9
```

2. Remove the Docker image from the instance. To do this, run the **`docker`** command on the instance
   with the **`image rm`** action and the image's tag.

```
sudo docker image rm cloud9-image:latest
```

3. Remove any additional Docker support files that might still exit. To do this, run the **`docker`** command on the instance
   with the **`system prune`** action.

```
sudo docker system prune -a
```

4. Uninstall Docker. To do this, run the **`yum`** command on the instance with the **`remove`** action, specifying the
   **`docker`** package to uninstall.

For Amazon Linux:

```
sudo yum -y remove docker
```

For Ubuntu Server:

```
sudo apt -y remove docker
```

You can also remove the `Dockerfile` and `authorized_keys` files you created earlier. For example, run the
**`rm`** command on the instance.

```
sudo rm /tmp/Dockerfile
sudo rm /tmp/authorized_keys
```

### Step 6.4: Terminate the

instance

To terminate the Amazon EC2 instance, see [Terminate Your Instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in the _Amazon EC2 User Guide_.
