# Getting Started with Amazon Corretto 17 on Docker Images

This topic describes how to build and launch a Docker image that uses Amazon Corretto 17. You
must have the latest version of Docker installed.

## Using the official image for Amazon Corretto 17.

Amazon Corretto 17 is available as an [official image on Docker Hub](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto"). The following example runs a container and
displays Corretto 17's version.

```
docker run amazoncorretto:17 java -version
```

Output:

```
openjdk version "17.0.18" 2026-01-20 LTS
OpenJDK Runtime Environment Corretto-17.0.18.9.1 (build 17.0.18+9-LTS)
OpenJDK 64-Bit Server VM Corretto-17.0.18.9.1 (build 17.0.18+9-LTS, mixed mode, sharing)
```

## Using the Corretto ECR Instance

###### Note

The Corretto ECR Private Registry located at
[489478819445.dkr.ecr.us-west-2.amazonaws.com/amazoncorretto](489478819445.dkr.ecr.us-west-2.amazonaws.com/amazoncorretto.md "489478819445.dkr.ecr.us-west-2.amazonaws.com/amazoncorretto.md")
is now deprecated. Please migrate existing usages to the
[Corretto ECR Public Gallery.](https://gallery.ecr.aws/amazoncorretto/amazoncorretto "https://gallery.ecr.aws/amazoncorretto/amazoncorretto")
See
[corretto-docker#154](https://github.com/corretto/corretto-docker/issues/154 "https://github.com/corretto/corretto-docker/issues/154")
for more information.

To use the Corretto ECR instance, run the following commands:

```
docker pull public.ecr.aws/amazoncorretto/amazoncorretto:17
docker run -it public.ecr.aws/amazoncorretto/amazoncorretto:17 /bin/bash
```

You can see the list of available images by going [here](https://gallery.ecr.aws/amazoncorretto/amazoncorretto "https://gallery.ecr.aws/amazoncorretto/amazoncorretto"):

## Amazon Corretto on Alpine

Amazon Corretto on Alpine Linux images are available on
[Amazon ECR Public Gallery](https://gallery.ecr.aws/docker/library/amazoncorretto "https://gallery.ecr.aws/docker/library/amazoncorretto") and
[Dockerhub](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto")

Using dockerhub

```
docker pull amazoncorretto:17-alpine-jdk
docker run -it amazoncorretto:17-alpine-jdk /bin/sh
```

## Build a Docker Image with Amazon Corretto 17

Run the following command to build an image that uses Amazon Corretto 17.

```
docker build -t amazon-corretto-17 github.com/corretto/corretto-docker#main:17/jdk/al2023
```

After the command completes, you have an image called
_amazon-corretto-17_.

To launch this image locally, run the following command.

```
docker run -it amazon-corretto-17
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
FROM amazoncorretto:17
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
