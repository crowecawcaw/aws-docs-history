# EC2 Windows Utility Driver version history

The following table shows which `EC2WinUtil` drivers run on each version of Windows
Server on Amazon EC2. Earlier versions of the operating system use the driver that's preinstalled on
AWS Windows Server AMIs that the instance launched from. AMIs that are shared with you or that
you subscribe to through AWS Marketplace don't have the driver preinstalled.

| Windows Server version | EC2WinUtil driver version |
| ---------------------- | ------------------------- |
| Windows Server 2025    | latest version            |
| Windows Server 2022    | latest version            |
| Windows Server 2019    | latest version            |
| Windows Server 2016    | latest version            |

###### Note

Prior to driver version 3.0.0, the `EC2WinUtil` driver was not
available to download for manual installation. Earlier versions were only
available as preinstalled drivers for AWS Windows AMIs.

The following table describes the released versions of the `EC2WinUtil`
driver.

| Package version                                                                                                                                                                          | Driver version | Details                                                                                                                               | Release date      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [3.1.0](https://s3.amazonaws.com/ec2-windows-drivers-downloads/EC2WinUtil/3.1.0/EC2WinUtil.zip "https://s3.amazonaws.com/ec2-windows-drivers-downloads/EC2WinUtil/3.1.0/EC2WinUtil.zip") | 3.1.0          | Improved power management event handling.                                                                                             | Feb 4, 2026       |
| 3.0.0                                                                                                                                                                                    | 3.0.0          | Modernized the driver for Windows 10 and added support for installation<br>as a primitive driver.                                     | June 13, 2024     |
| 2.0.0                                                                                                                                                                                    | 2.0.0          | Added support for output on MMIO serial ports for metal instance types. Also improved<br>crash parsing and updated the output format. | August 23, 2018   |
| 1.0.1                                                                                                                                                                                    | 1.0.1          | Changed the driver name to `EC2WinUtil` due to a namespace conflict<br>with Amazon Inspector. Several bug fixes are included.         | March 1, 2018     |
| 1.0.0                                                                                                                                                                                    | 1.0.0          | Initial release. The driver was initially called `AwsAgent`.                                                                          | November 28, 2017 |
