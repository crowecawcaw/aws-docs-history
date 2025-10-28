# Add your website as an allowed URL

To configure allowed websites for your existing web experience, you can use the
Amazon Q Business console or the Amazon Q Business API.

###### Note

- The allowed _base URLs_ must begin with
  `https://` or `http://`.
- You must only submit a _base URL_, and not the full
  path. For example, `https://docs.aws.amazon.com`.

1. Sign in to the [Amazon Q console](https://console.aws.amazon.com/amazonq/business/ "https://console.aws.amazon.com/amazonq/business/").
2. Choose **Applications**, then select the name of your
   application from the list.

###### Note

    * Copy and save the **Deployed URL** for
     your Amazon Q application. You'll need this URL
     when you embed the web experience on your website.
    * For [anonymous applications](create-anonymous-application.md "create-anonymous-application.md"), the
     **Deployed URL** must be generated
     every time using the  `CreateAnonymousWebExperienceUrl` API
     operation. For more information, see [Share an anonymous web
     experience](supported-exp-actions-anonymous.md#create-experience-anonymous-url "supported-exp-actions-anonymous.md#create-experience-anonymous-url").

3. From the left navigation pane, choose **Amazon Q
   embedded** under the **Enhancements**
   section.
4. On the main page, choose **Add allowed website** and
   enter the _base URL_ of the website where you'll be
   embedding the Amazon Q Business web experience.

```

aws qbusiness update-web-experience \
  --application-id application-id \
  --web-experience-id web-experience-id \
  --origins `origins`

aws qbusiness get-web-experience \
  --application-id application-id \
  --web-experience-id experience-id

```

The `get-web-experience` operation will return the
`defaultEndpoint`, which is the web experience URL that you will
embed in your website.
