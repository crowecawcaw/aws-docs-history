

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Start a session with a document by specifying the session documents in IAM policies
<a name="getting-started-specify-session-document"></a>

If you use the [start-session](https://docs.aws.amazon.com/cli/latest/reference/ssm/start-session.html) AWS CLI command using the default session document, you can omit the document name. The system automatically calls the `SSM-SessionManagerRunShell` session document.

In all other cases, you must specify a value for the `document-name` parameter. When a user specifies the name of a session document in a command, the systems checks their IAM policy to verify they have permission to access the document. If they don't have permission, the connection request fails. The following examples includes the `document-name` parameter with the `AWS-StartPortForwardingSession` session document.

```
aws ssm start-session \
    --target i-02573cafcfEXAMPLE \
    --document-name AWS-StartPortForwardingSession \
    --parameters '{"portNumber":["80"], "localPortNumber":["56789"]}'
```

For an example of how to specify a Session Manager session document in an IAM policy, see [Quickstart end user policies for Session Manager](getting-started-restrict-access-quickstart.md#restrict-access-quickstart-end-user).

**Note**  
To start a session using SSH, you must complete configuration steps on the target managed node *and* the user's local machine. For information, see [(Optional) Allow and control permissions for SSH connections through Session Manager](session-manager-getting-started-enable-ssh-connections.md).