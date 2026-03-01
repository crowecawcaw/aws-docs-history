# Deploying server-side rendered applications with Amplify Hosting

You can use AWS Amplify to deploy and host web apps that use server-side rendering (SSR).
Amplify Hosting automatically detects applications created using the Next.js framework and you
don't have to perform any manual configuration in the AWS Management Console.

Amplify also supports any Javascript based SSR framework with an open source build adapter
that transforms an application's build output into the directory structure that Amplify
Hosting expects. For example, you can deploy app's created with the Nuxt, Astro, and SvelteKit
frameworks by installing the available adapters.

Advanced users can use the deployment specification to create a build adapter or configure a
post-build script.

You can deploy the following frameworks to Amplify Hosting with minimal
configuration.

**Next.js**

- Amplify supports Next.js 15 applications without the need for an adapter. To get
  started, see [Amplify support for Next.js](ssr-amplify-support.md "ssr-amplify-support.md").

**Nuxt.js**

- Amplify supports Nuxt.js application deployments with a preset adapter. To get
  started, see [Amplify support for Nuxt.js](nuxt-support.md "nuxt-support.md").

**Astro.js**

- Amplify supports Astro.js application deployments with a community adapter. To
  get started, see [Amplify support for Astro.js](astro-support.md "astro-support.md").

**SvelteKit**

- Amplify supports SvelteKit application deployments with a community adapter. To
  get started, see [Amplify support for SvelteKit](sveltekit-support.md "sveltekit-support.md").

**Open source adapters**

- **Use an open source adapter -** For instructions on
  using any adapter that isn't in the preceding list, see [Using open source adapters for any SSR framework](using-framework-adapter.md "using-framework-adapter.md") .
- **Build a framework adapter -** Framework authors that
  want to integrate features that a framework provides, can use the Amplify Hosting
  deployment specification to configure your build output to conform to the structure
  that Amplify expects. For more information, see [Using the Amplify Hosting deployment
  specification to configure build output](ssr-deployment-specification.md "ssr-deployment-specification.md").
- **Configure a post-build script -** You can use the
  Amplify Hosting deployment specification to manipulate your build output as needed for
  specific scenarios. For more information, see [Using the Amplify Hosting deployment
  specification to configure build output](ssr-deployment-specification.md "ssr-deployment-specification.md"). For an example, see [Deploying an Express server using the deployment manifest](deploy-express-server.md "deploy-express-server.md").

###### Topics

- [Amplify support for Next.js](ssr-amplify-support.md "ssr-amplify-support.md")
- [Amplify support for Nuxt.js](nuxt-support.md "nuxt-support.md")
- [Amplify support for Astro.js](astro-support.md "astro-support.md")
- [Amplify support for SvelteKit](sveltekit-support.md "sveltekit-support.md")
- [Deploying an SSR app to Amplify](#deploy-ssr-framework-app "#deploy-ssr-framework-app")
- [SSR supported features](ssr-supported-features.md "ssr-supported-features.md")
- [Troubleshooting SSR deployments](troubleshooting-ssr-deployment.md "troubleshooting-ssr-deployment.md")
- [Advanced: Open source adapters](advanced-open-source-adapters.md "advanced-open-source-adapters.md")

## Deploying an SSR app to Amplify

You can use these instructions to deploy an app created with any framework with a
deployment bundle that conforms to the build output that Amplify expects. If you're
deploying a Next.js application, no adapter is needed.

If you're deploying an SSR app that uses a framework adapter, you must first install and
configure the adapter. For instructions, see [Using open source adapters for any SSR framework](using-framework-adapter.md "using-framework-adapter.md").

###### To deploy an SSR app to Amplify Hosting

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. On the **All apps** page, choose **Create new
   app**.
3. On the **Start building with Amplify** page, choose your Git
   repository provider, then choose **Next**.
4. On the **Add repository branch** page do the following:
   1. Select the name of the repository to connect.
   2. Select the name of the repository branch to connect.
   3. Choose **Next**.

5. On the **App settings** page, Amplify automatically detects Next.js
   SSR apps.

If you are deploying an SSR app that uses an adapter for another framework, you must
explicitly enable Amazon CloudWatch Logs. Open the **Advanced settings** section, then
choose **Enable SSR app logs** in the **Server-Side Rendering
(SSR) deployment** section. 6. The app requires an IAM service role that Amplify assumes to deliver logs to your
AWS account.

The procedure for adding a service role varies depending on whether you want to create
a new role or use an existing one.

    * To create a new role:


    	1. Choose **Create and use a new service role**.
    * To use an existing role:


    	1. Choose **Use an existing role**.
    	2. In the service role list, select the role to use.

7. Choose **Next**.
8. On the **Review** page, choose **Save and
   deploy**.
