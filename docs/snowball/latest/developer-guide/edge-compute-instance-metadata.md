Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Supported EC2-compatible instance metadata and user data on Snowball Edge

_Instance metadata_ is data about your instance that
you can use to configure or manage the running instance. Snowball Edge supports a
subset of instance metadata categories for your compute instances. For more information,
see [Instance metadata and user
data](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md") in the Amazon EC2 User Guide.

The following categories are supported. Using any other categories returns a
`404` error message.

| Supported instance metadata categories on a Snowball Edge device | Data                                                               | Description |
| ---------------------------------------------------------------- | ------------------------------------------------------------------ | ----------- |
| `ami-id`                                                         | The AMI ID used to launch the instance.                            |
| `hostname`                                                       | The private IPv4 DNS hostname of the instance.                     |
| `instance-id`                                                    | The ID of this instance.                                           |
| `instance-type`                                                  | The type of instance.                                              |
| `local-hostname`                                                 | The private IPv4 DNS hostname of the instance.                     |
| `local-ipv4`                                                     | The private IPv4 address of the instance.                          |
| `mac`                                                            | The instance's media access control (MAC) address.                 |
| `network/interfaces/macs/`mac`/local-hostname`                   | The interface's local hostname.                                    |
| `network/interfaces/macs/`mac`/local-ipv4s`                      | The private IPv4 addresses associated with the interface.          |
| `network/interfaces/macs/`mac`/mac`                              | The instance's MAC address.                                        |
| `network/interfaces/macs/`mac`/public-ipv4s`                     | The Elastic IP addresses associated with the interface.            |
| `public-ipv4`                                                    | The public IPv4 address.                                           |
| `public-keys/0/openssh-key`                                      | Public key. Only available if supplied at instance launch<br>time. |
| `reservation-id`                                                 | The ID of the reservation.                                         |
| userData                                                         | Shell scripts to send instructions to an instance at launch.       |

| Supported instance dynamic data categories on a Snowball Edge device | Data                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| instance-identity/document                                           | JSON containing instance attributes. Only `instanceId`,<br>`imageId`, `privateIp`, and<br>`instanceType` have values, and the other returned<br>attributes are null. For more information, see [Instance<br>Identity Documents](../../../AWSEC2/latest/UserGuide/instance-identity-documents.md "../../../AWSEC2/latest/UserGuide/instance-identity-documents.md") in the _Amazon EC2 User Guide_. |

## Computer instance user data on Snowball Edge

Use shell scripts to access compute instance user data on a
Snowball Edge device. Using shell scripts, you can send instructions to an instance at
launch. You can change user data with the `modify-instance-attribute`
AWS CLI command, or the `ModifyInstanceAttribute` API action.

###### To change user data

1. Stop your compute instance with the `stop-instances` AWS CLI
   command.
2. Using the `modify-instance-attribute` AWS CLI command, modify the
   `userData` attribute.
3. Restart your compute instance with the `start-instances` AWS CLI
   command.

Only shell scripts are supported for compute instances. There is no support for
`cloud-init` package directives on compute instances running on a
Snowball Edge device. For more information about working with AWS CLI commands, see the
_[AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md")._
