# Monorepo custom header requirements

When you specify custom headers for an app in a monorepo, be aware of the following setup
requirements:

- There is a specific YAML format for a monorepo. For the correct syntax, see [Custom header YAML reference](custom-header-YAML-format.md "custom-header-YAML-format.md").
- You can specify custom headers for an application in a monorepo using the
  **Custom headers** section of the Amplify console. You must redeploy
  your application to apply the new custom headers.
- As an alternative to using the console, you can specify custom headers for an app in a
  monorepo in a `customHttp.yml` file. You must save the
  `customHttp.yml` file in the root of your repo and then redeploy the
  application to apply the new custom headers. Custom headers specified in the
  `customHttp.yml` file override any custom headers specified using the
  **Custom headers** section of the
  Amplify console.
