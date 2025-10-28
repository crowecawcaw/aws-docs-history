# Making environment variables accessible to

server-side runtimes

Amplify Hosting supports adding environment variables to your application's builds by
setting them in the project's configuration in the Amplify console.

However, a Next.js
server component doesn't have access to those environment variables by default. This
behavior is intentional to protect any secrets stored in environment variables that your
application uses during the build phase.

To make specific environment variables accessible to Next.js, you can modify the
Amplify build specification file to set them in the environment files that Next.js
recognizes. This enables Amplify to load these environment variables before it builds the
application.

###### Important

We strongly recommend that you don't store any credentials, secrets, or sensitive information in your environment variables as any user with access
to deployment artifacts can read them.

To give your SSR compute function access to AWS resources, we recommend [using IAM roles](amplify-SSR-compute-role.md "amplify-SSR-compute-role.md").

The following build specification example demonstrates how to add environment
variables in the build commands section.

```
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        - env | grep -e API_BASE_URL >> .env.production
        - env | grep -e NEXT_PUBLIC_ >> .env.production
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
      - .next/cache/**/*
```

In this example, the build commands section includes two commands that write environment
variables to the `.env.production` file before the application build
runs. Amplify Hosting allows your application to access these variables when the
application receives traffic.

The following line from the build commands section in the preceding example demonstrates
how to take a specific variable from the build environment and add it to the
`.env.production` file.

```
- env | grep -e API_BASE_URL -e APP_ENV >> .env.production
```

If the variables exist in your build environment, the
`.env.production` file will contain the following environment
variables.

```
API_BASE_URL=localhost
APP_ENV=dev
```

The following line from the build commands section in the preceding example demonstrates
how to add an environment variable with a specific prefix to the
`.env.production` file. In this example, all variables with the prefix
`NEXT_PUBLIC_` are added.

```
- env | grep -e NEXT_PUBLIC_ >> .env.production
```

If multiple variables with the `NEXT_PUBLIC_` prefix exist in the build
environment, the `.env.production` file will look similar to the
following.

```
NEXT_PUBLIC_ANALYTICS_ID=abcdefghijk
NEXT_PUBLIC_GRAPHQL_ENDPOINT=uowelalsmlsadf
NEXT_PUBLIC_FEATURE_FLAG=true
```

## SSR environment variables for

monorepos

If you are deploying an SSR app in a monorepo and want to make specific environment
variables accessible to Next.js, you must prefix the `.env.production`
file with your application root. The following example build specification for a Next.js
app within a Nx monorepo demonstrates how to add environment variables in the build
commands section.

```
version: 1
applications:
  - frontend:
      phases:
        preBuild:
          commands:
            - npm ci
        build:
          commands:
            - env | grep -e API_BASE_URL -e APP_ENV >> apps/app/.env.production
            - env | grep -e NEXT_PUBLIC_ >> apps/app/.env.production
            - npx nx build app
      artifacts:
        baseDirectory: dist/apps/app/.next
        files:
          - '**/*'
      cache:
        paths:
          - node_modules/**/*
      buildPath: /
    appRoot: apps/app
```

The following lines from the build commands section in the preceding example
demonstrate how to take specific variables from the build environment and add them to the
`.env.production` file for an app in a monorepo with the application
root `apps/app`.

```
- env | grep -e API_BASE_URL -e APP_ENV >> apps/app/.env.production
- env | grep -e NEXT_PUBLIC_ >> apps/app/.env.production
```
