# Connecting to Amazon VPC

You can configure and update your project to use Amazon VPC endpoints. The VPC-ENI configuration is configured
on a per-project basis. A project can have only one VPC-ENI endpoint at any given time. To configure VPC
access for a project, you must know the following details:

- The VPC ID in `us-west-2` if your app is hosted there or the `us-west-2` VPC
  ID that connects to some other VPC in a different Region.
- The applicable security groups to apply to the connection.
- The subnets that will be associated with the connection. When a session starts, the largest
  available subnet is used. We recommend having multiple subnets associated with different
  availability zones to improve the availability posture of your VPC connectivity.
- When using VPC-ENI, the DNS resolver used by the Device Farm test hosts and devices will be the server provided by DHCP services in the customer subnet. In a default configuration, this will be the VPC's default resolver. Customers wishing to specify custom DNS resolvers may configure a DHCP Option Set in their VPC.
  Once you have created your VPC-ENI configuration, you can update its details using the console or CLI
  using the steps below.

Console

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. On the Device Farm navigation panel, choose **Mobile Device
   Testing**, then choose **Projects**.
3. Under **Mobile Testing projects**, choose the name of
   your project from the list.
4. Choose **Project settings**.
5. In the **Virtual Private Cloud (VPC)
   Settings** section, you can change the
   `VPC`, `Subnets` (private subnets only), and
   `Security Groups`.
6. Choose **Save**.

CLI
Use the following AWS CLI command to update the Amazon VPC:

```
$  aws devicefarm update-project \
--arn arn:aws:devicefarm:us-west-2:111122223333:project:12345678-1111-2222-333-456789abcdef \
--vpc-config \
securityGroupIds=sg-02c1537701a7e3763,sg-005dadf9311efda25,\
subnetIds=subnet-09b1a45f9cac53717,subnet-09b1a45f9cac12345,\
vpcId=vpc-0238fb322af81a368
```

You can also configure an Amazon VPC when creating your project:

```
$  aws devicefarm create-project \
--name VPCDemo \
--vpc-config \
securityGroupIds=sg-02c1537701a7e3763,sg-005dadf9311efda25,\
subnetIds=subnet-09b1a45f9cac53717,subnet-09b1a45f9cac12345,\
vpcId=vpc-0238fb322af81a368
```
