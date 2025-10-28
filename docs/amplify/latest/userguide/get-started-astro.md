# Deploy an Astro.js app to Amplify Hosting

Use the following instructions to deploy an Astro.js application to Amplify Hosting.
You can use an existing application, or create a starter application using one of the
official examples that Astro provides. To create a starter application, see [Use
a theme or starter template](https://docs.astro.build/en/install-and-setup/#use-a-theme-or-starter-template "https://docs.astro.build/en/install-and-setup/#use-a-theme-or-starter-template") in the _Astro
documentation_.

To deploy an Astro site with SSR to Amplify Hosting, you must add an adapter to your
application. We do not maintain an Amplify owned adapter for the Astro framework. This
tutorial uses the `astro-aws-amplify` adapter that was created by a
member of the community. This adapter is available at [github.com/alexnguyennz/astro-aws-amplify](https://github.com/alexnguyennz/astro-aws-amplify "https://github.com/alexnguyennz/astro-aws-amplify") on the GitHub website. AWS does not
maintain this adapter.

###### To deploy an Astro app to Amplify Hosting

1. On your local computer, navigate to the Astro application to deploy.
2. To install the adapter, open a terminal window and run the following command. This
   example uses the community adapter available at [github.com/alexnguyennz/astro-aws-amplify](https://github.com/alexnguyennz/astro-aws-amplify "https://github.com/alexnguyennz/astro-aws-amplify"). You can replace
   `astro-aws-amplify` with the name of the adapter that you
   are using.

```
npm install `astro-aws-amplify`
```

3. In the project folder for your Astro app, open the
   `astro.config.mjs` file. Update the file to add the adapter.
   The file should look like the following.

```
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
`import awsAmplify from 'astro-aws-amplify';`

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://example.com',
  integrations: [mdx(), sitemap()],
  adapter: `awsAmplify()`,
  output: 'server',
});
```

4. Commit the change and push the project to your Git repository.

Now you are ready to deploy your Astro app to Amplify. 5. Sign in to the AWS Management Console and open the [Amplify
console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/"). 6. On the **All apps** page, choose **Create new
app**. 7. On the **Start building with Amplify** page, choose your Git
repository provider, then choose **Next**. 8. On the **Add repository branch** page, do the following:

    1. Select the name of the repository to connect.
    2. Select the name of the repository branch to connect.
    3. Choose **Next**.

9. On the **App settings** page, locate the **Build
   settings** section. For **Build output directory** enter
   `.amplify-hosting`.
10. You must also update the app's frontend build commands in the build
    specification. To open the build specification, choose **Edit YML file**.
11. In the `amplify.yml` file, locate the frontend build commands
    section. Enter `mv node_modules
./.amplify-hosting/compute/default`

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
                - 'mv node_modules ./.amplify-hosting/compute/default'
    artifacts:
        baseDirectory: .amplify-hosting
        files:
            - '**/*'
    cache:
        paths:
            - '.npm/**/*'

```

12. Choose **Save**.
13. If you want Amplify to be able to deliver app logs to Amazon CloudWatch Logs, you must
    explicitly enable this in the console. Open the **Advanced
    settings** section, then choose **Enable SSR app logs**
    in the **Server-Side Rendering (SSR) deployment** section.
14. Choose **Next**.
15. On the **Review** page, choose **Save and
    deploy**.
