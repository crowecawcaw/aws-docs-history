# Why Use GraphQL over REST?

REST is one of the cornerstone architectural styles of web APIs. However, as the world
becomes more interconnected, the need to develop robust and scalable applications will
become a more pressing issue. While REST is often used to build web APIs, there are several
recurring drawbacks to RESTful implementations that have been identified:

1. **Data requests**: Using RESTful APIs, you would typically request the
   data you need through endpoints. The problem arises when you have data that may not be so neatly
   packaged. The data you need may be sitting behind multiple layers of abstraction, and the only way to
   fetch the data is by using multiple endpoints, which means making multiple requests to extract all of the
   data.
2. **Overfetching and underfetching**: To add to the problems of multiple
   requests, the data from each endpoint is strictly defined, meaning you will return whatever data was
   defined for that API, even if you didn't technically want it.

This can result in _over-fetching_, which means our requests return
superfluous data. For example, let's say you're requesting company personnel data and want to know the
names of the employees in a certain department. The endpoint that returns the data will contain the
names, but it might also contain other data like job title or date of birth. Because the API is fixed,
you can't just request the names alone; the rest of the data comes with it.

The opposite situation in which we don't return enough data is called _under-fetching_. To get all of the requested data, you may have to make multiple requests
to the service. Depending on how the data was structured, you could run into inefficient queries
resulting in issues like the dreaded n+1 problem. 3. **Slow development iterations**: Many developers tailor their RESTful
APIs to fit the flow of their applications. However, as their applications grow, both the front- and
backends may require extensive changes. As a result, the APIs may no longer fit the shape of the data in
a way that's efficient or impactful. This results in slower product iterations due to the need for API
modifications. 4. **Performance at scale**: Due to these compounding issues, there are many
areas where scalability will be impacted. Performance on the application side may be impacted because
your requests will return too much data or too little (resulting in more requests). Both situations cause
unnecessary strain on the network resulting in poor performance. On the developer side, the speed of
development may be reduced because your APIs are fixed and no longer fit the data they're
requesting.
GraphQL's selling point is to overcome the drawbacks of REST. Here are some of the key solutions GraphQL
offers to developers:

1. **Single endpoints**: GraphQL uses a single endpoint to query data.
   There's no need to build multiple APIs to fit the shape of the data. This results in fewer requests going
   over the network.
2. **Fetching**: GraphQL solves the perennial issues of over- and
   under-fetching by simply defining the data you need. GraphQL lets you shape the data to fit your needs so
   you only receive what you asked for.
3. **Abstraction**: GraphQL APIs contain a few components and systems that
   describe the data using a language-agnostic standard. In other words, the shape and structure of the data
   are standardized so both the front- and backends know how it will be sent over the network. This allows
   developers on both ends to work with GraphQL's systems and not around them.
4. **Rapid iterations**: Because of the standardization of data, changes on
   one end of development may not be required on the other. For example, frontend presentation changes may
   not result in extensive backend changes because GraphQL allows the data specification to be modified
   readily. You can simply define or modify the shape of the data to fit the needs of the application as it
   grows. This results in less potential development work.
   These are only some of the benefits of GraphQL. In the next few sections, you'll learn how GraphQL is
   structured and the properties that make it a unique alternative to REST.
