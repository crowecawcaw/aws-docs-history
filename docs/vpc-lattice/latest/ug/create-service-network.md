# Create a VPC Lattice service network

Use the console to create a service network and optionally configure it with services,
associations, access settings, and access logs.

###### To create a service network using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Service networks**.
3. Choose **Create service network**.
4. For **Identifiers**, enter a name, an optional description,
   and optional tags. The name must be between 3 and 63 characters. You can use
   lowercase letters, numbers, and hyphens. The name must begin and end with a
   letter or number. Do not use consecutive hyphens. The description can have up to
   256 characters. To add a tag, choose **Add new tag** and
   specify a tag key and tag value.
5. (Optional) To associate a service, choose the service from **Service
   associations**, **Services**. The list includes
   services that are in your account and any services that are shared with you from
   a different account. If there aren't any services in the list, you can create a
   service by choosing **Create an VPC Lattice service**.

Alternatively, to associate a service after you've created the service
network, see [Manage service
associations](service-network-associations.md#service-network-service-associations "service-network-associations.md#service-network-service-associations"). 6. (Optional) To associate a resource configuration, choose the resource
configuration service from **Resource Configuration
associations**, **Resource configuration**. The
list includes resource configurations that are in your account and any resource
configurations that are shared with you from a different account. If there
aren't any resource configurations in the list, you can create a resource
configuration by choosing **Create an Amazon VPC Lattice resource
configuration**.

Alternatively, to associate a resource configuration after you've created the
service network, see [Manage resource
configuration associations](service-network-associations.md#service-network-resource-config-associations "service-network-associations.md#service-network-resource-config-associations"). 7. (Optional) To associate a VPC, choose **Add VPC
association**. Select the VPC to associate from
**VPC**, and select up to five security groups from
**Security groups**. To create a security group, choose
**Create new security group**.

Alternatively, you can skip this step and connect a VPC to the service network
using a VPC endpoint (powered by AWS PrivateLink). For more information, see
[Access
service networks](../../../vpc/latest/privatelink/privatelink-access-service-networks.md "../../../vpc/latest/privatelink/privatelink-access-service-networks.md") in the _AWS PrivateLink user
guide_. 8. When creating a service network, you have to decide if you intend sharing the
service network with other accounts or not. Your selection is immutable and
cannot be changed after you create the service network. If you choose to allow
sharing, the service network can be shared with other accounts through
AWS Resource Access Manager.

To [share
your service network](sharing.md "sharing.md") with other accounts, choose the AWS RAM resource
shares from **Resource shares**.

To create a resource share, go to the AWS RAM console and choose
**Create a resource share**. 9. For **Network access**, you can leave the default auth type,
**None**, if you want the clients in the associated VPCs to
access the services in this service network. To apply an [auth policy](auth-policies.md "auth-policies.md") to control access to your
services, choose **AWS IAM** and do one of the following
for **Auth policy**:

    * Enter a policy in the input field. For example policies that you can
     copy and paste, choose **Policy examples**.
    * Choose **Apply policy template** and select the
     **Allow authenticated and unauthenticated access**
     template. This template allows a client from another account to access
     the service either by signing the request (meaning authenticated) or
     anonymously (meaning unauthenticated).
    * Choose **Apply policy template** and select the
     **Allow only authenticated access** template. This
     template allows a client from another account to access the service only
     by signing the request (meaning authenticated).

10. (Optional) To turn on [access
    logs](monitoring-access-logs.md "monitoring-access-logs.md"), select the **Access logs** toggle switch and
    specify a destination for your access logs as follows:
    - Select **CloudWatch Log group** and choose a
      CloudWatch Log group. To create a log group, choose **Create a
      log group in CloudWatch**.
    - Select **S3 bucket** and enter the S3 bucket path,
      including any prefix. To search your S3 buckets, choose **Browse
      S3**.
    - Select **Kinesis Data Firehose delivery stream** and
      choose a delivery stream. To create a delivery stream, choose
      **Create a delivery stream in Kinesis**.

11. (Optional) To [share your service network](sharing.md "sharing.md") with
    other accounts, choose the AWS RAM resource shares from **Resource
    shares**. To create a resource share, choose **Create a
    resource share in RAM console**.
12. Review your configuration in the **Summary** section, and
    then choose **Create service network**.

###### To create a service network using the AWS CLI

Use the [create-service-network](../../../cli/latest/reference/vpc-lattice/create-service-network.md "../../../cli/latest/reference/vpc-lattice/create-service-network.md") command. This command creates only the basic
service network. To create a fully functional service network, you must also use the
commands that create [service
associations](service-network-associations.md#service-network-service-associations "service-network-associations.md#service-network-service-associations"), [VPC
associations](service-network-associations.md#service-network-vpc-associations "service-network-associations.md#service-network-vpc-associations"), and [access
settings](service-network-access.md "service-network-access.md").
