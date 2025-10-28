# Managing cache key cookies

When you deploy your app to Amplify, you can choose whether you want to include or exclude
cookies in the cache key. In the Amplify console, this setting is specified on the
**Custom headers and cache** page using the **Cache key
settings** toggle. For instructions, see [Including or excluding cookies from the cache
key](#set-cache-key-cookies "#set-cache-key-cookies").

**Include cookies in the cache key**

With this setting, Amplify automatically chooses an optimal cache configuration for
your app based on the type of content that is being served. You must explicitly choose this
cache configuration type.

If you are using the SDKs or the AWS CLI, this setting corresponds to setting
`cacheConfig.type` to `AMPLIFY_MANAGED` with the `CreateApp` or `UpdateApp` APIs.

**Exclude cookies from the cache key**

This is the default cache configuration. This cache configuration is similar to the
`AMPLIFY_MANAGED` configuration, except that it excludes all cookies from the
cache key.

Choosing to exclude cookies from the cache key can result in better cache performance.
However, before you choose this cache configuration, it is important to consider whether your
app uses cookies to serve dynamic content.

If you are using the SDKs or the AWS CLI, this setting corresponds to setting the
`cacheConfig.type` to `AMPLIFY_MANAGED_NO_COOKIES` with the `CreateApp` or `UpdateApp` APIs.

For more information about the cache key, see [Understand the
cache key](../../../AmazonCloudFront/latest/DeveloperGuide/understanding-the-cache-key.md "../../../AmazonCloudFront/latest/DeveloperGuide/understanding-the-cache-key.md") in the _Amazon CloudFront Developer Guide;_.

## Including or excluding cookies from the cache

key

You can set the cache key cookie configuration for an app in the Amplify console, SDKs,
or the AWS CLI.

Use the following procedure to specify whether to include or exclude cookies from the cache
key when you are deploying a new app using the Amplify console.

###### To set the cache key cookie configuration when deploying an app to Amplify

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. On the **All apps** page, choose **Create new
   app**.
3. On the **Start building with Amplify** page, choose your Git
   repository provider, then choose **Next**.
4. On the **Add repository branch** page, do the following:
   1. Select the name of the repository to connect.
   2. Select the name of the repository branch to connect.
   3. Choose **Next**.

5. If the app requires an IAM service role, you can either allow Amplify Hosting compute
   to automatically create a service role for you or you can specify a role that you have
   created.
   - To allow Amplify to automatically create a role and attach it to your app:
     1. Choose **Create and use a new service role**.

   - To attach a service role that you previously created:
     1. Choose **Use an existing service role**.
     2. Select the role to use from the list.

6. Choose **Advanced settings**, then locate the **Cache key
   settings** section.
7. Choose either **Keep cookies in cache key** or **Remove cookies
   from cache key**. The following screenshot shows the **Cache key
   settings** toggle in the console.

![Screenshot of the Cache key settings toggle in the Amplify console.](images/amplify-caching-1.png) 8. Choose **Next**. 9. On the **Review** page, choose **Save and
deploy**.

## Changing the cache key cookie configuration for an

app

You can change the cache key cookie configuration for an app that is already deployed to
Amplify. Use the following procedure to change whether to include or exclude cookies from the
cache key for an app using the Amplify console.

###### To change the cache key cookie configuration for a deployed app

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. On the **All apps** page, choose the application you want to
   update.
3. In the navigation pane, choose **Hosting**, then choose **Custom
   headers and cache**.
4. On the **Custom headers and cache** page, locate the **Cache key
   settings** section and choose **Edit**.
5. Choose either **Keep cookies in cache key** or **Remove cookies
   from cache key**. The following screenshot shows the **Cache key
   settings** toggle in the console.

![Screenshot of the Cache key settings toggle in the Amplify console.](images/amplify-caching-1.png) 6. Choose **Save**.
