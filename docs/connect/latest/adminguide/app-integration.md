

# Use an allowlist for integrated applications in Connect Customer
<a name="app-integration"></a>

All domains that embed the CCP for a particular instance must be explicitly allowed for cross-domain access to the instance. For example, to integrate with Salesforce, you must place your Salesforce Visualforce domain in an allowlist.

**To allow a domain URL**

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. Choose the name of the instance from **Instance Alias**.

1. In the navigation pane, choose **Approved origins**.

1. Choose **Add origin**.

1. Type the URL and choose **Add**.

**Note**  
When Connect Customer is embedded in another app, it's possible for users to get a **Session expired** error message when the close and then reopen Connect Customer, and then log in.  
If you see the **Session expired** message while logging in, you probably just need to refresh the session token. Go to your identity provider and log in. Refresh the Connect Customer page. If you still get this message, contact your IT team.