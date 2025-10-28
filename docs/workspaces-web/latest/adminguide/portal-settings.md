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
For more information, see [Amazon WorkSpaces Secure Browser Pricing](https://aws.amazon.com/workspaces/web/pricing/ "https://aws.amazon.com/workspaces/web/pricing/"). 3. Under **User access logging**, for **Kinesis stream
ID**, select the Amazon Kinesis data stream you want to send your data to. For more
information, see [Setting up user activity logging in Amazon WorkSpaces Secure Browser](user-logging.md "user-logging.md"). 4. Under **Policy settings**, complete the following:

    * For **Policy options**, select **Visual
     editor** or **JSON file upload**. You can use either
     method to provide the policy configuration details for your web portal. For more
     information, see [Managing browser policy in Amazon WorkSpaces Secure Browser](browser-policies.md "browser-policies.md").




    	+ WorkSpaces Secure Browser includes support for Chrome enterprise policies. You can add and
    	 manage policies with either a visual editor or a manual upload for policy files.
    	 You can switch between either option at any time.
    	+ When you upload a policy file, you can see the available policies in the
    	 file in the console. However, you can't edit all policies in the visual editor.
    	 The console lists policies in your JSON file that you can't edit with the visual
    	 editor under **Additional JSON policies**. To make changes to
    	 these policies, you must edit them manually.
    * (Optional) For **Startup URL - optional**, enter a domain to
     use as the homepage when users launch their browser. Your VPC must have a stable
     connection to this URL.
    * Select or clear **Private browsing** and **History
     deletion** to turn these features on or off during a user's session


    ###### Note

    URLs visited while browsing privately, or before a user deletes their browser
     history, can't be recorded in user access logging. For more information, see [Setting up user activity logging in Amazon WorkSpaces Secure Browser](user-logging.md "user-logging.md").
    * Under **URL filtering**, you can configure which URLs users can
     visit during a session. For more information, see [Setting up URL filtering in Amazon WorkSpaces Secure Browser](url-filtering.md "url-filtering.md").
    * (Optional) For **Browser bookmarks - optional**, enter the
     **Display name**, **Domain**, and
     **Folder** for any bookmarks you want your users to see in their
     browser. Then, choose **Add bookmark**.


    ###### Note

    **Domain** is a required field for browser bookmarks.

    In Chrome, users can find managed bookmarks in the **Managed
     bookmarks** folder on the bookmarks toolbar.
    * (Optional) Add **Tags** to your portal. You can use tags to
     search for or filter your AWS resources. Tags consist of a key and optional value
     and are associated with your portal resource.

5. Under **IP Access Control (optional)**, choose whether to restrict
   access to trusted networks. For more information, see [Managing IP access controls in Amazon WorkSpaces Secure Browser](ip-access-controls.md "ip-access-controls.md").
6. Choose **Next** to continue.
