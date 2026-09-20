

# Your AWS Elastic Beanstalk environment security
<a name="using-features.managing.security"></a>

Elastic Beanstalk uses AWS Identity and Access Management (IAM) roles to act on your behalf and to control what the compute running your application can access. The specific roles and settings depend on your environment's mode.
+ With **Beanstalk Standard**, you configure a service role and an Amazon EC2 instance profile. See [Configuring service access for a Beanstalk Standard environment](configuring-standard-service-access.md) and [Elastic Beanstalk Service roles, instance profiles, and user policies](concepts-roles.md).
+ With **Beanstalk Cluster**, you provide the IAM roles that the Amazon EKS cluster and its nodes use. See [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md).