This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Context values

Context values are key-value pairs that can be associated with an app, stack, or
construct. They can be supplied to your app from a file (usually either
`cdk.json` or `cdk.context.json` in your project directory) or on
the command line. CDK uses context values to control the configuration of the
application. Wickr Enterprise uses CDK context values to provide control over
settings such as the domain name of your Wickr Enterprise installation or the number of
days to retain RDS backups.

There are multiple ways to set context values, but we recommend editing the values in
`cdk.context.json` to fit your particular use case. Only context values that
begin with `wickr/` are related to the Wickr Enterprise deployment.

| Name                               | Description                                                                                                                                                                               | Default       |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `wickr/licensePath`                | The path to your KOTS license (a `.yaml` file provided by Wickr).                                                                                                                         | null          |
| `wickr/domainName`                 | The domain name to use for this Wickr Enterprise deployment. If using a Route 53 public hosted zone, DNS records and ACM certificates for this domain name will be automatically created. | null          |
| `wickr/route53:hostedZoneId`       | Route 53 hosted zone ID in which to create DNS records.                                                                                                                                   | null          |
| `wickr/route53:hostedZoneName`     | Route 53 hosted zone Name in which to create DNS records.                                                                                                                                 | null          |
| `wickr/acm:certificateArn`         | ARN of an ACM certificate to use on the Load Balancer. This value must be supplied if a Route 53 public hosted zone is not available in your account.                                     | null          |
| `wickr/caPath`                     | Certificate path, only required when using self-signed certificates.                                                                                                                      | null          |
| `wickr/vpc:id`                     | The ID of the VPC to deploy resources into. Only required when deploying into an existing VPC. If unset, a new VPC will be created.                                                       | null          |
| `wickr/vpc:cidr`                   | IPv4 CIDR to associate with the created VPC. If deploying into an existing VPC, set this to the CIDR of the existing VPC.                                                                 | 172.16.0.0/16 |
| `wickr/vpc:availabilityZones`      | Comma-separated list of availability zones. Only required when deploying into an existing VPC.                                                                                            | null          |
| `wickr/vpc:publicSubnetIds`        | Comma-separated list of public subnet IDs. Only required when deploying into an existing VPC.                                                                                             | null          |
| `wickr/vpc:privateSubnetIds`       | Comma-separated list of private subnet IDs. Only required when deploying into an existing VPC.                                                                                            | null          |
| `wickr/vpc:isolatedSubnetIds`      | Comma-separated list of isolated subnet IDs for the RDS database. Only required when deploying into an existing VPC.                                                                      | null          |
| `wickr/rds:deletionProtection`     | Enable deletion protection on RDS instances.                                                                                                                                              | true          |
| `wickr/rds:removalPolicy`          | Removal policy for RDS instances 'snapshot', 'destroy', or 'retain.'                                                                                                                      | snapshot      |
| `wickr/rds:readerCount`            | Number of reader instances to create in the RDS cluster.                                                                                                                                  | 1             |
| `wickr/rds:instanceType`           | Instance type to use for RDS instances.                                                                                                                                                   | r6g.xlarge    |
| `wickr/rds:backupRetentionDays`    | Number of days to retain backups.                                                                                                                                                         | 7             |
| `wickr/eks:namespace`              | Default namespace for Wickr services in EKS.                                                                                                                                              | wickr         |
| `wickr/eks:defaultCapacity`        | Number of EKS worker nodes for Messaging infrastructure.                                                                                                                                  | 3             |
| `wickr/eks:defaultCapacityCalling` | Number of EKS worker nodes for Calling infrastructure.                                                                                                                                    | 2             |
| `wickr/eks:instanceTypes`          | Comma-separated list of instance types to use for Messaging EKS worker nodes.                                                                                                             | m5.xlarge     |
| `wickr/eks:instanceTypesCalling`   | Comma-separated list of instance types to use for Calling EKS worker nodes.                                                                                                               | c5n.large     |
| `wickr/eks:enableAutoscaler`       | Toggles enabling the Cluster Autoscaler functionality for EKS.                                                                                                                            | true          |
| `wickr/s3:expireAfterDays`         | Number of days after which file uploads will be removed from the S3 bucket.                                                                                                               | 1095          |
| `wickr/eks:clusterVersion`         | Cluster versions, including Kubernetes version, kubectlLayer version, albController version, nodeGroupRelease version and more.                                                           | 1.27          |
| `wickr/stackSuffix`                | A suffix to apply to CloudFormation stack names.                                                                                                                                          | "             |
| `wickr/autoDeployWickr`            | Auto deploy the Wickr application with lambda.                                                                                                                                            | true          |
