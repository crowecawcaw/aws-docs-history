# Step 2: Create a Streaming URL for User Authentication

You must create a streaming URL to authenticate users for embedded WorkSpaces Applications streaming
sessions. SAML 2.0 and user pools are currently not supported for embedded streaming
sessions. To create a streaming URL, use one of the following methods:

- WorkSpaces Applications console
- The [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") API action
- The [create-streaming-url](../../../cli/latest/reference/appstream/create-streaming-url.md "../../../cli/latest/reference/appstream/create-streaming-url.md") AWS CLI command

## Configuration Requirements for Using Custom Domains

Whether you use custom domains to apply your company branding or to ensure that embedded WorkSpaces Applications streaming sessions work with browsers that block third-party cookies, the configuration requirements are the same.

For web browsers that block third-party cookies, custom domains are required.
WorkSpaces Applications uses browser cookies to authenticate streaming sessions and lets users
reconnect to an active session without being prompted to provide their sign-in
credentials every time. By default, WorkSpaces Applications streaming URLs include
`appstream.com` as the domain. When you embed a streaming
session within your website, `appstream.com` is treated as a
third-party domain. As a result, streaming sessions may be blocked when modern
browsers are used that block third-party cookies by default.

To avoid embedded WorkSpaces Applications streaming sessions from being blocked in this scenario, follow these steps:

1. Specify a custom domain to host your embedded WorkSpaces Applications streaming sessions.

When you configure your custom domain, make sure that the domain is a subdomain of the webpage in which you plan to embed WorkSpaces Applications. For example, if you update your stack to specify `training.example.com` as the host domain, you can create a subdomain called `content.training.example.com` for your embedded streaming sessions. 2. Create a streaming URL for embedded WorkSpaces Applications streaming sessions that uses the same custom subdomain. To create the streaming URL, use the [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") API action or the [create-streaming-url](../../../cli/latest/reference/appstream/create-streaming-url.md "../../../cli/latest/reference/appstream/create-streaming-url.md") AWS CLI command. You cannot use the WorkSpaces Applications console to create a streaming URL in this scenario.

To create a streaming URL for embedded WorkSpaces Applications streaming sessions, in the URL, replace `appstream2.``region``.aws.amazon.com` with your own domain.

By default, WorkSpaces Applications streaming URLs are formatted as follows:

```
`https://appstream2.``region``.aws.amazon.com/authenticate?parameters=``authenticationcode`
```

If your subdomain is `content.training.example.com`, your new streaming URL follows this format:

```
`https://content.training.example.com/authenticate?parameters=``authenticationcode`
```

###### Note

When you create a custom domain, you can use the domain for embedded WorkSpaces Applications streaming sessions only in the AWS Region for which it was configured. If you plan to support custom domains in multiple Regions, create a custom domain for each applicable Region. Also, embedded streaming sessions are only supported over HTTPS [TCP port 443]. 3. Add `appstream-custom-url-domain` to the header of the webpage that will host the embedded streaming sessions. For the header value, use the domain that your reverse proxy displays to users. For example:

```
Header name: `appstream-custom-url-domain`
Header value: `training.example.com`
```

Setting a custom domain and creating a streaming URL that specifies the
same domain lets the cookies be saved as first-party cookies. For
information about how to configure custom domains by using Amazon CloudFront, see
[Using Custom Domains with WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-custom-domains-with-amazon-appstream-2-0/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/using-custom-domains-with-amazon-appstream-2-0/").

After you set up a custom domain for your embedded WorkSpaces Applications streaming sessions, if your streaming URLs don't redirect to your custom domain, or if your custom domain doesn't display correctly for your users, see the following troubleshooting topics:

- [I set up a custom domain for my embedded WorkSpaces Applications streaming sessions, but my WorkSpaces Applications streaming URLs aren't redirecting to my custom domain.](troubleshooting-general.md#embedded-streaming-sessions-streaming-urls-not-redirected-to-custom-domain "troubleshooting-general.md#embedded-streaming-sessions-streaming-urls-not-redirected-to-custom-domain")
