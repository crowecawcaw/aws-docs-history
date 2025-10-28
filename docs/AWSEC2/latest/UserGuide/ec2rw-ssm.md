# Troubleshoot impaired Windows instance with EC2Rescue and Systems Manager

Support provides you with a Systems Manager Run Command document to interface with your
Systems Manager-enabled instance to run EC2Rescue for Windows Server. The Run Command document is called
`AWSSupport-RunEC2RescueForWindowsTool`.

This Systems Manager Run Command document performs the following tasks:

- Downloads and verifies EC2Rescue for Windows Server.
- Imports a PowerShell module to ease your interaction with the tool.
- Runs EC2RescueCmd with the provided command and parameters.
  The Systems Manager Run Command document accepts three parameters:

- **Command**—The EC2Rescue for Windows Server action. The current
  allowed values are:
  - **ResetAccess**—Resets the local Administrator password.
    The local Administrator password of the current instance will be reset and the
    randomly generated password will be securely stored in Parameter Store as
    `/EC2Rescue/Password/<INSTANCE_ID>`. If you select this action and
    provide no parameters, passwords are encrypted automatically with the default KMS key.
    Optionally, you can specify a KMS key ID in Parameters to encrypt the password with
    your own key.
  - **CollectLogs**—Runs EC2Rescue for Windows Server with the
    `/collect:all` action. If you select this action, `Parameters`
    must include an Amazon S3 bucket name to upload the logs to.
  - **FixAll**—Runs EC2Rescue for Windows Server with the
    `/rescue:all` action. If you select this action, `Parameters`
    must include the block device name to rescue.

- **Parameters**—The PowerShell parameters to pass for the
  specified command.

## Requirements

To run the **ResetAccess** action, your Amazon EC2 instance must
have the a policy attached that grants permissions to write the encrypted password
to Parameter Store. After attaching the policy, wait a few minutes before attempting
to reset the password of an instance after you have attached this policy to the
related IAM role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:PutParameter"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:parameter/EC2Rescue/Passwords/`<instanceid>`"
 ]
 }
 ]
}`

```

If you are using a custom KMS key, not the default KMS key, use this policy
instead.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:PutParameter"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:parameter/EC2Rescue/Passwords/`<instanceid>`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`<kmskeyid>`"
 ]
 }
 ]
}`

```

## View the JSON for the document

The following procedure describes how to view the JSON for this document.

###### To view the JSON for the Systems Manager Run Command document

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, expand **Change Management Tools** and choose
   **Documents**.
3. In the search bar, enter `AWSSupport-RunEC2RescueForWindowsTool`, and then
   select the `AWSSupport-RunEC2RescueForWindowsTool` document.
4. Choose the **Content** tab.

## Examples

Here are some examples on how to use the Systems Manager Run Command document to run
EC2Rescue for Windows Server, using the AWS CLI. For more information about sending commands using
the AWS CLI, see [send-command](../../../cli/latest/reference/ssm/send-command.md "../../../cli/latest/reference/ssm/send-command.md").

###### Examples

- [Attempt to fix all identified issues on an offline root
  volume](#ec2rw-ssm-exam1 "#ec2rw-ssm-exam1")
- [Collect logs from the current Amazon EC2 Windows
  instance](#ec2rw-ssm-exam2 "#ec2rw-ssm-exam2")
- [Reset the local Administrator password](#ec2rw-ssm-exam4 "#ec2rw-ssm-exam4")

### Attempt to fix all identified issues on an offline root

volume

Attempt to fix all identified issues on an offline root volume attached to an Amazon EC2
Windows instance:

```
aws ssm send-command --instance-ids "`i-0cb2b964d3e14fd9f`" --document-name "AWSSupport-RunEC2RescueForWindowsTool" --parameters "Command=FixAll, Parameters='`xvdf`'" --output text
```

### Collect logs from the current Amazon EC2 Windows

instance

Collect all logs from the current online Amazon EC2 Windows instance and upload them to an
Amazon S3 bucket:

```
aws ssm send-command --instance-ids "`i-0cb2b964d3e14fd9f`" --document-name "AWSSupport-RunEC2RescueForWindowsTool" --parameters "Command=CollectLogs, Parameters='`amzn-s3-demo-bucket`'" --output text
```

### Reset the local Administrator password

The following examples show methods you can use to reset the local Administrator
password. The output provides a link to Parameter Store, where you can find the randomly
generated secure password you can then use to RDP to your Amazon EC2 Windows instance as the
local Administrator.

Reset the local Administrator password of an online instance using the default AWS KMS key
alias/aws/ssm:

```
aws ssm send-command --instance-ids "`i-0cb2b964d3e14fd9f`" --document-name "AWSSupport-RunEC2RescueForWindowsTool" --parameters "Command=ResetAccess" --output text
```

Reset the local Administrator password of an online instance using a KMS key:

```
aws ssm send-command --instance-ids "`i-0cb2b964d3e14fd9f`" --document-name "AWSSupport-RunEC2RescueForWindowsTool" --parameters "Command=ResetAccess, Parameters=`a133dc3c-a2g4-4fc6-a873-6c0720104bf0`" --output text
```

###### Note

In this example, the KMS key is
`a133dc3c-a2g4-4fc6-a873-6c0720104bf0`.
