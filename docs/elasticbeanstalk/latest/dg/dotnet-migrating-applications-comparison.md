

# Comparing migration options: EB CLI vs. AWS Transform MGN
<a name="dotnet-migrating-applications-comparison"></a>

AWS offers multiple paths for migrating Windows applications to the cloud. This section compares two primary options: the **eb migrate** command in the EB CLI and AWS Transform MGN (MGN). Understanding the differences between these approaches will help you choose the most appropriate migration strategy for your specific needs.


**Comparison of migration options**  

| Feature | EB CLI (**eb migrate**) | AWS Transform MGN (MGN) | 
| --- | --- | --- | 
| Primary focus | Application-level migration of IIS websites and applications | Server-level rehosting of entire machines (physical, virtual, or cloud servers) | 
| Best suited for | IIS applications that you want to migrate directly to Elastic Beanstalk with minimal reconfiguration | Large-scale migrations involving many servers or complex infrastructure | 
| Discovery approach | Application-level discovery of IIS sites, applications, and configurations | Server-level replication of entire machines, including operating system and applications | 
| Target environment | Directly creates and configures Elastic Beanstalk environments optimized for Windows applications | Creates EC2 instances that require additional configuration to work with Elastic Beanstalk | 
| Configuration preservation | Automatically preserves IIS-specific configurations (sites, application pools, bindings) | Preserves entire server configuration, which may include unnecessary components | 
| Deployment model | Creates a clean Elastic Beanstalk environment with your applications deployed using Elastic Beanstalk best practices | Creates a replica of your source server that may require optimization for cloud operations | 
| Scale of migration | Ideal for targeted migrations of specific applications | Designed for large-scale migrations of many servers | 
| Post-migration steps | Minimal; environment is ready for use with Elastic Beanstalk management tools | Requires additional steps to integrate with Elastic Beanstalk, such as executing SSM post-launch actions | 

## When to use each migration option
<a name="dotnet-migrating-applications-comparison-when"></a>

**Choose **eb migrate** when you have the following requirements:**  
+ You want to migrate specific IIS applications rather than entire servers
+ Your goal is to adopt Elastic Beanstalk as your application management platform
+ You want to leverage Elastic Beanstalk's managed platform features like easy scaling, deployment, and monitoring
+ You prefer a clean deployment that follows AWS best practices for cloud-native operations
+ You want to minimize post-migration configuration work

**Choose AWS Transform MGN when you have the following requirements:**  
+ You need to migrate a large number of servers
+ You have complex server configurations that must be preserved exactly
+ Your applications have compatibility issues that require maintaining the exact server environment
+ You want to "lift and shift" with minimal changes to your applications
+ You plan to refactor or optimize your applications after migration

## Migration workflow comparison
<a name="dotnet-migrating-applications-comparison-workflow"></a>

**EB CLI (**eb migrate**) workflow:**

1. Install the EB CLI on either your source IIS server or a bastion host.

1. Run **eb migrate** to discover IIS applications.

1. The command packages your applications and configurations.

1. An Elastic Beanstalk environment is created with appropriate resources.

1. Your applications are deployed to the new environment.

1. You can immediately manage your applications using Elastic Beanstalk tools.

**AWS Transform MGN workflow:**

1. Install the AWS Replication Agent on source servers.

1. Configure and test data replication.

1. Launch test instances to verify functionality.

1. Schedule cutover to AWS.

1. Launch production instances.

1. Execute post-launch actions to optimize for cloud.

1. If Elastic Beanstalk is the target platform, additional configuration is required to integrate with Elastic Beanstalk.

## Conclusion
<a name="dotnet-migrating-applications-comparison-conclusion"></a>

Elastic Beanstalk is the preferred destination for Windows platform applications on AWS, offering a managed environment that simplifies deployment, scaling, and management. The **eb migrate** command provides a direct path to Elastic Beanstalk for IIS applications, with automatic discovery and configuration that preserves your application settings.

While AWS Transform MGN offers powerful capabilities for large-scale server migrations, it requires additional steps to integrate with Elastic Beanstalk. For most IIS application migrations where Elastic Beanstalk is the target platform, **eb migrate** offers a more streamlined approach that aligns with Elastic Beanstalk's managed service model.

Choose the migration approach that best fits your specific requirements, considering factors such as scale, complexity, and your desired end-state architecture on AWS.

For more information about AWS Transform MGN, see [What is AWS Transform MGN?](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) in the AWS Transform MGN User Guide.