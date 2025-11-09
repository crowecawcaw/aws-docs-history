# Run builds on reserved capacity fleets

CodeBuild offers the following compute fleets:

- On-demand fleets
- Reserved capacity fleets
  With on-demand fleets, CodeBuild provides compute for your builds.
  The machines are destroyed when the build finishes. On-demand fleets are
  fully managed, and includes automatic scaling capabilities to handle spikes in
  demand.

###### Note

On-demand ﬂeets do not support macOS.

CodeBuild also offers reserved capacity fleets which contain instances powered by Amazon EC2 that
are maintained by CodeBuild. With reserved capacity fleets, you configure a set of dedicated
instances for your build environment. These machines remain idle, ready to process builds or
tests immediately and reduces build durations. With reserved capacity fleets, your machines
are always running and will continue to incur costs as long they're provisioned.

###### Important

Regardless of how long you run an instance for, reserved capacity fleets incur an
initial charge per instance, after which there may be additional associated costs. For
more information, see [https://aws.amazon.com/codebuild/pricing/](https://aws.amazon.com/codebuild/pricing/ "https://aws.amazon.com/codebuild/pricing/").

###### Topics

- [Create a reserved capacity fleet](#fleets.how-to "#fleets.how-to")
- [Best practices](#fleets.best-practices "#fleets.best-practices")
- [Can I share a reserved capacity fleet across multiple
  CodeBuild projects?](#fleets.share "#fleets.share")
- [How does attribute-based compute work?](#fleets.attribute-compute "#fleets.attribute-compute")
- [Can I manually specify an Amazon EC2 instance for my fleet?](#fleets.manual-input-compute "#fleets.manual-input-compute")
- [Which regions support reserved capacity fleets?](#fleets.regions "#fleets.regions")
- [How do I configure a reserved capacity macOS fleet?](#fleets.configure-macos "#fleets.configure-macos")
- [How do I configure a custom Amazon Machine Image (AMI) for a reserved capacity fleet?](#fleets.custom-ami "#fleets.custom-ami")
- [Limitations of reserved capacity fleets](#fleets.limitations "#fleets.limitations")
- [Reserved capacity fleet
  properties](fleets.md "fleets.md")
- [Reserved capacity samples with
  AWS CodeBuild](reserved-capacity-samples.md "reserved-capacity-samples.md")

## Create a reserved capacity fleet

Use the following instructions to create a reserved capacity fleet.

###### To create a reserved capacity fleet

1. Sign in to the AWS Management Console and open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. In the navigation pane, choose **Compute fleets**,
   and then choose **Create Fleet**.
3. In the **Compute fleet name** text field, enter a name for
   your fleet.
4. From the **Operating system** drop-down menu, choose the
   operating system.
5. From the **Architecture** drop-down menu, choose the
   architecture.
6. (Optional) Select **Use instance running mode - optional** to
   run on an Amazon EC2 instance directly instead of a Docker container. Then choose a
   **Major version** and **Minor version**.
7. (Optional) In **Additional
   configuration** do the following:
   - Select **Configure VPC - optional** to
     connect your fleet to a VPC to access private resources during usage.
     - From the **VPC** drop-down menu, select a
       VPC that your CodeBuild fleet will access.
     - From the **Subnets** drop-down menu, select the
       subnets that CodeBuild should use to set up your VPC configuration.
     - From the **Security groups** drop-down menu, select
       the security groups that CodeBuild should use to work with your VPC.
     - In the **Fleet Service Role** field, choose an existing service role.

     ###### Note

     Make sure that your fleet role has the necessary permissions. For more information, see
     [Allow a user to add a permission policy for a fleet service role](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-permission-policy-fleet-service-role "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-permission-policy-fleet-service-role").
     - If you chose the Amazon Linux operating system, select **Define proxy configurations - optional** to apply network access control for your reserved capacity instances.
     - For **Default behavior**, choose to allow or deny outgoing traffic to all destinations by default.
     - For **Proxy rules**, choose **Add proxy rule** to specify destination domains or IPs to allow or deny network access control to.

   - Select **Configure custom AMI - optional** to
     use a custom Amazon Machine Image (AMI).
     - From the **AMI** drop-down menu, select a
       an Amazon Machine Image (AMI) for your fleet.
     - In the **Fleet Service Role** field, choose an existing service role.

     ###### Note

     Make sure that your fleet role has the necessary permissions. For more information, see
     [Allow a user to add a permission policy for a fleet service role](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-permission-policy-fleet-service-role "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-permission-policy-fleet-service-role").

8. In **Capacity configuration**, from
   **Compute selection mode**, choose one of the following:
   - If you choose **Guided selection**, do the following:
     - For **Compute**, choose the type of
       instances included in this fleet.
     - In the **Capacity** text field, enter the minimum number of
       instances in the fleet.
     - (Optional) In **Additional
       configuration** do the following:
       - Select **Configure scaling - optional** to
         automatically scale your fleet based on this configuration. From the
         **Scaling mode - optional** drop-down menu,
         choose the behavior when demand exceeds the fleet capacity.

   - If you choose **Custom instance**, do the following:
     - From the **Compute instance type** drop-down menu, select the type of
       instances included in this fleet.
     - In the **Additional EBS volume size - optional** text field,
       enter the volume additional to the 64GB of disk space provided.
     - In the **Capacity** text field, enter the minimum number of
       instances in the fleet.
     - (Optional) In **Additional
       configuration** do the following:
       - Select **Configure scaling - optional** to
         automatically scale your fleet based on this configuration. From the
         **Scaling mode - optional** drop-down menu,
         choose the behavior when demand exceeds the fleet capacity.

9. Choose **Create compute fleet**.
10. After the compute fleet is created, create a new CodeBuild project or edit an
    existing one. From **Environment**, choose **Reserved
    capacity** under **Provisioning model**, and then
    choose the specified fleet under **Fleet name**.

## Best practices

When using reserved capacity fleets, we recommend that you follow these best
practices.

- We recommend using source cache mode to help improve the build performance by
  caching the source.
- We recommend using Docker layer caching to help improve the build performance
  by caching existing Docker layers.

## Can I share a reserved capacity fleet across multiple

CodeBuild projects?

Yes, you can maximize the utilization of a fleet's capacity by using it across
multiple projects.

###### Important

When using the reserved capacity feature, data cached on fleet instances,
including source files, Docker layers, and cached directories specified in the
buildspec, can be accessible to other projects within the same account. This is by
design and allows projects within the same account to share fleet instances.

## How does attribute-based compute work?

If you choose `ATTRIBUTE_BASED_COMPUTE` as your fleet's `computeType`, you can specify
the attributes in a new field called `computeConfiguration`. These attributes include vCPUs,
memory, disk space, and the `machineType`. This `machineType` is either `GENERAL`
or `NVME`. After specifying one or some of the available attributes, CodeBuild will choose a compute type
from the available supported instance types as the finalized `computeConfiguration`.

###### Note

CodeBuild will choose the cheapest instance that match all input requirements. The chosen instances' memory,
vCPUs, and disk space will all be greater than or equal to the input requirements. You can check the resolved
`computeConfiguration` in the created or updated fleet.

If you input a `computeConfiguration` that is not possible to satisfy in CodeBuild, you'll receive a
validation exception. Also note that on-demand fleet overflow behavior will be overridden to queue behavior
if the `computeConfiguration` is not available for on-demand.

## Can I manually specify an Amazon EC2 instance for my fleet?

Yes, you can directly input your desired Amazon EC2 instance in the console by selecting **Custom instance**
or by configuring the API parameter, `InstanceType`. This field is used in the following APIs: CreateFleet,
UpdateFleet, CreateProject, UpdateProject and StartBuild. For more information, see [Compute instance type](fleets.md#compute "fleets.md#compute").

## Which regions support reserved capacity fleets?

Reserved capacity Amazon Linux and Windows fleets are supported in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Mumbai),
Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Frankfurt), Europe (Ireland), and South America (São Paulo). For more information about AWS Regions
where CodeBuild is available, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

Reserved capacity macOS Medium fleets are supported in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney),
and Europe (Frankfurt). Reserved capacity macOS Large fleets are supported in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), and Asia Pacific (Sydney).

## How do I configure a reserved capacity macOS fleet?

###### To configure a reserved capacity macOS fleet

1. Sign in to the AWS Management Console and open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. In the navigation pane, choose **Compute fleets**,
   and then choose **Create Fleet**.
3. In the **Compute fleet name** text field, enter a
   name for your fleet.
4. From the **Operating system** drop-down menu, choose **macOS**.
5. In the **Compute** field, choose one of the following compute machine types: **Apple M2, 24 GB memory, 8 vCPUs**
   or **Apple M2, 32 GB memory, 12 vCPUs**.
6. In the **Capacity** text field, enter the minimum number
   of instances in the fleet.
7. (Optional) To use a custom image for your fleet, see [How do I configure a custom Amazon Machine Image (AMI) for a reserved capacity fleet?](#fleets.custom-ami "#fleets.custom-ami") to ensure that your Amazon Machine Image (AMI) has the required prerequisites.
8. (Optional) To configure a VPC with your fleet, in **Additional configuration** do the
   following:
   - From the **VPC - optional** drop-down menu, select a VPC that your CodeBuild fleet will access.
   - From the **Subnets** drop-down menu, select the subnets that CodeBuild should use to set up your VPC configuration.
   - From the **Security groups** drop-down menu, select the security groups that CodeBuild should use to work with your VPC.
   - In the **Fleet service role** field, choose an existing service role.

   ###### Note

   Make sure that your fleet role has the necessary permissions. For more information, see
   [Allow a user to add a permission policy for a fleet service role](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-permission-policy-fleet-service-role "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-permission-policy-fleet-service-role").

9. Choose **Create compute fleet** and wait for the fleet instance to launch. Once launched the
   capacity will be ``n`/`n``, where `n` is
   the capacity provided.
10. After the compute fleet has launched, create a new CodeBuild project or edit an existing one. From **Environment**, choose
    **Reserved capacity** under **Provisioning model**, and then choose the specified fleet
    under **Fleet name**.

## How do I configure a custom Amazon Machine Image (AMI) for a reserved capacity fleet?

###### To configure a custom Amazon Machine Image (AMI) for a reserved capacity fleet

1. Sign in to the AWS Management Console and open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. In the navigation pane, choose **Compute fleets**,
   and then choose **Create Fleet**.
3. In the **Compute fleet name** text field, enter a
   name for your fleet.
4. Choose **Custom image** for your fleet and ensure that your Amazon Machine Image (AMI) has the following prerequisites:
   - If your environment type is `MAC_ARM`, make sure that your AMI **Architecture** is 64-bit `Mac-Arm`.
   - If your environment type is `LINUX_EC2`, make sure that your AMI **Architecture** is 64-bit `x86`.
   - If your environment type is `ARM_EC2`, make sure that your AMI **Architecture** is 64-bit `Arm`.
   - If your environment type is `WINDOWS_EC2`, make sure that your AMI **Architecture** is 64-bit `x86`.
   - The AMI allows the CodeBuild service **Organization ARN**. For a list of Organization ARNs, see
     [Amazon Machine Images (AMI)](fleets.md#ami "fleets.md#ami").
   - If the AMI is encrypted with a AWS KMS key, the AWS KMS key must also allow the CodeBuild service **Organization ID**.
     For a list of Organization IDs, see [Amazon Machine Images (AMI)](fleets.md#ami "fleets.md#ami").
     For more information on AWS KMS keys, see
     [Allow organizations and OUs to use a KMS key](../../../AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.md#allow-org-ou-to-use-key "../../../AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.md#allow-org-ou-to-use-key") in the _Amazon EC2 User Guide_. To give CodeBuild organization permission
     to use a KMS key, add the following statement to the key policy:

   ```
   {
       "Sid": "Allow access for organization root",
       "Effect": "Allow",
       "Principal": "*",
       "Action": [
           "kms:Describe*",
           "kms:List*",
           "kms:Get*",
           "kms:Encrypt",
           "kms:Decrypt",
           "kms:ReEncrypt*",
           "kms:GenerateDataKey*",
           "kms:CreateGrant"
       ],
       "Resource": "*",
       "Condition": {
           "StringEquals": {
               "aws:PrincipalOrgID": "o-123example"
           }
       }
   }
   ```

   - In the **Fleet service role** field, grant the following Amazon EC2 permissions:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "ec2:DescribeImages",
    "ec2:DescribeSnapshots"
    ],
    "Resource": "*"
    }
    ]
   }`

   ```

## Limitations of reserved capacity fleets

There are some use-cases which reserved capacity fleets do not support, and if they
impact you, use on-demand fleets instead:

- Reserved capacity fleets don't support build utilization
  metrics.
- Reserved capacity macOS fleets don't support debug session.

For more information on limits and quotas, see [Compute fleets](limits.md#fleet-limits "limits.md#fleet-limits").
