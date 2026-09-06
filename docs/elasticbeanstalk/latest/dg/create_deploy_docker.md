

# Deploying with Docker containers to Elastic Beanstalk
<a name="create_deploy_docker"></a>

This chapter explains how you can use Elastic Beanstalk to deploy web applications from Docker containers. Docker containers are self contained and include all the configuration information and software that your web application requires to run. With Docker containers you can define your own runtime environment. You can also choose your own programming language and application dependencies, such as package managers or tools, which typically aren't supported by other Elastic Beanstalk platforms. 

Follow the steps in [QuickStart for Docker](docker-quickstart.md) to create a Docker "Hello World" application and deploy it to an Elastic Beanstalk environment using the EB CLI.

**Topics**
+ [Elastic Beanstalk Docker platform branches](docker-platform.md)
+ [Using the Elastic Beanstalk Docker platform branch](docker.md)
+ [Using the ECS managed Docker platform branch in Elastic Beanstalk](create_deploy_docker_ecs.md)
+ [Authenticating with image repositories](docker-configuration.remote-repo.md)
+ [Configuring Elastic Beanstalk Docker environments](create_deploy_docker.container.console.md)
+ [Legacy platforms](create_deploy_dockerpreconfig-legacy.md)