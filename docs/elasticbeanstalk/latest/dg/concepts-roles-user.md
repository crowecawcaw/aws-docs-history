# Elastic Beanstalk user policy

Create IAM users for each user who uses Elastic Beanstalk to avoid using your root account or
sharing credentials. As a security best practice, only grant these users permissions to access
services and features that they need.

Elastic Beanstalk requires permissions not only for its own API actions, but also for several other
AWS services. Elastic Beanstalk uses user permissions to launch resources in an environment. These
resources include EC2 instances, an ELB load balancer, and an Amazon EC2 Auto Scaling group. Elastic Beanstalk also uses
user permissions to save logs and templates to Amazon Simple Storage Service (Amazon S3), send notifications to Amazon SNS,
assign instance profiles, and publish metrics to CloudWatch. Elastic Beanstalk requires CloudFormation permissions to
orchestrate resource deployments and updates. It also requires Amazon RDS permissions to create
databases when needed, and Amazon SQS permissions to create queues for worker environments.

For more information about user policies, see [Managing Elastic Beanstalk user policies](AWSHowTo.iam.md "AWSHowTo.iam.md").
