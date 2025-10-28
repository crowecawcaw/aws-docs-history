# Creating an endpoint on an Outpost

To route requests to an Amazon S3 on Outposts access point, you must create and configure an
S3 on Outposts endpoint. In order to create an endpoint, you will need an active connection with your service link to your Outposts home region. Each virtual private cloud (VPC) on your Outpost can have one associated endpoint. For more information about endpoint quotas, see [S3 on Outposts network
requirements](S3OnOutpostsRestrictionsLimitations.md#S3OnOutpostsConnectivityRestrictions "S3OnOutpostsRestrictionsLimitations.md#S3OnOutpostsConnectivityRestrictions"). You must create an endpoint to be able to
access your Outposts buckets and perform object operations. For more information, see [Endpoints](S3OutpostsWorkingBuckets.md#S3OutpostsEP "S3OutpostsWorkingBuckets.md#S3OutpostsEP").

###### Permissions

For more information about the permissions that are required to create an endpoint, see
[Permissions for S3 on Outposts
endpoints](S3OutpostsIAM.md#S3OutpostsEndpointPermissions "S3OutpostsIAM.md#S3OutpostsEndpointPermissions").

When you create an endpoint, S3 on Outposts also creates a service-linked role in your
AWS account. For more information, see [Using service-linked roles for
Amazon S3 on Outposts](S3OutpostsServiceLinkedRoles.md "S3OutpostsServiceLinkedRoles.md").

The following examples show you how to create an S3 on Outposts endpoint by using the
AWS Management Console, AWS Command Line Interface (AWS CLI), and AWS SDK for Java.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Outposts access
   points**.
3. Choose the **Outposts endpoints** tab.
4. Choose **Create Outposts endpoint**.
5. Under **Outpost**, choose the Outpost to create this endpoint
   on.
6. Under **VPC**, choose a VPC that does not yet have an endpoint and
   that also complies with the rules for Outposts endpoints.

A virtual private cloud (VPC) enables you to launch AWS resources into a virtual
network that you define. This virtual network closely resembles a traditional network that
you would operate in your own data center, with the benefits of using the scalable
infrastructure of AWS.

If you don’t have a VPC, choose **Create VPC**. For more information,
see [Creating access points restricted to a virtual private cloud (VPC)](../userguide/access-points-vpc.md "../userguide/access-points-vpc.md") in the
_Amazon S3 User Guide_. 7. Choose **Create Outposts endpoint**.
The following AWS CLI example creates an endpoint for an Outpost by using the VPC resource
access type. The VPC is derived from the subnet. To run this command, replace the
`user input placeholders` with your own
information.

```
aws s3outposts create-endpoint --outpost-id `op-01ac5d28a6a232904` --subnet-id subnet-`8c7a57c5` --security-group-id `sg-ab19e0d1`
```

The following AWS CLI example creates an endpoint for an Outpost by using the customer-owned IP
address pool (CoIP pool) access type. To run this command, replace the
`user input placeholders` with your own
information.

```
aws s3outposts create-endpoint --outpost-id `op-01ac5d28a6a232904` --subnet-id subnet-`8c7a57c5` --security-group-id `sg-ab19e0d1` --access-type CustomerOwnedIp --customer-owned-ipv4-pool `ipv4pool-coip-12345678901234567`
```

For examples of how to create an endpoint for an S3 Outpost with the AWS SDK for Java, see [CreateOutpostsEndPoint.java](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/outposts/CreateOutpostsEndPoint.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/s3/src/main/java/com/example/s3/outposts/CreateOutpostsEndPoint.java") in the _AWS SDK for Java 2.x Code Examples_.
