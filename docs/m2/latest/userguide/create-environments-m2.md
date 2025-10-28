AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Create an AWS Mainframe Modernization runtime environment

Use the AWS Mainframe Modernization console to create an AWS Mainframe Modernization environment.

These instructions assume that you've completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md").

## Create a runtime environment

###### To create a runtime environment

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where you want to create the
   environment.
3. On the **Environments** page, choose **Create
   environment**.
4. On the **Specify basic information** page, provide the following
   information:
   1. In the **Name and description** section, enter a name for the
      environment.
   2. (Optional). In the **Environment description** field, enter a
      description for the environment. This description can help you and other users
      identify the purpose of the runtime environment.
   3. In the **Engine options** section, choose **Blu
      Age** for automated refactoring, or **Micro Focus
      (Rocket)** for replatforming.
   4. Choose a version for the engine that you selected.
   5. (Optional). In the **Tags** section, choose **Add new
      tag** to add one or more environment tags to your environment. An
      environment tag is a custom attribute label that helps you organize and manage your
      AWS resources.
   6. Choose **Next**.

5. On the **Specify configurations** page, provide the following
   information:
   1. In the **Availability** section, choose **Standalone
      runtime environment** or **High availability
      cluster**.

   The availability pattern determines how available your application will be when
   it runs. _Standalone_ is fine for development purposes.
   _High availability_ is for applications that must be available
   at all times. 2. In **Resources**, choose an instance type and desired
   capacity.

   These resources are the AWS Mainframe Modernization managed Amazon EC2 instances that will host your runtime
   environment. Standalone runtime environments offer two choices for instance type and
   permit only one instance. High availability runtime environments offer two choices
   for instance type and permit up to two instances.

   For more information, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/"), and contact an AWS mainframe specialist for
   guidance.

6. In the **Security and network** section, do the following:
   1. If you want the applications to be publicly accessible, choose **Allow
      applications deployed to this environment to be publicly
      accessible**.
   2. Choose the network type. If you choose IPv4, AWS Mainframe Modernization environment applications serve
      only IPv4 requests. In the dual-stack mode, applications will serve both IPv4 and
      IPv6 requests. If you choose the dual-stack mode, make sure there is at least 1 VPC
      with IPv6-enabled subnets.
   3. Choose a Virtual Private Cloud (VPC).
   4. If you're using the high availability pattern, choose two or more subnets. If
      you're using the standalone pattern with the AWS Blu Age engine, choose two or more
      subnets. If you're using the standalone pattern with the Rocket Software engine, you can
      specify one subnet.
   5. Choose a security group for the VPC that you selected.

   ###### Note

   AWS Mainframe Modernization creates a Network Load Balancer for you to distribute connections to your
   runtime environment. Make sure your security group inbound and outbound rules
   allow access from an IP address to the port you specified in the `Listener(s) -
 required` property of
   the application definition. For more information, see [Update the security groups for your Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-security-groups.md "../../../elasticloadbalancing/latest/network/load-balancer-security-groups.md") in the
   _User Guide for Network Load Balancers_. 6. In the **KMS key** field, choose **Customize encryption
   settings** if you want to use a customer managed AWS KMS key. For more
   information, see [Data encryption at rest for AWS Mainframe Modernization service](data-protection.md#encryption-rest "data-protection.md#encryption-rest").

   ###### Note

   By default, AWS Mainframe Modernization encrypts your data with a AWS KMS key that AWS Mainframe Modernization owns and
   manages for you. However, you can choose to use a customer managed
   AWS KMS key. 7. (Optional) Choose an AWS KMS key by name or Amazon Resource Name (ARN).
   Alternately, choose **Create an AWS KMS key** to go to the AWS KMS
   console and create a new AWS KMS key. 8. Choose **Next**.

7. (Optional) On the **Attach storage** page, choose one or more Amazon EFS
   or Amazon FSx file systems.

The file system mounted to an AWS Mainframe Modernization environment must be owned by a suitable user
to be used by your applications that are running in the AWS Mainframe Modernization
console.

To configure these user settings, you can attach the drive to a Linux Amazon EC2
instance. Then create a group with ID `101` and a user with ID
`3001`. Also, ensure the desired data folder that will be used by your
application(s) must be owned by this user.

For example, the `myFiles` folder can be used by your AWS Mainframe Modernization
applications running in AWS Mainframe Modernization Managed.

```
groupadd -g 101 mygroup
useradd -M -g mygroup -p mypassword -u 3001 myuser
mkdir myFiles
chown myuser:mygroup myFiles
```

###### Note

To enable access to the file system, the following security groups rules should be
configured for establishing network connectivity between the EFS and M2 environment
instance:

    * **M2 environment security group** – Include an
     outbound rule that allows traffic over the NFS 2049 port.
    * **File system mount targets security group** –
     Include an inbound rule that allows traffic over the NFS 2049 port from the
     instance security group (listed above), and an outbound rule that allows traffic
     over the NFS 2049 port.

8.  Choose **Next**.
9.  In the **Maintenance window** section, choose when you want to
    apply pending changes to the environment.

        * If you choose **No preference**, AWS Mainframe Modernization chooses an optimized
         maintenance window for you.
        * To specify a particular maintenance window, choose **Select new
         maintenance window**. Then choose a day of the week, a start time, and a
         duration for the maintenance window.

    For more information about the maintenance window, see [AWS Mainframe Modernization maintenance window](update-environments-m2.md#update-environments-m2-maintenance "update-environments-m2.md#update-environments-m2-maintenance").

Choose **Next**. 10. On the **Review and create** page, review the information that you
entered, and then choose **Create environment**.
