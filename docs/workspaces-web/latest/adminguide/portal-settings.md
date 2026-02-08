# Configuring portal settings for Amazon WorkSpaces Secure Browser

On the **Step 2: Configure web portal settings** page, complete the
following steps to customize your users' browsing experience when they start a session.

1. Under **Web portal details**, for **Display
   name**, enter an identifiable name for your web portal.
2. Under **Instance Type**, select the instance type for your web
   portal from the drop-down menu. Then, enter your **Max concurrent user
   limit** for the web portal. For more information, see [Managing service quotas for your portal in Amazon WorkSpaces Secure Browser](request-service-quota.md "request-service-quota.md").

###### Note

Selecting a new instance type will change the cost for each monthly active user.
For more information, see [Amazon WorkSpaces Secure Browser Pricing](https://aws.amazon.com/workspaces/web/pricing/ "https://aws.amazon.com/workspaces/web/pricing/"). 3. Under **Custom Domain**, you can configure a custom domain for your portal to enable access through your own domain name instead of the default portal endpoint. For more information, see [Configuring custom domain for your portal](custom-domains.md "custom-domains.md"). **This is optional.** 4. Under **Session Logger**, you can specify a S3 bucket for storing session log files. For more information, see [Setting up Session Logger for Amazon WorkSpaces Secure Browser](session-logger.md "session-logger.md"). **This is optional.** 5. Under **User access logging**, for **Kinesis stream
ID**, select the Amazon Kinesis data stream you want to send log files to. For more
information, see [Setting up user activity logging in Amazon WorkSpaces Secure Browser](user-logging.md "user-logging.md"). **This is optional.** 6. Under **IP Access Control**, choose whether to restrict
access to trusted networks. For more information, see [Managing IP access controls in Amazon WorkSpaces Secure Browser](ip-access-controls.md "ip-access-controls.md"). **This is optional.** 7. Under **Data Protection Settings**, you can create policies for WorkSpaces Secure Browser to redact sensitive information. For more information, see [Managing data protection settings in Amazon WorkSpaces Secure Browser](data-protection-settings.md "data-protection-settings.md"). **This is optional**. 8. Under **URL filtering**, you can specify which URLs end users are allowed to access or block specific URLs or domain categories to restrict access. For more information, see [Web content filtering in Amazon WorkSpaces Secure Browser](web-content-filtering.md "web-content-filtering.md"). **This is optional.**

    1. To restrict session browsing to a few selected domains, enable the toggle **Block all URLs** and click **add URL** to provide the list of URLs your end users are allowed to access.
    2. To create a list of URLs to block for end users, click **Add URL** to list the single URLs to block or click **Add categories** to select categories of domains that are blocked (e.g., Social Networking).

9. Under **Policy settings**, you can set any browser policy using Chrome policies available for the latest stable version to the web portal. For more information, see [Managing browser policy in Amazon WorkSpaces Secure Browser](browser-policies.md "browser-policies.md"). **This is optional.**
   1. You can quickly select some of the most common policies in the **Visual editor**
      - For **Startup URL - optional**, enter a domain to use as the homepage when users launch their browser. Your VPC must have a stable connection to this URL.
      - Select or clear **Private browsing** and **History deletion** to turn these features on or off during a user's session

      ###### Note

      URLs visited while browsing privately, or before a user deletes their browser history, can't be recorded in user access logging. For more information, see [Setting up user activity logging in Amazon WorkSpaces Secure Browser](user-logging.md "user-logging.md").
      - For **Browser bookmarks - optional**, enter the **Display name**, **Domain**, and **Folder** for any bookmarks you want your users to see in their browser. Then, choose **Add bookmark**.

      ###### Note

      **Domain** is a required field for browser bookmarks.

      In Chrome, users can find managed bookmarks in the **Managed bookmarks** folder on the bookmarks toolbar.

   2. You can also directly add or edit policies by using the JSON editor instead of the visual editor. For the specific format of a policy, please refer to [Chrome Enterprise policy list](https://chromeenterprise.google/policies/ "https://chromeenterprise.google/policies/").
   3. You can also import the Chrome policies used in your organization by uploading a JSON file into the web portal. For details, please see [Tutorial: Setting a custom browser policy in Amazon WorkSpaces Secure Browser](browser-policies-custom.md "browser-policies-custom.md")

   When you upload a policy file, you can see the available policies in the file in the console. However, you can't edit all policies in the visual editor. The console lists policies in your JSON file that you can't edit with the visual editor under **Additional JSON policies**. To make changes to these policies, you must edit them manually.

10. Add **Tags** to your portal. You can use tags to search for or filter your AWS resources. Tags consist of a key and optional value and are associated with your portal resource. **This is optional.**
11. Choose **Next** to continue.
