# File Server Resource Manager on FSx for Windows File Server

File Server Resource Manager (FSRM) is a Windows Server feature that helps you manage and classify data stored on your Amazon FSx for Windows File Server file system. FSRM provides automated policy enforcement and reporting capabilities that help you control storage costs, maintain compliance with data management policies, and organize files based on business rules.

With FSRM, you can set storage limits to prevent users from consuming excessive storage, automatically identify and classify sensitive data, block unauthorized file types from being saved to business folders, and generate detailed reports about storage usage patterns. These capabilities help you maintain an organized, efficient, and compliant file system without requiring manual intervention for every file or folder.

FSRM is particularly valuable for organizations that need to:

- Control storage costs by limiting how much disk space users and departments can store
- Identify sensitive data such as personally identifiable information or financial records
- Enforce policies about which file types are allowed in specific folders
- Generate compliance reports about data retention, file ownership, or storage usage
- Maintain visibility into how storage is being used across the organization

## Key capabilities

- **[Quota Management](fsrm-quota-management.md "fsrm-quota-management.md")** - Set storage limits on folders to control how much space users and applications can consume. You can configure hard quotas that prevent users from exceeding limits or soft quotas that allow overages while sending notifications. Quotas help you manage storage costs and prevent users or departments from consuming disproportionate amounts of storage.
- **[File Screening](fsrm-file-screening.md "fsrm-file-screening.md")** - Control which types of files users can save to specific folders. You can block unauthorized file types such as executable files, media files, or personal documents in business folders. File screening helps you enforce data management policies, reduce security risks, and prevent storage waste from non-business files.
- **[File Classification](fsrm-file-classification.md "fsrm-file-classification.md")** - Automatically assign metadata properties to files based on their content or location. Classification helps you organize files, identify sensitive data, apply retention policies, and generate reports based on file characteristics. You can classify files by data sensitivity, department, retention period, or any other custom properties you define.
- **[Storage Reports](fsrm-storage-reports.md "fsrm-storage-reports.md")** - Generate detailed reports about file system usage, including large files, duplicate files, files by owner, files by type, and quota usage. Storage reports help you understand how storage is being consumed, identify files that can be archived or deleted, and make informed decisions about storage management.

###### Topics

- [Getting Started with File Server Resource Manager](enabling-fsrm.md "enabling-fsrm.md")
- [Quota Management](fsrm-quota-management.md "fsrm-quota-management.md")
- [File Groups](fsrm-file-groups.md "fsrm-file-groups.md")
- [File Screening](fsrm-file-screening.md "fsrm-file-screening.md")
- [File Classification](fsrm-file-classification.md "fsrm-file-classification.md")
- [Storage Reports](fsrm-storage-reports.md "fsrm-storage-reports.md")
- [File Management Tasks](fsrm-file-management.md "fsrm-file-management.md")
- [FSRM Settings](fsrm-settings.md "fsrm-settings.md")
- [Event Logs](fsrm-event-logs.md "fsrm-event-logs.md")
- [Common Use Cases](fsrm-common-use-cases.md "fsrm-common-use-cases.md")
