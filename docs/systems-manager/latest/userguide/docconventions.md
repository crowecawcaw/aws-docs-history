# Document conventions

The following are common typographical conventions for the _AWS Systems Manager User Guide_.

**Differentiated examples for local operating systems or command line
languages**

We use tabs to present different examples of commands based on a user's local
operating system type. For Linux and macOS examples, we use the backslash
(`\` ) character to break long commands into multiple lines. For
Windows Server examples, we use the caret (`^`) character to break commands
into multiple lines.

Example:

Linux & macOS

```
aws ssm update-service-setting \
    --setting-id arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier \
    --setting-value advanced
```

Windows

```
aws ssm update-service-setting ^
    --setting-id arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier ^
    --setting-value advanced
```

**Elements in the user interface**

Formatting: Text in bold

Example: Choose **File**,
**Properties**.

**User input (text that a user types)**

Formatting: Text in a monospace font

Example: For the name, type `my-new-resource`.

**Placeholder text for a required value**

Formatting: Text in `italics`

Example:

```
aws ec2 register-image --image-location `amzn-s3-demo-bucket`/image.manifest.xml
```
