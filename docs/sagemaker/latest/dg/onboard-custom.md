# Use custom setup for Amazon SageMaker AI

The **Set up for organizations** (custom setup) guides you through an
advanced setup for your Amazon SageMaker AI domain. This option provides information and recommendations to
help you understand and control all aspects of the account configuration, including permissions,
integrations, and encryption. Use this option if you want to set up a custom domain. For
information about domains, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

###### Topics

- [Authentication methods](#onboard-custom-authentication-details "#onboard-custom-authentication-details")
- [Setup for organizations (custom setup)](#onboard-custom-instructions "#onboard-custom-instructions")
- [Access the domain after
  onboarding](#onboard-custom-users-accesss-domain "#onboard-custom-users-accesss-domain")

## Authentication methods

Before you set up the domain consider the authentication methods for your users to access
the domain.

**AWS Identity Center**:

- **Helps simplify administration of access permissions to groups of
  users.** You can grant or deny permissions to groups of users, instead of applying
  those permissions to each individual user. If a user moves to a different organization, you can
  move that user to a different AWS Identity and Access Management Identity center (AWS IAM Identity Center) group. The user then
  automatically receives the permissions that are needed for the new organization.

Note that the IAM Identity Center needs to be in the same AWS Region as the domain.

To set up with IAM Identity Center, use the following instructions from the _AWS IAM Identity Center User
Guide_:

    + Begin with [Enabling
     AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md").
    + [Create a
     permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") that follows the best practice of applying least-privilege
     permissions.
    + [Add
     groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") to your IAM Identity Center directory.
    + [Assign single sign-on
     access](../../../singlesignon/latest/userguide/useraccess.md#assignusers "../../../singlesignon/latest/userguide/useraccess.md#assignusers") to users and groups.
    + View the basic workflows to [get started with common tasks in
     IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md").

- The users in IAM Identity Center can access the domain using an AWS access portal URL that is emailed
  to them. The email provides instructions to create an account to access the domain. For
  more information, see [Sign in to the
  AWS access portal](../../../singlesignon/latest/userguide/howtosignin.md "../../../singlesignon/latest/userguide/howtosignin.md").

As an administrator you can find the AWS access portal URL by navigating to the [IAM Identity Center](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon") and finding the **AWS access portal
URL** under **Settings summary**.

- Your domain must use AWS Identity and Access Management (IAM) authentication if you wish to restrict access to
  your domains exclusively to particular Amazon Virtual Private Clouds (VPCs), interface endpoints, or a
  predefined set of IP addresses. This feature is not supported for domains that use IAM Identity Center
  authentication. You can still use IAM Identity Center to enable centralized workforce identity control. For
  instructions on how to implement these restrictions while keeping IAM Identity Center to provide a consistent
  user sign-in experience, see [Secure access to Amazon SageMaker Studio Classic with IAM Identity Center and a SAML application](https://aws.amazon.com/blogs/machine-learning/secure-access-to-amazon-sagemaker-studio-with-aws-sso-and-a-saml-application/ "https://aws.amazon.com/blogs/machine-learning/secure-access-to-amazon-sagemaker-studio-with-aws-sso-and-a-saml-application/") in the _AWS machine learning blog_. Note that AWS SSO is IAM Identity Center in this
  blog.

**Login through IAM**:

- The user profiles can access the domain through the SageMaker AI console after logging into
  the account.
- You can restrict access to your domains exclusively to particular Amazon Virtual Private Clouds
  (VPCs), interface endpoints, or a predefined set of IP addresses when using AWS Identity and Access Management
  (IAM) authentication. For more information, see [Allow Access Only from Within Your
  VPC](studio-interface-endpoint.md#studio-private-link-restrict "studio-interface-endpoint.md#studio-private-link-restrict").

## Setup for organizations (custom setup)

After satisfying the prerequisites in [Complete Amazon SageMaker AI prerequisites](gs-set-up.md "gs-set-up.md"), open the **Set up SageMaker AI Domain** (custom setup) page and expand the
following sections for information on the setup.

###### Open the **Set up SageMaker AI Domain** from the SageMaker AI console

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations** to expand
   the options.
3. Under **Admin configurations**, choose
   **Domains**.
4. From the **Domains** page, choose **Create
   domain**.
5. On the **Set up SageMaker AI domain** page, choose **Set up for
   organizations**.
6. Choose **Set up**.
   Once you opened the **Set up SageMaker AI Domain** page, use the following
   instructions:

7. For **Domain name**, enter a unique name for your domain. For
   example, this can be your project or team name.
8. Choose **Next**.
   In this step you set up the authentication method, users, and permissions for your
   domain.

9. Under **How do you want to access Studio?**, you can choose one
   of two options. For information on the authentication methods, see [Authentication methods](#onboard-custom-authentication-details "#onboard-custom-authentication-details"). Details on the options are
   provided in the following:
   - **AWS Identity Center**:

   Under **Who will use Studio?** choose an AWS IAM Identity Center group that will
   access the domain.

   If you choose **No Identity Center user group** you create a
   domain with no users. You can add IAM Identity Center groups to the domain after the domain's
   creation. For more information, see [Edit domain settings](domain-edit.md "domain-edit.md").
   - **Login through IAM**:

   Under **Who will use Studio?** choose **+ Add
   user**, enter a new user profile name, and choose **Add** to
   create and add a user profile name.

   You can repeat this process to create multiple user profiles.

10. Under **Who will use Studio?** select the IAM Identity Center users or groups, then
    choose **Select**. You need to set up Amazon SageMaker Studio within the same
    Region in which your IAM Identity Center is configured. You can change the Region of your domain by
    choosing the Region from the dropdown list on the top right of the console or you can
    change your IAM Identity Center Region by navigating to the [AWS access portal](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
11. Under **What ML activities do they perform?** you can use an existing
    role by choosing **Use an existing role** or you can create a new role by
    choosing **Create a new role** and checking the ML activities you want the
    role to have access.
12. While selecting ML activities, you may need to satisfy requirements. To satisfy a
    requirement, choose **Add** and complete the requirement.
13. After all requirements are satisfied, choose **Next**.
    In this step, you can configure the applications you have enabled in the previous step.
    For more information on the ML activities, see [ML activity reference](role-manager-ml-activities.md "role-manager-ml-activities.md").

If the application has not been enabled, you receive a warning for that application. To
enable an application that has not been enabled, return to the previous step by choosing
**Back** and follow the previous instructions.

- **Studio** configuration:

Under **Studio**, you have the option to choose between the
newer and classic version of Studio as your default experience. This means choosing
which ML environment you interact with when you open Studio.

    + **Studio** includes multiple integrated development
     environments (IDEs) and applications, including Amazon SageMaker Studio Classic. If chosen, the Studio Classic
     IDE has default settings. For information on the default settings, see [Default settings](onboard-quick-start.md#onboard-quick-start-defaults "onboard-quick-start.md#onboard-quick-start-defaults").


    For information on Studio, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").
    + **Studio Classic** includes the Jupyter IDE. If chosen, you may
     configure your Studio Classic configuration.


    For information on Studio Classic, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

- **SageMaker Canvas** configuration:

If you have Amazon SageMaker Canvas enabled, see [Getting started with using Amazon SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md") for the instructions and configuration details
for onboarding.

- **Studio Classic** configuration:

If you chose **Studio** (recommended) as your default
experience, the Studio Classic IDE has default settings. For information on the default
settings, see [Default settings](onboard-quick-start.md#onboard-quick-start-defaults "onboard-quick-start.md#onboard-quick-start-defaults").

If you chose Studio Classic as your default experience, you can choose to enable or
disable notebook resource sharing. Notebook resources include artifacts such as cell output
and Git repositories. For more information on Notebook resources, see [Share and Use an Amazon SageMaker Studio Classic Notebook](notebooks-sharing.md "notebooks-sharing.md").

If you enabled notebook resource sharing:

    1. Under **S3 location for shareable notebook resources**, input your
     Amazon S3 location.
    2. Under **Encryption key - *optional***, leave as **No Custom Encryption** or
     choose an existing AWS KMS key or choose **Enter a KMS key ARN** and enter
     your AWS KMS key's ARN.
    3. Under **Notebook cell output sharing preference**, choose
     **Allow users to share cell output** or **Disable cell output
     sharing**.

- **RStudio** configuration:

To enable RStudio, you need an RStudio license. To set that up, see [Get an RStudio license](rstudio-license.md "rstudio-license.md").

    1. Under **RStudio Workbench**, verify that your RStudio license is
     automatically detected. For more information about getting an RStudio license and
     activating it with SageMaker AI, see [Get an RStudio license](rstudio-license.md "rstudio-license.md").
    2. Select an instance type to launch your RStudio Server on. For more information, see
     [RStudioServerPro instance type](rstudio-select-instance.md "rstudio-select-instance.md").
    3. Under **Permission**, create your role or select an existing role.
     The role must have the following permissions policy. This policy allows the
     RStudioServerPro application to access necessary resources. It also allows Amazon SageMaker AI to
     automatically launch an RStudioServerPro application when the existing RStudioServerPro
     application is in a `Deleted` or `Failed` status. For information
     about adding permissions to a role, see [Modifying a role permissions policy (console)](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy").



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "VisualEditor0",
     "Effect": "Allow",
     "Action": [
     "license-manager:ExtendLicenseConsumption",
     "license-manager:ListReceivedLicenses",
     "license-manager:GetLicense",
     "license-manager:CheckoutLicense",
     "license-manager:CheckInLicense",
     "logs:CreateLogDelivery",
     "logs:CreateLogGroup",
     "logs:CreateLogStream",
     "logs:DeleteLogDelivery",
     "logs:Describe*",
     "logs:GetLogDelivery",
     "logs:GetLogEvents",
     "logs:ListLogDeliveries",
     "logs:PutLogEvents",
     "logs:PutResourcePolicy",
     "logs:UpdateLogDelivery",
     "sagemaker:CreateApp"
     ],
     "Resource": "*"
     }
     ]
    }`

    ```
    4. Under **RStudio Connect**, add the URL for your RStudio Connect
     server. RStudio Connect is a publishing platform for Shiny applications, R Markdown
     reports, dashboards, plots, and more. When you onboard to RStudio on SageMaker AI, an RStudio
     Connect server is not created. For more information, see [Add an RStudio Connect URL](rstudio-configure-connect.md "rstudio-configure-connect.md").
    5. Under **RStudio Package Manager**, add the URL for your RStudio
     Package Manager. SageMaker AI creates a default package repository for the Package Manager when
     you onboard RStudio. For more information about RStudio Package Manager, see [Update the RStudio Package Manager URL](rstudio-configure-pm.md "rstudio-configure-pm.md").
    6. Select **Next**.

- **Code Editor** configuration:

If you have Code Editor enabled, see [Code Editor in Amazon SageMaker Studio](code-editor.md "code-editor.md") for an overview and the configuration details.
In this section you can customize the viewable applications and machine learning (ML)
tools displayed in Studio. This customization only hides the applications and ML tools
in the left navigation pane in Studio. For information on the Studio UI, see [Amazon SageMaker Studio UI overview](studio-updated-ui.md "studio-updated-ui.md").

For information about the applications, see [Applications supported in Amazon SageMaker Studio](studio-updated-apps.md "studio-updated-apps.md").

The customize Studio UI feature is not available in Studio Classic. If you wish to set
Studio as your default experience, choose **Previous** and to return to
the previous step.

1. On the **Customize Studio UI** page you can hide applications
   and ML tools displayed in Studio by toggling them off.
2. Once you have reviewed your changes, choose **Next**.
   Choose how you want Studio to connect to other AWS services.

You can choose to disable internet access to your Studio by specifying using
**Virtual Private Cloud (VPC) Only** network access type. If you choose
this option, you cannot run a Studio notebook unless your VPC has an interface endpoint
to the SageMaker API and runtime, or a Network Address Translation (NAT) gateway with internet
access, and your security groups allow outbound connections. For more information on Amazon VPCs,
see [Choose an Amazon VPC](onboard-vpc.md "onboard-vpc.md").

If you choose Virtual Private Cloud (VPC) Only the following steps are required. If you
choose **Public internet access**, the first two of the following steps are
required.

1. Under **VPC**, choose the Amazon VPC ID.
2. Under **Subnet**, choose one or more subnets. If you don't choose any
   subnets, SageMaker AI uses all the subnets in the Amazon VPC. We recommend that you use multiple subnets
   that are not created in constrained Availability Zones. Using subnets in these constrained
   Availability Zones can result in insufficient capacity errors and longer application
   creation times. For more information about constrained Availability Zones, see [Availability Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones").
3. Under **Security group(s)**, choose one or more subnets.
   If **VPC only** is selected, SageMaker AI automatically applies the security
   group settings defined for the domain to all shared spaces created in the domain. If
   **Public internet only** is selected, SageMaker AI does not apply the security
   group settings to shared spaces created in the domain.

You have the option to encrypt your data. The [Amazon Elastic File System (Amazon EFS)](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md") and [Amazon Elastic Block Store (Amazon EBS)](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md") file systems that are
created for you when you create a domain. Amazon EBS sizes are used by both Code Editor and
JupyterLab spaces.

You cannot change the encryption key after you encrypt your Amazon EFS and Amazon EBS file
systems. To encrypt your Amazon EFS and Amazon EBS file systems, you can use the following
configurations.

- Under **Encryption key - _optional_**, leave as **No Custom Encryption** or
  choose an existing KMS key or choose **Enter a KMS key ARN** and enter
  the ARN of your KMS key.
- Under **Default space size - _optional_**, enter the default space size.
- Under **Maximum space size - _optional_**, enter the maximum space size.
  Review your domain settings. If you need to change the settings, choose
  **Edit** next to the relevant step. Once you confirm that your domain
  settings are accurate, choose **Submit** and the domain is created for
  you. This process may take a few minutes.

The following sections provide AWS CLI instructions for the custom setup your domain
using the IAM Identity Center or IAM authentication methods.

After satisfying the prerequisites, including setting up your AWS CLI credentials, in [Complete Amazon SageMaker AI prerequisites](gs-set-up.md "gs-set-up.md"), use the following the steps.

1. Create an execution role that is used to create a domain and attach the [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess") policy. You can also use an existing role that has, at a
   minimum, an attached trust policy that grants SageMaker AI permission to assume the role. For more
   information, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").

```
aws iam create-role --role-name `execution-role-name` --assume-role-policy-document `file://execution-role-trust-policy.json`
aws iam attach-role-policy --role-name `execution-role-name` --policy-arn arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
```

2. Get the default Amazon Virtual Private Cloud (Amazon VPC) of your account.

```
aws --region `region` ec2 describe-vpcs --filters Name=isDefault,Values=true --query "Vpcs[0].VpcId" --output text
```

3. Get the list of subnets in the default Amazon VPC.

```
aws --region `region` ec2 describe-subnets --filters Name=vpc-id,Values=`default-vpc-id` --query "Subnets[*].SubnetId" --output json
```

4. Create a domain by passing the default Amazon VPC ID, subnets, and execution role ARN.
   You must also pass a SageMaker image ARN. For information on the available JupyterLab version
   ARNs, see [Setting a default JupyterLab
   version](studio-jl.md#studio-jl-set "studio-jl.md#studio-jl-set").

For `authentication-mode`, use `SSO`
for IAM Identity Center authentication or `IAM` for IAM authentication.

```
aws --region `region` sagemaker create-domain --domain-name `domain-name` --vpc-id `default-vpc-id` --subnet-ids `subnet-ids` --auth-mode `authentication-mode` --default-user-settings "ExecutionRole=arn:aws:iam::`account-number`:role/`execution-role-name`,JupyterServerAppSettings={DefaultResourceSpec={InstanceType=system,SageMakerImageArn=`image-arn`}}" \ --query DomainArn --output text
```

You can use the AWS CLI to customize the applications and ML tools displayed in
Studio for the domain, using [StudioWebPortalSettings](../APIReference/API_StudioWebPortalSettings.md "../APIReference/API_StudioWebPortalSettings.md"). Use `HiddenAppTypes` to hide applications and
`HiddenMlTools` to hide ML tools. For more information on customizing the left
navigation of the Studio UI, see [Hide machine learning tools and
applications in the Amazon SageMaker Studio UI](studio-updated-ui-customize-tools-apps.md "studio-updated-ui-customize-tools-apps.md"). This feature is not available for
Studio Classic. 5. Verify that the domain has been created.

```
aws --region `region` sagemaker list-domains
```

For information about creating a domain using AWS CloudFormation, see [AWS::SageMaker::Domain](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.md") in the _AWS CloudFormation User
Guide._

For an example of an AWS CloudFormation template that you can use to set up your domain, see
[Creating Amazon SageMaker AI domains using AWS CloudFormation](https://github.com/aws-samples/cloudformation-studio-domain "https://github.com/aws-samples/cloudformation-studio-domain") in the `aws-samples` GitHub repository.

After the domain is set up, the administrative user can view and edit the domain.
For information, see [View domains](domain-view.md "domain-view.md") and
[Edit domain settings](domain-edit.md "domain-edit.md").

## Access the domain after

onboarding

The users can access SageMaker AI using:

- The sign-in URL if the domain was set up using the IAM Identity Center authentication. For
  information, see [How to sign in to the user
  portal](../../../singlesignon/latest/userguide/howtosignin.md "../../../singlesignon/latest/userguide/howtosignin.md").
- The [SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
