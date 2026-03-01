# Welcome to AWS Amplify Hosting

Amplify Hosting provides a Git-based workflow for hosting full-stack serverless web
applications with continuous deployment. Amplify deploys your app to the AWS global content
delivery network (CDN). This user guide provides the information you need to get started with
Amplify Hosting.

## Supported frameworks

Amplify Hosting supports many common SSR frameworks, single-page application (SPA)
frameworks, and static site generators, including the following.

###### SSR frameworks

- Next.js
- Nuxt
- Astro with a community adapter
- SvelteKit with a community adapter
- Any SSR framework with a custom adapter

###### SPA frameworks

- React
- Angular
- Vue.js
- Ionic
- Ember

###### Static site generators

- Eleventy
- Gatsby
- Hugo
- Jekyll
- VuePress

## Amplify Hosting features

**[Feature branches](multi-environments.md "multi-environments.md")**

Manage production and staging environments for your frontend and backend by
connecting new branches.

**[Custom domains](custom-domains.md "custom-domains.md")**

Connect your application to a custom domain.

**[Pull request previews](pr-previews.md "pr-previews.md")**

Preview changes during code reviews.

**[End-to-end testing](running-tests.md "running-tests.md")**

Improve your app quality with end-to-end tests.

**[Password protected branches](access-control.md "access-control.md")**

Password protect your web app so you can work on new features without making
them publicly accessible.

**[Redirects and rewrites](redirects.md "redirects.md")**

Set up rewrites and redirects to maintain SEO rankings and route traffic based
on your client app requirements.

**Atomic deployments**

Atomic deployments eliminate maintenance windows by ensuring that your web app
is updated only after the entire deployment finishes. This eliminates scenarios
where files fail to upload properly.

## Getting started with Amplify Hosting

To get started with Amplify Hosting, see the [Getting started with deploying an app to Amplify Hosting](getting-started.md "getting-started.md") tutorial. After completing the tutorial, you will know
how to connect a web app in a Git repository (GitHub, BitBucket, GitLab, or AWS CodeCommit) and
deploy it to Amplify Hosting with continuous deployment.

## Building a backend

AWS Amplify Gen 2 introduces a TypeScript-based, code-first developer experience for
defining backends. To learn how to use Amplify Gen 2 to build and connect a backend to
your app, see [Build &
connect backend](https://docs.amplify.aws/nextjs/build-a-backend "https://docs.amplify.aws/nextjs/build-a-backend") in the _Amplify docs_.

To better understand Amplify Gen 2's code-first approach, see the
[Amplify Gen 2
Workshop](https://catalog.workshops.aws/amplify-core/en-US "https://catalog.workshops.aws/amplify-core/en-US") on the _AWS Workshop Studio_ website. In this
comprehensive tutorial, you build a serverless application with React and Next.js and learn
how to use Amplify Gen 2 Data and Auth libraries and the Amplify UI library to add functionality
to the application.

If you are looking for the documentation for building backends for a Gen 1 app, using
the CLI and Amplify Studio, see [Build & connect
backend](https://docs.amplify.aws/gen1/react/build-a-backend/ "https://docs.amplify.aws/gen1/react/build-a-backend/") in the _Gen 1 Amplify docs_.

## Amplify Hosting pricing

AWS Amplify only charges you for what you use. For more information, see [AWS Amplify Pricing](https://aws.amazon.com/amplify/pricing/ "https://aws.amazon.com/amplify/pricing/").
