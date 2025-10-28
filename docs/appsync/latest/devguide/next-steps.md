# Supplemental sections for the AWS AppSync console

These sections are a reference for more advanced AWS AppSync topics. We recommend following the _Supplemental reading_ section before doing anything else.

## Integration

In the console tab, if you choose the name of your API, the **Integration**
page appears:

![AWS AppSync sidebar menu with APIs, Todo API highlighted, and other options listed.](images/explorer-example-6.png)

It summarizes the steps for setting up your API and outlines the next steps for building a client
application. The **Integrate with your app** section provides details for using
the [AWS Amplify toolchain](https://aws-amplify.github.io/ "https://aws-amplify.github.io/") to automate the process of
connecting your API with iOS, Android, and JavaScript applications through config and code generation. The
Amplify toolchain provides full support for building projects from your local workstation including GraphQL
provisioning and workflows for CI/CD.

The **Client Samples** section also lists sample client applications (e.g.,
JavaScript, iOS, Android) for testing an end-to-end experience. You can clone and download these samples,
and the configuration file has the necessary information (such as your endpoint URL) you need to get
started. Follow the instructions on the [AWS Amplify
toolchain](https://aws-amplify.github.io/ "https://aws-amplify.github.io/") page to run your app.

## Supplemental reading

- [Designing GraphQL APIs with AWS AppSync](designing-a-graphql-api.md "designing-a-graphql-api.md") - This is a
  comprehensive guide for creating your GraphQL using a blank schema with no data sources or
  resolvers.
