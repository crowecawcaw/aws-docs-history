# Using Podman with Amazon ECR

Using Podman with Amazon ECR enables organizations to leverage the security and
simplicity of Podman while benefiting from the scalability and reliability of
Amazon ECR for container image management. By following the outlined steps and commands,
developers and administrators can streamline their container workflows, enhance security,
and optimize resource utilization. As containerization continues to gain momentum, using
Podman and Amazon ECR provides a robust and flexible solution for managing and
deploying containerized applications.

## Using Podman to authenticate with

Amazon ECR

Before interacting with Amazon ECR using Podman, authentication is required.
This can be achieved by running the `aws ecr get-login-password` command to
retrieve an authentication token, and then using that token with the `podman
 login` command to authenticate with Amazon ECR.

```
`aws ecr get-login-password --region `<region>` | podman login --username AWS --password-stdin `<aws_account_id>`.dkr.ecr.`<region>`.amazonaws.com`
```

## Using the Amazon ECR credential helper

with Podman

Amazon ECR provides a Docker credential helper that works with Podman. The credential
helper makes it easier to store and use Docker credentials when pushing and pulling
images to Amazon ECR. For installation and configuration steps, see [Amazon ECR Docker
Credential Helper](https://github.com/awslabs/amazon-ecr-credential-helper "https://github.com/awslabs/amazon-ecr-credential-helper").

###### Important

Podman only partially supports the docker-creds-helper specification. Podman
supports the `credHelpers` keyword in Docker configuration but does not
support the `credsStore` keyword.

To use the Amazon ECR credential helper with Podman, configure your Docker
configuration file with the `credHelpers` format:

```
{
    "credHelpers": {
        "public.ecr.aws": "ecr-login",
        "<aws_account_id>.dkr.ecr.<region>.amazonaws.com": "ecr-login"
    }
}
```

The following `credsStore` configuration is not supported by
Podman:

```
{
    "credsStore": "ecr-login"
}
```

###### Note

The Amazon ECR Docker credential helper does not support multi-factor authentication
(MFA) currently.

## Pulling images from Amazon ECR with Podman

After successful authentication, container images can be pulled from Amazon ECR using the
`podman pull` command with the full Amazon ECR repository URI.

```
`podman pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`repository_name`:`tag``
```

## Running containers for Amazon ECR with

Podman

Once the desired image has been pulled, a container can be instantiated using the
`podman run` command.

```
`podman run -d `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`repository_name`:`tag``
```

## Pushing images to Amazon ECR with

Podman

To push a local image to Amazon ECR, the image must first be tagged with the Amazon ECR
repository URI using `podman tag`, and then the `podman push`
command can be used to upload the image to Amazon ECR.

```
`podman tag `local_image`:`tag` `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`repository_name`:`tag`
podman push `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`repository_name`:`tag``
```
