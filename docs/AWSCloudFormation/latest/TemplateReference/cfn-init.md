This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# cfn-init

In a CloudFormation template, you can use `AWS::CloudFormation::Init` within the
`Metadata` section of an Amazon EC2 resource to define initialization tasks. For
more information, see [AWS::CloudFormation::Init](aws-resource-init.md "aws-resource-init.md").

The `cfn-init` helper script reads template metadata from the
`AWS::CloudFormation::Init` key and acts accordingly to:

- Fetch and parse metadata from CloudFormation
- Install packages
- Write files to disk
- Enable/disable and start/stop services
  The `cfn-init` helper script is typically run from an Amazon EC2 instance's or
  launch template's user data.

If you're new to using helper scripts, we recommend you first complete the [Deploying applications
on Amazon EC2](../UserGuide/deploying.md "../UserGuide/deploying.md") tutorial in the _AWS CloudFormation User Guide_.

###### Topics

- [Syntax](#cfn-init-Syntax "#cfn-init-Syntax")
- [Options](#cfn-init-options "#cfn-init-options")
- [Examples](#cfn-init-examples "#cfn-init-examples")
- [Related resources](#cfn-init-related-resources "#cfn-init-related-resources")

###### Note

If you use `cfn-init` to update an existing file, it creates a backup copy
of the original file in the same directory with a .bak extension. For example, if you
update
`/`path`/`to`/`file_name``,
 the action produces two files:
 `/`path`/`to`/`file_name`.bak`
 contains the original file's contents and
 `/`path`/`to`/`file_name``
contains the updated contents.

## Syntax

```
cfn-init --stack|-s `stack.name.or.id` \
         --resource|-r `logical.resource.id` \
         --region `region` \
         --access-key `access.key` \
         --secret-key `secret.key` \
         --role `rolename` \
         --credential-file|-f `credential.file` \
         --configsets|-c `config.sets` \
         --url|-u `service.url` \
         --http-proxy `HTTP.proxy` \
         --https-proxy `HTTPS.proxy` \
         --verbose|-v

```

###### Note

`cfn-init` doesn't require credentials, so you don't need to use the
`--access-key`, `--secret-key`, `--role`, or
`--credential-file` options. However, if no credentials are specified,
CloudFormation checks for stack membership and limits the scope of the call to the stack
that the instance belongs to. For more information, see [Permissions for helper
scripts](cfn-helper-scripts-reference.md#cfn-helper-scripts-reference-permissions "cfn-helper-scripts-reference.md#cfn-helper-scripts-reference-permissions").

## Options

| Name                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `-s, --stack`           | Stack name or stack ID.<br>_Type_: String<br>_Default_: None<br>_Example_: `--stack { "Ref" : "AWS::StackName"<br>},`                                                                                                                                                                                                                                                                                                                                                                     | Yes      |
| `-r, --resource`        | The logical resource ID of the resource that contains the<br>metadata.<br>_Type_: String<br>_Example_: `--resource<br>WebServerHost`                                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `--region`              | The CloudFormation regional endpoint to use.<br>_Type_: String<br>_Default_: `us-east-1`<br>_Example_:`--region ", { "Ref" : "AWS::Region"<br>},`                                                                                                                                                                                                                                                                                                                                         | No       |
| `--access-key`          | AWS access key for an account with permission to call<br>`DescribeStackResource` on CloudFormation. The credential file<br>parameter supersedes this parameter.<br>_Type_: String                                                                                                                                                                                                                                                                                                         | No       |
| `--secret-key`          | AWS secret access key that corresponds to the specified AWS access<br>key.<br>_Type_: String                                                                                                                                                                                                                                                                                                                                                                                              | No       |
| `--role`                | The name of an IAM role that's associated with the instance.<br>_Type_: String<br>Condition: The credential file parameter supersedes this<br>parameter.                                                                                                                                                                                                                                                                                                                                  | No       |
| `-f, --credential-file` | A file that contains both a secret access key and an access key. The<br>credential file parameter supersedes the --role, --access-key, and<br>--secret-key parameters.<br>_Type_: String                                                                                                                                                                                                                                                                                                  | No       |
| `-c, --configsets`      | A comma-separated list of configsets to run (in order).<br>_Type_: String<br>_Default_: `default`                                                                                                                                                                                                                                                                                                                                                                                         | No       |
| `-u, --url`             | The CloudFormation endpoint to use.<br>_Type_: String                                                                                                                                                                                                                                                                                                                                                                                                                                     | No       |
| `--http-proxy`          | An HTTP proxy (non-SSL). Use the following format:<br>`http://`user:password`@`host`:`port``<br>_Type_: String                                                                                                                                                                                                                                                                                                                                                                            | No       |
| `--https-proxy`         | An HTTPS proxy. Use the following format:<br>`https://`user:password`@`host`:`port``<br>_Type_: String                                                                                                                                                                                                                                                                                                                                                                                    | No       |
| `-v, --verbose`         | Verbose output. This is useful for debugging cases where<br>`cfn-init` is failing to initialize.<br>NoteTo debug initialization events, you should turn<br>`DisableRollback` on. You can then SSH into the console<br>and read the logs at `/var/log/cfn-init.log`. For<br>more information, see [Choose how to handle<br>failures when provisioning resources](../UserGuide/stack-failure-options.md "../UserGuide/stack-failure-options.md") in the<br>_AWS CloudFormation User Guide_. | No       |
| `-h, --help`            | Shows the help message and exits.                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No       |

## Examples

### Amazon Linux examples

The following examples show the `UserData` property of an EC2 instance,
which runs the `InstallAndRun` configset that's associated with the
`WebServerInstance` resource.

To include the latest version, add `yum install -y aws-cfn-bootstrap`
to the `UserData`.

#### JSON

`UserData` property using the `Fn::Join` intrinsic
function.

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

`UserData` property using the `Fn::Sub` intrinsic
function.

```
UserData: !Base64
  Fn::Sub: |-
    #!/bin/bash -xe
    yum update -y aws-cfn-bootstrap
    # Install the files and packages from the metadata
    /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource WebServerInstance --configsets InstallAndRun --region ${AWS::Region}
```

## Related resources

For a tutorial with a sample template, see [Deploying applications on Amazon EC2](../UserGuide/deploying.md "../UserGuide/deploying.md")
in the _AWS CloudFormation User Guide_.

For a Windows example, see [Bootstrapping
Windows-based CloudFormation stacks](../UserGuide/cfn-windows-stacks-bootstrapping.md "../UserGuide/cfn-windows-stacks-bootstrapping.md") in the
_AWS CloudFormation User Guide_.

You can also visit our GitHub repository to download [sample
templates](../UserGuide/template-guide.md#sample-templates "../UserGuide/template-guide.md#sample-templates") that use `cfn-init`, including the following
templates.

- [InstanceWithCfnInit.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/EC2/InstanceWithCfnInit.yaml "https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/EC2/InstanceWithCfnInit.yaml")
- [AutoScalingRollingUpdates.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/AutoScaling/AutoScalingRollingUpdates.yaml "https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/AutoScaling/AutoScalingRollingUpdates.yaml")

For example LAMP stack templates that use `cfn-init`,
see [ec2-lamp-server](https://github.com/aws-samples/ec2-lamp-server "https://github.com/aws-samples/ec2-lamp-server")
on the GitHub website.
