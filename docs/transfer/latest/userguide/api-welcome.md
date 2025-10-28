# AWS Transfer Family API Reference

The complete API Reference guide for Transfer Family is available at [AWS Transfer Family API Reference](../APIReference/api-welcome.md "../APIReference/api-welcome.md").

AWS Transfer Family is a secure transfer service that you can use to transfer files into and out of
Amazon Simple Storage Service (Amazon S3) storage over the following protocols:

- Secure Shell (SSH) File Transfer Protocol (SFTP)
- File Transfer Protocol Secure (FTPS)
- File Transfer Protocol (FTP)
- Applicability Statement 2 (AS2)
  Servers, users, and roles are all identified by their Amazon Resource Name (ARN). You can
  assign tags, which are key-value pairs, to entities with an ARN. Tags are metadata that can
  be used to group or search for these entities. One example where tags are useful is for
  accounting purposes.

The following conventions are observed in AWS Transfer Family ID formats:

- `ServerId` values take the form
  `s-01234567890abcdef`.
- `SshPublicKeyId` values take the form
  `key-01234567890abcdef`.
  Amazon Resource Name (ARN) formats take the following form:

- For servers, ARNs take the form
  `arn:aws:transfer:*`region`*:*`account-id`*:server/*`server-id`*`.

An example of a server ARN is:
`arn:aws:transfer:us-east-1:123456789012:server/s-01234567890abcdef`.

- For users, ARNs take the form
  `arn:aws:transfer:*`region`*:*`account-id`*:user/*`server-id`\*/``username```.

An example is
`arn:aws:transfer:us-east-1:123456789012:user/s-01234567890abcdef/user1`.
DNS entries (endpoints) in use are as follows:

- API endpoints take the form
  `transfer.*`region`*.amazonaws.com`.
- Server endpoints take the form
  `server.transfer.*`region`*.amazonaws.com`.
  This API interface reference for AWS Transfer Family contains documentation for a programming
  interface that you can use to manage AWS Transfer Family. The reference structure is as follows:

- For the alphabetical list of API actions, see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md").
- For the alphabetical list of data types, see [Types](../APIReference/API_Types.md "../APIReference/API_Types.md").
- For a list of common query parameters, see [Common
  Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md").
- For descriptions of the error codes, see [Common
  Errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md").

###### Tip

Rather than actually running a command, you can use the
`--generate-cli-skeleton` parameter with any API call to generate and display
a parameter template. You can then use the generated template to customize and use as input
on a later command. For details, see [Generate and use a parameter skeleton file](../../../cli/latest/userguide/cli-usage-skeleton.md#cli-usage-skeleton-generate "../../../cli/latest/userguide/cli-usage-skeleton.md#cli-usage-skeleton-generate").
