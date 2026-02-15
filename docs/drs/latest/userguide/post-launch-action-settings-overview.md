# Configuring the default post-launch actions

After finishing the AWS DRS initialization process, you can configure your default
post-launch actions settings. The default post-launch actions settings apply to newly
added source servers and controls which post-launch actions run when launching new
instances. These settings are created automatically for each server based on the default
settings and can be modified at any time for any individual source server.

You can also use this settings to install the IAM roles required for post-launch actions to work,
if the roles were not already installed in your account during the first initialization of AWS DRS.
The IAM roles need to be installed once per AWS account, regardless of the region used.

Post launch actions can be of two different types: command and automation.
Command post-launch actions run on the launched instance using the instance profile attached to the instance.
Note that if no instance profile is defined on the EC2 launch template, AWS Elastic Disaster Recovery (AWS DRS) places the **AWSElasticDisasterRecoveryRecoveryInstanceWithLaunchActionsRole** instance profile by default if post-launch actions is active for the source server.

Automation actions run with the credentials of the same IAM entity that started the
drill, recovery or failback. In addition some automation actions accept a parameter that
is sent to the assumeRole key in the SSM document if provided, the action assumes that
role for that action execution.

###### Note

- In order to use post-launch actions, you should make sure you have the required permissions. To get these permissions, you can attach the **AWSElasticDisasterRecoveryLaunchActionsPolicy**
  or **AWSElasticDisasterRecoveryConsoleFullAccess_v2** policies to your IAM identity.
  These policies contain the permissions needed to run SSM Command and Automation documents that are owned by Amazon or by the account as post-launch actions.
- Installation of the SSM Agent requires a minimum of 200 MB of free disk space and 200 KB of free disk space in the `/var` directory.
- Installation of the SSM Agent is not supported on these operating systems:
  - CentOS 5.x
  - CentOS 6.x
  - RHEL 6.x
  - Oracle 6.x
  - Amazon Linux 1
  - Windows 2008
  - Windows 2008 R2

###### Note

In order to run an SSM command or Automation document owned by a different account as a post-launch action you should
provide the permission to use `ssm:SendCommand` and `ssm:StartAutomation` on the relevant document.

For example, if you have shared the SSM documents MyCommand (command) and MyAutomation (automation) from account 111111111111, you should attach these permissions to you your IAM entities:

###### Example

```

                {
                    "Effect": "Allow",
                    "Action": [
                        "ssm:SendCommand",
                    ],
                    "Resource": "arn:aws:ssm:*:111111111111:document/MyAutomation",
                    "Condition": {
                        "ForAnyValue:StringEquals": {
                            "aws:CalledVia": [
                                "drs.amazonaws.com"
                            ]
                        }
                    }
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "ssm:StartAutomationExecution"
                    ],
                    "Resource": "arn:aws:ssm:*:111111111111:automation-definition/MyAutomation",
                    "Condition": {
                        "ForAnyValue:StringEquals": {
                            "aws:CalledVia": [
                                "drs.amazonaws.com"
                            ]
                        }
                    }
                }

```

###### Topics

- [Install the required IAM roles if needed](post-launch-action-settings-roles.md "post-launch-action-settings-roles.md")
- [Activating post-launch actions default settings](post-launch-action-settings-activation-default.md "post-launch-action-settings-activation-default.md")
- [Adding custom actions](post-launch-action-settings-adding-custom-default.md "post-launch-action-settings-adding-custom-default.md")
- [Activating, deactivating and editing predefined or custom actions](post-launch-action-settings-editing-default.md "post-launch-action-settings-editing-default.md")
- [Deleting custom actions](post-launch-action-settings-deleting-default.md "post-launch-action-settings-deleting-default.md")
- [Predefined post-launch actions](predefined-post-launch-actions-default.md "predefined-post-launch-actions-default.md")
- [Validate disk space](#validate-disk-space "#validate-disk-space")
- [Amazon EC2 connectivity checks](#ec2-connectivity-checks "#ec2-connectivity-checks")
- [Verify HTTP/HTTPS response](#verify-http-response "#verify-http-response")
- [Verify tags](#verify-tags "#verify-tags")

## Validate disk space

Use the **Disk space validation** feature to obtain visibility into the disc space that you have at your disposal, as well as logs with actionable insights.

## Amazon EC2 connectivity checks

Use the **EC2 connectivity checks** feature to conduct network connectivity checks to a predefined list of ports and hosts.

###### Note

Up to 5 Port:IP couples can be checked in a single action.

## Verify HTTP/HTTPS response

Use the **Verify HTTP/HTTPS response** feature to
conduct HTTP/HTTPS connectivity checks to a predefined list of URLs. The feature
verifies that HTTP/HTTPS requests (for example, https://localhost) receive the
correct response.

## Verify tags

Use the **Verify Tags** feature to validate that tags which have been defined in the launch template and on the source server are copied to the migrated server.
