# How AWS Elastic Beanstalk uses AWS Secrets Manager

With AWS Elastic Beanstalk, you can quickly deploy and manage applications in the AWS Cloud
without having to learn about the infrastructure that runs those applications. Elastic Beanstalk can
launch Docker environments by building an image described in a Dockerfile or pulling a
remote Docker image. To authenticate with the online registry that hosts the private
repository, Elastic Beanstalk uses a Secrets Manager secret. For more information, see [Docker
configuration](../../../elasticbeanstalk/latest/dg/single-container-docker-configuration.md "../../../elasticbeanstalk/latest/dg/single-container-docker-configuration.md") in the _AWS Elastic Beanstalk Developer Guide_.
