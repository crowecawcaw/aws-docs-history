# What is the Render Farm Deployment Kit on AWS?

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

The Render Farm Deployment Kit (RFDK) on AWS is an open-source software development kit that can be used to deploy, configure, and manage your render farm infrastructure in the cloud.
The RFDK is built to operate with the [AWS Cloud Development Kit (CDK)](../../../cdk/latest/guide/home.md "../../../cdk/latest/guide/home.md") and provides a library of classes, called constructs,
that each deploy and configure a component of your cloud-based render farm. The current version of the RFDK supports render farms built using
[AWS Thinkbox Deadline](https://www.awsthinkbox.com/deadline "https://www.awsthinkbox.com/deadline") render management software, and provides the ability for you to easily go from nothing to a production-ready render
farm in the cloud.

You can model, deploy, configure, and update your AWS render farm infrastructure by writing an application for the
[CDK toolkit](../../../cdk/latest/guide/cli.md "../../../cdk/latest/guide/cli.md") using the libraries provided by the CDK and RFDK together and with other CDK-compatible libraries.
The RFDK supports applications written in either [Python](https://www.python.org/ "https://www.python.org/") or [Node.js](https://nodejs.org/en/ "https://nodejs.org/en/").
Your application is written in an object-oriented style where creation of an object from the CDK and RFDK libraries represents the creation of a resource, or collection of
resources, in your AWS account when the CDK toolkit deploys your application with [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md").
The parameters of an object’s creation control the configuration of the resource.

## Why use the RFDK?

With the RFDK, you can easily model the cloud components of your render farm as object-oriented code. This gives you the benefits of infrastructure as code:

- **Visibility**: Your render farm infrastructure is available as an easy-to-understand application that makes it easy for anyone on your team to see and understand what has been deployed.
- **Stability**: Combining infrastructure as code with version control, like git, makes accidental errors, like an incorrect setting, harder to make and easier to recover from.
- **Scalability**: Your application can be deployed repeatedly within the same region, in other regions, or even in other AWS accounts. This means that once you have modeled your render farm using the RFDK then you can create as many exact copies of that render farm as you need and be sure that they have all been created to your specifications.
- **Security**: The RFDK and CDK are built with security as a top priority so that your render farm is built on a secure foundation. Each component’s configuration can be customized to meet your organizations security requirements. If you create one well secured render farm using the RFDK then you can reuse it and know that every deployed version is meeting the same security requirements.

To use the RFDK to create the components of your cloud render farm, you will write simple and easy to understand code like in the example shown below. Creating an equivalent AWS CloudFormation template directly would require provisioning and correctly configuring 106 separate resources of 42 different types; the resulting template would be around three thousand lines long.

Python

```
# A simple AWS CloudFormation stack that creates a bare-bones infrastructure with
# AWS Thinkbox Deadline installed, configured, and ready to perform renders.
class BareBonesDeadlineRenderFarm(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # A Virutal Private Cloud (VPC) is a logically isolated section of the
        # AWS Cloud. To deploy a VPC, you create an instance of the CDK's Vpc
        # that uses two availability zones (AZs).
        vpc = ec2.Vpc(self, "Vpc", max_azs=2)

        # Specify version of AWS Thinkbox Deadline to use
        version = rfdk_deadline.VersionQuery(self, "Version",
            version=`"10.2.0"`,
        )

        # Use AWS Thinkbox published Deadline container images for specified Deadline version
        images = rfdk_deadline.ThinkboxDockerImages(self, 'Images',
            version=version,
            # The ThinkboxDockerImages will install Deadline onto one or more EC2 instances.
            # By downloading or using the Deadline software, you agree to the AWS Customer Agreement (https://aws.amazon.com/agreement/)
            # and AWS Intellectual Property License (https://aws.amazon.com/legal/aws-ip-license-terms/). You acknowledge that Deadline
            # is AWS Content as defined in those Agreements.
            # Please set the user_aws_customer_agreement_and_ip_license_acceptance property to
            # USER_ACCEPTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE to signify your acceptance of these terms.
            user_aws_customer_agreement_and_ip_license_acceptance=rfdk_deadline.AwsCustomerAgreementAndIpLicenseAcceptance.`USER_REJECTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE`
        )

        # To operate Deadline you will need a backing-store for Deadline files
        # and scheduling data. You create one by creating an instance of the
        # RFDK's Repository. This will deploy an Amazon DocumentDB and
        # AWS Elastic File System (EFS), in private subnets, and run the
        # Deadline Repository installer to initialize them both.
        repository = rfdk_deadline.Repository(self, 'Repository',
            vpc=vpc,
            version=version,
            # Allow resources to be deleted when we delete the sample
            removal_policy=rfdk_deadline.RepositoryRemovalPolicies(
                database=cdk.RemovalPolicy.DESTROY,
                filesystem=cdk.RemovalPolicy.DESTROY
            )
        )

        # To create the server to which all Deadline client applications (like
        # the Worker or artist's Monitor) connect you create an instance
        # of the RFDK's RenderQueue. This will create an Amazon ECS, running
        # the Deadline Remote Connection Server (RCS), running behind behind
        # an Application Load Balancer. All Deadline client connections
        # are made with this load balancer.
        render_queue = rfdk_deadline.RenderQueue(self, 'RenderQueue',
            vpc=vpc,
            version=version,
            images=images.for_render_queue(),
            repository=repository,
            # Allow the load-balancer to be deleted when we delete the sample
            deletion_protection=False,
        )

        # To create a collection of Workers you create an instance of the
        # RFDK's WorkerInstanceFleet. This creates an AWS Auto Scaling Group,
        # in the VPC's private subnets, of EC2-Spot instances that are running
        # the Deadline Client.
        # Note: You must currently set the fleet's desired capacity manually.
        # Note2: You can create as many instances of WorkerInstanceFleet as you like.
        workers = rfdk_deadline.WorkerInstanceFleet(self, 'Workers',
          vpc=vpc,
          render_queue=render_queue,
          worker_machine_image=ec2.MachineImage.generic_linux({
              # Fill in your AMI id here
              f"{cdk.Stack.of(self).region}": `"ami-00000000000000000"`
          }),
          min_capacity=5,
          instance_type=ec2.InstanceType("c5.large"),
          spot_price=0.08
        )

        # You can create a filesystem to hold your render assets for the
        # workers in many ways. Here, to create an Amazon Elastic File
        # System (EFS) you create an instance of the CDK's FileSystem.
        asset_filesystem = efs.FileSystem(self, 'RenderAssets',
            vpc=vpc,
            encrypted=True,
            # Allow filesystem to be deleted when we delete the sample
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        # Finally, you mount that asset filesystem onto your Linux Workers
        # when they are launched by using the RFDK's MountableEfs helper-class.
        rfdk_core.MountableEfs(self,
            filesystem=asset_filesystem
        ).mount_to_linux_instance(workers.fleet, location="/mnt/assets")
```

TypeScript

```
// A simple CloudFormation stack that creates a bare-bones infrastructure with
// AWS Thinkbox Deadline installed, configured, and ready to perform renders.
export class BareBonesDeadlineRenderFarm extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // A Virutal Private Cloud (VPC) is a logically isolated section of the
    // AWS Cloud. To deploy a VPC, you create an instance of the CDK's Vpc
    // that uses two availability zones (AZs).
    const vpc = new ec2.Vpc(this, 'Vpc', { maxAzs: 2 });

    // Specify version of AWS Thinkbox Deadline to use
    const version = rfdkDeadline.VersionQuery(this, 'Version', {
      version: `'10.2.0'`,
    });

    // Use AWS Thinkbox published Deadline container images for specified Deadline version
    const images = new rfdkDeadline.ThinkboxDockerImages(this, 'Images', {
      version,
      /**
       * The ThinkboxDockerImages will install Deadline onto one or more EC2 instances.
       * By downloading or using the Deadline software, you agree to the AWS Customer Agreement (https://aws.amazon.com/agreement/)
       * and AWS Intellectual Property License (https://aws.amazon.com/legal/aws-ip-license-terms/). You acknowledge that Deadline
       * is AWS Content as defined in those Agreements.
       * Please set the userAwsCustomerAgreementAndIpLicenseAcceptance property to
       * USER_ACCEPTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE to signify your acceptance of these terms.
       */
      userAwsCustomerAgreementAndIpLicenseAcceptance: rfdkDeadline.AwsCustomerAgreementAndIpLicenseAcceptance.`USER_REJECTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE`,
    });

    // To operate Deadline you will need a backing-store for Deadline files
    // and scheduling data. You create one by creating an instance of the
    // RFDK's Repository. This will deploy an Amazon DocumentDB and
    // AWS Elastic File System (EFS), in private subnets, and run the
    // Deadline Repository installer to initialize them both.
    const repository = new rfdkDeadline.Repository(this, 'Repository', {
      vpc,
      version,
      // Allow resources to be deleted when we delete the sample
      removalPolicy: {
        database: cdk.RemovalPolicy.DESTROY,
        filesystem: cdk.RemovalPolicy.DESTROY
      },
    });

    // To create the server to which all Deadline client applications (like
    // the Worker or artist's Monitor) connect you create an instance
    // of the RFDK's RenderQueue. This will create an Amazon ECS, running
    // the Deadline Remote Connection Server (RCS), running behind behind
    // an Application Load Balancer. All Deadline client connections
    // are made with this load balancer.
    const renderQueue = new rfdkDeadline.RenderQueue(this, 'RenderQueue', {
      vpc,
      version,
      images.forRenderQueue(),
      repository,
      // Allow the load-balancer to be deleted when we delete the sample
      deletionProtection: false,
    });

    // To create a collection of Workers you create an instance of the
    // RFDK's WorkerInstanceFleet. This creates an AWS Auto Scaling Group,
    // in the VPC's private subnets, of EC2-Spot instances that are running
    // the Deadline Client.
    // Note: You must currently set the fleet's desired capacity manually.
    // Note2: You can create as many instances of WorkerInstanceFleet as you like.
    const workers = new rfdkDeadline.WorkerInstanceFleet(this, 'Workers', {
      vpc,
      renderQueue,
      workerMachineImage: ec2.MachineImage.genericLinux({
        // Fill in your AMI id here
        [cdk.Stack.of(this).region]: 'ami-00000000000000000',
      }),
      minCapacity: 5,
      instanceType: new ec2.InstanceType('c5.large'),
      spotPrice: 0.08,
    });

    // You can create a filesystem to hold your render assets for the
    // workers in many ways. Here, to create an Amazon Elastic File
    // System (EFS) you create an instance of the CDK's FileSystem.
    const assetFilesystem = new efs.FileSystem(this, 'RenderAssets', {
      vpc,
      encrypted: true,
      // Allow filesystem to be deleted when we delete the sample
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Finally, you mount that asset filesystem onto your Linux Workers
    // when they are launched by using the RFDK's MountableEfs helper-class.
    const mountableEfs = new rfdk_core.MountableEfs(this, {
      filesystem: assetFilesystem,
    });
    mountableEfs.mountToLinuxInstance(workers.fleet, { location: '/mnt/assets' });
  }
}
```

## Where can I get the RFDK?

The RFDK is available today on:

- The official RFDK GitHub — https://github.com/aws/aws-rfdk  — contributions welcome!
- [pypi.org](http://pypi.org/ "http://pypi.org/") for Python developers to use via pip — https://pypi.org/project/aws-rfdk
- [npmjs.org](http://npmjs.org/ "http://npmjs.org/") for Node.js developers to use via npm — https://www.npmjs.com/package/aws-rfdk

## Additional documentation and resources

- [RFDK API Reference](../../api/latest.md "../../api/latest.md")
- [RFDK on GitHub](https://github.com/aws/aws-rfdk "https://github.com/aws/aws-rfdk")
  - [Issues](https://github.com/aws/aws-rfdk/issues "https://github.com/aws/aws-rfdk/issues")
  - [Example applications](https://github.com/aws/aws-rfdk/tree/mainline/examples "https://github.com/aws/aws-rfdk/tree/mainline/examples")
  - [License](https://github.com/aws/aws-rfdk/blob/mainline/LICENSE "https://github.com/aws/aws-rfdk/blob/mainline/LICENSE")
  - [Releases](https://github.com/aws/aws-rfdk/releases "https://github.com/aws/aws-rfdk/releases")

- [CDK Workshop](https://cdkworkshop.com/ "https://cdkworkshop.com/")
- [CDK User Guide](../../../cdk/latest/guide/home.md "../../../cdk/latest/guide/home.md")
- [CDK API Reference](../../../cdk/api/latest/docs/aws-construct-library.md "../../../cdk/api/latest/docs/aws-construct-library.md")
- [CloudFormation Documentation](../../../cloudformation/index.md "../../../cloudformation/index.md")
- [Deadline Documentation](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html")

## About Amazon Web Services

Amazon Web Services (AWS) is a collection of digital infrastructure services that developers can use when developing their applications. The services include computing, storage, database, and application synchronization (messaging and queuing).

AWS uses a pay-as-you-go service model. You are charged only for the services that you — or your applications — use. Also, to make AWS useful as a platform for prototyping and experimentation, AWS offers a free usage tier, in which services are free below a certain level of usage. For more information about AWS costs and the free usage tier, see [Test-Driving AWS in the Free Usage Tier](../../../awsaccountbilling/latest/aboutv2/billing-free-tier.md "../../../awsaccountbilling/latest/aboutv2/billing-free-tier.md").

To obtain an AWS account, go to [aws.amazon.com](https://aws.amazon.com/ "https://aws.amazon.com/"), and then choose **Create an AWS Account**.
