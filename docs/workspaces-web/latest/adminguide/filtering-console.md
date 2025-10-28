# Setting up URL filtering using the console in Amazon WorkSpaces Secure Browser

To set up URL filtering using the console, follow these steps.

1.  Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/ "https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/").
2.  Choose **WorkSpaces Secure Browser**, **Web portals**, choose your
    web portal, and then choose **View details**.
3.  For **URL filtering**, choose from the following options:

        * **Allow access to all URLs**: By default, a web portal allows access to
         all URLs. You can add specific websites to the **BlockURL** list to prevent
         users from visiting those sites during a session. For example, adding
         **www.anycorp.com** to the **BlockURL** list will prevent
         user from navigating to www.anycorp.com during their session.
        * **Block access to all URLs**: By default, the web portal blocks access
         to all URLS. You can add specific websites to the URL allowlist to curate a list of websites
         users can visit, and block traffic to any other websites. Consider adding each URL as a
         bookmark to enable 1-click access for users during their session.
        * **Advanced configuration**: Choose this option to create
         **allowURL** and **blockURL** lists in parallel. The
         **URL allowlist** has priority over **URL blocklist**.
         This option enables URL filtering by path. For example, you can add
         **www.anycorp.com** to the blocklist, and then add
         **www.anycorp.com/hr** to the allow list. This allows users to visit
         www.anycorp.com/hr, but they won't be able to access other URL paths, such as
         www.anycorp.com/finance.

    For more guidance about using block and allow URLs, see [Allow or block
    access to websites](https://support.google.com/chrome/a/answer/7532419?hl=en#zippy=%2Clinux "https://support.google.com/chrome/a/answer/7532419?hl=en#zippy=%2Clinux"). Add URLs to these lists following Chrome's blocklist filter format
    for the best results. For more information, see [URL blocklist filter format](https://support.google.com/chrome/a/answer/9942583?_ga=2.44620960.505898626.1675896662-439274379.1675896662&visit_id=638114931513376779-3689089291&p=url_blocklist_filter_format&rd=1 "https://support.google.com/chrome/a/answer/9942583?_ga=2.44620960.505898626.1675896662-439274379.1675896662&visit_id=638114931513376779-3689089291&p=url_blocklist_filter_format&rd=1").
