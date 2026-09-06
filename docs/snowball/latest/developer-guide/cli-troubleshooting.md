

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/). 

# Troubleshooting AWS CLI problems with Snowball Edge
<a name="cli-troubleshooting"></a>

Use the following topics to help you resolve problems when working with an AWS Snowball Edge device and the AWS CLI. 

## Troubleshooting AWS CLI error message: "Profile Cannot Be Null" with Snowball Edge
<a name="null-profile-troubleshooting"></a>

When working with the AWS CLI, you might encounter an error message that says Profile cannot be null. You can encounter this error if the AWS CLI hasn't been installed or an AWS CLI profile hasn't been configured.

**Action to take**  
Ensure that you have downloaded and configured the AWS CLI on your workstation. For more information, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide.*

## Troubleshooting null pointer error when transferring data with the AWS CLI with Snowball Edge
<a name="null-pointer-troubleshooting"></a>

When using the AWS CLI to transfer data, you might encounter a null pointer error. This error can occur in the following conditions:
+ If the specified file name is misspelled, for example `flowwer.png` or `flower.npg` instead of `flower.png`
+ If the specified path is incorrect, for example `C:\Documents\flower.png` instead of `C:\Documents\flower.png`
+ If the file is corrupted

**Action to take**  
Confirm that your file name and path are correct, and try again. If you continue to experience this issue, confirm that the file has not been corrupted, abandon the transfer, or attempt repairs to the file.