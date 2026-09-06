

# Deploy a Nuxt.js app to Amplify Hosting
<a name="get-started-nuxt"></a>

Use the following instructions to deploy a Nuxt.js application to Amplify Hosting. Nuxt has implemented a preset adapter using the Nitro server. This enables you to deploy a Nuxt project without any additional configuration.

**To deploy a Nuxt app to Amplify Hosting**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. On the **All apps** page, choose **Create new app**.

1. On the **Start building with Amplify** page, choose your Git repository provider, then choose **Next**.

1. On the **Add repository branch** page, do the following:

   1. Select the name of the repository to connect.

   1. Select the name of the repository branch to connect.

   1. Choose **Next**.

1. If you want Amplify to be able to deliver app logs to Amazon CloudWatch Logs, you must explicitly enable this in the console. Open the **Advanced settings** section, then choose **Enable SSR app logs** in the ** Server-Side Rendering (SSR) deployment** section.

1. Choose **Next**.

1. On the **Review** page, choose **Save and deploy**.