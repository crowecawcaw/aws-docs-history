# ADVPERF05-BP03 Use load balancers to improve high availability and load distribution in your workload

Use the load balancing service provided by AWS to enhance the high
availability of applications. In the event of disruptions that cause targets to become unhealthy, load balancers can automatically exclude unhealthy targets from traffic routing.

## Implementation guidance

Elastic Load Balancing (ELB) employs various load balancing
algorithms, such as round-robin, least outstanding requests, or
IP hash, to distribute traffic evenly across healthy targets,
which optimizes resource utilization and prevents overloading of
individual targets. It supports content-based routing, which
routes traffic based on the content of the request, such as the
URL path or headers, efficiently handling different types of
requests. ELB can offload SSL/TLS decryption and encryption from
your targets, reducing the computational overhead on your
application servers and improving overall performance.

## Key AWS services

- [Amazon Elastic
  Load balancer (ELB)](https://aws.amazon.com/elasticloadbalancing/ "https://aws.amazon.com/elasticloadbalancing/")
- [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")

## Resources

- [What's
  the Difference Between Application, Network, and Gateway Load Balancing?](https://aws.amazon.com/compare/the-difference-between-the-difference-between-application-network-and-gateway-load-balancing/ "https://aws.amazon.com/compare/the-difference-between-the-difference-between-application-network-and-gateway-load-balancing/")
- [Monitor
  your Application Load Balancers](../../../elasticloadbalancing/latest/application/load-balancer-monitoring.md "../../../elasticloadbalancing/latest/application/load-balancer-monitoring.md")
- [ELB
  Best Practices Guides](https://aws.github.io/aws-elb-best-practices/ "https://aws.github.io/aws-elb-best-practices/")
