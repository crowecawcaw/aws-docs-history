# Using the Cache-Control header to increase app performance

Amplify's default hosting architecture optimizes the balance between hosting performance
and deployment availability. For most customers, we recommend that you use the default
architecture.

If you require finer control over an app's performance, you can manually set the HTTP
`Cache-Control` header to optimize for hosting performance by keeping content
cached at the content delivery network (CDN) edge for a longer interval.

The HTTP `Cache-Control` header's `max-age` and `s-maxage`
directives affect the content caching duration for your app. The `max-age`
directive tells the browser how long (in seconds) that you want content to remain in the
cache before it is refreshed from the origin server. The `s-maxage` directive
overrides `max-age` and lets you specify how long (in seconds) that you want
content to remain at the CDN edge before it is refreshed from the origin server.

Apps hosted with Amplify honor the `Cache-Control` headers that are sent by the
origin, unless you override them with custom headers that you define. Amplify only applies
`Cache-Control` custom headers for successful responses with a `200 OK` status
code. This prevents error responses from being cached and served to other users that make the same request.

You can manually adjust the `s-maxage` directive to have more control over
the performance and deployment availability of your app. For example, to change the length
of time that your content stays cached at the edge, you can manually set the time to live
(TTL) by updating `s-maxage` to a value other than the default 31536000 seconds
(one year).

You can define custom headers for an app in the **Custom headers**
section of the Amplify console. For an example of the YAML format, see
[Setting Cache-Control custom headers](setting-custom-headers.md#example-cache-headers "setting-custom-headers.md#example-cache-headers").

Use the following procedure to set the `s-maxage` directive to keep
content cached at the CDN edge for 24 hours.

###### To set a custom Cache-Control header

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app to set custom headers for.
3. In the navigation pane, choose **Hosting**, **Custom
   headers**.
4. On the **Custom headers** page, choose
   **Edit**.
5. In the **Edit custom headers** window, enter the information
   for your custom header as follows:
   1. For `pattern`, enter `**/*` for all
      paths.
   2. For `key`, enter `Cache-Control`.
   3. For `value`, enter `s-maxage=86400`.

6. Choose **Save**.
7. Redeploy the app to apply the new custom header.
