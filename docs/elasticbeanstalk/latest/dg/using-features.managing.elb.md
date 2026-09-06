

# Load balancer for your Elastic Beanstalk environment
<a name="using-features.managing.elb"></a>

A load balancer distributes traffic among your environment's instances. When you [enable load balancing](using-features-managing-env-types.md#using-features.managing.changetype), AWS Elastic Beanstalk creates an [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/) load balancer dedicated to your environment. Elastic Beanstalk fully manages this load balancer, taking care of security settings and of terminating the load balancer when you terminate your environment.

Alternatively, you can choose to share a load balancer across several Elastic Beanstalk environments. With a shared load balancer, you save on operational cost by avoiding a dedicated load balancer for each environment. You also assume more of the management responsibility for the shared load balancer that your environments use.

Elastic Load Balancing has these load balancer types:
+ [Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/) – The previous-generation load balancer. Routes HTTP, HTTPS, or TCP request traffic to different ports on environment instances.
+ [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) – An application layer load balancer. Routes HTTP or HTTPS request traffic to different ports on environment instances based on the request path.
+ [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/) – A network layer load balancer. Routes TCP or TLS request traffic to different ports on environment instances. Supports both active and passive health checks.

Elastic Beanstalk supports all three load balancer types. The following table shows which types you can use with the two usage patterns:


| Load balancer type | Dedicated | Shared | 
| --- | --- | --- | 
| Classic Load Balancer |  ![](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/icon-no.png) No | 
| Application Load Balancer |  ![](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/icon-yes.png) Yes | 
| Network Load Balancer |  ![](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/icon-no.png) No | 

**Note**  
The Classic Load Balancer (CLB) option is disabled on the **Create Environment** console wizard. If you have an existing environment configured with a Classic Load Balancer you can create a new one by [cloning the existing environment](using-features.managing.clone.md) using either the Elastic Beanstalk console or the [EB CLI](using-features.managing.clone.md#using-features.managing.clone.CLI). You also have the option to use the EB CLI or the [AWS CLI](environments-create-awscli.md) to create a new environment configured with a Classic Load Balancer. These command line tools will create a new environment with a CLB even if one doesn’t already exist in your account. 

By default, Elastic Beanstalk creates an Application Load Balancer for your environment when you enable load balancing with the Elastic Beanstalk console or the EB CLI. It configures the load balancer to listen for HTTP traffic on port 80 and forward this traffic to instances on the same port. You can choose the type of load balancer that your environment uses only during environment creation. Later, you can change settings to manage the behavior of your running environment's load balancer, but you can't change its type.

**Note**  
Your environment must be in a VPC with subnets in at least two Availability Zones to create an Application Load Balancer. All new AWS accounts include default VPCs that meet this requirement. 

See the following topics to learn about each load balancer type that Elastic Beanstalk supports, its functionality, how to configure and manage it in an Elastic Beanstalk environment, and how to configure a load balancer to [upload access logs](environments-cfg-loadbalancer-accesslogs.md) to Amazon S3. 

**Topics**
+ [Configuring a Classic Load Balancer](environments-cfg-clb.md)
+ [Configuring an Application Load Balancer](environments-cfg-alb.md)
+ [Configuring a shared Application Load Balancer](environments-cfg-alb-shared.md)
+ [Configuring a Network Load Balancer](environments-cfg-nlb.md)
+ [Configuring dual-stack Elastic Beanstalk load balancers](environments-cfg-elbv2-ipv6-dualstack.md)
+ [Configuring access logs](environments-cfg-loadbalancer-accesslogs.md)