This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Step 2: Configure the host

Complete the following procedure to configure the host.

1. Connect to your EC2 or host machine and create a directory for your Docker volume. For
   this example, we'll use a directory in the current user's home, `~/WickrIO`.
   This directory will mount inside the container at `/opt/WickrIO`.

```
`cd ~
mkdir WickrIO`
```

2. Make sure that the `~/WickrIO` directory or your chosen directory is
   shared with Docker. For more information, see [Sharing local files with containers](https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/ "https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/").
3. Pull the public Wickr IO Docker image:

```
`docker pull public.ecr.aws/x3s2s6k3/wickrio/bot-cloud:latest`
```

###### Note

If you have a Docker image saved in in .tar format, you must load it using the following
command before starting the docker container:

`docker load -i `image-name`.tar`

Replace `image-name` with the actual file name of your Docker
image.
