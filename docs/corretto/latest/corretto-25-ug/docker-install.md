

# Getting Started with Amazon Corretto 25 on Docker Images
<a name="docker-install"></a>

 This topic describes how to build and launch a Docker image that uses Amazon Corretto 25. You must have the latest version of Docker installed. 

## Using the official image for Amazon Corretto 25.
<a name="docker-hello-world"></a>

 Amazon Corretto 25 is available as an [official image on Docker Hub](https://hub.docker.com/_/amazoncorretto). The following example runs a container and displays Corretto 25's version. 

**Example**  

```
docker run amazoncorretto:25 java -version
```

 Output: 

**Example**  

```
openjdk version "25.0.4" 2026-08-18 LTS
OpenJDK Runtime Environment Corretto-25.0.4.8.1 (build 25.0.4+8-LTS)
OpenJDK 64-Bit Server VM Corretto-25.0.4.8.1 (build 25.0.4+8-LTS, mixed mode)
```

## Using the Corretto ECR Instance
<a name="amazon-corretto-yum-ecr"></a>

To use the Corretto ECR instance, run the following commands: 

**Example**  

```
docker pull public.ecr.aws/amazoncorretto/amazoncorretto:25
docker run -it public.ecr.aws/amazoncorretto/amazoncorretto:25 /bin/bash
```

You can see the list of available images by going [here](https://gallery.ecr.aws/amazoncorretto/amazoncorretto):

## Amazon Corretto on Alpine
<a name="alpine-images"></a>

Amazon Corretto on Alpine Linux images are available on [Amazon ECR Public Gallery](https://gallery.ecr.aws/docker/library/amazoncorretto) and [Dockerhub](https://hub.docker.com/_/amazoncorretto) 

Using dockerhub

**Example**  

```
docker pull amazoncorretto:25-alpine-jdk
docker run -it amazoncorretto:25-alpine-jdk /bin/sh
```

## Build a Docker Image with Amazon Corretto 25
<a name="docker-build-instruct"></a>

 Run the following command to build an image that uses Amazon Corretto 25. 

**Example**  

```
docker build -t amazon-corretto-25 github.com/corretto/corretto-docker#main:25/jdk/al2023
```

 After the command completes, you have an image called *amazon-corretto-25*. 

 To launch this image locally, run the following command. 

**Example**  

```
docker run -it amazon-corretto-25
```

 You can also push this image to Amazon ECR. See the [Pushing an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) topic in the *Amazon Elastic Container Registry User Guide* for details. 

## Create an Image
<a name="docker-new-image"></a>

 You can create a new Docker image using [Corretto's official Docker Hub image](https://hub.docker.com/_/amazoncorretto). 

1.  Create a Dockerfile with the following content.   
**Example**  

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

1.  Build the new image.   
**Example**  

   ```
   docker build -t hello-app .
   ```

1.  Run the new image.   
**Example**  

   ```
   docker run hello-app
   ```

    You get the following output. 

    `Welcome to Amazon Corretto!` 