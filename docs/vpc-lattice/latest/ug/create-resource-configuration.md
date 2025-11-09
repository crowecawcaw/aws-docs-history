# Create a resource configuration in

VPC Lattice

Create a resource configuration.

AWS Management Console###### To create a resource configuration using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **PrivateLink and Lattice**,
   choose **Resource configurations**.
3. Choose **Create resource configuration**.
4. Enter a name that is unique within your AWS account. You can't change this
   name after the resource configuration is created.
5. For **Configuration type**, choose
   **Resource** for a single or child resource or
   **Resource group** for a group of child resources.
6. Choose a resource gateway that you previously created or create a one
   now.
7. (Optional) To enter a custom domain name, do one of the following:
   - If you have a resource configuration of type single, you
     can enter a custom domain name. Resource consumers can use
     this domain name to access your resource configurations.
   - If you have a resource configuration of type group and
     child, you must first specify a group domain on the group
     resource configuration. Next, the child resource
     configurations can have custom domains that are subdomains
     of the group domain.

8. (Optional) Enter the verification ID.

Provide a verification ID if you want your domain name to be verified. This
lets resource consumers know that you own the domain name. 9. Choose the identifier for the resource that you want this resource
configuration to represent. 10. Choose the port ranges through which you want to share the resource. 11. For **Association settings**, specify whether this resource
configuration can be associated with shareable service networks. 12. For **Share resource configuration**, choose the resource
shares that identify the principals who can access this resource. 13. (Optional) For **Monitoring**, enable **Resource
access logs** and the delivery destination if you want to monitor
requests and responses to and from the resource configuration. 14. (Optional) To add a tag, choose **Add new tag** and enter the
tag key and the tag value. 15. Choose **Create resource configuration**.

AWS CLIThe following [create-resource-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-configuration.html") command creates a single resource configuration and associates it with the custom domain name
`example.com`.

```
aws vpc-lattice create-resource-configuration \
    --name my-resource-config \
    --type SINGLE \
    --resource-gateway-identifier rgw-0bba03f3d56060135 \
    --resource-configuration-definition 'ipResource={ipAddress=10.0.14.85}' \
    --custom-domain-name example.com \
    --verification-id dv-aaaa0000000111111
```

The following [create-resource-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-configuration.html") command creates a group resource configuration and associates it with the custom domain name
`example.com`.

```
aws vpc-lattice-custom-dns create-resource-configuration \
  --name my-custom-dns-resource-config-group \
  --type GROUP \
  --resource-gateway-identifier rgw-0bba03f3d56060135 \
  --domain-verification-identifier dv-aaaa0000000111111
```

The following [create-resource-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-configuration.html") command creates a child resource configuration and associates it with the custom domain name
`child.example.com`.

```
aws vpc-lattice-custom-dns create-resource-configuration \
  --name my-custom-dns-resource-config-child \
  --type CHILD \
  --resource-configuration-definition 'dnsResource={domainName=my-alb-123456789.us-west-2.elb.amazonaws.com,ipAddressType=IPV4}' \
  --resource-configuration-group-identifier rcfg-07129f3acded87626 \
  --custom-domain-name child.example.com
```
