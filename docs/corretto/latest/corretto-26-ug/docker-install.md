# Getting Started with Amazon Corretto 26 on Docker Images

This topic describes how to build and launch a Docker image that uses Amazon Corretto 26. You
must have the latest version of Docker installed.

## Using the official image for Amazon Corretto 26.

Amazon Corretto 26 is available as an [official image on Docker Hub](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto"). The following example runs a container and
displays Corretto 26's version.

###### Example

```
docker run amazoncorretto:26 java -version
```

Output:

###### Example

```
openjdk version "26.0.0" 2026-02-05
OpenJDK Runtime Environment Corretto-26.0.0.34.1 (build 26.0.0+34-FR)
OpenJDK 64-Bit Server VM Corretto-26.0.0.34.1 (build 26.0.0+34-FR, mixed mode)
```

## Using the Corretto ECR Instance

To use the Corretto ECR instance, run the following commands:

###### Example

```
docker pull public.ecr.aws/amazoncorretto/amazoncorretto:26
docker run -it public.ecr.aws/amazoncorretto/amazoncorretto:26 /bin/bash
```

You can see the list of available images by going [here](https://gallery.ecr.aws/amazoncorretto/amazoncorretto "https://gallery.ecr.aws/amazoncorretto/amazoncorretto"):

## Amazon Corretto on Alpine

Amazon Corretto on Alpine Linux images are available on
[Amazon ECR Public Gallery](https://gallery.ecr.aws/docker/library/amazoncorretto "https://gallery.ecr.aws/docker/library/amazoncorretto") and
[Dockerhub](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto")

Using dockerhub

###### Example

```
docker pull amazoncorretto:26-alpine-jdk
docker run -it amazoncorretto:26-alpine-jdk /bin/sh
```

## Build a Docker Image with Amazon Corretto 26

Run the following command to build an image that uses Amazon Corretto 26.

###### Example

```
docker build -t amazon-corretto-26 github.com/corretto/corretto-docker#main:26/jdk/al2023
```

After the command completes, you have an image called
_amazon-corretto-26_.

To launch this image locally, run the following command.

###### Example

```
docker run -it amazon-corretto-26
```

You can also push this image to Amazon ECR. See the
[Pushing an Image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md") topic in the _Amazon Elastic Container Registry User Guide_
for details.

## Create an

Image

You can create a new Docker image using
[Corretto's official Docker Hub image](https://hub.docker.com/_/amazoncorretto "https://hub.docker.com/_/amazoncorretto").

1. Create a Dockerfile with the following content.

###### Example

```
FROM amazoncorretto:26
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

###### Example

```
docker build -t hello-app .
```

3. Run the new image.

###### Example

```
docker run hello-app
```

You get the following output.

`Welcome to Amazon Corretto!`
