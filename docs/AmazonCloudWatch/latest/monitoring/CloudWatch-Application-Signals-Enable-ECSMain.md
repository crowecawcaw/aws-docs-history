# Enable your applications on Amazon ECS

Enable CloudWatch Application Signals on Amazon ECS by using the custom setup steps described in this section.

For applications running on Amazon ECS, you install and configure the CloudWatch agent and AWS Distro for OpenTelemetry yourself. On these architectures enabled with a custom Application Signals setup, Application Signals 
 doesn't autodiscover the names of your services or the hosts or clusters they run on. You must specify these names during the custom setup, and the names that you specify are what is displayed on Application Signals dashboards.


## Use a custom setup to enable Application Signals on Amazon ECS


Use these custom setup instructions to onboard your applications on Amazon ECS to CloudWatch Application Signals. 
 You install and configure the CloudWatch agent and AWS Distro for OpenTelemetry yourself.


There are two methods for deploying Application Signals on Amazon ECS. Choose the one that is best for your
 environment.



* [Deploy using the sidecar strategy](CloudWatch-Application-Signals-ECS-Sidecar.md "CloudWatch-Application-Signals-ECS-Sidecar.md") – You add a CloudWatch agent sidecar container
 to each task definition in the cluster.


Advantages:




	+ Supports both the `ec2` and `Fargate` launch types.
	+ You can always use `localhost` as the IP address when you set up environment variables.
Disadvantages:




	+ You must set up the CloudWatch agent sidecar container for each service task that runs in the cluster.
	+ Only the `awsvpc` network mode is supported.
* [Deploy using the daemon strategy](CloudWatch-Application-Signals-ECS-Daemon.md "CloudWatch-Application-Signals-ECS-Daemon.md") – You add a CloudWatch agent task only once 
 in the cluster, and the [Amazon ECS daemon scheduling strategy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html#service_scheduler_daemon "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html#service_scheduler_daemon") deploys it as needed. The ensures that each instance continuously receives traces and metrics, providing
 centralized visibility without the need for the agent to run as a sidecar with each application task definition.


Advantages:



	+ You need to set up the daemon service for the CloudWatch agent only once in the cluster.
Disadvantages:




	+ Doesn't support the Fargate launch type.
	+ If you use the `awsvpc` or `bridge` network mode, you have to manually 
	 specify each container instance's private IP address in the environment variables.

With either method, on Amazon ECS clusters Application Signals doesn't autodiscover the names of your services. You must 
 specify your service names during the custom setup, and the names that you specify are what is displayed on 
 Application Signals dashboards.
