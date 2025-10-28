# Use AMS SSP to provision Amazon ECS on AWS Fargate in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon ECS on AWS Fargate capabilities directly in your AMS managed account. AWS Fargate is a technology that you can use with Amazon ECS to run containers
(see [Containers on AWS](https://aws.amazon.com/what-are-containers "https://aws.amazon.com/what-are-containers")) without having
to manage servers or clusters of Amazon EC2 instances. With AWS Fargate, you no longer have to
provision, configure, or scale, clusters of virtual machines to run containers. This removes the
need to choose server types, decide when to scale your clusters, or optimize cluster packing.

To learn more, see
[Amazon ECS on AWS Fargate](../../../AmazonECS/latest/developerguide/AWS_Fargate.md "../../../AmazonECS/latest/developerguide/AWS_Fargate.md").

## Amazon ECS on Fargate in AWS Managed Services FAQ

**Q: How do I request access to Amazon ECS on Fargate in my AMS account?**

Request access to Amazon ECS on Fargate by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM roles to your account:
`customer_ecs_fargate_console_role` (if no existing IAM role is provided to
associate the ECS policy to), `customer_ecs_fargate_events_service_role`,
`customer_ecs_task_execution_service_role`,
`customer_ecs_codedeploy_service_role`, and
`AWSServiceRoleForApplicationAutoScaling_ECSService`.
Once provisioned in your account, you must onboard the roles in your federation solution.

**Q: What are the restrictions to using Amazon ECS on Fargate in my AMS account?**

- Amazon ECS task monitoring and logging are considered your responsibility
  since container level activities occur above the hypervisor, and logging capabilities
  are limited by Amazon ECS on Fargate. As a user of Amazon ECS on Fargate, we recommend that you
  take the necessary steps to enable logging on your Amazon ECS tasks. For more information, see
  [Enabling the awslogs Log Driver for Your Containers](../../../AmazonECS/latest/developerguide/using_awslogs.md#enable_awslogs "../../../AmazonECS/latest/developerguide/using_awslogs.md#enable_awslogs").
- Security and malware protection at the container level are also considered
  to be your responsibility. Amazon ECS on Fargate doesn't include Trend Micro or preconfigured
  network security components.
- This service is available for both multi-account landing zone and single-account landing zone AMS accounts.
- Amazon ECS
  [Service Discovery](../../../AmazonECS/latest/developerguide/service-discovery.md "../../../AmazonECS/latest/developerguide/service-discovery.md") is restricted
  by default in the self-provisioned role since elevated permissions are required to create Route 53 private hosted zones. To enable
  Service Discovery on a service, submit a Management | Other | Other | Update change type. To provide the information required to
  enable Service Discovery for your Amazon ECS Service, see the
  [Service Discovery manual](../../../AmazonECS/latest/developerguide/service-discovery.md "../../../AmazonECS/latest/developerguide/service-discovery.md").
- AMS does not currently manage or restrict images used to deploy to containers onto Amazon ECS Fargate. You will be able to
  deploy images from Amazon ECR, Docker Hub, or any other private image repository. Therefore, we advised
  that public or any unsecured images not be deployed, since they may result in malicious activity on the account.

**Q: What are the prerequisites or dependencies to using Amazon ECS on Fargate in my
AMS account?**

- The following are dependencies of Amazon ECS on Fargate; however, no additional action is required to
  enable these services with your self-provisioned role:
  - CloudWatch logs
  - CloudWatch events
  - CloudWatch alarms
  - CodeDeploy
  - App Mesh
  - Cloud Map
  - Route 53

- Depending on your use case, the following are resources that Amazon ECS
  relies on, and may require prior to using Amazon ECS on Fargate in your account:
  - Security group to be used with the Amazon ECS service. You can use the
    Deployment | Advanced stack components | Security Group | Create (auto) (ct-3pc215bnwb6p7), or,
    if your security group requires special rules, use
    Deployment | Advanced stack components | Security Group | Create (managed automation)
    (ct-1oxx2g2d7hc90). Note: The security group your select with Amazon ECS has to be
    created specifically for Amazon ECS where the Amazon ECS service or cluster reside.
    You can learn more in the **Security Group** section at
    [Setting Up with Amazon ECS](../../../AmazonECS/latest/developerguide/get-set-up-for-amazon-ecs.md "../../../AmazonECS/latest/developerguide/get-set-up-for-amazon-ecs.md") and
    [Security in Amazon Elastic Container Service](../../../AmazonECS/latest/developerguide/security.md "../../../AmazonECS/latest/developerguide/security.md").
  - Application load balancer (ALB), network load balancer (NLB), classic load balancer (ELB) for load balancing between tasks.
  - Target Groups for ALBs.
  - App mesh resources (for instance, Virtual Routers, Virtual Services, Virtual Nodes) to
    integrate with your Amazon ECS Cluster.

- Currently, there is no way for AMS to automatically mitigate risk associated with supporting
  security groups' permissions when created outside of the standard
  AMS change types. We recommend that you request a specific
  security group for use with your Fargate cluster to limit the
  possibility of using a security group not designated for the use
  with Amazon ECS.
