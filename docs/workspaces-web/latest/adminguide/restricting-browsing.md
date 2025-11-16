# Restricting browsing to specific URLs

You can implement a "default deny" policy where only explicitly approved websites and URLs are accessible. It's ideal for high-security environments where internet access must be tightly controlled and every permitted site has been vetted for business necessity and security compliance.

In the AWS console, under URL filtering:

- Navigate to Block list and select the toggle **Block all URLs**
- Under Allow list, click **Add URL** to add a URL that will be allow listed for your end user. Add one entry per URL.
- Click **Save**
