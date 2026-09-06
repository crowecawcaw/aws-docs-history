

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/). 

# Troubleshooting AWS Snowball Edge
<a name="troubleshooting"></a>

Keep the following general guidelines in mind when troubleshooting.
+ Objects in Amazon S3 have a maximum file size of 5 TB.
+ Objects transferred onto an AWS Snowball Edge device have a maximum key length of 933 bytes. Key names that include characters that take up more than 1 byte each still have a maximum key length of 933 bytes. When determining key length, you include the file or object name and also its path or prefixes. Thus, files with short file names within a heavily nested path can have keys longer than 933 bytes. The bucket name is not factored into the path when determining the key length. Some examples follow.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/snowball/latest/developer-guide/troubleshooting.html)
+ For security purposes, jobs using an AWS Snowball Edge device must be completed within 360 days of being prepared. If you need to keep one or more devices for longer than 360 days, see [Updating the SSL certificate on Snowball Edge devices](update-ssl-cert.md). Otherwise, after 360 days,the device becomes locked, can no longer be accessed, and must be returned. If the AWS Snowball Edge device becomes locked during an import job, we can still transfer the existing data on the device into Amazon S3.
+ If you encounter unexpected errors using an AWS Snowball Edge device, we want to hear about it. Copy the relevant logs and include them along with a brief description of the issues that you encountered in a message to AWS Support. For more information about logs, see [Configuring and using the Snowball Edge Client](using-client-commands.md).

**Topics**
+ [How to identify a Snowball Edge](identifying-device.md)
+ [Troubleshooting boot‐up problems with Snowball Edge](boot-troubleshoot.md)
+ [Troubleshooting connection problems with Snowball Edge](connection-troubleshooting.md)
+ [Troubleshooting `unlock-device` command problems with Snowball Edge](unlock-command-troubleshooting.md)
+ [Troubleshooting credentials problems with Snowball Edge](credentials-troubleshooting.md)
+ [Troubleshooting data transfer problems with Snowball Edge](transfer-troubleshooting.md)
+ [Troubleshooting AWS CLI problems with Snowball Edge](cli-troubleshooting.md)
+ [Troubleshooting compute instances on Snowball Edge](troubleshooting-ec2-edge.md)