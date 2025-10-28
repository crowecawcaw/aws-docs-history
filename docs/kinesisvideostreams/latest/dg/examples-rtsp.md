# Example: Streaming from an RTSP source

The [C++](producer-sdk-cpp.md "producer-sdk-cpp.md") contains
a definition for a [Docker](https://www.docker.com/ "https://www.docker.com/") container that

connects to a Real-Time Streaming Protocol (RTSP) network camera. Using Docker
standardizes the operating environment for Kinesis Video Streams, which streamlines building and using
the application.

The following procedure demonstrates how to set up and use the RTSP demo
application.

###### Topics

- [Video tutorials](#rtsp-video "#rtsp-video")
- [Prerequisites](#examples-rtsp-prerequisites "#examples-rtsp-prerequisites")
- [Build the Docker image](#examples-rtsp-build "#examples-rtsp-build")
- [Run the RTSP example application](#examples-rtsp-procedure "#examples-rtsp-procedure")

## Video tutorials

This video shows how to set up a Raspberry Pi to send RTSP feeds to AWS cloud
and Amazon Kinesis Video Streams. This is an end-to-end demonstration.

This video demonstrates how to capture images from a feed to use computer vision
and Amazon Rekognition to process the images and send alerts.

## Prerequisites

To run the Kinesis Video Streams RTSP example application, you must have the following:

- **Docker:** For information about installing
  and using Docker, see the following links:
  - [Docker download
    instructions](https://docs.docker.com/desktop/ "https://docs.docker.com/desktop/")
  - [Getting started
    with Docker](https://docs.docker.com/guides/getting-started/ "https://docs.docker.com/guides/getting-started/")

- **RTSP network camera source:** For
  information about recommended cameras, see [System requirements](system-requirements.md "system-requirements.md").

## Build the Docker image

First, build the Docker image that the demo application will run inside.

1. Clone the Amazon Kinesis Video Streams demos repository.

```
git clone https://github.com/aws-samples/amazon-kinesis-video-streams-demos.git
```

2. Change to the directory containing the Dockerfile. In this case, it is the
   [docker-rtsp](https://github.com/aws-samples/amazon-kinesis-video-streams-demos/blob/master/producer-cpp/docker-rtsp/ "https://github.com/aws-samples/amazon-kinesis-video-streams-demos/blob/master/producer-cpp/docker-rtsp/") directory.

```
cd amazon-kinesis-video-streams-demos/producer-cpp/docker-rtsp/
```

3. Use the following command to build the Docker image. This command creates
   the image and tags it as rtspdockertest.

```
docker build -t rtspdockertest .
```

4. Run `docker images` and search for the image ID tagged with
   `rtspdockertest`.

For example, in the sample output below, the `IMAGE ID` is
`54f0d65f69b2`.

```
REPOSITORY        TAG       IMAGE ID        CREATED           PLATFORM       SIZE         BLOB SIZE
rtspdockertest    latest    54f0d65f69b2    10 minutes ago    linux/arm64    653.1 MiB    292.4 MiB
```

You will need this in a later step.

## Run the RTSP example application

You can run the RTSP example application either from within or outside the Docker
container. Follow the appropriate instructions below.

###### Topics

- [Within the Docker container](#examples-rtsp-within "#examples-rtsp-within")
- [Outside the Docker container](#examples-rtsp-outside "#examples-rtsp-outside")

### Within the Docker container

###### Run the RTSP example application

1. Start the Amazon Kinesis Video Streams Docker container using the following
   command:

```
docker run -it `YourImageId` /bin/bash
```

2. To start the sample application, provide your AWS credentials, the
   name of the Amazon Kinesis video stream, and the URL of the RTSP network
   camera.

###### Important

If you are using temporary credentials, you'll also need to
provide your `AWS_SESSION_TOKEN`. See the second example
below.

```
export AWS_ACCESS_KEY_ID=`YourAccessKeyId`
export AWS_SECRET_ACCESS_KEY=`YourSecretKeyId`
export AWS_DEFAULT_REGION=`YourAWSRegion`
./kvs_gstreamer_sample `YourStreamName` `YourRtspUrl`
```

**Temporary credentials:**

```
export AWS_ACCESS_KEY_ID=`YourAccessKeyId`
export AWS_SECRET_ACCESS_KEY=`YourSecretKeyId`
export AWS_SESSION_TOKEN=`YourSessionToken`
export AWS_DEFAULT_REGION=`YourAWSRegion`
./kvs_gstreamer_sample `YourStreamName` `YourRtspUrl`
```

3. Sign into the AWS Management Console and open the [Kinesis Video Streams console](https://console.aws.amazon.com/kinesisvideo/home/ "https://console.aws.amazon.com/kinesisvideo/home/").

View the stream. 4. To exit the Docker container, close the terminal window or type
`exit`.

### Outside the Docker container

From **outside** the Docker container, use the
following command:

```
docker run -it `YourImageId` /bin/bash -c "export AWS_ACCESS_KEY_ID=`YourAccessKeyId`; export AWS_SECRET_ACCESS_KEY=`YourSecretKeyId`; export AWS_SESSION_TOKEN=`YourSessionToken`; export AWS_DEFAULT_REGION=`YourAWSRegion`; ./kvs_gstreamer_sample `YourStreamName` `YourRtspUrl`"
```
