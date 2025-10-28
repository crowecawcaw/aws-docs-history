# Using multiple Elastic Load Balancing listeners

You can configure multiple Elastic Load Balancing listeners on a ECS managed Docker environment in order to support inbound traffic for proxies or other services that
don't run on the default HTTP port.

Create a `.ebextensions` folder in your source bundle and add a file with a `.config` file extension. The
following example shows a configuration file that creates an Elastic Load Balancing listener on port 8080.

**`.ebextensions/elb-listener.config`**

```
option_settings:
  aws:elb:listener:8080:
    ListenerProtocol: HTTP
    InstanceProtocol: HTTP
    InstancePort: 8080
```

If your environment is running in a custom [Amazon Virtual Private Cloud](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") (Amazon VPC) that you created, Elastic Beanstalk takes care of the rest. In a
default VPC, you need to configure your instance's security group to allow ingress from the load balancer. Add a second configuration file that adds an
ingress rule to the security group:

**`.ebextensions/elb-ingress.config`**

```
Resources:
  port8080SecurityGroupIngress:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      GroupId: {"Fn::GetAtt" : ["AWSEBSecurityGroup", "GroupId"]}
      IpProtocol: tcp
      ToPort: 8080
      FromPort: 8080
      SourceSecurityGroupName: { "Fn::GetAtt": ["AWSEBLoadBalancer", "SourceSecurityGroup.GroupName"] }
```

For more information on the configuration file format, see [Adding and customizing Elastic Beanstalk environment resources](environment-resources.md "environment-resources.md") and [Option settings](ebextensions-optionsettings.md "ebextensions-optionsettings.md").

In addition to adding a listener to the Elastic Load Balancing configuration and opening a port in the security group, you need to map the port on the host instance
to a port on the Docker container in the `containerDefinitions` section of the `Dockerrun.aws.json` v2 file. The following
excerpt shows an example:

```
"portMappings": [
  {
    "hostPort": 8080,
    "containerPort": 8080
  }
]
```

See [Dockerrun.aws.json v2](create_deploy_docker_v2config.md#create_deploy_docker_v2config_dockerrun "create_deploy_docker_v2config.md#create_deploy_docker_v2config_dockerrun") for details about the
`Dockerrun.aws.json` v2 file format.
