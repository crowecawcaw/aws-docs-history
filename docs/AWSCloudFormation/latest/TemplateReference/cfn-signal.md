This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# cfn-signal

The `cfn-signal` helper script signals CloudFormation to indicate whether Amazon EC2
instances have been successfully created or updated. If you install and configure software
applications on instances, you can signal CloudFormation when those software applications are
ready.

You use the `cfn-signal` script in conjunction with a [CreationPolicy attribute](aws-attribute-creationpolicy.md "aws-attribute-creationpolicy.md") or
an [UpdatePolicy attribute](aws-attribute-updatepolicy.md "aws-attribute-updatepolicy.md")
with `WaitOnResourceSignals` for Amazon EC2 Auto Scaling groups. When CloudFormation creates or
updates resources with those policies, it suspends work on the stack until the resource
receives the required number of signals or until the timeout period is exceeded. For each
valid signal that CloudFormation receives, it publishes the signals to the stack events so that
you track each signal.

###### Topics

- [Syntax for resource signaling (recommended)](#w2294aac32c29b9 "#w2294aac32c29b9")
- [Syntax for use with wait condition
  handle](#cfn-signal-Syntaxwaitcondition "#cfn-signal-Syntaxwaitcondition")
- [Options](#cfn-signal-options "#cfn-signal-options")
- [Examples](#cfn-signal-examples "#cfn-signal-examples")
- [Related resources](#cfn-signal-related-resources "#cfn-signal-related-resources")

## Syntax for resource signaling (recommended)

If you want to signal CloudFormation resources, use the following syntax.

```
cfn-signal --success|-s `signal.to.send` \
        --access-key `access.key` \
        --credential-file|-f `credential.file` \
        --exit-code|-e `exit.code` \
        --http-proxy `HTTP.proxy` \
        --https-proxy `HTTPS.proxy` \
        --id|-i `unique.id` \
        --region `AWS.region` \
        --resource `resource.logical.ID` \
        --role `IAM.role.name` \
        --secret-key `secret.key` \
        --stack `stack.name.or.stack.ID` \
        --url `AWS CloudFormation.endpoint`
```

###### Note

`cfn-signal` doesn't require credentials, so you don't need to use the
`--access-key`, `--secret-key`, `--role`, or
`--credential-file` options. However, if no credentials are specified,
CloudFormation checks for stack membership and limits the scope of the call to the stack
that the instance belongs to. For more information, see [Permissions for helper
scripts](cfn-helper-scripts-reference.md#cfn-helper-scripts-reference-permissions "cfn-helper-scripts-reference.md#cfn-helper-scripts-reference-permissions").

## Syntax for use with wait condition

handle

If you want to signal a wait condition handle, use the following syntax.

```
cfn-signal --success|-s `signal.to.send` \
        --reason|-r `resource.status.reason` \
        --data|-d `data` \
        --id|-i `unique.id` \
        --exit-code|-e `exit.code` \
        `waitconditionhandle.url`
```

## Options

The options that you can use depend on whether you're signaling a creation policy or
a wait condition handle. Some options that apply to a creation policy might not apply to
a wait condition handle.

| Name                                                   | Description                                                                                                                                                                                                                                                                | Required |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--access-key` (resource signaling only)               | AWS access key for an account with permission to call the CloudFormation `SignalResource` API. The credential file parameter supersedes this parameter. _Type_: String                                                                                                     | No       |
| `-d, --data` (wait condition handle only)              | Data to send back with the `waitConditionHandle`. Defaults to blank. _Type_: String _Default_: blank                                                                                                                                                                       | No       |
| `-e, --exit-code`                                      | The error code from a process that can be used to determine success or failure. If specified, the `--success` option is ignored. _Type_: String _Examples_: `-e $?` (for Linux), `-e %ERRORLEVEL%` (for Windows cmd.exe), and `-e $lastexitcode` (for Windows PowerShell). | No       |
| `-f, --credential-file` (resource signaling only)      | A file that contains both a secret access key and an access key. The credential file parameter supersedes the --role, --access-key, and --secret-key parameters. _Type_: String                                                                                            | No       |
| `--http-proxy`                                         | An HTTP proxy (non-SSL). Use the following format: `http://`user:password`@`host`:`port`` _Type_: String                                                                                                                                                                   | No       |
| `--https-proxy`                                        | An HTTPS proxy. Use the following format: `https://`user:password`@`host`:`port`` _Type_: String                                                                                                                                                                           | No       |
| `-i, --id`                                             | The unique ID to send. _Type_: String _Default_: The ID of the Amazon EC2 instance. If the ID can't be resolved, the machine's Fully Qualified Domain Name (FQDN) is returned.                                                                                             | No       |
| `-r, --reason` (wait condition handle only)            | A status reason for the resource event (currently only used on failure) - defaults to 'Configuration failed' if success is false. _Type_: String                                                                                                                           | No       |
| `--region` (resource signaling only)                   | The CloudFormation regional endpoint to use. _Type_: String _Default_: `us-east-1`                                                                                                                                                                                         | No       |
| `--resource` (resource signaling only)                 | The logical ID of the resource that contains the creations policy you want to signal. _Type_: String                                                                                                                                                                       | Yes      |
| `--role` (resource signaling only)                     | The name of an IAM role that's associated with the instance. _Type_: String Condition: The credential file parameter supersedes this parameter.                                                                                                                            | No       |
| `-s, --success`                                        | If true, signal `SUCCESS`, else `FAILURE`. _Type_: Boolean _Default_: `true`                                                                                                                                                                                               | No       |
| `--secret-key` (resource signaling only)               | AWS secret access key that corresponds to the specified AWS access key. _Type_: String                                                                                                                                                                                     | No       |
| `--stack` (resource signaling only)                    | The stack name or stack ID that contains the resource you want to signal. _Type_: String                                                                                                                                                                                   | Yes      |
| `-u, --url` (resource signaling only)                  | The CloudFormation endpoint to use. _Type_: String                                                                                                                                                                                                                         | No       |
| `waitconditionhandle.url` (wait condition handle only) | A presigned URL that you can use to signal success or failure to an associated `WaitCondition` _Type_: String                                                                                                                                                              | Yes      | ## Examples ### Amazon Linux example A common usage pattern is to use `cfn-init` and `cfn-signal` together. The `cfn-signal` call uses the return status of the call to `cfn-init` (using the $? shell construct). If the application fails to install, the instance will fail to create and the stack will rollback. #### JSON `{ "AWSTemplateFormatVersion": "2010-09-09", "Description": "Simple EC2 instance", "Resources": { "MyInstance": { "Type": "AWS::EC2::Instance", "Metadata": { "AWS::CloudFormation::Init": { "config": { "files": { "/tmp/test.txt": { "content": "Hello world!", "mode": "000755", "owner": "root", "group": "root" } } } } }, "Properties": { "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}", "InstanceType": "t2.micro", "UserData": { "Fn::Base64": { "Fn::Join": [ "", [ "#!/bin/bash -x\n", "# Install the files and packages from the metadata\n", "yum install -y aws-cfn-bootstrap", "\n", "/opt/aws/bin/cfn-init -v ", "         --stack ", { "Ref": "AWS::StackName" }, "         --resource MyInstance ", "         --region ", { "Ref": "AWS::Region" }, "\n", "# Signal the status from cfn-init\n", "/opt/aws/bin/cfn-signal -e $? ", "         --stack ", { "Ref": "AWS::StackName" }, "         --resource MyInstance ", "         --region ", { "Ref": "AWS::Region" }, "\n" ] ] } } }, "CreationPolicy": { "ResourceSignal": { "Timeout": "PT5M" } } } } }` #### YAML ``` AWSTemplateFormatVersion: 2010-09-09 Description: Simple EC2 instance Resources: MyInstance: Type: 'AWS::EC2::Instance' Metadata: 'AWS::CloudFormation::Init': config: files: /tmp/test.txt: content: Hello world! mode: '000755' owner: root group: root Properties: ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}' InstanceType: t2.micro UserData: !Base64 'Fn::Join': <br>• '' <br>• - | #!/bin/bash -x <br>• | # Install the files and packages from the metadata <br>• yum install -y aws-cfn-bootstrap <br>• | + <br>• | <br>• '/opt/aws/bin/cfn-init -v ' <br>• ' --stack ' <br>• !Ref 'AWS::StackName' <br>• ' --resource MyInstance ' <br>• ' --region ' <br>• !Ref 'AWS::Region' <br>• | + <br>• | # Signal the status from cfn-init <br>• '/opt/aws/bin/cfn-signal -e $? ' <br>• ' --stack ' <br>• !Ref 'AWS::StackName' <br>• ' --resource MyInstance ' <br>• ' --region ' <br>• !Ref 'AWS::Region' <br>• | + CreationPolicy: ResourceSignal: Timeout: PT5M ```## Related resources You can also visit our GitHub repository to download [sample templates](../UserGuide/template-guide.md#sample-templates "../UserGuide/template-guide.md#sample-templates") that use`cfn-signal`, including the following templates. <br>• [InstanceWithCfnInit.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/EC2/InstanceWithCfnInit.yaml "https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/EC2/InstanceWithCfnInit.yaml") <br>• [AutoScalingRollingUpdates.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/AutoScaling/AutoScalingRollingUpdates.yaml "https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/AutoScaling/AutoScalingRollingUpdates.yaml") |
