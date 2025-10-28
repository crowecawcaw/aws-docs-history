# Storage

The storage services we use across this guide are:

- Amazon EBS
  - Provides persistent storage for SAP application and database. The EBS volumes can be resized and even the EBS volume type can be changed without disrupting the applications. For more information, see [Requesting Modifications to Your EBS Volumes](../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md "../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md"). You will need to [extend the filesystem](../../../AWSEC2/latest/WindowsGuide/recognize-expanded-volume-windows.md "../../../AWSEC2/latest/WindowsGuide/recognize-expanded-volume-windows.md") to match the extended volume size using the Windows operating system tools.

- Amazon FSx for Windows File Server
  - Does not need you to explicitly provision storage at all – you simply pay for what you use.
  - Does need regular maintenance, but you can define your own maintenance window as per [Amazon FSx Maintenance Windows](../../../fsx/latest/WindowsGuide/maintenance-windows.md "../../../fsx/latest/WindowsGuide/maintenance-windows.md").
  - The Amazon FSx Service Level Agreement provides for a service credit if your monthly uptime percentage is below our service commitment in any billing cycle.

- Amazon S3
  - Does not need you to explicitly provision storage at all – you simply pay for what you use.
  - You can use [Object Lifecycle Management](../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md "../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md") to set rules that define when objects are transitioned or archived to colder storage, such as S3 Standard-IA, S3 Glacier, or S3 Glacier Deep Archive, and when they expire. These actions happen automatically after being set.
