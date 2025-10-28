# Security best practices for the RFDK

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

## Secure the CDK bootstrap AWS S3 bucket

The CDK provides an [assets](../../../cdk/latest/guide/assets.md "../../../cdk/latest/guide/assets.md") feature that can be used to upload files from the machine performing the CDK deployment to an
S3 bucket prior to executing a CloudFormation deployments. This bucket is referred to as the **CDK bootstrap bucket**, and has many important uses. The RFDK makes use of CDK assets
to provide scripts that are run when instances launch and to provide code for AWS Lambda.

It is important to secure access to the CDK bootstrap bucket. Any modification to the objects stored in the CDK bootstrap bucket by malicious actors could cause arbitrary remote
code execution which could cause data loss, disruption to the render farm, or leaking of confidential assets.

It is recommended that write access to the bucket be restricted to the IAM user that is used to perform the deployments of your RFDK application.

If you plan to use multiple CDK applications within the same AWS account and region, then you should consider creating a separate CDK bootstrap bucket using:

```
cdk bootstrap --bootstrap-bucket-name my-bootstrap-bucket-name
```

If doing so, you will also need to modify **cdk.json** in the root of your CDK application with
(see the [CDK docs](https://github.com/aws/aws-cdk/tree/master/packages/aws-cdk#json-configuration-files "https://github.com/aws/aws-cdk/tree/master/packages/aws-cdk#json-configuration-files")):

```
{
  // ...
  "toolkitBucketName": "my-bootstrap-bucket-name",
  // ...
}
```

## Deploying Components into Dedicated Subnets

We highly recommend creating dedicated subnets for each component in your farm (e.g. `RenderQueue`, `WorkerInstanceFleet`, `SpotEventPluginFleet`, etc.) as it is considered best practice and has security benefits for your farm:

- Finer-grained control of inbound/outbound subnet traffic to each component with [Network ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md")
- The IP addresses of instances deployed into a component’s subnet are guaranteed to be within the subnet’s CIDR block. This is especially important if you are using
  [Deadline Secrets Management in the RFDK](deadline-secrets-management-rfdk.md "deadline-secrets-management-rfdk.md").

The following example creates a dedicated subnet group for the `RenderQueue` to use for its Application Load balancer. You can follow this pattern for other components in your farm.

Python

```
vpc = Vpc(self, 'Vpc',
  # ...
  subnet_configuration=[
    # ...

    # Provide a subnet configuration for the Render Queue subnet group
    SubnetConfiguration(
      name='RenderQueueSubnets',
      subnet_type=SubnetType.PRIVATE,
      cidr_mask=27,
    ),

    # ...
  ],
  # ...
)

# ...

render_queue = RenderQueue(self, 'RenderQueue',
  # ...
  vpc=self.vpc,

  # Select the dedicated Render Queue subnets to put the ALB in
  vpc_subnets_alb=SubnetSelection(subnet_group_name='RenderQueueSubnets'),

  # ...
)
```

TypeScript

```
const vpc = new Vpc(this, 'Vpc', {
  // ...
  subnetConfiguration: [
    // ...

    // Provide a subnet configuration for the Render Queue subnet group
    {
      name: 'RenderQueueSubnets',
      subnetType: SubnetType.PRIVATE,
      cidrMask: 27,
    },

    // ...
  ],
  // ...
});

// ...

const renderQueue = new RenderQueue(this, 'RenderQueue', {
  // ...
  vpc,

  // Select the dedicated Render Queue subnets to put the ALB in
  vpcSubnetsAlb: { subnetGroupName: 'RenderQueueSubnets' },

  // ...
});
```
