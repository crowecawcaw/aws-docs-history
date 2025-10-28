# Best practices for using FSx for Windows File Server with

Amazon ECS

Make note of the following best practice recommendations when you use FSx for Windows File Server
with Amazon ECS.

## Security and access controls for

FSx for Windows File Server

FSx for Windows File Server offers the following access control features that you can use to
ensure that the data stored in an FSx for Windows File Server file system is secure and accessible
only from applications that need it.

### Data encryption for FSx for Windows File Server volumes

FSx for Windows File Server supports two forms of encryption for file systems. They are
encryption of data in transit and encryption at rest. Encryption of data in
transit is supported on file shares that are mapped on a container instance that
supports SMB protocol 3.0 or newer. Encryption of data at rest is automatically
enabled when creating an Amazon FSx file system. Amazon FSx automatically encrypts
data in transit using SMB encryption as you access your file system without the
need for you to modify your applications. For more information, see [Data
encryption in Amazon FSx](../../../fsx/latest/WindowsGuide/encryption.md "../../../fsx/latest/WindowsGuide/encryption.md") in the
_Amazon FSx for Windows File Server User Guide_.

### Use

Windows ACLs for folder level access control

The Windows Amazon EC2 instance access Amazon FSx file shares using Active Directory
credentials. It uses standard Windows access control lists (ACLs) for
fine-grained file-level and folder-level access control. You can create multiple
credentials, each one for a specific folder within the share which maps to a
specific task.

In the following example, the task has access to the folder `App01`
using a credential saved in Secrets Manager. Its Amazon Resource Name (ARN) is
`1234`.

```
"rootDirectory": "`\\path\\to\\my\\data\App01`",
"credentialsParameter": "`arn-1234`",
"domain": "corp.fullyqualified.com",
```

In another example, a task has access to the folder `App02` using a
credential saved in the Secrets Manager. Its ARN is `6789`.

```
"rootDirectory": "`\\path\\to\\my\\data\App02`",
"credentialsParameter": "`arn-6789`",
"domain": "corp.fullyqualified.com",
```
