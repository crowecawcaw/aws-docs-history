

# Deploy a SvelteKit app to Amplify Hosting
<a name="get-started-sveltekit"></a>

Use the following instructions to deploy a SvelteKit application to Amplify Hosting. You can use your own application, or create a starter app. For more information, see [Creating a project](https://kit.svelte.dev/docs/creating-a-project) in the *SvelteKit documentation*.

To deploy a SvelteKit app with SSR to Amplify Hosting, you must add an adapter to your project. We do not maintain an Amplify owned adapter for the SvelteKit framework. In this example, we are using the `amplify-adapter` created by a member of the community. The adapter is available at [github.com/gzimbron/amplify-adapter](https://github.com/gzimbron/amplify-adapter) on the GitHub website. AWS does not maintain this adapter.

**To deploy a SvelteKit app to Amplify Hosting**

1. On your local computer, navigate to the SvelteKit application to deploy.

1. To install the adapter, open a terminal window and run the following command. This example uses the community adapter available at [github.com/gzimbron/amplify-adapter](https://github.com/gzimbron/amplify-adapter). If you are using a different community adapter, replace {{amplify-adapter}} with the name of your adapter.

   ```
   npm install {{amplify-adapter}}
   ```

1. In the project folder for your SvelteKit app, open the `svelte.config.js` file. Edit the file to use the `amplify-adapter` or replace {{'amplify-adapter'}} with the name of your adapter. The file should look like the following.

   ```
   import adapter from {{'amplify-adapter'}};
   import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
   
                 
   /** @type {import('@sveltejs/kit').Config} */
   const config = {
           // Consult https://kit.svelte.dev/docs/integrations#preprocessors
           // for more information about preprocessors
           preprocess: vitePreprocess(),
   
           kit: {
                   // adapter-auto only supports some environments, see https://kit.svelte.dev/docs/adapter-auto for a list.
                   // If your environment is not supported, or you settled on a specific environment, switch out the adapter.
                   // See https://kit.svelte.dev/docs/adapters for more information about adapters.
                   adapter: adapter()
           }
   };
   
   export default config;
   ```

1. Commit the change and push the application to your Git repository.

1. Now you are ready to deploy your SvelteKit app to Amplify.

   Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. On the **All apps** page, choose **Create new app**.

1. On the **Start building with Amplify** page, choose your Git repository provider, then choose **Next**.

1. On the **Add repository branch** page, do the following:

   1. Select the name of the repository to connect.

   1. Select the name of the repository branch to connect.

   1. Choose **Next**.

1. On the **App settings** page, locate the **Build settings** section. For **Build output directory** enter **build**.

1. You must also update the app's frontend build commands in the build specification. To open the build specification, choose **Edit YML file**.

1. In the `amplify.yml` file, locate the frontend build commands section. Enter **- cd build/compute/default/** and **- npm i --production**.

   Your build settings file should look like the following.

   ```
   version: 1
   frontend:
       phases:
           preBuild:
               commands:
                   - 'npm ci --cache .npm --prefer-offline'
           build:
               commands:
                   - 'npm run build'
                   - 'cd build/compute/default/'
                   - 'npm i --production'
                 
       artifacts:
           baseDirectory: build
           files:
               - '**/*'
       cache:
           paths:
               - '.npm/**/*'
   ```

1. Choose **Save**.

1. If you want Amplify to be able to deliver app logs to Amazon CloudWatch Logs, you must explicitly enable this in the console. Open the **Advanced settings** section, then choose **Enable SSR app logs** in the ** Server-Side Rendering (SSR) deployment** section.

1. Choose **Next**.

1. On the **Review** page, choose **Save and deploy**.