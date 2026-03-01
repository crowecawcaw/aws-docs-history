# Using Amazon Q Developer plugins

Amazon Q Developer integrates with third party monitoring tools and security platforms so you can
access your AWS application insights without leaving the AWS builder environment. In the
AWS Management Console, you can chat about metrics provided by these tools to understand and address
application performance, errors, or vulnerabilities.

After you configure a plugin, add the plugin alias to the beginning of your question when you
chat with Amazon Q in the AWS console. Amazon Q calls the third party provider APIs to
retrieve resources and generates a response with deep links to the external resources.

When Amazon Q calls a third party API, the API will not appear in AWS CloudTrail logs. The
CloudTrail log will only show when an AWS Secrets Manager secret is accessed by Amazon Q to
retrieve credentials to connect to the third party provider.

Amazon Q doesn't share any information with third party providers when you configure or
use plugins. For more information on how Amazon Q uses your data, see
[Data protection](data-protection.md "data-protection.md").

###### Note

Member accounts within an AWS organization don't have access to plugins that are
configured in the organization's management account profile. Each member account must
create their own Q Developer profile before they can configure and use plugins in their
account.

###### Warning

Third party provider user permissions are not detected by Amazon Q Developer plugins. When an
administrator configures a plugin in an AWS account, users with plugin permissions in
that account have access to any resources in the third party provider account
retrievable by the plugin.

You can configure IAM policies to restrict which plugins users have access to. For
more information, see
[Allow users to chat with plugins from one provider](id-based-policy-examples-users.md#id-based-policy-examples-allow-plugin-type "id-based-policy-examples-users.md#id-based-policy-examples-allow-plugin-type").

To get started, see the topic for the plugin you want to use with Amazon Q Developer.

###### Topics

- [Configuring the Amazon Q Developer CloudZero plugin](cloudzero-plugin.md "cloudzero-plugin.md")
- [Configuring the Amazon Q Developer Datadog plugin](datadog-plugin.md "datadog-plugin.md")
- [Configuring the Amazon Q Developer Wiz plugin](wiz-plugin.md "wiz-plugin.md")
