# Create a network package in AWS TNB

A network package consists of a network service descriptor (NSD) file (required) and any
additional files (optional), such as scripts specific to your needs. For example, if you
have multiple function packages in your network package, you can use the NSD to define
which network functions should run in certain VPCs, subnets, or Amazon EKS clusters.

Create a network package after creating function packages. Once you've created a network
package, you need to create a network instance.

Console

###### To create a network package using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Network
   packages**.
3. Choose **Create network package**.
4. Choose **Choose files** and upload each NSD as a
   `.zip` file. You can upload a maximum of 10 files.
5. Choose **Next**.
6. Review the package details.
7. Choose **Create network package**.

AWS CLI

###### To create a network package using the AWS CLI

1. Use the [create-sol-network-package](../../../cli/latest/reference/tnb/create-sol-network-package.md "../../../cli/latest/reference/tnb/create-sol-network-package.md") command to create a network
   package.

```
aws tnb create-sol-network-package
```

2. Use the [put-sol-network-package-content](../../../cli/latest/reference/tnb/put-sol-network-package-content.md "../../../cli/latest/reference/tnb/put-sol-network-package-content.md") command to upload network
   package content. For example:

```
aws tnb put-sol-network-package-content \
--nsd-info-id `^np-[a-f0-9]{17}$` \
--content-type application/zip \
--file "`fileb://free5gc-core-1.0.9.zip`" \
--endpoint-url "`https://tnb.us-west-2.amazonaws.com`" \
--region `us-west-2`
```
