

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# cfn-signal
<a name="cfn-signal"></a>

The `cfn-signal` helper script signals CloudFormation to indicate whether Amazon EC2 instances have been successfully created or updated. If you install and configure software applications on instances, you can signal CloudFormation when those software applications are ready.

You use the `cfn-signal` script in conjunction with a [`CreationPolicy` attribute](aws-attribute-creationpolicy.md) or an [`UpdatePolicy` attribute](aws-attribute-updatepolicy.md) with `WaitOnResourceSignals` for Amazon EC2 Auto Scaling groups. When CloudFormation creates or updates resources with those policies, it suspends work on the stack until the resource receives the required number of signals or until the timeout period is exceeded. For each valid signal that CloudFormation receives, it publishes the signals to the stack events so that you track each signal.

**Topics**
+ [Syntax for resource signaling (recommended)](#w2aac32c29b9)
+ [Syntax for use with wait condition handle](#cfn-signal-Syntaxwaitcondition)
+ [Options](#cfn-signal-options)
+ [Examples](#cfn-signal-examples)
+ [Related resources](#cfn-signal-related-resources)

## Syntax for resource signaling (recommended)
<a name="w2aac32c29b9"></a>

If you want to signal CloudFormation resources, use the following syntax.

```
cfn-signal --success|-s {{signal.to.send}} \
        --access-key {{access.key}} \
        --credential-file|-f {{credential.file}} \
        --exit-code|-e {{exit.code}} \
        --http-proxy {{HTTP.proxy}} \
        --https-proxy {{HTTPS.proxy}} \
        --id|-i {{unique.id}} \
        --region {{AWS.region}} \
        --resource {{resource.logical.ID}} \
        --role {{IAM.role.name}} \
        --secret-key {{secret.key}} \
        --stack {{stack.name.or.stack.ID}} \
        --url {{CloudFormation.endpoint}}
```

**Note**  
`cfn-signal` doesn't require credentials, so you don't need to use the `--access-key`, `--secret-key`, `--role`, or `--credential-file` options. However, if no credentials are specified, CloudFormation checks for stack membership and limits the scope of the call to the stack that the instance belongs to. For more information, see [Permissions for helper scripts](cfn-helper-scripts-reference.md#cfn-helper-scripts-reference-permissions).

## Syntax for use with wait condition handle
<a name="cfn-signal-Syntaxwaitcondition"></a>

If you want to signal a wait condition handle, use the following syntax.

```
cfn-signal --success|-s {{signal.to.send}} \
        --reason|-r {{resource.status.reason}} \
        --data|-d {{data}} \
        --id|-i {{unique.id}} \
        --exit-code|-e {{exit.code}} \
        {{waitconditionhandle.url}}
```

## Options
<a name="cfn-signal-options"></a>

The options that you can use depend on whether you're signaling a creation policy or a wait condition handle. Some options that apply to a creation policy might not apply to a wait condition handle.


| Name | Description | Required | 
| --- | --- | --- | 
| `--access-key` (resource signaling only) | AWS access key for an account with permission to call the CloudFormation `SignalResource `API. The credential file parameter supersedes this parameter.<br />*Type*: String | No | 
| `-d, --data` (wait condition handle only) | Data to send back with the `waitConditionHandle`. Defaults to blank.<br />*Type*: String<br />*Default*: blank | No | 
| `-e, --exit-code`  | The error code from a process that can be used to determine success or failure. If specified, the `--success` option is ignored.<br />*Type*: String<br />*Examples*: `-e $?` (for Linux), `-e %ERRORLEVEL%` (for Windows cmd.exe), and `-e $lastexitcode` (for Windows PowerShell). | No | 
| `-f, --credential-file` (resource signaling only) | A file that contains both a secret access key and an access key. The credential file parameter supersedes the --role, --access-key, and --secret-key parameters.<br />*Type*: String | No | 
| `--http-proxy` | An HTTP proxy (non-SSL). Use the following format: `http://{{user:password}}@{{host}}:{{port}}`<br />*Type*: String | No | 
| `--https-proxy` | An HTTPS proxy. Use the following format: `https://{{user:password}}@{{host}}:{{port}}`<br />*Type*: String | No | 
| `-i, --id` | The unique ID to send.<br />*Type*: String<br />*Default*: The ID of the Amazon EC2 instance. If the ID can't be resolved, the machine's Fully Qualified Domain Name (FQDN) is returned. | No | 
| `-r, --reason ` (wait condition handle only) | A status reason for the resource event (currently only used on failure) - defaults to 'Configuration failed' if success is false.<br />*Type*: String | No | 
| --region (resource signaling only) | The CloudFormation regional endpoint to use.<br />*Type*: String<br />*Default*: `us-east-1` | No | 
| --resource (resource signaling only) | The logical ID of the resource that contains the creations policy you want to signal.<br />*Type*: String | Yes | 
| `--role` (resource signaling only) | The name of an IAM role that's associated with the instance.<br />*Type*: String<br />Condition: The credential file parameter supersedes this parameter. | No | 
| `-s, --success`  | If true, signal `SUCCESS`, else `FAILURE`.<br />*Type*: Boolean<br />*Default*: `true` | No | 
| `--secret-key` (resource signaling only) | AWS secret access key that corresponds to the specified AWS access key.<br />*Type*: String | No | 
| `--stack` (resource signaling only) | The stack name or stack ID that contains the resource you want to signal.<br />*Type*: String | Yes | 
| -u, --url (resource signaling only) | The CloudFormation endpoint to use.<br />*Type*: String | No | 
| `waitconditionhandle.url` (wait condition handle only) | A presigned URL that you can use to signal success or failure to an associated `WaitCondition`<br />*Type*: String | Yes | 

## Examples
<a name="cfn-signal-examples"></a>

### Amazon Linux example
<a name="w2aac32c29c15b3"></a>

A common usage pattern is to use `cfn-init` and `cfn-signal` together. The `cfn-signal` call uses the return status of the call to `cfn-init` (using the $? shell construct). If the application fails to install, the instance will fail to create and the stack will rollback.

#### JSON
<a name="cfn-signal-example.json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Simple EC2 instance",
    "Resources": {
        "MyInstance": {
            "Type": "AWS::EC2::Instance",
            "Metadata": {
                "AWS::CloudFormation::Init": {
                    "config": {
                        "files": {
                            "/tmp/test.txt": {
                                "content": "Hello world!",
                                "mode": "000755",
                                "owner": "root",
                                "group": "root"
                            }
                        }
                    }
                }
            },
            "Properties": {
                "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}",
                "InstanceType": "t2.micro",
                "UserData": {
                    "Fn::Base64": {
                        "Fn::Join": [
                            "",
                            [
                                "#!/bin/bash -x\n",
                                "# Install the files and packages from the metadata\n",
                                "yum install -y aws-cfn-bootstrap",
                                "\n",
                                "/opt/aws/bin/cfn-init -v ",
                                "         --stack ",
                                {
                                    "Ref": "AWS::StackName"
                                },
                                "         --resource MyInstance ",
                                "         --region ",
                                {
                                    "Ref": "AWS::Region"
                                },
                                "\n",
                                "# Signal the status from cfn-init\n",
                                "/opt/aws/bin/cfn-signal -e $? ",
                                "         --stack ",
                                {
                                    "Ref": "AWS::StackName"
                                },
                                "         --resource MyInstance ",
                                "         --region ",
                                {
                                    "Ref": "AWS::Region"
                                },
                                "\n"
                            ]
                        ]
                    }
                }
            },
            "CreationPolicy": {
                "ResourceSignal": {
                    "Timeout": "PT5M"
                }
            }
        }
    }
}
```

#### YAML
<a name="cfn-signal-example.yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Simple EC2 instance
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Metadata:
      'AWS::CloudFormation::Init':
        config:
          files:
            /tmp/test.txt:
              content: Hello world!
              mode: '000755'
              owner: root
              group: root
    Properties:
      ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}'
      InstanceType: t2.micro
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash -x
          # Install the files and packages from the metadata
          yum install -y aws-cfn-bootstrap
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource MyInstance --region ${AWS::Region}
          # Signal the status from cfn-init
          /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource MyInstance --region ${AWS::Region}
    CreationPolicy:
      ResourceSignal:
        Timeout: PT5M
```

## Related resources
<a name="cfn-signal-related-resources"></a>

You can also visit our GitHub repository to download [sample templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html#sample-templates) that use `cfn-signal`, including the following templates.
+  [InstanceWithCfnInit.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/EC2/InstanceWithCfnInit.yaml) 
+  [AutoScalingRollingUpdates.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/AutoScaling/AutoScalingRollingUpdates.yaml) 