

# Enabling LNI on your Outpost subnet
<a name="enable-lni"></a>

To use Local Network Interface (LNI) on your Outposts server, you must first enable LNI on your Outpost subnet. This configuration allows instances launched in the subnet to attach LNI at a specific network device index.

**To enable LNI using the AWS CLI**  
Run the following command, replacing the subnet ID with your Outpost subnet:

```
aws ec2 modify-subnet-attribute \
    --subnet-id {{subnet-xxxxxxxxx}} \
    --enable-lni-at-device-index 1
```

**Important**  
You must run this command before launching instances that will use LNI. The device index value of 1 means that LNI will be attached as the second network interface (eth1) on your instances.

After enabling LNI on the subnet, you can create network interfaces and attach them to your instances at device index 1 to establish Layer 2 connectivity with your on-premises network.

For a complete walkthrough with architecture diagrams and additional configuration examples, see [Architecting for seamless on-premises connectivity with AWS Outposts servers](https://aws.amazon.com/blogs/networking-and-content-delivery/architecting-for-seamless-on-premises-connectivity-with-aws-outposts-servers/).