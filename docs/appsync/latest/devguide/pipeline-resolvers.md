# Configuring and using pipeline resolvers in AWS AppSync (VTL)

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the APPSYNC_JS
runtime and its guides [here](configuring-resolvers-js.md "configuring-resolvers-js.md").

AWS AppSync executes resolvers on a GraphQL field. In some cases, applications require executing multiple
operations to resolve a single GraphQL field. With pipeline resolvers, developers can now compose operations
called Functions and execute them in sequence. Pipeline resolvers are useful for applications that, for instance,
require performing an authorization check before fetching data for a field.

A pipeline resolver is composed of a **Before** mapping template, an **After** mapping template, and a list of Functions. Each Function has a **request** and **response** mapping template that it executes
against a data source. As a pipeline resolver delegates execution to a list of functions, it is therefore not
linked to any data source. Unit resolvers and functions are primitives that execute operations against data
sources. See the [Resolver mapping
template overview](resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview "resolver-mapping-template-reference-overview.md#aws-appsync-resolver-mapping-template-reference-overview") for more information.

## Step 1: Creating a pipeline resolver

In the AWS AppSync console, go to the **Schema** page.

Save the following schema:

```
schema {
    query: Query
    mutation: Mutation
}

type Mutation {
    signUp(input: Signup): User
}

type Query {
    getUser(id: ID!): User
}

input Signup {
    username: String!
    email: String!
}

type User {
    id: ID!
    username: String
    email: AWSEmail
}
```

We are going to wire a pipeline resolver to the **signUp** field on the
**Mutation** type. In the **Mutation** type on the
right side, choose **Attach** next to the `signUp` mutation field. On
the create resolver page, click on **Actions**, then **Update
runtime**. Choose `Pipeline Resolver`, then choose `VTL`, then choose
**Update**. The page should now show three sections: a **Before mapping template** text area, a **Functions** section, and an
**After mapping template** text area.

Our pipeline resolver signs up a user by first validating the email address input and then saving the user
in the system. We are going to encapsulate the email validation inside a **validateEmail** function, and the saving of the user inside a **saveUser** function. The **validateEmail** function executes first,
and if the email is valid, then the **saveUser** function executes.

The execution flow will be as follow:

1. Mutation.signUp resolver request mapping template
2. validateEmail function
3. saveUser function
4. Mutation.signUp resolver response mapping template

Because we will probably reuse the **validateEmail** function in other
resolvers on our API, we want to avoid accessing `$ctx.args` because these will change from one
GraphQL field to another. Instead, we can use the `$ctx.stash` to store the email attribute from the
`signUp(input: Signup)` input field argument.

**BEFORE** mapping template:

```
## store email input field into a generic email key
$util.qr($ctx.stash.put("email", $ctx.args.input.email))
{}
```

The console provides a default passthrough **AFTER** mapping template that will
we use:

```
$util.toJson($ctx.result)
```

Choose **Create** or **Save** to update the
resolver.

## Step 2: Creating a function

From the pipeline resolver page, in the **Functions** section, click on
**Add function**, then **Create new function**. It
is also possible to create functions without going through the resolver page; to do this, in the AWS AppSync
console, go to the **Functions** page. Choose the **Create
function** button. Let’s create a function that checks if an email is valid and comes from a
specific domain. If the email is not valid, the function raises an error. Otherwise, it forwards whatever input
it was given.

On the new function page, choose **Actions**, then **Update
runtime**. Choose `VTL`, then **Update**. Make sure you
have created a data source of the **NONE** type. Choose this data source in the
**Data source name** list. For **function name**,
enter in `validateEmail`. In the **function code** area, overwrite
everything with this snippet:

```
#set($valid = $util.matches("^[a-zA-Z0-9_.+-]+@(?:(?:[a-zA-Z0-9-]+\.)?[a-zA-Z]+\.)?(myvaliddomain)\.com", $ctx.stash.email))
#if (!$valid)
    $util.error("$ctx.stash.email is not a valid email.")
#end
{
    "payload": { "email": $util.toJson(${ctx.stash.email}) }
}
```

Paste this into the response mapping template:

```
$util.toJson($ctx.result)
```

Review your changes, then choose **Create**. We just created our **validateEmail** function. Repeat these steps to create the **saveUser** function with the following request and response mapping templates (For the sake of
simplicity, we use a **NONE** data source and pretend the user has been saved in
the system after the function executes.):

Request mapping template:

```
## $ctx.prev.result contains the signup input values. We could have also
## used $ctx.args.input.
{
    "payload": $util.toJson($ctx.prev.result)
}
```

Response mapping template:

```
## an id is required so let's add a unique random identifier to the output
$util.qr($ctx.result.put("id", $util.autoId()))
$util.toJson($ctx.result)
```

We just created our **saveUser** function.

## Step 3: Adding a function to a pipeline resolver

Our functions should have been added automatically to the pipeline resolver we just created. If this wasn't
the case, or you created the functions through the **Functions** page, you can
click on **Add function** on the resolver page to attach them. Add both the
**validateEmail** and **saveUser** functions to
the resolver. The **validateEmail** function should be placed before the **saveUser** function. As you add more functions, you can use the **move up** and **move down** options to reorganize the order of
execution of your functions. Review your changes, then choose **Save**.

## Step 4: Executing a query

In the AWS AppSync console, go to the **Queries** page. In the explorer,
ensure that you're using your mutation. If you aren't, choose `Mutation` in the drop-down list, then
choose `+`. Enter the following query:

```
mutation {
  signUp(input: {
    email: "nadia@myvaliddomain.com"
    username: "nadia"
  }) {
    id
    email
  }
}
```

This should return something like:

```
{
  "data": {
    "signUp": {
      "id": "256b6cc2-4694-46f4-a55e-8cb14cc5d7fc",
      "email": "nadia@myvaliddomain.com"
    }
  }
}
```

We have successfully signed up our user and validated the input email using a pipeline resolver. To follow a
more complete tutorial focusing on pipeline resolvers, you can go to [Tutorial: Pipeline Resolvers](tutorial-pipeline-resolvers.md#aws-appsync-tutorial-pipeline-resolvers "tutorial-pipeline-resolvers.md#aws-appsync-tutorial-pipeline-resolvers")
