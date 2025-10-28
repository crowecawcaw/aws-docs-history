# Taking a tour of the AWS AppSync console

Before we add data to our DynamoDB table, we should review the basic features of the AWS AppSync console
experience. The AWS AppSync console tab on the left-hand side of the page allows users to easily navigate to any
of the major components or configuration options that AWS AppSync provides:

![AWS AppSync console navigation menu showing APIs, Todo API options, and Documentation link.](images/explorer-example-5.jpg)

## Schema designer

Choose **Schema** to view the schema you just created. If you review the
schema's contents, you'll notice that it has already been loaded with a bunch of helper operations to
streamline the development process. In the **Schema** editor, if you scroll
through the code, you'll eventually reach the model you defined in the previous section:

```
type Todo {
	id: ID!
	name: String
	when: String
	where: String
	description: String
}
```

Your model became the base type that was used throughout your schema. We'll start adding data to our data
source using mutations that were automatically generated from this type.

Here are some additional tips and facts about the **Schema** editor:

1. The code editor has linting and error-checking capabilities that you can use when writing your own
   apps.
2. The right side of the console shows the GraphQL types that have been created and resolvers on
   different top-level types, such as queries.
3. When adding new types to a schema (for example, `type User {...}`), you can have
   AWS AppSync provision DynamoDB resources for you. These include the proper primary key, sort key, and index
   design to best match your GraphQL data access pattern. If you choose **Create
   Resources** at the top and choose one of these user-defined types from the menu, you can
   choose different field options in the schema design. We will cover this in the [design a schema](designing-your-schema.md#aws-appsync-designing-your-schema "designing-your-schema.md#aws-appsync-designing-your-schema") section.

### Resolver configuration

In the schema designer, the **Resolvers** section contains all of the
types and fields in your schema. If you scroll through the list of fields, you'll notice that you can
attach resolvers to certain fields by choosing **Attach**. This will open up
a code editor in which you can write your resolver code. AWS AppSync supports both VTL and JavaScript
runtimes, which can be changed at the top of the page by choosing **Actions**, then **Update Runtime**. At the bottom of the page,
you can also create functions that will run several operations in a sequence. However, resolvers are an
advanced topic, and we won't be covering that in this section.

## Data sources

Choose **Data sources** to view your DynamoDB table. By choosing the
`Resource` option (if available), you can view your data source's configuration. In our
example, this leads to the DynamoDB console. From there, you can edit your data. You can also directly edit
some of the data by choosing the data source, then choosing **Edit**. If you
ever need to delete your data source, you can choose your data source, then select **Delete**. Lastly, you can create new data sources by choosing **Create data
source**, then configuring the name and type. Note that this option is for linking the AWS AppSync
service to an existing resource. You still need to create the resource in your account using the relevant
service before AWS AppSync recognizes it.

## Queries

Choose **Queries** to view your queries and mutations. When we created our
GraphQL API using our model, AWS AppSync automatically generated some helper mutations and queries for testing
purposes. In the query editor, the left-hand side contains the **Explorer**.
This is a list showing all of your mutations and queries. You can easily enable the operations and fields
you want to use here by clicking on their name values. This will cause the code to appear automatically in
the center part of the editor. Here, you can edit your mutations and queries by modifying values. At the
bottom of the editor, you have the **Query Variable** editor that allows you to
enter the field values for the input variables of your operations. Choosing **Run** at the top of the editor will bring up a drop-down list to select the query/mutation to
run. The output for this run will appear on the right-hand side of the page. Back in the **Explorer** section at the top, you can choose an operation (Query, Mutation,
Subscription), then choose the **+** symbol to add a new instance of that
particular operation. At the top of the page, there will be another drop-down list that contains the
authorization mode for your query runs. However, we will not be covering that feature in this section (For
more information, see [Security](security-authz.md#aws-appsync-security "security-authz.md#aws-appsync-security").).

## Settings

Choose **Settings** to view some configuration options for your GraphQL API.
Here, you can enable some options like logging, tracing, and web application firewall functionality. You can
also add new authorization modes to protect your data from unwanted leaks to the public. However, these
options are more advanced and will not be covered in this section.

###### Note

The default authorization mode, `API_KEY`, uses an API key to test the application. This is
the base authorization that's given to all newly created GraphQL APIs. We recommend that you use a
different method for production. For the sake of the example in this section, we will only use the API
key. For more information about the supported authorization methods, see [Security](security-authz.md#aws-appsync-security "security-authz.md#aws-appsync-security").
