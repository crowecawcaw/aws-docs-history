# Register an on-premises instance with

CodeDeploy

To register an on-premises instance, you must use an IAM identity to authenticate your
requests. You can choose from the following options for the IAM identity and registration
method you use:

- Use an IAM role ARN to authenticate requests.
  - Use the [register-on-premises-instance](../../../cli/latest/reference/deploy/register-on-premises-instance.md "../../../cli/latest/reference/deploy/register-on-premises-instance.md") command and periodically
    refreshed temporary credentials generated with the AWS Security Token Service (AWS STS) to manually
    configure most registration options. This option offers the highest level of security,
    because authentication occurs using a temporary token that times out and must be
    refreshed periodically. This option is recommended for production deployments of any
    size. For information, see [Use the
    register-on-premises-instance command (IAM Session ARN) to register an on-premises
    instance](register-on-premises-instance-iam-session-arn.md "register-on-premises-instance-iam-session-arn.md").

- (Not recommended) Use an IAM user ARN to authenticate requests.
  - Use the [register](../../../cli/latest/reference/deploy/register.md "../../../cli/latest/reference/deploy/register.md") command for the most automated registration process.
    This option should only be used for non-production deployments where security is less of
    a concern. This option is less secure because it uses static (permanent) credentials for
    authentication. This option works well for registering a single on-premises instance.
    For information, see [Use the register command (IAM user
    ARN) to register an on-premises instance](instances-on-premises-register-instance.md "instances-on-premises-register-instance.md").
  - Use the [register-on-premises-instance](../../../cli/latest/reference/deploy/register-on-premises-instance.md "../../../cli/latest/reference/deploy/register-on-premises-instance.md") command to manually configure
    most registration options. Suitable for registering a small number of on-premises
    instances. For information, see [Use the
    register-on-premises-instance command (IAM user ARN) to register an on-premises
    instance](register-on-premises-instance-iam-user-arn.md "register-on-premises-instance-iam-user-arn.md").

###### Topics

- [Use the
  register-on-premises-instance command (IAM Session ARN) to register an on-premises
  instance](register-on-premises-instance-iam-session-arn.md "register-on-premises-instance-iam-session-arn.md")
- [Use the register command (IAM user
  ARN) to register an on-premises instance](instances-on-premises-register-instance.md "instances-on-premises-register-instance.md")
- [Use the
  register-on-premises-instance command (IAM user ARN) to register an on-premises
  instance](register-on-premises-instance-iam-user-arn.md "register-on-premises-instance-iam-user-arn.md")
