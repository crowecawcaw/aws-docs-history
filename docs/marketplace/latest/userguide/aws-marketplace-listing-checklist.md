

# AMI product checklist for AWS Marketplace
<a name="aws-marketplace-listing-checklist"></a>

Before submitting your Amazon Machine Image (AMI) product to AWS, use this checklist to validate your submission. Following these requirements will help ensure an efficient publication process.

## Product usage
<a name="product-usage-checklist"></a>
+ AMI is production-ready.
+ Product usage is not restricted by time or any other measurements.
+ AMI is compatible with the 1-click fulfillment experience.
+ Everything required to use the product is in the software, including client applications. Products that require external dependencies, such as software packages or client applications, follow the [Product usage policies](product-and-ami-policies.md#product-usage) that include proper disclosure.
+ AMI meets the mandatory [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md). 
+ No additional license is required to use the product. 
+ The buyer doesn't have to provide personally identifiable information (for example, their email address) to use the product.

## AMI preparation
<a name="ami-preparation-checklist"></a>
+ Your product name and description must match the **Description** field of the AMI product that you are providing.
+ Uses Hardware Virtual Machine (HVM) virtualization and 64-bit architecture. 
+ Product does not contain any known vulnerabilities, malware, or viruses. 
+ Customers are able to access the instance over network and use administrative access.
+ No hardcoded secrets are present on the AMI. Examples of hardcoded secrets include default passwords for system users and services, private keys, and credentials.
+ No hardcoded SSH authorized public keys are present on the AMI.
+ The Test 'Add Version' validation test completes successfully with no issues.

## Windows AMIs
<a name="windows-amis-checklist"></a>
+ For Windows Server 2012 and later operating systems, your AMI uses the latest version of [EC2Launch v2](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch-v2-install.html).
+ If you're using EC2Launch v2, complete the following:
  + In [Amazon EC2Launch settings](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch-v2-settings.html#ec2launch-v2-ui), choose **Random** under **Set administrator account** to have an administrator password generated at runtime.
  + In [Amazon EC2Launch settings](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch-v2-settings.html#ec2launch-v2-ui), select **Re-enable and start SSM service after Sysprep**.
  + Add **UserData** to the [EC2 v2 task configuration](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch-v2-settings.html#ec2launch-v2-task-configuration).
+ For Windows Server 2012 and later versions, avoid using [EC2Config](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/UsingConfig_Install.html). If EC2Config is required, ensure that you use the latest version.
+ If you use EC2Config, enable the following parameters in the [settings files](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2config-service.html#UsingConfigXML_WinAMI) for your AMI:
  + `Ec2SetPassword`
  + `Ec2WindowsActivate`
  + `Ec2HandleUserData`
+ Ensure that there are no guest accounts or remote desktop users present.

## Linux AMIs
<a name="linux-amis-checklist"></a>
+ Remote login as superuser is prohibited.
+ Password-based remote access is prohibited.

## Product load form or Product tab
<a name="product-load-form-checklist"></a>
+ All required fields are completed. 
+ All values are within specified character limits. 
+ All URLs load without error. 
+ The product image is at least 110 pixels wide and between a 1:1 and 2:1 ratio. 
+ Pricing is specified for all enabled instance types (for hourly, hourly-based monthly pricing, and hourly-based annual pricing models). 
+ Monthly pricing is specified (for hourly-based monthly and monthly pricing models). 