# Application configuration parameters

AWS Resilience Hub provides an input mechanism to gather additional information about the resources
associated with your applications. With this information, AWS Resilience Hub will gain a deeper
understanding of your resources and provide better resiliency recommendations.

The **Application configuration parameters** section lists all the
configuration parameters of your cross-Region failover support for AWS Elastic Disaster Recovery. You can
identify the configuration parameters by the following:

- **Topic** – Indicates the area of your application that is
  configured. For example, failover configuration.
- **Purpose** – Indicates the reason why AWS Resilience Hub requested
  the information.
- **Parameter** – Indicates the details that are specific to
  the area of application, which AWS Resilience Hub will be using to provide recommendations
  for your application. Currently, this parameter uses a key-value of only one
  failover Region and one associated account.
