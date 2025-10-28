# Link your account with

Grafana Labs

Workspaces upgraded to Amazon Managed Grafana Enterprise plugins get access to support
and consulting from Grafana Labs. To access this feature, the AWS account must be
linked with a Grafana Labs account token. You register your new or existing Grafana Labs
account with AWS when you [upgrade to
an Enterprise license](AMG-workspace-manage-enterprise.md "AMG-workspace-manage-enterprise.md").

###### Note

You only need to register your Grafana Labs account token one time per region.
If your account was previously linked (for example, when upgrading a
different workspace in the region to access Enterprise plugins), you are not
prompted to link again.

Linking consists of getting a token from a Grafana Labs account that is
used in Amazon Managed Grafana to register the account. You can create a new account at Grafana
Labs or use an existing one.

We recommend that you copy and save your Grafana Labs token in a secure, convenient
location for future use.

###### To link your Grafana Labs account

1. Follow the instructions in [Managing your access to Amazon Managed Grafana
   Enterprise plugins](AMG-workspace-manage-enterprise.md "AMG-workspace-manage-enterprise.md") to upgrade your account
   with access Enterprise plugins. You are prompted to link your account
   by adding a token during the upgrade process.
2. If you already have a token, you can enter it directly. If you do not
   have a token, select **Get your token**. This
   opens the [Grafana
   Labs website](https://grafana.com/partners/amg/support "https://grafana.com/partners/amg/support") in a new browser tab.

From the Grafana Labs website, you can sign into your Grafana Labs
account (or create a new one), then get a token. 3. After you copy the token, return to the Amazon Managed Grafana browser tab or
window. Enter the token in the **Grafana Labs Token**
section. 4. You are now able to choose **Save** to complete your
upgrade.
**Reusing your token with other workspaces**

If you have previously registered your Grafana Labs account and are prompted
for a Grafana Labs token (for example, when upgrading a workspace in another region),
you can use the same token to register each time, so that you do not need to create
a new Grafana Labs account. If you have not saved your token, you may be
able to retrieve it in one of these ways:

- You can get the token by looking it up in your Grafana Labs account by
  going to [https://grafana.com/partners/amg/support](https://grafana.com/partners/amg/support "https://grafana.com/partners/amg/support"), and choosing **My
  Account**.
- You can get the token from an existing, already linked workspace, by using
  the [DescribeWorkspace](../APIReference/API_DescribeWorkspace.md "../APIReference/API_DescribeWorkspace.md")
  API to retrieve the token.
- If the token is no longer available to you via either of those methods, you
  must [contact Grafana Labs support](https://grafana.com/contact "https://grafana.com/contact").
