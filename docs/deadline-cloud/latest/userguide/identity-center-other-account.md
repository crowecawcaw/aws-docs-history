

# Using an IAM Identity Center instance in another AWS account
<a name="identity-center-other-account"></a>

Your monitor and farms can be in a different AWS account from your IAM Identity Center instance. Both accounts must be in the same organization in AWS Organizations (Organizations), and you must use the organization instance of IAM Identity Center. You enable the organization instance in your organization's management account, and then you can create a monitor that connects to it from any member account in the organization. For example, you can keep IAM Identity Center in your management account and run each project's farms in that project's own account.

Create the monitor in the same account as the farms that it shows. When the Deadline Cloud console asks which IAM Identity Center instance to use, choose the organization instance.

A member account can read the users and groups in the organization instance but can't create them. An IAM Identity Center administrator for your organization creates the users and groups. You then assign them to farms, queues, and fleets from the member account. If the organization instance has no groups, you can assign individual users instead.

A monitor can't use an IAM Identity Center instance from a different organization. It also can't use an account instance that belongs to another account, because an account instance serves only the account that created it. For more information about instance types, see [Organization and account instances of AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html) in the IAM Identity Center User Guide.