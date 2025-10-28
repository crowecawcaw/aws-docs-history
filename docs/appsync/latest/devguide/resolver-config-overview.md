# Configuring resolvers in AWS AppSync

In the previous sections, you learned how to create your GraphQL schema and data source, then linked them
together in the AWS AppSync service. In your schema, you may have established one or more fields (operations) in your
query and mutation. While the schema described the kinds of data the operations would request from the data
source, it never implemented how those operations would behave around the data.

An operation's behavior is always implemented in the resolver, which will be linked to the field performing the
operation. For more information about how resolvers work in general, see the [Resolvers](resolver-components.md "resolver-components.md") page.

In AWS AppSync, your resolver is tied to a runtime, which is the environment in which your resolver executes.
Runtimes dictate the language that your resolver will be written in. There are currently two supported runtimes:
APPSYNC_JS (JavaScript) and Apache Velocity Template Language (VTL).

When implementing resolvers, there is a general structure they follow:

- **Before step**: When a request is made by the client, the resolvers for the
  schema fields being used (typically your queries, mutations, subscriptions) are passed the request data. The
  resolver will begin processing the request data with a before step handler, which allows some preprocessing
  operations to be performed before the data moves through the resolver.
- **Function(s)**: After the before step runs, the request
  is passed to the functions list. The first function in the list will execute against the
  data source. A function is a subset of your resolver's code containing its own request
  and response handler. A request handler will take the request data and perform
  operations against the data source. The response handler will process the data source's
  response before passing it back to the list. If there is more than one function, the
  request data will be sent to the next function in the list to be executed. Functions in
  the list will be executed serially in the order defined by the developer. Once all
  functions have been executed, the final result is passed to the after step.
- **After step**: The after step is a handler function that allows you to
  perform some final operations on the final function's response before passing it to the GraphQL
  response.
  This flow is an example of a pipeline resolver. Pipeline resolvers are supported in both runtimes. However,
  this is a simplified explanation of what pipeline resolvers can do. Also, we're describing only one possible
  resolver configuration. For more information about supported resolver configurations, see the [JavaScript resolvers
  overview](resolver-reference-overview-js.md "resolver-reference-overview-js.md") for APPSYNC_JS or the [Resolver mapping template
  overview](resolver-mapping-template-reference-overview.md "resolver-mapping-template-reference-overview.md") for VTL.

As you can see, resolvers are modular. In order for the components of the resolver to work properly, they must
be able to peer into the state of the execution from other components. From the [Resolvers](resolver-components.md "resolver-components.md") section, you know that each component
in the resolver can be passed vital information about the state of the execution as a set of arguments
(`args`, `context`, etc.). In AWS AppSync, this is handled strictly by the
`context`. It's a container for the information about the field being resolved. This can include
everything from arguments being passed, results, authorization data, header data, etc. For more information about
the context, see the [Resolver context object reference](resolver-context-reference-js.md "resolver-context-reference-js.md") for APPSYNC_JS or the [Resolver mapping template context
reference](resolver-context-reference.md "resolver-context-reference.md") for VTL.

The context isn't the only tool you can use to implement your resolver. AWS AppSync supports a wide range of
utilities for value generation, error handling, parsing, conversion, etc. You can see a list of utilities [here](resolver-util-reference-js.md "resolver-util-reference-js.md") for
APPSYNC_JS or [here](resolver-util-reference.md "resolver-util-reference.md") for VTL.

In the following sections, you will learn how to configure resolvers in your GraphQL API.

###### Topics

- [Creating basic queries (JavaScript)](configuring-resolvers-js.md "configuring-resolvers-js.md")
- [Creating basic queries (VTL)](configuring-resolvers.md "configuring-resolvers.md")
