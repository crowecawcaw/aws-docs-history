

# Beanstalk Standard
<a name="beanstalk-standard"></a>

Deploy your application to a managed platform on Amazon Elastic Compute Cloud (Amazon EC2) instances that Elastic Beanstalk provisions and operates.

With Beanstalk Standard, you choose a managed platform for your language runtime or Docker application and provide your application source. Elastic Beanstalk provisions the Amazon EC2 instances and other resources in your AWS account, configures load balancing and capacity scaling, applies platform updates, and monitors environment health through [Enhanced health reporting and monitoring](health-enhanced.md).

A Beanstalk Standard environment can use the web server tier to serve client requests or the worker tier to process background tasks from an Amazon SQS queue. For web applications, you can start with a single instance or use a load-balanced, scalable environment. See [Elastic Beanstalk worker environments](using-features-managing-env-tiers.md) and [Environment types](using-features-managing-env-types.md).

**Topics**
+ [Next steps](#beanstalk-standard-next-steps)
+ [Managing Beanstalk Standard environments](managing-standard-environments.md)
+ [Configuring Beanstalk Standard environments](configuring-standard-environments.md)
+ [Monitoring Beanstalk Standard environments](monitoring-standard-environments.md)
+ [Elastic Beanstalk platforms](concepts-all-platforms.md)
+ [Using the EB CLI with AWS CodeBuild](eb-cli-codebuild.md)
+ [Elastic Beanstalk Service roles, instance profiles, and user policies](concepts-roles.md)

## Next steps
<a name="beanstalk-standard-next-steps"></a>

Review the available [Platforms](concepts-all-platforms.md) and select the language or container topic in this part for platform-specific deployment guidance. To deploy a sample application to a Beanstalk Standard environment, follow [Getting started tutorial](GettingStarted.md). To use the container and Amazon EKS model instead, start with [Beanstalk Cluster](beanstalk-cluster.md).