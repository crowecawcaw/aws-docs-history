# GraphQL and AWS AppSync architecture

###### Note

This guide assumes the user has a working knowledge of the REST architectural style. We recommend reviewing
this and other front-end topics before working with GraphQL and AWS AppSync.

GraphQL is a query and manipulation language for APIs. GraphQL provides a flexible and intuitive syntax to
describe data requirements and interactions. It enables developers to ask for exactly what is needed and get back
predictable results. It also makes it possible to access many sources in a single request, reducing the number of
network calls and bandwidth requirements, therefore saving battery life and CPU cycles consumed by applications.

Making updates to data is made simple with mutations, allowing developers to describe how the data should
change. GraphQL also facilitates the quick setup of real-time solutions via subscriptions. All of these features
combined, coupled with powerful developer tools, make GraphQL essential to managing application data.

GraphQL is an alternative to REST. RESTful architecture is currently one of the more popular solutions for
client-server communication. It's centered on the concept of your resources (data) being exposed by a URL. These
URLs can be used to access and manipulate the data through CRUD (create, read, update, delete) operations in the
form of HTTP methods like `GET`, `POST`, and `DELETE`. REST's advantage is that
it's relatively simple to learn and implement. You can quickly set up RESTful APIs to call a wide range of
services.

However, technology is getting more complicated. As applications, tools, and services begin to scale for a
worldwide audience, the need for fast, scalable architectures is of paramount importance. REST has many
shortcomings when dealing with scalable operations. See this [use
case](https://aws.amazon.com/blogs/architecture/what-to-consider-when-modernizing-apis-with-graphql-on-aws/ "https://aws.amazon.com/blogs/architecture/what-to-consider-when-modernizing-apis-with-graphql-on-aws/") for an example.

In the following sections, we'll review some of the concepts surrounding RESTful APIs. We'll then introduce
GraphQL and how it works.

For more information about GraphQL and the benefits of migrating over to AWS, see the [Decision guide to GraphQL implementations](https://aws.amazon.com/graphql/guide/ "https://aws.amazon.com/graphql/guide/").

###### Topics

- [What is an API](what-is-an-api.md "what-is-an-api.md")
- [What is REST](what-is-rest.md "what-is-rest.md")
- [What is GraphQL](what-is-graphql.md "what-is-graphql.md")
- [Comparing REST and GraphQL](comparing-rest-graphql.md "comparing-rest-graphql.md")
- [Why Use GraphQL over REST](why-use-graphql.md "why-use-graphql.md")
- [Components of a GraphQL API](api-components.md "api-components.md")
- [Additional properties of GraphQL](graphql-properties.md "graphql-properties.md")
