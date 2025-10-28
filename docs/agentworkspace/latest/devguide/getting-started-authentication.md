# Authentication for applications in

Amazon Connect Agent Workspace

Apps in Amazon Connect Agent Workspace must provide their own authentication to their users. It
is recommended that apps use the same identity provider that the Amazon Connect instance has
been configured to use when it was created. This will make it so users only need to
log in once for both the agent workspace and their applications, since they both use
the same single sign on provider.

###### Note

On Jul 22, 2024, Google announced that they no longer plan to deprecate
third-party cookies **[1]**. With this
announcement, there will be no impact to third-party applications embedded
within Amazon Connect’s agent workspace, unless third-party application
users explicitly opt-in for deprecation. We advise third-party application
developers to adopt the third-party cookie deprecation impact prevention
solutions below as a forward-looking preventative measure.

If you have any questions or concerns, please contact AWS Support **[2]**.

**[1]** [https://privacysandbox.com/news/privacy-sandbox-update/](https://privacysandbox.com/news/privacy-sandbox-update/ "https://privacysandbox.com/news/privacy-sandbox-update/")

**[2]** [https://aws.amazon.com/support](https://aws.amazon.com/support "https://aws.amazon.com/support")

For more information, see the [3p admin
guide](../../../connect/latest/adminguide/3p-apps-agent-workspace.md "../../../connect/latest/adminguide/3p-apps-agent-workspace.md").

**Third-party Cookie Deprecation**

We are aware of the **Google Chrome** Third-Party Cookies
Deprecation (3PCD) that may impact the third-party applications experience. If
your application is embedded within Amazon Connect’s agent workspace in an iframe and
uses cookie based Authentication/Authorization, then your application is likely
to be impacted by Third-Party Cookie Deprecation. You can test if your user
experience will be impacted by 3PCD by using the following [Test for Breakage](https://developers.google.com/privacy-sandbox/3pcd/prepare/test-for-breakage "https://developers.google.com/privacy-sandbox/3pcd/prepare/test-for-breakage") guidance.

Here are the recommendations to ensure customers continue to have good
experiences when accessing your application within the Amazon Connect agent workspace
with Google Chrome.

- **Temporary solution**: Allow 3p cookie
  access [here](https://support.google.com/chrome/a/answer/14439269?hl=en "https://support.google.com/chrome/a/answer/14439269?hl=en").
- **Permanent solution**: Refer to the
  [guidance](https://developers.google.com/privacy-sandbox/3pcd "https://developers.google.com/privacy-sandbox/3pcd") from Chrome to choose the best option suitable for
  your application.
