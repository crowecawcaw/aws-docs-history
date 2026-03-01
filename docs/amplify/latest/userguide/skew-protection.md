# Skew protection for Amplify deployments

Deployment skew protection is available to Amplify applications to eliminate version skew
issues between client and servers in web applications. When you apply skew protection to an
Amplify application, you can ensure that your clients always interact with the correct version
of server-side assets, regardless of when a deployment occurs.

Version skew is a common challenge for web developers. It occurs when a web browser is
running an outdated version of an application and the server is running a new one. This
discrepancy can cause unpredictable behavior, errors, and a degraded experience for the user of
the application. The Amplify deployment skew protection feature pins clients running on web
browsers to a specific deployment. This ensures that Amplify always serves the assets for that
particular deployment, keeping the client and server synchronized.

Amplify's skew protection feature can reduce errors for your application's users as you
release new deployments. It can also improve the developer experience by reducing the time spent
managing backward and forward compatibility issues.

Skew protection feature details:

**Supported application types**

You can add skew protection to static and SSR applications created with any framework
that Amplify supports. Applications can be deployed from a Git repository or a manual
deployment.

You can't add skew protection to an application that is deployed to the
`WEB_DYNAMIC` platform (Next.js version 11 or earlier).

**Duration**

For static applications, Amplify serves one week of deployments. For SSR
applications, we guarantee skew protection for up to eight previous deployments.

**Cost**

There is no additional cost for adding skew protection to an application.

**Performance consideration**

When skew protection is enabled for an application, Amplify must update its CDN
cache configurations. Therefore, you should expect your first deployment after enabling
skew protection to take up to ten minutes.

###### Topics

- [Configuring deployment skew protection for an Amplify application](configure-skew-protection.md "configure-skew-protection.md")
- [How skew protection works](skew-protection-headers.md "skew-protection-headers.md")
