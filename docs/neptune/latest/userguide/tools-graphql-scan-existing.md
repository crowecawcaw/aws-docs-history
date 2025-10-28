# Scanning data in an existing Neptune database

Whether you are familiar with GraphQL or not, the command below is the fastest
way to create a GraphQL API. This assumes that you have installed and configured the
Neptune utility for GraphQL as described in the [installation
section](tools-graphql-setup.md "tools-graphql-setup.md"), so that it's connected to the endpoint of your Neptune database.

```
neptune-for-graphql \
  --input-graphdb-schema-neptune-endpoint `(your neptune database endpoint)`:`(port number)` \
  --create-update-aws-pipeline \
  --create-update-aws-pipeline-name `(your new GraphQL API name)` \
  --output-resolver-query-https
```

The utility analyzes the database to discover the schema of the nodes, edges, and
properties in it. Based on that schema, it infers a GraphQL schema with associated
queries and mutations. Then it creates an AppSync GraphQL API and the required AWS
resources to use it. These resources include a pair of IAM roles and a Lambda
function containing the GraphQL resolver code.

When the utility has finished you'll find a new GraphQL API in the AppSync
console under the name you assigned in the command. To test it, use
the AppSync **Queries** option on the menu.

If you run the same command again after adding more data to the database,
will update the AppSync API and Lambda code accordingly.

To release all the resources associated with the command, run:

```
neptune-for-graphql \
  --remove-aws-pipeline-name `(your new GraphQL API name from above)`
```
