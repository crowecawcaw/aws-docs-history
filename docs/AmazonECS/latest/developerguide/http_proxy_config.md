# Using an HTTP proxy for Amazon ECS Linux container

instances

You can configure your Amazon ECS container instances to use an HTTP proxy for both the Amazon ECS
container agent and the Docker daemon. This is useful if your container instances do not
have external network access through an Amazon VPC internet gateway, NAT gateway, or instance.

To configure your Amazon ECS Linux container instance to use an HTTP proxy, set the following
variables in the relevant files at launch time (with Amazon EC2 user data). You can also manually
edit the configuration file, and then restart the agent.

`/etc/ecs/ecs.config` (Amazon Linux 2 and AmazonLinux
AMI)

`HTTP_PROXY=`10.0.0.131`:`3128``

Set this value to the hostname (or IP address) and port number of
an HTTP proxy to use for the Amazon ECS agent to connect to the internet.
For example, your container instances may not have external network
access through an Amazon VPC internet gateway, NAT gateway, or
instance.

`NO_PROXY=169.254.169.254,169.254.170.2,/var/run/docker.sock`

Set this value to
`169.254.169.254,169.254.170.2,/var/run/docker.sock`
to filter EC2 instance metadata, IAM roles for tasks, and Docker
daemon traffic from the proxy.

`/etc/systemd/system/ecs.service.d/http-proxy.conf`
(Amazon Linux 2 only)

`Environment="HTTP_PROXY=`10.0.0.131`:`3128`/"`

Set this value to the hostname (or IP address) and port number of
an HTTP proxy to use for `ecs-init` to connect to the
internet. For example, your container instances may not have
external network access through an Amazon VPC internet gateway, NAT
gateway, or instance.

`Environment="NO_PROXY=169.254.169.254,169.254.170.2,/var/run/docker.sock"`

Set this value to
`169.254.169.254,169.254.170.2,/var/run/docker.sock`
to filter EC2 instance metadata, IAM roles for tasks, and Docker
daemon traffic from the proxy.

`/etc/init/ecs.override` (Amazon Linux AMI only)

`env
 HTTP_PROXY=`10.0.0.131`:`3128``

Set this value to the hostname (or IP address) and port number of
an HTTP proxy to use for `ecs-init` to connect to the
internet. For example, your container instances may not have
external network access through an Amazon VPC internet gateway, NAT
gateway, or instance.

`env
 NO_PROXY=169.254.169.254,169.254.170.2,/var/run/docker.sock`

Set this value to
`169.254.169.254,169.254.170.2,/var/run/docker.sock`
to filter EC2 instance metadata, IAM roles for tasks, and Docker
daemon traffic from the proxy.

`/etc/systemd/system/docker.service.d/http-proxy.conf`
(Amazon Linux 2 only)

`Environment="HTTP_PROXY=http://`10.0.0.131`:`3128`"`

Set this value to the hostname (or IP address) and port number of
an HTTP proxy to use for the Docker daemon to connect to the
internet. For example, your container instances may not have
external network access through an Amazon VPC internet gateway, NAT
gateway, or instance.

`Environment="NO_PROXY=169.254.169.254,169.254.170.2"`

Set this value to `169.254.169.254,169.254.170.2` to filter EC2
instance metadata from the proxy.

`/etc/sysconfig/docker` (Amazon Linux AMI and
Amazon Linux 2 only)

`export
 HTTP_PROXY=http://`10.0.0.131`:`3128``

Set this value to the hostname (or IP address) and port number of
an HTTP proxy to use for the Docker daemon to connect to the
internet. For example, your container instances may not have
external network access through an Amazon VPC internet gateway, NAT
gateway, or instance.

`export NO_PROXY=169.254.169.254,169.254.170.2`

Set this value to `169.254.169.254,169.254.170.2` to filter EC2
instance metadata from the proxy.

Setting these environment variables in the above files only affects the Amazon ECS container
agent, `ecs-init`, and the Docker daemon. They do not configure any other
services (such as **yum**) to use the proxy.

For information about how to confiure thhe proxy, see [How do I set up
an HTTP proxy for Docker and the Amazon ECS container agent in Amazon Linux 2 or
AL2023](https://repost.aws/knowledge-center/ecs-http-proxy-docker-linux2 "https://repost.aws/knowledge-center/ecs-http-proxy-docker-linux2").
