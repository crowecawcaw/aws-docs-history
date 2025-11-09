# **eb init**

## Description

Sets default values for Elastic Beanstalk applications created with EB CLI by prompting you with a
series of questions.

###### Note

The values you set with **eb init** apply to the current directory and
repository on the current computer.

The command creates an Elastic Beanstalk application in your account. To create an Elastic Beanstalk environment, run **[eb
create](eb3-create.md "eb3-create.md")** after running **eb init**.

## Syntax

**eb init**

**eb init**
`application-name`

## Options

If you run **eb init** without specifying the `--platform` option, the EB CLI prompts you
to enter a value for each setting.

###### Note

To use **eb init** to create a new key pair, you must have
`ssh-keygen` installed on your local machine and available from the command
line.

| Name                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| `-i`<br>`--interactive`                                          | Forces EB CLI to prompt you to provide a value for every **eb init\*<br>• command option.<br>NoteThe `init` command prompts you to provide values for **eb init*<br>• command options that do not have a (default) value.<br>After the first time you run the \*\*eb init*<br>• command in a directory, EB CLI might not prompt you about any command options.<br>Therefore, use the `--interactive` option when you want to change a setting that you previously set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |     |
| `-k`<br>`keyname`<br>`--keyname`<br>`keyname`                    | The name of the Amazon EC2 key pair to use with the Secure Shell (SSH) client to securely log in to the Amazon EC2 instances running your Elastic Beanstalk<br>application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |
| `--modules `folder-1 folder-2``                                  | List of child directories to initialize. Only for use with [Compose Environments](ebcli-compose.md "ebcli-compose.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |
| `-p`<br>`platform-version`<br>`--platform`<br>`platform-version` | The [platform version](concepts.md "concepts.md") to use.<br>You can specify a platform, a platform and version, a platform branch, a solution stack name, or a solution stack ARN. For example:<br>• `php`, `PHP`, `node.js` – The latest platform version for the specified platform<br>• `php-7.2`, `"PHP 7.2"` – The recommended (typically latest) PHP 7.2 platform version<br>• `"PHP 7.2 running on 64bit Amazon Linux"` – The recommended (typically latest) PHP platform version in this platform branch<br>• `"64bit Amazon Linux 2017.09 v2.6.3 running PHP 7.1"` – The PHP platform version specified by this solution stack name<br>• `"arn:aws:elasticbeanstalk:us-east-2::platform/PHP 7.1 running on 64bit Amazon Linux/2.6.3"` – The PHP<br>platform version specified by this solution stack ARN<br>Use [eb platform list](eb3-platform.md "eb3-platform.md") to get a list of available configurations.<br>Specify the `--platform` option to skip interactive configuration.<br>NoteWhen you specify this option, then EB CLI does not prompt you for values for any other options. Instead, it assumes default values for<br>each option. You can specify options for anything for which you do not want to use default values. |     |
| `--source codecommit/`repository-name`/`branch-name``            | CodeCommit repository and branch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |     |
| `-﻿-﻿tags `key1`=`value1`[,`key2`=`value2` ...]`                 | Tag your application. Tags are specified as a comma-separated list of `key=value` pairs.<br>For more details, see [Tagging applications](applications-tagging.md "applications-tagging.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Common options](eb3-cmd-options.md "eb3-cmd-options.md")        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |

## CodeBuild support

If you run **eb init** in a folder that contains a [buildspec.yml](../../../codebuild/latest/userguide/build-spec-ref.md "../../../codebuild/latest/userguide/build-spec-ref.md") file, Elastic Beanstalk
parses the file for an **eb_codebuild_settings** entry with options specific to Elastic Beanstalk. For information about CodeBuild support in Elastic Beanstalk, see
[Using the EB CLI with AWS CodeBuild](eb-cli-codebuild.md "eb-cli-codebuild.md").

## Output

If successful, the command guides you through setting up a new Elastic Beanstalk application through
a series of prompts.

## Example

The following example request initializes EB CLI and prompts you to enter information
about your application. Replace `placeholder` text with your own values.

```
$ `eb init -i`
Select a default region
1) us-east-1 : US East (N. Virginia)
2) us-west-1 : US West (N. California)
3) us-west-2 : US West (Oregon)
4) eu-west-1 : Europe (Ireland)
5) eu-central-1 : Europe (Frankfurt)
6) ap-south-1 : Asia Pacific (Mumbai)
7) ap-southeast-1 : Asia Pacific (Singapore)
...
(default is 3): `3`

Select an application to use
1) HelloWorldApp
2) NewApp
3) [ Create new Application ]
(default is 3): `3`

Enter Application Name
(default is "tmp"):
Application tmp has been created.

It appears you are using PHP. Is this correct?
(y/n): `y`

Select a platform branch.
1) PHP 7.2 running on 64bit Amazon Linux
2) PHP 7.1 running on 64bit Amazon Linux (Deprecated)
3) PHP 7.0 running on 64bit Amazon Linux (Deprecated)
4) PHP 5.6 running on 64bit Amazon Linux (Deprecated)
5) PHP 5.5 running on 64bit Amazon Linux (Deprecated)
6) PHP 5.4 running on 64bit Amazon Linux (Deprecated)
(default is 1): `1`
Do you want to set up SSH for your instances?
(y/n): `y`

Select a keypair.
1) aws-eb
2) [ Create new KeyPair ]
(default is 2): `1`
```
