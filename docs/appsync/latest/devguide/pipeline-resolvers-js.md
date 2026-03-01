# Configuring and using pipeline resolvers in AWS AppSync (JavaScript)

AWS AppSync executes resolvers on a GraphQL field. In some cases, applications require executing multiple
operations to resolve a single GraphQL field. With pipeline resolvers, developers can now compose operations
called Functions and execute them in sequence. Pipeline resolvers are useful for applications that, for instance,
require performing an authorization check before fetching data for a field.

For more information about the architecture of a JavaScript pipeline resolver, see the [JavaScript
resolvers overview](resolver-reference-overview-js.md#anatomy-of-a-pipeline-resolver-js "resolver-reference-overview-js.md#anatomy-of-a-pipeline-resolver-js").

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
right side, choose **Attach** next to the `signUp` mutation field. Set
the resolver to `pipeline resolver` and the `APPSYNC_JS` runtime, then create the
resolver.

Our pipeline resolver signs up a user by first validating the email address input and then saving the user
in the system. We are going to encapsulate the email validation inside a **validateEmail** function and the saving of the user inside a **saveUser** function. The **validateEmail** function executes first,
and if the email is valid, then the **saveUser** function executes.

The execution flow will be as follows:

1. Mutation.signUp resolver request handler
2. validateEmail function
3. saveUser function
4. Mutation.signUp resolver response handler

Because we will probably reuse the **validateEmail** function in other
resolvers on our API, we want to avoid accessing `ctx.args` because these will change from one
GraphQL field to another. Instead, we can use the `ctx.stash` to store the email attribute from the
`signUp(input: Signup)` input field argument.

Update your resolver code by replacing your request and response functions:

```
export function request(ctx) {
    ctx.stash.email = ctx.args.input.email
    return {};
}

export function response(ctx) {
    return ctx.prev.result;
}
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

Make sure you have created a data source of the **NONE** type. Choose this data
source in the **Data source name** list. For the **function
name**, enter in `validateEmail`. In the **function code**
area, overwrite everything with this snippet:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { email } = ctx.stash;
  const valid = util.matches(
    '^[a-zA-Z0-9_.+-]+@(?:(?:[a-zA-Z0-9-]+\.)?[a-zA-Z]+\.)?(myvaliddomain)\.com',
    email
  );
  if (!valid) {
    util.error(`"${email}" is not a valid email.`);
  }

  return { payload: { email } };
}

export function response(ctx) {
  return ctx.result;
}
```

Review your inputs, then choose **Create**. We just created our **validateEmail** function. Repeat these steps to create the **saveUser** function with the following code (For the sake of simplicity, we use a **NONE** data source and pretend the user has been saved in the system after the function
executes.):

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  return ctx.prev.result;
}

export function response(ctx) {
  ctx.result.id = util.autoId();
  return ctx.result;
}
```

We just created our **saveUser** function.

## Step 3: Adding a function to a pipeline resolver

Our functions should have been added automatically to the pipeline resolver we just created. If this wasn't
the case, or you created the functions through the **Functions** page, you can
click on **Add function** back on the `signUp` resolver page to attach
them. Add both the **validateEmail** and **saveUser**
functions to the resolver. The **validateEmail** function should be placed before
the **saveUser** function. As you add more functions, you can use the **move up** and **move down** options to reorganize the
order of execution of your functions. Review your changes, then choose **Save**.

## Step 4: Running a query

In the AWS AppSync console, go to the **Queries** page. In the explorer,
ensure that you're using your mutation. If you aren't, choose `Mutation` in the drop-down list, then
choose `+`. Enter the following query:

```
mutation {
  signUp(input: {email: "nadia@myvaliddomain.com", username: "nadia"}) {
    id
    username
  }
}
```

This should return something like:

```
{
  "data": {
    "signUp": {
      "id": "256b6cc2-4694-46f4-a55e-8cb14cc5d7fc",
      "username": "nadia"
    }
  }
}
```

We have successfully signed up our user and validated the input email using a pipeline resolver.
