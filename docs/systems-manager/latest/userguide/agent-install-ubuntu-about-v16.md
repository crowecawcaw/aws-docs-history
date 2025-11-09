AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Determining the correct

SSM Agent version to install on 64-bit Ubuntu Server 16.04
instances

###### Important

Before you install SSM Agent on a 64-bit version of Ubuntu Server, ensure
that you are using the correction installation tools. Beginning with
Amazon Machine Images (AMIs) that are identified with 20180627, SSM Agent
is pre-installed on version 16.04 using Snap packages. On instances
created from earlier AMIs, SSM Agent must be installed using deb
installer packages. For more information, see Determining the correct
SSM Agent version to install on 64-bit Ubuntu Server 16.04
instances

Be aware that if an instance has more than one installation of the
SSM Agent (for example, one installed using a Snap and one installed
using a deb installer), your agent operations won't work
correctly.

You can verify the source AMI ID creation date for an instance using
either of the following methods. These procedures apply only to AWS
managed AMIs.

###### Verify a source AMI ID creation date (console)

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Instances**.
3. Select an instance.
4. On the **Details** tab, check for a
   `YYYYMMDD` identifier in the value under
   **AMI name** field. For example:
   `ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-20180627`.

###### Verify a source AMI ID creation date (AWS CLI)

- Run the following command.

```
aws ec2 describe-images --image-ids `ami-id`
```

`ami-id` represents the ID of an AMI
provided by AWS, such as
`ami-07c8bc5c1ce9598c3`.

If successful, the command returns information like the following,
in which you can check the `CreationDate` and
`Name` fields for information.

```
{
    "Images": [
        {
            "Architecture": "x86_64",
            **"CreationDate": "2020-07-24T20:40:27.000Z"**,
            "ImageId": "ami-07c8bc5c1ce9598c3",
-- truncated --
            "ImageOwnerAlias": "amazon",
            **"Name": "amzn2-ami-hvm-2.0.20200722.0-x86\_64-gp2"**,
            "RootDeviceName": "/dev/xvda",
            "RootDeviceType": "ebs",
            "SriovNetSupport": "simple",
            "VirtualizationType": "hvm"
        }
    ]
}
```
