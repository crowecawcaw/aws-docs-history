# Use load balancing to distribute Amazon ECS service traffic

Your service can optionally be configured to use Elastic Load Balancing to distribute traffic evenly across
the tasks in your service.

###### Note

When you use tasks sets, all the tasks in the set must all be configured to use Elastic Load Balancing
or to not use Elastic Load Balancing.

Amazon ECS services hosted on AWS Fargate support the Application Load Balancers, Network Load Balancers, and Gateway Load Balancers. Use the
following table to learn about what type of load balancer to use.

| Load Balancer type        | Use in these cases                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application Load Balancer | Route HTTP/HTTPS (or layer 7) traffic.Application Load Balancers offer several features<br>that make them attractive for use with Amazon ECS services:<br>• Each service can serve traffic from multiple load balancers<br>and expose multiple load balanced ports by specifying multiple<br>target groups.<br>• They are supported by tasks hosted on both<br>Fargate and EC2 instances.<br>• Application Load Balancers allow containers to use dynamic host port mapping (so<br>that multiple tasks from the same service are allowed per<br>container instance).<br>• Application Load Balancers support path-based routing and priority rules (so that<br>multiple services can use the same listener port on a single<br>Application Load Balancer). |
| Network Load Balancer     | Route TCP or UDP (or layer 4) traffic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Gateway Load Balancer     | Route TCP or UDP (or layer 4) traffic. Use virtual appliances, such<br>as firewalls, intrusion detection and prevention systems, and deep<br>packet inspection systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

We recommend that you use Application Load Balancers for your Amazon ECS services so that you can take advantage of
these latest features, unless your service requires a feature that is only available with
Network Load Balancers or Gateway Load Balancers. For more information about Elastic Load Balancing and the differences between the load
balancer types, see the [Elastic Load Balancing User Guide](../../../elasticloadbalancing/latest/userguide.md "../../../elasticloadbalancing/latest/userguide.md").

With your load balancer, you pay only for what you use. For more information, see [Elastic Load Balancing
pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").
