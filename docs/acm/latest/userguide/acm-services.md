# Services integrated with ACM

AWS Certificate Manager supports a growing number of AWS services. You cannot install your ACM
certificate or your private AWS Private CA certificate directly on your AWS based website or
application.

###### Note

Public ACM certificates can be installed on Amazon EC2 instances that are connected to a
[Nitro Enclave](#acm-nitro-enclave "#acm-nitro-enclave"). You can also [export a public certificate](export-public-certificate.md "export-public-certificate.md")
to use on any Amazon EC2 instance. For information about
setting up a standalone web server on an Amazon EC2 instance not connected to a Nitro Enclave, see [Tutorial: Install a LAMP web server
on Amazon Linux 2](../../../AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.md "../../../AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.md") or [Tutorial:
Install a LAMP web server with the Amazon Linux AMI](../../../AWSEC2/latest/UserGuide/install-LAMP.md "../../../AWSEC2/latest/UserGuide/install-LAMP.md").

ACM certificates are supported by the following services:

**Elastic Load Balancing**

Elastic Load Balancing automatically distributes your incoming application traffic across multiple
Amazon EC2 instances. It detects unhealthy instances and reroutes traffic to healthy
instances until the unhealthy instances have been restored. Elastic Load Balancing automatically scales
its request handling capacity in response to incoming traffic. For more information
about load balancing, see the [Elastic Load Balancing User Guide](../../../elasticloadbalancing/latest/userguide.md "../../../elasticloadbalancing/latest/userguide.md").

In general, to serve secure content over SSL/TLS, load balancers require that
SSL/TLS certificates be installed on either the load balancer or the back-end Amazon EC2
instance. ACM is integrated with Elastic Load Balancing to deploy ACM certificates on the load
balancer. For more information, see [Create an Application Load
Balancer](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md")

**Amazon CloudFront**

Amazon CloudFront is a web service that speeds up distribution of your dynamic and static web
content to end users by delivering your content from a worldwide network of edge
locations. When an end user requests content that you're serving through CloudFront, the user
is routed to the edge location that provides the lowest latency. This ensures that
content is delivered with the best possible performance. If the content is currently at
that edge location, CloudFront delivers it immediately. If the content is not currently at
that edge location, CloudFront retrieves it from the Amazon S3 bucket or web server that you have
identified as the definitive content source. For more information about CloudFront, see the
[Amazon CloudFront Developer Guide](../../../AmazonCloudFront/latest/DeveloperGuide.md "../../../AmazonCloudFront/latest/DeveloperGuide.md").

To serve secure content over SSL/TLS, CloudFront requires that SSL/TLS certificates be
installed on either the CloudFront distribution or on the backed content source. ACM is
integrated with CloudFront to deploy ACM certificates on the CloudFront distribution. For more
information, see [Getting an SSL/TLS Certificate](../../../AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.md#cnames-and-https-getting-certificates "../../../AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.md#cnames-and-https-getting-certificates").

###### Note

To use an ACM certificate with CloudFront, you must request or import the certificate
in the US East (N. Virginia) region.

**Amazon Cognito**

Amazon Cognito provides authentication, authorization, and user management for your web
and mobile applications. Users can sign in directly with your AWS account credentials
or through a third party such as Facebook, Amazon, Google, or Apple. For more
information about Amazon Cognito, see [Amazon Cognito Developer
Guide](../../../cognito/latest/developerguide.md "../../../cognito/latest/developerguide.md").

When you configure a Cognito user pool to use an Amazon CloudFront proxy, CloudFront may put an
ACM certificate in place to secure the custom domain. When this is the case, be aware
that you must remove the certificate's association with CloudFront before you can delete
it.

**AWS Elastic Beanstalk**

Elastic Beanstalk helps you deploy and manage applications in the AWS Cloud without worrying
about the infrastructure that runs those applications. AWS Elastic Beanstalk reduces management
complexity. You simply upload your application and Elastic Beanstalk automatically handles the
details of capacity provisioning, load balancing, scaling, and health monitoring. Elastic Beanstalk
uses the Elastic Load Balancing service to create a load balancer. For more information about Elastic Beanstalk,
see the [AWS Elastic Beanstalk Developer Guide](../../../elasticbeanstalk/latest/dg.md "../../../elasticbeanstalk/latest/dg.md").

To choose a certificate, you must configure the load balancer for your application
in the Elastic Beanstalk console. For more information, see [Configuring Your Elastic Beanstalk Environment's
Load Balancer to Terminate HTTPS](../../../elasticbeanstalk/latest/dg/configuring-https-elb.md "../../../elasticbeanstalk/latest/dg/configuring-https-elb.md").

**AWS App Runner**

App Runner is an AWS service that provides a fast, simple, and cost-effective way to
deploy from source code or a container image directly to a scalable and secure web
application in the AWS Cloud. You don't need to learn new technologies, decide which
compute service to use, or know how to provision and configure AWS resources. For more
information about App Runner, see the [AWS App Runner Developer Guide](../../../apprunner/latest/dg.md "../../../apprunner/latest/dg.md").

When you associate custom domain names with your App Runner service, App Runner internally
creates certificates that track domain validity. They're stored in ACM. App Runner doesn't
delete these certificates for seven days after a domain is disassociated from your
service or after the service is deleted. This entire process is automated and you don't
need to add or manage any certificates yourself. For more information, see [Managing custom
domain names for an App Runner service](../../../apprunner/latest/dg/manage-custom-domains.md "../../../apprunner/latest/dg/manage-custom-domains.md") in the _AWS App Runner Developer
Guide_.

**Amazon API Gateway**

With the proliferation of mobile devices and growth of the Internet of Things (IoT),
it has become increasingly common to create APIs that can be used to access data and
interact with back-end systems on AWS. You can use API Gateway to publish, maintain,
monitor, and secure your APIs. After you deploy your API to API Gateway, you can [set up a custom domain name](../../../apigateway/latest/developerguide/how-to-custom-domains.md "../../../apigateway/latest/developerguide/how-to-custom-domains.md") to
simplify access to it. To set up a custom domain name, you must provide an SSL/TLS
certificate. You can use ACM to generate or import the certificate. For more
information about Amazon API Gateway, see the [Amazon API Gateway Developer
Guide](../../../apigateway/latest/developerguide.md "../../../apigateway/latest/developerguide.md").

**AWS Nitro Enclaves**

AWS Nitro Enclaves is an Amazon EC2 feature that allows you to create isolated
execution environments, called _enclaves_, from Amazon EC2
instances. Enclaves are separate, hardened, and highly constrained virtual machines.
They provide only secure local socket connectivity with their parent instance. They have
no persistent storage, interactive access, or external networking. Users cannot SSH into
an enclave, and the data and applications inside the enclave cannot be accessed by the
parent instance's processes, applications, or users (including root or admin).

EC2 instances connected to Nitro Enclaves support ACM certificates. For more
information, see [AWS Certificate Manager for
Nitro Enclaves](../../../enclaves/latest/user/nitro-enclave-refapp.md "../../../enclaves/latest/user/nitro-enclave-refapp.md").

###### Note

You cannot associate ACM certificates with an EC2 instance that is not connected
to a Nitro Enclave.

**AWS CloudFormation**

AWS CloudFormation helps you model and set up your Amazon Web Services resources. You create a template
that describes the AWS resources that you want to use, such as Elastic Load Balancing or API Gateway. Then
AWS CloudFormation takes care of provisioning and configuring those resources for you. You don't need
to individually create and configure AWS resources and figure out what's dependent on
what; AWS CloudFormation handles all of that. ACM certificates are included as a template resource,
which means that AWS CloudFormation can request ACM certificates that you can use with AWS
services to enable secure connections. In addition, ACM certificates are included with
many of the AWS resources that you can set up with AWS CloudFormation.

For general information about CloudFormation, see the [AWS CloudFormation
User Guide](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md"). For information about ACM resources supported by CloudFormation, see
[AWS::CertificateManager::Certificate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.md").

With the powerful automation provided by AWS CloudFormation, it is easy to exceed your [certificate quota](acm-limits.md "acm-limits.md"), especially with new AWS
accounts. We recommend that you follow the ACM [best
practices](acm-bestpractices.md#best-practices-cloudformation "acm-bestpractices.md#best-practices-cloudformation") for AWS CloudFormation.

###### Note

If you create an ACM certificate with AWS CloudFormation, the AWS CloudFormation stack remains in the
**CREATE_IN_PROGRESS** state. Any further stack
operations are delayed until you act upon the instructions in the certificate
validation email. For more information, see [Resource Failed to Stabilize During a Create, Update, or Delete Stack
Operation](../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md#troubleshooting-resource-did-not-stabilize "../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md#troubleshooting-resource-did-not-stabilize").

**AWS Amplify**

Amplify is a set of purpose-built tools and features that enables front-end web
and mobile developers to quickly and easily build full-stack applications on AWS.
Amplify provides two services: Amplify Hosting and Amplify Studio. Amplify Hosting
provides a git-based workflow for hosting full-stack serverless web apps with continuous
deployment. Amplify Studio is a visual development environment that simplifies the
creation of scalable, full-stack web and mobile apps. Use Studio to build your front-end
UI with a set of ready-to-use UI components, create an app backend, and then connect the
two together. For more information about Amplify, see the [AWS Amplify](../../../amplify/latest/userguide/welcome.md "../../../amplify/latest/userguide/welcome.md")
User Guide.

If you connect a custom domain to your application, the Amplify console issues an
ACM certificate to secure it.

**Amazon OpenSearch Service**

Amazon OpenSearch Service is a search and analytics engine for use cases such as
log analytics, real-time application monitoring, and click stream analysis. For more
information, see the [Amazon OpenSearch Service Developer
Guide](../../../opensearch-service/latest/developerguide.md "../../../opensearch-service/latest/developerguide.md").

When you create an OpenSearch Service cluster that contains a [custom domain and endpoint](../../../opensearch-service/latest/developerguide/customendpoint.md "../../../opensearch-service/latest/developerguide/customendpoint.md"), you can use
ACM to provision the associated Application Load Balancer with a certificate.

**AWS Network Firewall**

AWS Network Firewall is a managed service that makes it easy to deploy essential network
protections for all of your Amazon Virtual Private Clouds (VPCs). For more information
about Network Firewall, see the [AWS Network Firewall Developer Guide](../../../network-firewall/latest/developerguide.md "../../../network-firewall/latest/developerguide.md").

Network Firewall firewall integrates with ACM for TLS inspection. If you use TLS inspection
in Network Firewall, you must configure an ACM certificate for the decryption and re-encryption
of the SSL/TLS traffic going through your firewall. For information about how Network Firewall
works with ACM for TLS inspection, see [Requirements for using
SSL/TLS certificates with TLS inspection configurations](../../../network-firewall/latest/developerguide/tls-inspection-certificate-requirements.md "../../../network-firewall/latest/developerguide/tls-inspection-certificate-requirements.md") in the
_AWS Network Firewall Developer Guide_.
