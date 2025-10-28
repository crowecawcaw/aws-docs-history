# Accessing an Amazon S3 general purpose bucket

You can access your Amazon S3 general purpose buckets by using the Amazon S3 console, AWS Command Line Interface, AWS SDKs, or the
Amazon S3 REST API. Each method of accessing an S3 general purpose bucket supports specific use cases. For
more information, see the following sections.

###### Topics

- [Use cases](#accessing-use-cases "#accessing-use-cases")
- [Amazon S3 console](#accessing-aws-management-console "#accessing-aws-management-console")
- [AWS CLI](#accessing-aws-cli "#accessing-aws-cli")
- [AWS SDKs](#accessing-aws-sdks "#accessing-aws-sdks")
- [Amazon S3 REST API](#AccessingUsingRESTAPI "#AccessingUsingRESTAPI")

### Use cases

Depending on the use case for your Amazon S3 general purpose bucket, there are different recommended
methods to access the underlying data in your buckets. The following list includes
common use cases for accessing your data.

- **Static websites** – You can use Amazon S3 to
  host a static website. In this use case, you can configure your S3 general purpose bucket to
  function like a website. For an example that walks you through the steps of
  hosting a website on Amazon S3, see [Tutorial: Configuring a static website on
  Amazon S3](HostingWebsiteOnS3Setup.md "HostingWebsiteOnS3Setup.md").

To host a static website with security settings like Block Public Access
enabled, we recommend using Amazon CloudFront with Origin Access Control (OAC) and
implementing additional security headers, such as HTTPS. For more information,
see [Getting started with a secure static website](../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md "../../../AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.md").

###### Note

Amazon S3 supports both [virtual-hosted–style](VirtualHosting.md#virtual-hosted-style-access "VirtualHosting.md#virtual-hosted-style-access") and [path-style URLs](VirtualHosting.md#path-style-access "VirtualHosting.md#path-style-access") for static website access. Because buckets can be accessed
using path-style and virtual-hosted–style URLs, we recommend that you create
buckets with DNS-compliant bucket names. For more information, see [General purpose bucket quotas, limitations, and restrictions](BucketRestrictions.md "BucketRestrictions.md").

- **Shared datasets** – As you scale on
  Amazon S3, it's common to adopt a multi-tenant model, where you assign different end
  customers or business units to unique prefixes within a shared general purpose bucket. By using
  [Amazon S3 access
  points](access-points.md "access-points.md"), you can divide one large bucket policy into separate,
  discrete access point policies for each application that needs to access the
  shared dataset. This approach makes it simpler to focus on building the right
  access policy for an application without disrupting what any other application
  is doing within the shared dataset. For more information, see [Managing access to shared datasets with access points](access-points.md "access-points.md").
- **High-throughput workloads** – Mountpoint
  for Amazon S3 is a high-throughput open source file client for mounting an Amazon S3
  general purpose bucket as a local file system. With Mountpoint, your applications can access
  objects stored in Amazon S3 through file-system operations, such as open and read.
  Mountpoint automatically translates these operations into S3 object API calls,
  giving your applications access to the elastic storage and throughput of Amazon S3
  through a file interface. For more information, see [Mount an Amazon S3 bucket as a local file system](mountpoint.md "mountpoint.md").
- **Multi-Region applications** – Amazon S3
  Multi-Region Access Points provide a global endpoint that applications can use to fulfill requests
  from S3 general purpose buckets that are located in multiple AWS Regions. You can use Multi-Region Access Points
  to build multi-Region applications with the same architecture that's used in a
  single Region, and then run those applications anywhere in the world. Instead of
  sending requests over the public internet, Multi-Region Access Points provide built-in network
  resilience with acceleration of internet-based requests to Amazon S3. For more
  information, see [Managing multi-Region traffic with Multi-Region Access Points](MultiRegionAccessPoints.md "MultiRegionAccessPoints.md").
- **Secure Shell (SSH) File Transfer Protocol
  (SFTP)** – If you’re trying to securely transfer sensitive
  data over the internet, you can use an SFTP-enabled server with your Amazon S3
  general purpose bucket. AWS SFTP is a network protocol that supports the full security and
  authentication functionality of SSH. With this protocol, you have fine-grained
  control over user identity, permissions, and keys or you can use IAM policies
  to manage access. To associate an SFTP enabled server with your Amazon S3 bucket,
  make sure to create your SFTP-enabled server first. Then, you set up user
  accounts, and associate the server with an Amazon S3 general purpose bucket. For a walkthrough of
  this process, see [AWS Transfer for SFTP – Fully Managed SFTP Service for Amazon S3](https://aws.amazon.com/blogs/aws/new-aws-transfer-for-sftp-fully-managed-sftp-service-for-amazon-s3/ "https://aws.amazon.com/blogs/aws/new-aws-transfer-for-sftp-fully-managed-sftp-service-for-amazon-s3/") in _AWS
  Blogs_.

### Amazon S3 console

The console is a web-based user interface for managing Amazon S3 and AWS resources. With the Amazon S3 console, you can
easily access a bucket and modify the bucket's properties. You can also perform
most bucket operations by using the console UI, without having to write any
code.

If you've signed up for an AWS account, you can access the Amazon S3 console by signing
into the Amazon S3 console and choosing **S3** from the Amazon S3 console home
page. You can also use this link to directly access the [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").

### AWS CLI

You can use the AWS CLI to issue commands or build scripts at
your system's command line to perform AWS (including S3) tasks. For example, if you need to access multiple
buckets, you can save time by using the AWS CLI to automate common and
repetitive tasks. Scriptability and repeatability for common actions are
frequent considerations as organizations scale.

The [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") provides commands
for a broad set of AWS services. The AWS CLI is supported on Windows, macOS, and
Linux. To get started, see the [_AWS Command Line Interface User Guide_](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). For more information about the commands for
Amazon S3, see [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html") and [s3control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html") in the _AWS CLI Command Reference_.

### AWS SDKs

AWS provides SDKs (software development kits) that consist of libraries and sample code
for various programming languages and platforms (Java, Python, Ruby, .NET, iOS,
Android, and so on). The AWS SDKs provide a convenient way to create programmatic
access to S3 and AWS. Amazon S3 is a REST service. You can send requests to Amazon S3 using
the AWS SDK libraries, which wrap the underlying Amazon S3 REST API and simplify your
programming tasks. For example, the SDKs take care of tasks such as calculating
signatures, cryptographically signing requests, managing errors, and retrying
requests automatically. For information about the AWS SDKs, including how to
download and install them, see [Tools for
AWS](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").

Every interaction with Amazon S3 is either authenticated or anonymous. If you are using
the AWS SDKs, the libraries compute the signature for authentication from the keys
that you provide. For more information about how to make requests to Amazon S3, see [Making requests](../API/MakingRequests.md "../API/MakingRequests.md") .

### Amazon S3 REST API

The architecture of Amazon S3 is designed to be programming language-neutral, using
AWS-supported interfaces to store and retrieve objects. You can access S3 and
AWS programmatically by using the Amazon S3 REST API. The REST API is an HTTP interface
to Amazon S3. With the REST API, you use standard HTTP requests to create, fetch, and
delete buckets and objects.

To use the REST API, you can use any toolkit that supports HTTP. You can even use
a browser to fetch objects, as long as they are anonymously readable.

The REST API uses standard HTTP headers and status codes, so that standard
browsers and toolkits work as expected. In some areas, we have added functionality
to HTTP (for example, we added headers to support access control). In these cases,
we have done our best to add the new functionality in a way that matches the style
of standard HTTP usage.

If you make direct REST API calls in your application, you must write the code to
compute the signature and add it to the request. For more information about how to
make requests to Amazon S3, see [Making requests](../API/MakingRequests.md "../API/MakingRequests.md") in the _Amazon S3 API Reference_.
