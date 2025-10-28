# Connect to VPC with

subnets without internet access

Before connecting Visual Studio Code to Studio spaces in private subnets without
internet access, ensure your administrator has [Set
up Studio to run with subnets without internet access within a VPC](remote-access-remote-setup-vpc-subnets-without-internet-access.md "remote-access-remote-setup-vpc-subnets-without-internet-access.md").

You have two options to connect your local Visual Studio Code to Studio spaces in
private subnets:

- Set up HTTP Proxy
- Pre-packaged VS Code remote server and extensions

###### Topics

- [HTTP Proxy with controlled allow-listing](#remote-access-local-ide-setup-vpc-no-internet-http-proxy-with-controlled-allow-listing "#remote-access-local-ide-setup-vpc-no-internet-http-proxy-with-controlled-allow-listing")
- [Pre-packaged VS Code remote server and extensions](#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions "#remote-access-local-ide-setup-vpc-no-internet-pre-packaged-vs-code-remote-server-and-extensions")

## HTTP Proxy with controlled allow-listing

When your Studio space is behind a firewall or proxy, ask your
administrator to allow access to VS Code server and extension-related CDNs and
endpoints. For more information, see [Set up HTTP Proxy with controlled allow-listing](remote-access-remote-setup-vpc-subnets-without-internet-access.md#remote-access-remote-setup-vpc-subnets-without-internet-access-setup-http-proxy-with-controlled-allow-listing "remote-access-remote-setup-vpc-subnets-without-internet-access.md#remote-access-remote-setup-vpc-subnets-without-internet-access-setup-http-proxy-with-controlled-allow-listing").

Once set up, you can configure the HTTP proxy for VS Code remote development
by providing the proxy URL with the `remote.SSH.httpProxy` or
`remote.SSH.httpsProxy` setting.

###### Note

Consider enabling “Remote.SSH: Use Curl And Wget Configuration Files” to
use the configuration from the remote environment’s `curlrc` and
`wgetrc` files. This is so that the `curlrc` and
`wgetrc` files, placed in their respective default locations
in the SageMaker space, can be used for enabling certain cases.

This option works when you are allowed to set up HTTP proxy and lets you
install additional extensions flexibly, as some extensions require a public
endpoint.

## Pre-packaged VS Code remote server and extensions

When your Studio spaces can’t access external endpoints to download
VS Code remote server and extensions, you can pre-package them. With this
approach, your administrator can export a tarball containing the `.VS
 Code-server` directory for a specific version of VS Code. Then,
the administrator uses a SageMaker AI Lifecycle Configuration (LCC) script to copy and
extract the tarball into your home directory
(`/home/sagemaker-user`). For more information, see [Set up Pre-packaged Visual Studio Code remote server and extensions](remote-access-remote-setup-vpc-subnets-without-internet-access.md#remote-access-remote-setup-vpc-subnets-without-internet-access-setup-pre-packaged-vs-code-remote-server-and-extensions "remote-access-remote-setup-vpc-subnets-without-internet-access.md#remote-access-remote-setup-vpc-subnets-without-internet-access-setup-pre-packaged-vs-code-remote-server-and-extensions").

**Instructions for using pre-packaging for your VS Code
remote server and extensions**

1. Install VS Code on your local machine
2. When you connect to the SageMaker space:
   - Use the Default profile to ensure compatibility with
     pre-packaged extensions. Otherwise, you’ll need to install
     extensions using downloaded VSIX files after connecting to the
     Studio space.
   - Choose a VS Code version specific LCC script to attach to the
     space when you launch the space.

### Example Dockerfile usage for pre-packaging your VS Code remote server

and extensions

The following is a sample Dockerfile to launch a local container with SSH
server pre-installed, if it is not possible to create a space with remote
access and internet enabled.

###### Note

- In this example the SSH server does not require authentication
  and is only used for exporting the VS Code remote
  server.
- The container should be built and run on an x64
  architecture.

```
FROM amazonlinux:2023

# Install OpenSSH server and required tools
RUN dnf install -y \
    openssh-server \
    shadow-utils \
    passwd \
    sudo \
    tar \
    gzip \
    && dnf clean all

# Create a user with no password
RUN useradd -m -s /bin/bash sagemaker-user && \
    passwd -d sagemaker-user

# Add sagemaker-user to sudoers via wheel group
RUN usermod -aG wheel sagemaker-user && \
    echo 'sagemaker-user ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/sagemaker-user && \
    chmod 440 /etc/sudoers.d/sagemaker-user

# Configure SSH to allow empty passwords and password auth
RUN sed -i 's/^#\?PermitEmptyPasswords .*/PermitEmptyPasswords yes/' /etc/ssh/sshd_config && \
    sed -i 's/^#\?PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Generate SSH host keys
RUN ssh-keygen -A

# Expose SSH port
EXPOSE 22

WORKDIR /home/sagemaker-user
USER sagemaker-user

# Start SSH server
CMD ["bash"]
```

Use the following commands to build and run the container:

```
# Build the image
docker build . -t remote_server_export

# Run the container
docker run --rm -it -d \
  -v /tmp/remote_access/.VS Code-server:/home/sagemaker-user/.VS Code-server \
  -p 2222:22 \
  --name remote_server_export \
  remote_server_export

# change the permisson for the mounted folder
docker exec -i remote_server_export \
       bash -c 'sudo chown sagemaker-user:sagemaker-user ~/.VS Code-server'

# start the ssh server in the container
docker exec -i remote_server_export bash -c 'sudo /usr/sbin/sshd -D &'
```

Connect using the following command:

```
ssh sagemaker-user@localhost -p 2222
```

Before this container can be connected, configure the following in the
`.ssh/config` file. Afterwards you will be able to
see the `remote_access_export` as a host name in the
remote SSH side panel when connecting. For example:

```
Host remote_access_export
  HostName localhost
  User=sagemaker-user
  Port 2222
  ForwardAgent yes
```

Archive `/tmp/remote_access/.VS Code-server` and follow
the steps in Pre-packaged VS Code remote server and extensions to connect
and install the extension. After unzipping, ensure that the `.VS
 Code-server` folder shows as the parent folder.

```
cd /tmp/remote_access/
sudo tar -czvf VS Code-server-with-extensions-for-1.100.2.tar.gz .VS Code-server
```

### Example LCC script (LCC-install-VS Code-server-v1.100.2)

The following is an example of how to install a specific version of
VS Code remote server.

```
#!/bin/bash

set -x

remote_server_file=VS Code-server-with-extensions-for-1.100.2.tar.gz

if [ ! -d "${HOME}/.VS Code-server" ]; then
    cd /tmp
    aws s3 cp s3://S3_BUCKET/remote_access/${remote_server_file} .
    tar -xzvf ${remote_server_file}
    mv .VS Code-server "${HOME}"
    rm ${remote_server_file}
else
    echo "${HOME}/.VS Code-server already exists, skipping download and install."
fi
```
