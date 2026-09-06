

# Set up components required to run CodeBuild in a proxy server
<a name="use-proxy-server-transparent-components"></a>

 You need these components to run AWS CodeBuild in a transparent or explicit proxy server: 
+  A VPC. 
+  One public subnet in your VPC for the proxy server. 
+  One private subnet in your VPC for CodeBuild. 
+  An internet gateway that allows communication between the VPC and the internet. 

 The following diagram shows how the components interact. 

![The diagram shows how the components interact.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/codebuild-proxy-transparent.png)


## Set up a VPC, subnets, and a network gateway
<a name="use-proxy-server-transparent-setup"></a>

 The following steps are required to run AWS CodeBuild in a transparent or explicit proxy server. 

1. Create a VPC. For information, see [Creating a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#Create-VPC) in the *Amazon VPC User Guide*.

1. Create two subnets in your VPC. One is a public subnet named `Public Subnet` in which your proxy server runs. The other is a private subnet named `Private Subnet` in which CodeBuild runs. 

   For information, see [Creating a subnet in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#AddaSubnet).

1.  Create and attach an internet gateway to your VPC. For more information, see [Creating and attaching an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Attach_Gateway). 

1.  Add a rule to the default route table that routes outgoing traffic from the VPC (0.0.0.0/0) to the internet gateway. For information, see [Adding and removing routes from a route table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#AddRemoveRoutes). 

1.  Add a rule to the default security group of your VPC that allows ingress SSH traffic (TCP 22) from your VPC (0.0.0.0/0). 

1.  Follow the instructions in [Launching an instance using the launch instance wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-instance.html) in the *Amazon EC2 User Guide* to launch an Amazon Linux instance. When you run the wizard, choose the following options: 
   +  In **Choose an Instance Type**, choose an Amazon Linux Amazon Machine Image (AMI). 
   +  In **Subnet**, choose the public subnet you created earlier in this topic. If you used the suggested name, it is **Public Subnet**. 
   +  In **Auto-assign Public IP**, choose **Enable**. 
   +  On the **Configure Security Group** page, for **Assign a security group**, choose **Select an existing security group**. Next, choose the default security group. 
   +  After you choose **Launch**, choose an existing key pair or create one. 

    Choose the default settings for all other options. 

1.  After your EC2 instance is running, disable source/destination checks. For information, see [Disabling Source/Destination checks](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html#EIP_Disable_SrcDestCheck) in the *Amazon VPC User Guide*. 

1.  Create a route table in your VPC. Add a rule to the route table that routes traffic destined for the internet to your proxy server. Associate this route table with your private subnet. This is required so that outbound requests from instances in your private subnet, where CodeBuild runs, are always routed through the proxy server. 

## Install and configure a proxy server
<a name="use-proxy-server-squid-install"></a>

 There are many proxy servers from which to choose. An open-source proxy server, Squid, is used here to demonstrate how AWS CodeBuild runs in a proxy server. You can apply the same concepts to other proxy servers. 

 To install Squid, use a yum repo by running the following commands: 

```
sudo yum update -y
sudo yum install -y squid
```

 After you install Squid, edit its `squid.conf` file using the instructions later in this topic. 

## Configure Squid for HTTPS traffic
<a name="use-proxy-server-squid-configure-https"></a>

 For HTTPS, the HTTP traffic is encapsulated in a Transport Layer Security (TLS) connection. Squid uses a feature called [SslPeekAndSplice](https://wiki.squid-cache.org/Features/SslPeekAndSplice) to retrieve the Server Name Indication (SNI) from the TLS initiation that contains the requested internet host. This is required so Squid does not need to unencrypt HTTPS traffic. To enable SslPeekAndSplice, Squid requires a certificate. Create this certificate using OpenSSL: 

```
sudo mkdir /etc/squid/ssl
cd /etc/squid/ssl
sudo openssl genrsa -out squid.key 2048
sudo openssl req -new -key squid.key -out squid.csr -subj "/C=XX/ST=XX/L=squid/O=squid/CN=squid"
sudo openssl x509 -req -days 3650 -in squid.csr -signkey squid.key -out squid.crt
sudo cat squid.key squid.crt | sudo tee squid.pem
```

**Note**  
 For HTTP, Squid does not require configuration. From all HTTP/1.1 request messages, it can retrieve the host header field, which specifies the internet host that is being requested. 