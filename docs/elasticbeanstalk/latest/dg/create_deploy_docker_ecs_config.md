# ECS managed Docker configuration for Elastic Beanstalk

This chapter explains how to configure your ECS managed Docker environment. The following list summarizes the configuration items that this chapter
explains.

- `Dockerrun.aws.json` v2 – This configuration file specifies your image repository and the name of your Docker images, among other
  components.
- EC2 Instance profile role – If you have a custom instance profile, we explain how to configure it so that the permissions required for ECS to
  manage your containers stay current.
- Elastic Load Balancing listeners – You'll need to configure multiple Elastic Load Balancing listeners if you need your environment to support inbound traffic for proxies or
  other services that don't run on the default HTTP port.

###### Topics

- [Configuring the Dockerrun.aws.json v2 file](create_deploy_docker_v2config.md "create_deploy_docker_v2config.md")
- [Container managed policy and EC2 instance role](create_deploy_docker_ecs_role.md "create_deploy_docker_ecs_role.md")
- [Using multiple Elastic Load Balancing listeners](create_deploy_docker_ecs_listeners.md "create_deploy_docker_ecs_listeners.md")
