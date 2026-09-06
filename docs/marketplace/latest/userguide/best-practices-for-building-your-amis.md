

# Best practices for building AMIs for use with AWS Marketplace
<a name="best-practices-for-building-your-amis"></a>

This topic provides best practices and references to help you build Amazon Machine Images (AMIs) for use with AWS Marketplace. AMIs built and submitted to AWS Marketplace must adhere to all AWS Marketplace product policies. For more information, see the following sections.

**Topics**
+ [Securing resell rights](#rights)
+ [Building an AMI](#building-an-ami)
+ [Preparing and securing your AMI for AWS Marketplace](#securing-an-ami)
+ [Scanning your AMI for publishing requirements](#self-service-scanning)
+ [Verifying your software is running on your AWS Marketplace AMI](#verifying-ami-runtime)

## Securing resell rights
<a name="rights"></a>

For non-free Linux distributions, you are responsible for securing resell rights for them with the exception of AWS-provided Amazon Linux, RHEL and SUSE. You don’t need to secure resell rights for Windows AMIs.

## Building an AMI
<a name="building-an-ami"></a>

Use the following guidelines for building AMIs:
+ Ensure that your AMI meets all[AWS Marketplace policies](https://docs.aws.amazon.com/marketplace/latest/userguide/product-and-ami-policies.html).
+ Create your AMI in the US East (N. Virginia) Region. 
+ Create products from existing, well-maintained AMIs backed by Amazon Elastic Block Store (Amazon EBS) with a clearly defined lifecycle provided by trusted, reputable sources such as AWS Marketplace. 
+ Build AMIs using the most up-to-date operating systems, packages, and software. 
+  Ensure that your AMI is based on a public Amazon EC2 AMI, that uses hardware virtual machine (HVM) virtualization and 64-bit architecture.
+ Develop a repeatable process for building, updating, and republishing AMIs. 
+ Use a consistent operating system (OS) user name across all versions and products. The recommended default user names are `ec2-user` for Linux and other Unix-like systems, and `Administrator` for Windows.
+ Before submitting a final AMI to AWS Marketplace publishing, launch and test an instance from your AMI to verify the intended end-user experience. Test all installation methods, features, and performance on this instance.
+ Check port settings as follows:
  + As a [best practice security configuration](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/) against open firewalls, reverse proxies, and SSRF vulnerabilities, the **IMDS support** option must be set to **IMDSv2** only. The following CLI can be used when registering a new AMI at the final build phase: 
    + `aws ec2 register-image --name my-image --root-device-name /dev/xvda --block-device-mappings DeviceName=/dev/xvda,Ebs={SnapshotId=snap-0123456789example} --architecture x86_64 --imds-support v2.0`

For more information about creating an AMI, see the following resources:
+  [Create an Amazon EBS-backed AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html) in the *Amazon EC2 User Guide*
+  [Create an Amazon EC2 AMI using Windows Sysprep](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-create-win-sysprep.html) in the *Amazon EC2 User Guide* 
+  [How do I create an Amazon Machine Image (AMI) from an EBS-backed instance?](https://aws.amazon.com/premiumsupport/knowledge-center/create-ami-ebs-backed/) 
+  [Amazon Linux AMI](https://aws.amazon.com/amazon-linux-ami/) 
+  [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/) and [Instance Types](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/instance-types.html?r=2153) 
+  [Configuring an AMI for IMDS V2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) use by default 

## Preparing and securing your AMI for AWS Marketplace
<a name="securing-an-ami"></a>

We recommend the following guidelines for creating secure AMIs:
+ Use the [Guidelines for Shared Linux AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/building-shared-amis.html) in the *Amazon EC2 User Guide*
+ Architect your AMI to deploy as a minimum installation to reduce the attack surface. Disable or remove unnecessary services and programs. 
+ Whenever possible, use end-to-end encryption for network traffic. For example, use Secure Sockets Layer (SSL) to secure HTTP sessions between you and your buyers. Ensure that your service uses only valid and up-to-date certificates. 
+ When documenting your AMI product, provide security group recommendations for buyers to control inbound traffic access to their instances. Your recommendations should specify the following:
  + The minimum set of ports required for your services to function.
  + The recommended ports and source IP address ranges for administrative access.

  These security group recommendations help buyers implement proper access controls. For more information about how to add a new version to your AMI product, see [Add a new version](single-ami-versions.md#single-ami-adding-version).
+ Consider performing a penetration test against your AWS computing environment at regular intervals, or consider employing a third party to conduct such tests on your behalf. For more information, including a penetration testing request form, see [AWS Penetration Testing](http://aws.amazon.com/security/penetration-testing/). 
+ Be aware of the top 10 vulnerabilities for web applications, and build your applications accordingly. To learn more, see [Open Web Application Security Project (OWASP) - Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/). When new internet vulnerabilities are discovered, promptly update any web applications that ship in your AMI. Examples of resources that include this information are [SecurityFocus](http://www.securityfocus.com/vulnerabilities) and the [NIST National Vulnerability Database](http://nvd.nist.gov/).

For more information related to security, see the following resources:
+  [AWS Cloud Security](http://aws.amazon.com/security/) 
+  [The Center for Internet Security (CIS): Security Benchmarks](http://benchmarks.cisecurity.org/downloads/benchmarks/) 
+  [The Open Web Application Security Project (OWASP): Secure Coding Practices - Quick Reference Guide](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) 
+  [OWASP Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/) 
+  [SANS (SysAdmin, Audit, Networking, and Security) Common Weakness Enumeration (CWE) Top 25 Most Dangerous Software Errors](http://www.sans.org/top25-software-errors/) 
+  [Security Focus](http://www.securityfocus.com/vulnerabilities) 
+  [NIST National Vulnerability Database](http://nvd.nist.gov/) 

## Scanning your AMI for publishing requirements
<a name="self-service-scanning"></a>

To publish your AMI on the AWS Marketplace Catalog, you must complete AMI scanning. AMI scanning checks for unpatched common vulnerabilities and exposures (CVEs) and verifies that your AMI follows security best practices. For more information, refer to [Preparing and securing your AMI for AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/best-practices-for-building-your-amis.html#securing-an-ami)

To initiate a test scan, you must have an existing AMI product. To learn how to create an AMI product, see [Creating AMI-based products](ami-single-ami-products.md). 

To perform AMI scanning:

1. From the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/homepage), navigate to the **Products** menu and choose **Server**. 

1. Select your product from **Server products**. This must be an AMI-based product. The product can be in any state and does not need to be in the **Public** published state for next steps.

1. Navigate to the **Request changes** menu and select **Update versions**. 

1. Select **Test ‘Add version’**. Follow the prompts to submit a request with your AMI details. If the request succeeds, this indicates that the AMI has passed scanning successfully. Unlike the **Add new version** option, **Test 'add version'** does not add a new version to the AMI-based product if the scan is successful.

**Note**  
To learn about giving AWS Marketplace access to your AMI, see [Giving AWS Marketplace access to your AMI](single-ami-marketplace-ami-access.md).

## Verifying your software is running on your AWS Marketplace AMI
<a name="verifying-ami-runtime"></a>

We strongly recommend that your software verify at runtime that it is running on an Amazon EC2 instance created from your AMI product.

To verify the Amazon EC2 instance is created from your AMI product, use the instance metadata service built into Amazon EC2. The following steps take you through this validation. For more information about using the metadata service, see [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon Elastic Compute Cloud User Guide*.

1. *Obtain the instance identity document*

   Each running instance has an identity document accessible from the instance that provides data about the instance itself. The following example shows using curl from the instance to retrieve the instance identity document.

   IMDSv2: (Recommended)

   ```
   TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
   && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/document
    {
      "accountId" : "0123456789",
      "architecture" : "x86_64",
      "availabilityZone" : "us-east-1e",
      "billingProducts" : null,
      "devpayProductCodes" : null,
      "marketplaceProductCodes" : [ "0vg0000000000000000000000" ],
      "imageId" : "ami-0123456789abcdef1",
      "instanceId" : "i-0123456789abcdef0",
      "instanceType" : "t2.medium",
      "kernelId" : null,
      "pendingTime" : "2020-02-25T20:23:14Z",
      "privateIp" : "10.0.0.2",
      "ramdiskId" : null,
      "region" : "us-east-1",
      "version" : "2017-09-30"
   }
   ```

   IMDSv1:

   ```
   curl http://169.254.169.254/latest/dynamic/instance-identity/document{
      "accountId" : "0123456789",
      "architecture" : "x86_64",
      "availabilityZone" : "us-east-1e",
      "billingProducts" : null,
      "devpayProductCodes" : null,
      "marketplaceProductCodes" : [ "0vg0000000000000000000000" ],
      "imageId" : "ami-0123456789abcdef1",
      "instanceId" : "i-0123456789abcdef0",
      "instanceType" : "t2.medium",
      "kernelId" : null,
      "pendingTime" : "2020-02-25T20:23:14Z",
      "privateIp" : "10.0.0.2",
      "ramdiskId" : null,
      "region" : "us-east-1",
      "version" : "2017-09-30"
   }
   ```

1. *Verify the instance identity document*

   You can verify that the instance identity is correct using the signature. For details about this process, see [ Instance identity documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html) in the *Amazon Elastic Compute Cloud User guide*.

1. *Verify the product code*

   When you initially submit your AMI product for publishing, your product is assigned a [product code](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-getting-started.html#ami-product-codes) by AWS Marketplace. You can verify the product code by checking the `marketplaceProductCodes` field in the instance identity document, or you can get it directly from the metadata service:

   IMDSv2:

   ```
   TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
    && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/product-codes
   ```

   If the product code matches the one for your AMI product, then the instance was created from your product.