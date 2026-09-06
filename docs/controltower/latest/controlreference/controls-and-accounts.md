

# Considerations for controls and accounts
<a name="controls-and-accounts"></a>

When working with controls and accounts, consider the following properties:

**Controls and accounts**
+ Accounts created through the Account Factory in AWS Control Tower inherit the controls of the parent OU, and the associated resources are created.
+ When you enable optional controls, AWS Control Tower creates and manages certain additional AWS resources in your accounts. Do not modify or delete resources created by AWS Control Tower . Doing so could result in the controls entering an unknown state. For more information, see [The AWS Control Tower controls library](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html).