# Getting Started with Amazon Corretto 21 on Docker Images

This topic describes how to build and launch a Docker image that uses Amazon Corretto 21. You
must have the latest version of Docker installed.

## Using the official image for Amazon Corretto 21.

Amazon Corretto 21 is available as an [official image on Docker Hub](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto"). The following example runs a container and
displays Corretto 21's version.

```
docker run amazoncorretto:21 java -version
```

Output:

```
openjdk version "21.0.9" 2025-10-21 LTS
OpenJDK Runtime Environment Corretto-21.0.9.11.1 (build 21.0.9+11-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.9.11.1 (build 21.0.9+11-LTS, mixed mode, sharing)
```

## Using the Corretto ECR Instance

To use the Corretto ECR instance, run the following commands:

```
docker pull public.ecr.aws/amazoncorretto/amazoncorretto:21
docker run -it public.ecr.aws/amazoncorretto/amazoncorretto:21 /bin/bash
```

You can see the list of available images by going [here](https://gallery.ecr.aws/amazoncorretto/amazoncorretto "https://gallery.ecr.aws/amazoncorretto/amazoncorretto"):

## Amazon Corretto on Alpine

Amazon Corretto on Alpine Linux images are available on
[Amazon ECR Public Gallery](https://gallery.ecr.aws/docker/library/amazoncorretto "https://gallery.ecr.aws/docker/library/amazoncorretto") and
[Dockerhub](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto")

Using dockerhub

```
docker pull amazoncorretto:21-alpine-jdk
docker run -it amazoncorretto:21-alpine-jdk /bin/sh
```

## Build a Docker Image with Amazon Corretto 21

Run the following command to build an image that uses Amazon Corretto 21.

```
docker build -t amazon-corretto-21 github.com/corretto/corretto-docker#main:21/jdk/al2023
```

After the command completes, you have an image called
_amazon-corretto-21_.

To launch this image locally, run the following command.

```
docker run -it amazon-corretto-21
```

You can also push this image to Amazon ECR. See the
[Pushing an Image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md") topic in the _Amazon Elastic Container Registry User Guide_
for details.

## Create an

Image

You can create a new Docker image using
[Corretto's official Docker Hub image](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto").

1. Create a Dockerfile with the following content.

```
FROM amazoncorretto:21
RUN echo $' \
public class Hello { \
public static void main(String[] args) { \
System.out.println("Welcome to Amazon Corretto!"); \
} \
}' > Hello.java
RUN javac Hello.java
CMD ["java", "Hello"]
```

2. Build the new image.

```
docker build -t hello-app .
```

3. Run the new image.

```
docker run hello-app
```

You get the following output.

`Welcome to Amazon Corretto!`
