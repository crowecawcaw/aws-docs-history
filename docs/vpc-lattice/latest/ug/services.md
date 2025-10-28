# Services in VPC Lattice

A service within VPC Lattice is an independently deployable unit of software that delivers a
specific task or function. A service can run on instances, containers, or as serverless
functions within an account or a virtual private cloud (VPC). A service has a listener that
uses rules, called listener rules, that you can configure to help route traffic to your
targets. The supported target types include EC2 instances, IP addresses, Lambda functions, Application Load Balancers, Amazon ECS tasks, and Kubernetes Pods. For more information, see [Target groups in VPC Lattice](target-groups.md "target-groups.md").
You can associate a service with multiple service networks. The following diagram shows
the key components of a typical service within VPC Lattice.

![A service with a listener, listener rules, and two target groups.](images/service.png)
You can create a service by giving it a name and description. However, to control and
monitor traffic to your service, it is important that you include access settings and
monitoring details. To send traffic from your service to your targets you must set up a
listener and configure rules. To allow traffic to flow from the service network to your
service, you must associate your service with the service network.

There is an idle timeout and overall connection timeout for connections to targets.
The idle connection timeout is 1 minute, after which we close the connection.
The maximum duration is 10 minutes, after which we do not allow new streams over the
connection and we begin the process of closing the existing streams.

###### Tasks

- [Step 1: Create a VPC Lattice service](#create-service "#create-service")
- [Step 2: Define routing](#define-routing "#define-routing")
- [Step 3: Create network associations](#associate-to-networks "#associate-to-networks")
- [Step 4: Review and create](#review-and-create "#review-and-create")
- [Manage associations](service-associations.md "service-associations.md")
- [Edit access settings](service-access.md "service-access.md")
- [Edit monitoring details](service-monitoring.md "service-monitoring.md")
- [Manage tags](service-tags.md "service-tags.md")
- [Configure a custom domain name](service-custom-domain-name.md "service-custom-domain-name.md")
- [BYOC](service-byoc.md "service-byoc.md")
- [Delete a service](delete-service.md "delete-service.md")

## Step 1: Create a VPC Lattice service

Create a basic VPC Lattice service with access settings and monitoring details.
However, the service is not fully functional until you define its routing
configuration and associate it with a service network.

###### To create a basic service using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Services**.
3. Choose **Create service**.
4. For **Identifiers**, do the following:
   1. Enter a name for the service. The name must be between 3-40 characters
      and use lowercase letters, numbers, and hyphens. It must begin and end
      with a letter or number. Do not use double hyphens.
   2. (Optional) Enter a description for the service network. You can set or change
      the description during or after creation. The description can have up to 256
      characters.

5. To specify a custom domain name for your service, select
   **Specify a custom domain configuration** and enter the custom
   domain name.

For HTTPS listeners, you can select the certificate that VPC Lattice will use
to perform TLS termination. If you do not select a certificate now, you can
select it when you create an HTTPS listener for the service.

For TCP listeners, you must specify a custom domain name for your service.
If you specify a certificate, it is not used. Instead, you perform TLS
termination in your application. 6. For **Service access**, choose **None** if
you want clients in the VPCs associated with the service network to access your
service. To apply an [auth policy](auth-policies.md "auth-policies.md") to control
access to the service, choose **AWS IAM**. To apply a resource
policy to the service, do one of the following for **Auth policy**:

    * Enter a policy in the input field. For example policies that you can
     copy and paste, choose **Policy examples**.
    * Choose **Apply policy template** and select the
     **Allow authenticated and unauthenticated access**
     template. This template allows a client from another account to access
     the service either by signing the request (meaning authenticated) or
     anonymously (meaning unauthenticated).
    * Choose **Apply policy template** and select the
     **Allow only authenticated access** template. This
     template allows a client from another account to access the service
     only by signing the request (meaning authenticated).

7. (Optional) To enable [access logs](monitoring-access-logs.md "monitoring-access-logs.md"),
   turn on the **Access logs** toggle switch and specify a destination
   for your access logs as follows:
   - Select **CloudWatch Log group** and choose a
     CloudWatch Log group. To create a log group, choose
     **Create a log group in CloudWatch**.
   - Select **S3 bucket** and enter the S3 bucket path,
     including any prefix. To search your S3 buckets, choose
     **Browse S3**.
   - Select **Kinesis Data Firehose delivery stream**
     and choose a delivery stream. To create a delivery stream, choose
     **Create a delivery stream in Kinesis**.

8. (Optional) To [share your service](sharing.md "sharing.md") with other accounts,
   choose an AWS RAM resource share from **Resource shares**. To create a
   resource share, choose **Create a resource share in RAM console**.
9. To review your configuration and create the service, choose **Skip to
   review and create**. Otherwise, choose **Next** to
   define the routing configuration for your service.

## Step 2: Define routing

Define your routing configuration using listeners so your service can send traffic to
the targets that you specify.

###### Prerequisite

Before you can add a listener, you must create a VPC Lattice target group.
For more information, see [Create a VPC Lattice target group](create-target-group.md "create-target-group.md").

###### To define routing for your service using the console

1. Choose **Add listener**.
2. For **Listener name**, you can either provide a custom
   listener name or use the protocol and port of your listener as the listener
   name. A custom name that you specify can have up to 63 characters, and it
   must be unique for every service in your account. The valid characters are
   a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character,
   or immediately after another hyphen. You cannot change the name of a listener
   after you create it.
3. Choose a protocol and then enter a port number.
4. For **Default action**, choose the VPC Lattice target group to
   receive traffic and choose the weight to assign to this target group. You can
   optionally add another target group for the default action. Choose
   **Add action** and then choose another target group and
   specify its weight.
5. (Optional) To add another rule, choose **Add rule** and then
   enter a name, a priority, a condition, and an action for the rule.

You can give each rule a priority number between 1 and 100. A listener can't
have multiple rules with the same priority. Rules are evaluated in priority
order, from the lowest value to the highest value. The default rule is evaluated
last.

For **Condition**, enter a path pattern for the path match
condition. The maximum size of each string is 200 characters. The comparison is
not case sensitive. 6. (Optional) To add tags, expand **Listener tags**, choose
**Add new tag**, and enter a tag key and a tag value. 7. To review your configuration and create the service, choose **Skip to
review and create**. Otherwise, choose **Next** to
associate your service to a service network.

## Step 3: Create network associations

Associate your service with a service network so that clients can communicate with
it.

###### To associate a service to a service network using the console

1. For **VPC Lattice service networks**, select the service network.
   To create a service network, choose **Create a VPC Lattice network**.
   You can associate your service with multiple service networks.
2. (Optional) To add a tag, expand **Service network association tags**,
   choose **Add new tag**, and enter a tag key and tag value.
3. Choose **Next**.

## Step 4: Review and create

###### To review the configuration and create the service using the console

1. Review the configuration for your service.
2. Choose **Edit** if you need to modify any portion
   of the service configuration.
3. When you have finished reviewing or editing your configuration, choose
   **Create VPC Lattice service**.
4. If you specified a custom domain name for the service, you must configure
   DNS routing after the service is created. For more information, see
   [Configure a custom domain name for your VPC Lattice service](service-custom-domain-name.md "service-custom-domain-name.md").
