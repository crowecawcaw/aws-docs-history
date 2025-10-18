# AWS CloudShell Security FAQs

The following are
 answers
 to frequently asked questions about security for
 CloudShell.


* [What
 AWS
 processes and
 technologies
 are used when you launch CloudShell and start a shell session?](#access-path-login-faq "#access-path-login-faq")
* [Is it possible to restrict network access to
 CloudShell?](#restrict-access-iam-faq "#restrict-access-iam-faq")
* [Can I customize my CloudShell environment?](#customize-faq "#customize-faq")
* [Where is my $HOME directory actually
 stored in the AWS Cloud?](#home-storage-faq "#home-storage-faq")
* [Is it possible to encrypt my $HOME
 directory?](#encrypt-home-faq "#encrypt-home-faq")
* [Can I run a virus scan on my $HOME
 directory?](#virus-scan-faq "#virus-scan-faq")

## What
 AWS
 processes and
 technologies
 are used when you launch CloudShell and start a shell session?


When signing into AWS Management Console, you enter your IAM user credentials. And, when you launch
 CloudShell from the console interface, these credentials are used in calls to the
 CloudShell API that create a compute environment for the service. An AWS Systems Manager session is then created for
 the compute environment, and CloudShell sends commands to that session.


[Back to list of security FAQs](cloudshell-security-faqs.md "cloudshell-security-faqs.md")


## Is it possible to restrict network access to
 CloudShell?


For public environments, it is not possible to restrict network access. If you want to
 restrict network access, you must enable permission to create only VPC environments and deny
 creation of public environments.


For more information, see [Ensure that users create only
 VPC environments and deny creation of public environments](sec-auth-with-identities.md#permission-to-create-VPC-env-only-example "sec-auth-with-identities.md#permission-to-create-VPC-env-only-example").


For CloudShell VPC environments, network settings are inherited from your VPC. Using
 CloudShell in a VPC enables you to control your CloudShell VPC environment’s network
 access. 


[Back to list of security FAQs](cloudshell-security-faqs.md "cloudshell-security-faqs.md")


## Can I customize my CloudShell environment?


You can download and install utilities and other third-party software for your
 CloudShell environment. Only software that's installed in your `$HOME`
 directory is persisted between sessions.


As defined by the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), you are responsible for the necessary
 configuration and management of applications that you install.


[Back to list of security FAQs](cloudshell-security-faqs.md "cloudshell-security-faqs.md")


## Where is my `$HOME` directory actually
 stored in the AWS Cloud?


For Public environments, the infrastructure for storing data in your
 `$HOME` is provided by Amazon S3.


For VPC environments, your `$HOME` directory is deleted when your VPC
 environment times out (after 20-30 minutes of inactivity), or when you delete or restart your
 environment. 


[Back to list of security FAQs](cloudshell-security-faqs.md "cloudshell-security-faqs.md")


## Is it possible to encrypt my `$HOME`
 directory?


No, it is not possible to encrypt your `$HOME` directory with your own
 key. But CloudShell encrypts your `$HOME` directory content while
 storing it in Amazon S3.


[Back to list of security FAQs](cloudshell-security-faqs.md "cloudshell-security-faqs.md")


## Can I run a virus scan on my `$HOME`
 directory?


At present, it's not possible to run a virus scan of your `$HOME`
 directory. Support for this feature is under review.


[Back to list of security FAQs](cloudshell-security-faqs.md "cloudshell-security-faqs.md")


## Can I restrict data ingress or egress for
 my CloudShell?


To restrict ingress or egress, we recommend that you use a CloudShell VPC environment.
 The `$HOME` directory of a VPC environment is deleted when your VPC
 environment times out (after 20-30 minutes of inactivity), or when you delete or restart your
 environment. In the **Actions** menu, the upload and download options are not
 available for VPC environments.


[Back to list of security FAQs](cloudshell-security-faqs.md "cloudshell-security-faqs.md")
