# Designing GraphQL APIs with AWS AppSync

AWS AppSync allows you to create GraphQL APIs using the console experience. You caught a glimpse of this in the
[Launching a sample schema](quickstart.md "quickstart.md") section. However,
that guide didn't show the entire catalog of options and configurations that you could leverage in AWS AppSync.

When you choose to create a GraphQL API in the console, there are several options to explore. If you followed
our [Launching a sample schema](quickstart.md "quickstart.md") guide, we showed
you how to create an API from a predefined model. In the following sections, we will guide you through the rest of
the options and configurations for creating GraphQL APIs in AWS AppSync.

In this section, you'll review the following concepts:

1. [Blank APIs or imports](blank-import-api.md#aws-appsync-blank-import-api "blank-import-api.md#aws-appsync-blank-import-api"): This guide will run through the entire creation
   process for creating a GraphQL API. You'll learn how to create a GraphQL from a blank template with no
   model, configure data sources for your schema, and add your first resolver to a field.
2. [Real-time data](aws-appsync-real-time-data.md#aws-appsync-real-time-data-anchor "aws-appsync-real-time-data.md#aws-appsync-real-time-data-anchor"): This guide will show you the potential options for creating
   an API using AWS AppSync's WebSocket engine.
3. [Merged APIs](merged-api.md#aws-appsync-merged-api "merged-api.md#aws-appsync-merged-api"): This guide will show you how to create new GraphQL APIs by associating and
   merging data from multiple existing GraphQL APIs.
4. [Building GraphQL APIs with RDS introspection](rds-introspection.md "rds-introspection.md"): This guide will show you how to integrate your Amazon RDS tables using a Data API.
