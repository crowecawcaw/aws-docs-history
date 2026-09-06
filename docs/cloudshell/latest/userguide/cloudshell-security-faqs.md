

# AWS CloudShell Security FAQs
<a name="cloudshell-security-faqs"></a>

The following are answers to frequently asked questions about security for CloudShell.
+ [What AWS processes and technologies are used when you launch CloudShell and start a shell session?](#access-path-login-faq)
+ [Is it possible to restrict network access to CloudShell?](#restrict-access-iam-faq)
+ [Can I customize my CloudShell environment?](#customize-faq)
+ [Where is my `$HOME` directory actually stored in the AWS Cloud?](#home-storage-faq)
+ [Is it possible to encrypt my `$HOME` directory?](#encrypt-home-faq)
+ [Can I run a virus scan on my `$HOME` directory?](#virus-scan-faq)
+ [Can I restrict a CloudShell user from root access within the container?](#restrict-root-access-faq)

## What AWS processes and technologies are used when you launch CloudShell and start a shell session?
<a name="access-path-login-faq"></a>

When signing into AWS Management Console, you enter your IAM user credentials. And, when you launch CloudShell from the console interface, these credentials are used in calls to the CloudShell API that create a compute environment for the service. An AWS Systems Manager session is then created for the compute environment, and CloudShell sends commands to that session.

[Back to list of security FAQs](#cloudshell-security-faqs)

## Is it possible to restrict network access to CloudShell?
<a name="restrict-access-iam-faq"></a>

For public environments, it is not possible to restrict network access. If you want to restrict network access, you must enable permission to create only VPC environments and deny creation of public environments.

For more information, see [Ensure that users create only VPC environments and deny creation of public environments](sec-auth-with-identities.md#permission-to-create-VPC-env-only-example).

For CloudShell VPC environments, network settings are inherited from your VPC. Using CloudShell in a VPC enables you to control your CloudShell VPC environment’s network access. 

[Back to list of security FAQs](#cloudshell-security-faqs)

## Can I customize my CloudShell environment?
<a name="customize-faq"></a>

You can download and install utilities and other third-party software for your CloudShell environment. Only software that's installed in your `$HOME` directory is persisted between sessions.

As defined by the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), you are responsible for the necessary configuration and management of applications that you install.

[Back to list of security FAQs](#cloudshell-security-faqs)

## Where is my `$HOME` directory actually stored in the AWS Cloud?
<a name="home-storage-faq"></a>

For Public environments, the infrastructure for storing data in your `$HOME` is provided by Amazon S3.

For VPC environments, your `$HOME` directory is deleted when your VPC environment times out, or when you delete or restart your environment. Environments time out after 20–30 minutes of inactivity. In AWS GovCloud (US) Regions, environments time out after 10 minutes of inactivity. 

[Back to list of security FAQs](#cloudshell-security-faqs)

## Is it possible to encrypt my `$HOME` directory?
<a name="encrypt-home-faq"></a>

No, it is not possible to encrypt your `$HOME` directory with your own key. But CloudShell encrypts your `$HOME` directory content while storing it in Amazon S3.

[Back to list of security FAQs](#cloudshell-security-faqs)

## Can I run a virus scan on my `$HOME` directory?
<a name="virus-scan-faq"></a>

At present, it's not possible to run a virus scan of your `$HOME` directory. Support for this feature is under review.

[Back to list of security FAQs](#cloudshell-security-faqs)

## Can I restrict data ingress or egress for my CloudShell?
<a name="restrict-data-ingress-egress-faq"></a>

To restrict ingress or egress, we recommend that you use a CloudShell VPC environment. The `$HOME` directory of a VPC environment is deleted when your VPC environment times out, or when you delete or restart your environment. Environments time out after 20–30 minutes of inactivity. In AWS GovCloud (US) Regions, environments time out after 10 minutes of inactivity. In the **Actions** menu, the upload and download options are not available for VPC environments.

[Back to list of security FAQs](#cloudshell-security-faqs)

## Can I restrict a CloudShell user from root access within the container?
<a name="restrict-root-access-faq"></a>

No. AWS CloudShell provides root access within the compute container by design. Containers in CloudShell serve as a code packaging and operational convenience. They are not security boundaries.

CloudShell manages access control through AWS Identity and Access Management (IAM). Each CloudShell session receives temporary, regularly-rotated IAM credentials scoped to the user's permissions. These credentials are the security boundary, not the container itself.

Because the container and the underlying instance share the same IAM credential scope, access beyond the container boundary provides no additional AWS permissions.

[Back to list of security FAQs](#cloudshell-security-faqs)