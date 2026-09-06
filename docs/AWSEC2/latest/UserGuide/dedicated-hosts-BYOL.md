

# Bring your own software licenses to Amazon EC2 Dedicated Hosts
<a name="dedicated-hosts-BYOL"></a>

Dedicated Hosts allow you to use your existing per-socket, per-core, or per-VM software licenses. When you bring your own license, you are responsible for managing your own licenses. However, Amazon EC2 has features that help you maintain license compliance, such as instance affinity and targeted placement.

These are the general steps to follow to bring your own volume licensed machine image into Amazon EC2.

1. Verify that the license terms controlling the use of your machine images allow usage in a virtualized cloud environment. For more information about Microsoft Licensing, see [Amazon Web Services and Microsoft Licensing](https://aws.amazon.com/windows/faq/#licensing).

1. After you have verified that your machine image can be used within Amazon EC2, import it using VM Import/Export. For information about how to import your machine image, see the [VM Import/Export User Guide](https://docs.aws.amazon.com/vm-import/latest/userguide/).

1. After you import your machine image, you can launch instances from it onto active Dedicated Hosts in your account.

1. When you run these instances, depending on the operating system, you might be required to activate these instances against your own KMS server (for example, Windows Server or Windows SQL Server). You can't activate your imported Windows AMI against the Amazon Windows KMS server.

**Note**  
To track how your images are used in AWS, enable host recording in AWS Config. You can use AWS Config to record configuration changes to a Dedicated Host and use the output as a data source for license reporting. For more information, see [Track Amazon EC2 Dedicated Host configuration changes using AWS Config](dedicated-hosts-aws-config.md). 