# Comparing REST and GraphQL

APIs (Application Programming Interfaces) play a crucial role in facilitating data
exchange between applications. As stated earlier, two prominent approaches for designing
APIs have emerged: GraphQL and REST. While both serve the fundamental purpose of enabling
client-server communication, they differ significantly in their implementation and use
cases.

GraphQL and REST share several key characteristics:

1. **Client-Server Model**: Both use a client-server
   architecture for data exchange.
2. **Statelessness**: Neither maintains client session
   information between requests.
3. **HTTP-Based**: Both typically use HTTP as the
   underlying communication protocol.
4. **Resource-Oriented Design**: Both design their data
   interchange around resources, which refer to any data or object that the client can
   access and manipulate through the API.
5. **Data Format Flexibility**: JSON is the most
   commonly used data exchange format in both, though other formats like XML and HTML
   are also supported.
6. **Language and Database Agnostic**: Both can work
   with any programming language or database structure, making them highly
   interoperable.
7. **Caching Support**: Both support caching, allowing
   clients and servers to store frequently accessed data for improved performance.
   While sharing some fundamental principles, GraphQL and REST differ significantly in
   their approach to API design and data fetching:

8. **Request Structure and Data Fetching**

REST uses different HTTP methods (GET, POST, PUT, DELETE) to perform operations on
resources. This often requires multiple endpoints for different resources, which can
lead to inefficiencies in data retrieval. For example, running a GET operation to
retrieve a user's data may lead to data over-fetching or under-fetching. To get the
correct data, truncation or multiple operations may be called.

GraphQL uses a single endpoint for all operations. It relies on queries for
fetching data and mutations for modifying data. Clients can use queries to fetch
exactly the data they need in a single request, which reduces network overhead by
minimizing data transfer. 2. **Server-side Schema**

REST doesn't require a server-side schema, though one can be optionally defined
for efficient API design and documentation.

GraphQL uses a strongly-typed server-side schema to define data and data services.
The schema, written in GraphQL Schema Definition Language (SDL), includes object
types and fields for each object and server-side resolver functions that define
operations for each field. 3. **Versioning**

REST often includes versioning in the URL, which can lead to maintaining multiple
API versions simultaneously. Versioning is not mandatory but can help prevent
breaking changes.

GraphQL promotes a continuous evolution of the API without explicit versioning by
requiring backward compatibility. Deleted fields return error messages, while
deprecation tags phase out old fields and return warning messages. 4. **Error Handling**

REST is weakly typed, requiring error handling to be built into the surrounding
code. This may not automatically identify type-related errors (e.g., parsing a number
as text).

By contrast, GraphQL is strongly typed and requires a comprehensive schema
definition. This allows your service to automatically identify many request errors
with a high level of detail. 5. **Use Cases**

REST is better suited for:

    * Smaller applications with less complex data requirements.
    * Scenarios where data and operations are used similarly by all clients.
    * Applications without complex data querying needs.

GraphQL is better suited for:

    * Scenarios with limited bandwidth, where minimizing requests and responses is
     crucial.
    * Applications with multiple data sources that need to be combined at a single
     endpoint.
    * Cases where client requests vary significantly and expect different response
     structures.

Note that it's possible to use both GraphQL and REST APIs within a single
application for different areas of functionality. Furthermore, you can upgrade a
RESTful API to include GraphQL capabilities without a complete rewrite. See [How to
build GraphQL resolvers for AWS data sources](https://aws.amazon.com/graphql/resolvers/ "https://aws.amazon.com/graphql/resolvers/") for an example.
