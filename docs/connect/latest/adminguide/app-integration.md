# Use an allowlist for integrated applications in

Amazon Connect

All domains that embed the CCP for a particular instance must be explicitly allowed
for cross-domain access to the instance. For example, to integrate with Salesforce, you
must place your Salesforce Visualforce domain in an allowlist.

###### To allow a domain URL

1. Open the Amazon Connect console at
   [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. Choose the name of the instance from **Instance
   Alias**.
3. In the navigation pane, choose **Approved origins**.
4. Choose **Add origin**.
5. Type the URL and choose **Add**.

###### Note

When Amazon Connect is embedded in another app, it's possible for users to get a
**Session expired** error message when the close and then
reopen Amazon Connect, and then log in.

If you see the **Session expired** message while logging in, you probably just need to
refresh the session token. Go to your identity provider and log in. Refresh the
Amazon Connect page. If you still get this message, contact your IT team.
