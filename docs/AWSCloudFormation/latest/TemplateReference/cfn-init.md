

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# cfn-init
<a name="cfn-init"></a>

In a CloudFormation template, you can use `AWS::CloudFormation::Init` within the `Metadata` section of an Amazon EC2 resource to define initialization tasks. For more information, see [`AWS::CloudFormation::Init`](aws-resource-init.md).

The `cfn-init` helper script reads template metadata from the `AWS::CloudFormation::Init` key and acts accordingly to:
+ Fetch and parse metadata from CloudFormation
+ Install packages
+ Write files to disk
+ Enable/disable and start/stop services

The `cfn-init` helper script is typically run from an Amazon EC2 instance's or launch template's user data.

If you're new to using helper scripts, we recommend you first complete the [Deploying applications on Amazon EC2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/deploying.applications.html) tutorial in the *AWS CloudFormation User Guide*.

**Topics**
+ [Syntax](#cfn-init-Syntax)
+ [Options](#cfn-init-options)
+ [Examples](#cfn-init-examples)
+ [Related resources](#cfn-init-related-resources)

**Note**  
If you use `cfn-init` to update an existing file, it creates a backup copy of the original file in the same directory with a .bak extension. For example, if you update `/{{path}}/{{to}}/{{file_name}}`, the action produces two files: `/{{path}}/{{to}}/{{file_name}}.bak` contains the original file's contents and `/{{path}}/{{to}}/{{file_name}}` contains the updated contents.

## Syntax
<a name="cfn-init-Syntax"></a>

```
cfn-init --stack|-s {{stack.name.or.id}} \
         --resource|-r {{logical.resource.id}} \
         --region {{region}} \
         --access-key {{access.key}} \
         --secret-key {{secret.key}} \
         --role {{rolename}} \
         --credential-file|-f {{credential.file}} \
         --configsets|-c {{config.sets}} \
         --url|-u {{service.url}} \
         --http-proxy {{HTTP.proxy}} \
         --https-proxy {{HTTPS.proxy}} \
         --verbose|-v
```

**Note**  
`cfn-init` doesn't require credentials, so you don't need to use the `--access-key`, `--secret-key`, `--role`, or `--credential-file` options. However, if no credentials are specified, CloudFormation checks for stack membership and limits the scope of the call to the stack that the instance belongs to. For more information, see [Permissions for helper scripts](cfn-helper-scripts-reference.md#cfn-helper-scripts-reference-permissions).

## Options
<a name="cfn-init-options"></a>


| Name | Description | Required | 
| --- | --- | --- | 
|  `-s, --stack`  | Stack name or stack ID.<br />*Type*: String<br />*Default*: None<br />*Example*: `--stack { "Ref" : "AWS::StackName" },` | Yes | 
|  `-r, --resource `  | The logical resource ID of the resource that contains the metadata.<br />*Type*: String<br />*Example*: `--resource WebServerHost` | Yes | 
|  `--region`  | The CloudFormation regional endpoint to use.<br />*Type*: String<br />*Default*: `us-east-1`<br />*Example*:`--region ", { "Ref" : "AWS::Region" },` | No | 
|  `--access-key`  | AWS access key for an account with permission to call `DescribeStackResource` on CloudFormation. The credential file parameter supersedes this parameter.<br />*Type*: String | No | 
|  `--secret-key`  | AWS secret access key that corresponds to the specified AWS access key.<br />*Type*: String | No | 
|  `--role`  | The name of an IAM role that's associated with the instance.<br />*Type*: String<br />Condition: The credential file parameter supersedes this parameter. | No | 
|  `-f, --credential-file`  | A file that contains both a secret access key and an access key. The credential file parameter supersedes the --role, --access-key, and --secret-key parameters.<br />*Type*: String | No | 
|  `-c, --configsets`  | A comma-separated list of configsets to run (in order).<br />*Type*: String<br />*Default*: `default` | No | 
|  `-u, --url`  | The CloudFormation endpoint to use.<br />*Type*: String | No | 
| `--http-proxy` | An HTTP proxy (non-SSL). Use the following format: `http://{{user:password}}@{{host}}:{{port}}`<br />*Type*: String | No | 
| `--https-proxy` | An HTTPS proxy. Use the following format: `https://{{user:password}}@{{host}}:{{port}}`<br />*Type*: String | No | 
| `-v, --verbose` | Verbose output. This is useful for debugging cases where `cfn-init` is failing to initialize. To debug initialization events, you should turn `DisableRollback` on. You can then SSH into the console and read the logs at `/var/log/cfn-init.log`. For more information, see [Choose how to handle failures when provisioning resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-failure-options.html) in the *AWS CloudFormation User Guide*.  | No | 
| `-h, --help` | Shows the help message and exits. | No | 

## Examples
<a name="cfn-init-examples"></a>

### Amazon Linux examples
<a name="w2aac32c27c21b3"></a>

The following examples show the `UserData` property of an EC2 instance, which runs the `InstallAndRun` configset that's associated with the `WebServerInstance` resource.

To include the latest version, add `yum install -y aws-cfn-bootstrap` to the `UserData`.

#### JSON
<a name="cfn-init-example.json"></a>

`UserData` property using the `Fn::Join` intrinsic function.

```
{
    "UserData": {
        "Fn::Base64": {
            "Fn::Join": [
                "",
                [
                    "#!/bin/bash -xe\n",
                    "",
                    "yum install -y aws-cfn-bootstrap",
                    "/opt/aws/bin/cfn-init -v ",
                    "         --stack ",
                    {
                        "Ref": "AWS::StackName"
                    },
                    "         --resource WebServerInstance ",
                    "         --configsets InstallAndRun ",
                    "         --region ",
                    {
                        "Ref": "AWS::Region"
                    },
                    "\n"
                ]
            ]
        }
    }
}
```

#### YAML
<a name="cfn-init-example.yaml"></a>

`UserData` property using the `Fn::Sub` intrinsic function.

```
UserData:
  Fn::Base64: !Sub |
    #!/bin/bash -xe
    yum update -y aws-cfn-bootstrap
    # Install the files and packages from the metadata
    /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource WebServerInstance --configsets InstallAndRun --region ${AWS::Region}
```

## Related resources
<a name="cfn-init-related-resources"></a>

For a tutorial with a sample template, see [Deploying applications on Amazon EC2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/deploying.applications.html) in the *AWS CloudFormation User Guide*.

For a Windows example, see [Bootstrapping Windows-based CloudFormation stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-windows-stacks-bootstrapping.html) in the *AWS CloudFormation User Guide*.

You can also visit our GitHub repository to download [sample templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html#sample-templates) that use `cfn-init`, including the following templates.
+  [InstanceWithCfnInit.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/EC2/InstanceWithCfnInit.yaml) 
+  [AutoScalingRollingUpdates.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/AutoScaling/AutoScalingRollingUpdates.yaml) 

For example LAMP stack templates that use `cfn-init`, see [ec2-lamp-server](https://github.com/aws-samples/ec2-lamp-server) on the GitHub website.