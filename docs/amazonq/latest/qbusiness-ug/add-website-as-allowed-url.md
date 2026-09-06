

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Add your website as an allowed URL
<a name="add-website-as-allowed-url"></a>

To configure allowed websites for your existing web experience, you can use the Amazon Q Business console or the Amazon Q Business API.

**Note**  
The allowed *base URLs* must begin with `https://` or `http://`.
You must only submit a *base URL*, and not the full path. For example, `https://docs.aws.amazon.com`.

## Using the console
<a name="add-website-as-allowed-url-console"></a>

1. Sign in to the [Amazon Q console](https://console.aws.amazon.com/amazonq/business/).

1. Choose **Applications**, then select the name of your application from the list.
**Note**  
Copy and save the **Deployed URL** for your Amazon Q application. You'll need this URL when you embed the web experience on your website.
For [anonymous applications](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-anonymous-application.html), the **Deployed URL** must be generated every time using the `[ CreateAnonymousWebExperienceUrl](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateAnonymousWebExperienceUrl.html)` API operation. For more information, see [Share an anonymous web experience](supported-exp-actions-anonymous.md#create-experience-anonymous-url).

1. From the left navigation pane, choose **Amazon Q embedded** under the **Enhancements** section.

1. On the main page, choose **Add allowed website** and enter the *base URL* of the website where you'll be embedding the Amazon Q Business web experience.

## Using the AWS CLI
<a name="add-website-as-allowed-url-cli"></a>

```
aws qbusiness update-web-experience \
  --application-id application-id \
  --web-experience-id web-experience-id \
  --origins {{origins}}

aws qbusiness get-web-experience \
  --application-id application-id \
  --web-experience-id experience-id
```

The `get-web-experience` operation will return the `defaultEndpoint`, which is the web experience URL that you will embed in your website.