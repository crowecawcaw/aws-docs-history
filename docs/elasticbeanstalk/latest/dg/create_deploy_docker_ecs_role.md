# Container managed policy and EC2 instance role

When you create an environment in the Elastic Beanstalk console, it prompts you to create a default instance profile that includes the
`AWSElasticBeanstalkMulticontainerDocker` managed policy. So initially, your default EC2 instance profile, should include this
managed policy. If your environment uses a custom EC2 instance profile role instead of the default, make sure that the managed policy
`AWSElasticBeanstalkMulticontainerDocker` is attached so the required permissions for container management stay up-to-date.

Elastic Beanstalk uses an Amazon ECS-optimized AMI with an Amazon ECS container agent that runs in a Docker container. The agent communicates with Amazon ECS to coordinate
container deployments. In order to communicate with Amazon ECS, each Amazon EC2 instance must have the corresponding IAM permissions, which are specified in this
managed policy. See the [AWSElasticBeanstalkMulticontainerDocker](../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkMulticontainerDocker.md "../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkMulticontainerDocker.md") in the _AWS Managed Policy Reference Guide_ to view these permissions.

If you use Elastic Beanstalk environment variables that are configured to access secrets or parameters that are stored in AWS Secrets Manager or AWS Systems Manager Parameter Store,
you must customize your EC2 instance profile with additional permissions. For more information, see [Execution Role ARN format](create_deploy_docker_v2config.md#create_deploy_docker_v2config_executionRoleArn_format "create_deploy_docker_v2config.md#create_deploy_docker_v2config_executionRoleArn_format").
