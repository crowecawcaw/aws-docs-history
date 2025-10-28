# Deploying a Next.js app in a monorepo

Amplify supports apps in generic monorepos as well as apps in monorepos created using
npm workspace, pnpm workspace, Yarn workspace, Nx, and Turborepo. When you deploy your app,
Amplify automatically detects the monorepo build framework that you are using. Amplify
automatically applies build settings for apps in an npm workspace, Yarn workspace or Nx.
Turborepo and pnpm apps require additional configuration. For more information, see [Configuring monorepo build settings](monorepo-configuration.md "monorepo-configuration.md").

For a detailed Nx example, see the [Share code between Next.js apps with Nx on AWS Amplify Hosting](https://aws.amazon.com/blogs/mobile/share-code-between-next-js-apps-with-nx-on-aws-amplify-hosting/ "https://aws.amazon.com/blogs/mobile/share-code-between-next-js-apps-with-nx-on-aws-amplify-hosting/") blog post.
