# Getting Started with Amazon Corretto 25 on Docker Images

This topic describes how to build and launch a Docker image that uses Amazon Corretto 25. You
must have the latest version of Docker installed.

## Using the official image for Amazon Corretto 25.

Amazon Corretto 25 is available as an [official image on Docker Hub](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto"). The following example runs a container and
displays Corretto 25's version.

```
docker run amazoncorretto:25 java -version
```

Output:

```
openjdk version "25.0.2" 2026-01-20 LTS
OpenJDK Runtime Environment Corretto-25.0.2.10.1 (build 25.0.2+10-LTS)
OpenJDK 64-Bit Server VM Corretto-25.0.2.10.1 (build 25.0.2+10-LTS, mixed mode)
```

## Using the Corretto ECR Instance

To use the Corretto ECR instance, run the following commands:

```
docker pull public.ecr.aws/amazoncorretto/amazoncorretto:25
docker run -it public.ecr.aws/amazoncorretto/amazoncorretto:25 /bin/bash
```

You can see the list of available images by going [here](https://gallery.ecr.aws/amazoncorretto/amazoncorretto "https://gallery.ecr.aws/amazoncorretto/amazoncorretto"):

## Amazon Corretto on Alpine

Amazon Corretto on Alpine Linux images are available on
[Amazon ECR Public Gallery](https://gallery.ecr.aws/docker/library/amazoncorretto "https://gallery.ecr.aws/docker/library/amazoncorretto") and
[Dockerhub](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto")

Using dockerhub

```
docker pull amazoncorretto:25-alpine-jdk
docker run -it amazoncorretto:25-alpine-jdk /bin/sh
```

## Build a Docker Image with Amazon Corretto 25

Run the following command to build an image that uses Amazon Corretto 25.

```
docker build -t amazon-corretto-25 github.com/corretto/corretto-docker#main:25/jdk/al2023
```

After the command completes, you have an image called
_amazon-corretto-25_.

To launch this image locally, run the following command.

```
docker run -it amazon-corretto-25
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
FROM amazoncorretto:25
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
