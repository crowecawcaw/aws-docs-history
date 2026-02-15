# Build a container image for Amazon GameLift Servers

This topic describes how to create a container image with your game server software to use
with Amazon GameLift Servers. A game server container image includes the game server executable and any
dependencies it needs to run. Game server container images are used with an Amazon GameLift Servers managed
containers hosting solution. For details on building the complete solution, see:

- [Development roadmap for hosting with Amazon GameLift Servers managed
  containers](gamelift-roadmap-containers.md "gamelift-roadmap-containers.md")
- [How containers work in Amazon GameLift Servers](containers-howitworks.md "containers-howitworks.md")
  Complete the following tasks to get your game server container image ready for deployment to
  an Amazon GameLift Servers container fleet. Before starting these tasks, finish integrating your game server
  code with the Amazon GameLift Servers server SDK.

###### Topics

- [Create a game server container image](#containers-prepare-images-build "#containers-prepare-images-build")
- [Push a container image to Amazon ECR](#containers-prepare-images-upload "#containers-prepare-images-upload")

## Create a game server container image

Follow these instructions while working on a Linux-based platform or using Windows Subsystem
for Linux (WSL) with Docker installed.

###### To create a game server container image

1. Prepare a working directory with your game server software. On a local machine, create a
   working directory to organize the files for your game server container. Your container
   image uses this file structure when deploying the container to Amazon GameLift Servers resources for
   hosting. For example:

```
``[~/]$` mkdir -p work/glc/gamebuild && cd work && find .``.
./glc
./glc/gamebuild`
```

###### Note

If you're trying out this feature and don't have a working game server build yet,
try our sample game server, [SimpleServer](https://github.com/aws-solutions-library-samples/guidance-for-custom-game-backend-hosting-on-aws/tree/main/BackendFeatures/AmazonGameLiftIntegration/SimpleServer "https://github.com/aws-solutions-library-samples/guidance-for-custom-game-backend-hosting-on-aws/tree/main/BackendFeatures/AmazonGameLiftIntegration/SimpleServer"), which is available on GitHub. 2. Create a new Dockerfile using the template provided. 3. Follow the instructions in the Dockerfile template to update it for your own use.

    * Update the base image as needed.
    * Set environment variables for your game server build.

4. Build the container image. Run the `docker build`, specifying your own repository name. For example:

```
``[~/work/glc]$` docker build -t `<local repository name>`:`<optional tag>` .`
```

You can view your repositories and images IDs using the `docker images` command, as illustrated in this
example:

This template contains the minimum instructions that a game server container needs to
usable in an Amazon GameLift Servers fleet. Modify the content as needed for your game server.

```
# Base image
# ----------
  # Add the base image that you want to use,
  # Make sure to use an image with the same architecture as the
  # Instance type you are planning to use on your fleets.
FROM public.ecr.aws/amazonlinux/amazonlinux
  #
# Game build directory
# --------------------
  # Add your gamebuild directory to the env variable below.
  # The game build provided here needs to be integrated with server sdk for Amazon GameLift Servers.
ENV GAME_BUILD_DIRECTORY="<ADD_GAME_BUILD_DIRECTORY>" \
  #
# Game executable and launch parameters
# ---------------
  # Add the relative path to your executable in the 'GAME_EXECUTABLE' env variable below.
  # The game build provided over here needs to be integrated with server sdk for Amazon GameLift Servers.
  # This template assumes that the executable path is relative to the game build directory.
  # Add any launch parameters to pass into your executable in the 'LAUNCH_PARAMS' env variable below.
  # Add 'HOME_DIR' to identify where the game executable and logs exist.
GAME_EXECUTABLE="<ADD NAME OF EXECUTABLE WITHIN THE GAME DIRECTORY>" \
LAUNCH_PARAMS=<ADD LAUNCH PARAMETERS> \
HOME_DIR="/local/game" \


# Install dependencies as necessary
RUN yum install -y shadow-utils

RUN mkdir -p $HOME_DIR
COPY ./$GAME_BUILD_DIRECTORY/ $HOME_DIR

# Change directory to home
WORKDIR $HOME_DIR

# Set up for 'gamelift' user
RUN useradd -m gamelift && \
  echo "gamelift ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
  chown -R gamelift:gamelift $HOME_DIR

# Add permissions to game build
RUN chmod +x ./$GAME_EXECUTABLE

USER gamelift

# Check directory before starting the container
RUN ls -lhrt .

# Check path before starting the container
RUN echo $PATH

# Start the game build
ENTRYPOINT ["/bin/sh", "-c", "./$GAME_EXECUTABLE", "$LAUNCH_PARAMS"]
```

## Push a container image to Amazon ECR

After you've created a container image for deployment to Amazon GameLift Servers, store the image In a public or
private repository in Amazon ECR. This repository is assigned a URI value, which Amazon GameLift Servers uses to take
a snapshot of the image for deployment to a container fleet.

###### Note

If you don't yet have an Amazon ECR private repository, then [create one](../../../AmazonECR/latest/userguide/repository-create.md "../../../AmazonECR/latest/userguide/repository-create.md").

###### To push your container image to Amazon ECR

1. Get your Amazon ECR credentials. Before pushing a container image to Amazon ECR, first acquire your AWS
   credentials in temporary form and provide them to Docker. Docker needs these credentials to log in.

```
``[~/work/glc]$` aws ecr get-login-password --region `us-west-2` | docker login --username AWS --password-stdin `aws_account_id`.dkr.ecr.`us-west-2`.amazonaws.com``WARNING! Your password will be stored unencrypted in
/home/`user-name`/.docker/config.json.
Configure a credential helper to remove this warning.
See https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded`
```

2. Copy the URI of the [Amazon ECR private repository](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories") you want to use.
3. Apply an Amazon ECR tag to your container image.

###### Example

```
``[~/work/glc]$` docker tag `<IMAGE ID from above>` `<Amazon ECR private repository URI>`:`<optional tag>``
```

4. Push your container image to Amazon ECR

###### Example

```
``[~/work/glc]$` docker image push `<Amazon ECR private repository URI>``
```
