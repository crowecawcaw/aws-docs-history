AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Start a session with

a document by specifying the session documents in IAM policies

If you use the [start-session](../../../cli/latest/reference/ssm/start-session.md "../../../cli/latest/reference/ssm/start-session.md")
AWS CLI command using the default session document, you can omit the document
name. The system automatically calls the `SSM-SessionManagerRunShell`
session document.

In all other cases, you must specify a value for the
`document-name` parameter. When a user specifies the name of a
session document in a command, the systems checks their IAM policy to verify
they have permission to access the document. If they don't have permission, the
connection request fails. The following examples includes the
`document-name` parameter with the
`AWS-StartPortForwardingSession` session document.

```
aws ssm start-session \
    --target i-02573cafcfEXAMPLE \
    --document-name AWS-StartPortForwardingSession \
    --parameters '{"portNumber":["80"], "localPortNumber":["56789"]}'
```

For an example of how to specify a Session Manager session document in an IAM
policy, see [Quickstart end user
policies for Session Manager](getting-started-restrict-access-quickstart.md#restrict-access-quickstart-end-user "getting-started-restrict-access-quickstart.md#restrict-access-quickstart-end-user").

###### Note

To start a session using SSH, you must complete configuration steps on the
target managed node _and_ the user's local machine. For
information, see [(Optional) Allow and control permissions for SSH connections through Session Manager](session-manager-getting-started-enable-ssh-connections.md "session-manager-getting-started-enable-ssh-connections.md").
