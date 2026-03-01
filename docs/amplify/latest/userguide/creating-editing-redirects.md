# Creating and editing redirects in the Amplify console

You can create and edit redirects for an application in the Amplify console. Before
you get started, you will need the following information about the parts of a
redirect.

**An original address**

The address the user requested.

**A destination address**

The address that actually serves the content that the user sees.

**A redirect type**

Types include a permanent redirect (301), a temporary redirect (302), a rewrite
(200), or not found (404).

**A two letter country code (optional)**

A value you can include to segment the user experience of your app by
geographical region.

###### To create a redirect in the Amplify console

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app you want to create a redirect for.
3. In the navigation pane, choose **Hosting**, and then choose
   **Rewrites and redirects**.
4. On the **Rewrites and redirects** page, choose **Manage
   redirects**.
5. Manually add or update redirects in the **Rewrites
   and redirects** JSON editor.
   1. For `source`, specify the original address
      the user requested.
   2. For `status`, specify the type of redirect.
   3. For `target`, specify the destination address
      that renders the content to the user.
   4. (Optional) For `condition`, enter a two letter
      country code condition.

6. Choose **Save**.
