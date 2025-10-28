# Setting custom headers

There are two ways to specify custom HTTP headers for an Amplify app. You can specify
headers in the Amplify console or you can specify headers by downloading and editing an
app's `customHttp.yml` file and saving it in your project's root
directory.

###### To set custom headers for an app and save them in the console

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app to set custom headers for.
3. In the navigation pane, choose **Hosting**, then
   choose**Custom headers**.
4. On the **Custom headers** page, choose
   **Edit**.
5. In the **Edit custom headers** window, enter the information for your
   custom headers using the [custom header YAML
   format](custom-header-YAML-format.md "custom-header-YAML-format.md").
   1. For `pattern`, enter the pattern to match.
   2. For `key`, enter the name of the custom header.
   3. For `value`, enter the value of the custom header.

6. Choose **Save**.
7. Redeploy the app to apply the new custom headers.
   - For a CI/CD app, navigate to the branch to deploy and choose **Redeploy
     this version**. You can also perform a new build from your Git
     repository.
   - For a manual deploy app, deploy the app again in the Amplify console.

###### To set custom headers for an app and save them in the root of your repository

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app to set custom headers for.
3. In the navigation pane, choose **Hosting**, then choose
   **Custom headers**.
4. On the **Custom headers** page, choose **Download
   YML**.
5. Open the downloaded `customHttp.yml` file in the code editor of
   your choice and enter the information for your custom headers using the [custom header YAML format](custom-header-YAML-format.md "custom-header-YAML-format.md").
   1. For `pattern`, enter the pattern to match.
   2. For `key`, enter the name of the custom header.
   3. For `value`, enter the value of the custom header.

6. Save the edited `customHttp.yml` file in your project's root
   directory. If you are working with a monorepo, save the
   `customHttp.yml` file in the root of your repo.
7. Redeploy the app to apply the new custom headers.
   - For a CI/CD app, perform a new build from your Git repository that includes the
     new `customHttp.yml` file.
   - For a manual deploy app, deploy the app again in the Amplify console and include
     the new `customHttp.yml` file with the artifacts that you
     upload.

###### Note

Custom headers set in the `customHttp.yml` file and deployed in the
app's root directory override custom headers defined in the **Custom
headers** section in the Amplify console.

## Security custom headers example

Custom security headers enable enforcing HTTPS, preventing XSS attacks, and defending your
browser against clickjacking. Use the following YAML syntax to apply custom security headers
to your app.

```
customHeaders:
  - pattern: '**'
    headers:
      - key: 'Strict-Transport-Security'
        value: 'max-age=31536000; includeSubDomains'
      - key: 'X-Frame-Options'
        value: 'SAMEORIGIN'
      - key: 'X-XSS-Protection'
        value: '1; mode=block'
      - key: 'X-Content-Type-Options'
        value: 'nosniff'
      - key: 'Content-Security-Policy'
        value: "default-src 'self'"
```

## Setting Cache-Control custom headers

Apps hosted with Amplify honor the `Cache-Control` headers that are sent by
the origin, unless you override them with custom headers that you define. Amplify only applies
Cache-Control custom headers for successful responses with a `200 OK` status code.
This prevents error responses from being cached and served to other users that make the same
request.

You can manually adjust the `s-maxage` directive to have more control over the
performance and deployment availability of your app. For example, to increase the length of
time that your content stays cached at the edge, you can manually increase the time to live
(TTL) by updating `s-maxage` to a value longer than the default 600 seconds (10
minutes).

To specify a custom value for `s-maxage`, use the following YAML format. This
example keeps the associated content cached at the edge for 3600 seconds (one hour).

```
customHeaders:
  - pattern: '/img/*'
    headers:
      - key: 'Cache-Control'
        value: 's-maxage=3600'
```

For more information about controlling application performance with headers, see [Using the Cache-Control header to
increase app performance](Using-headers-to-control-cache-duration.md "Using-headers-to-control-cache-duration.md").
