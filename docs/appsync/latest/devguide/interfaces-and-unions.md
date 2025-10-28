# Interfaces and unions

in GraphQL

The GraphQL type system supports [Interfaces](https://graphql.org/learn/schema/#interfaces "https://graphql.org/learn/schema/#interfaces").
An interface exposes a certain set of fields that a type must include to implement the interface.

The GraphQL type system also supports [Unions](https://graphql.org/learn/schema/#union-types "https://graphql.org/learn/schema/#union-types").
Unions are identical to interfaces, except that they don’t define a common set of fields. Unions are generally
preferred over interfaces when the possible types do not share a logical hierarchy.

The following section is a reference for schema typing.

## Interface examples

We could represent an `Event` interface that represents any kind of activity or gathering of
people. Some possible event types are `Concert`, `Conference`, and `Festival`.
These types all share common characteristics, including a name, a venue where the event is taking place, and a
start and end date. These types also have differences; a `Conference` offers a list of speakers and
workshops, while a `Concert` features a performing band.

In Schema Definition Language (SDL), the `Event` interface is defined as follows:

```
interface Event {
        id: ID!
        name : String!
        startsAt: String
        endsAt: String
        venue: Venue
        minAgeRestriction: Int
}
```

And each of the types implements the `Event` interface as follows:

```
type Concert implements Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
    performingBand: String
}

type Festival implements Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
    performers: [String]
}

type Conference implements Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
    speakers: [String]
    workshops: [String]
}
```

Interfaces are useful to represent elements that might be of several types. For example, we could search for
all events happening at a specific venue. Let’s add a `findEventsByVenue` field to the schema as
follows:

```
schema {
    query: Query
}

type Query {
    # Retrieve Events at a specific Venue
    findEventsAtVenue(venueId: ID!): [Event]
}

type Venue {
    id: ID!
    name: String
    address: String
    maxOccupancy: Int
}

type Concert implements Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
    performingBand: String
}

interface Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
}

type Festival implements Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
    performers: [String]
}

type Conference implements Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
    speakers: [String]
    workshops: [String]
}
```

The `findEventsByVenue` returns a list of `Event`. Because GraphQL interface fields are
common to all the implementing types, it’s possible to select any fields on the `Event` interface
(`id`, `name`, `startsAt`, `endsAt`, `venue`, and
`minAgeRestriction`). Additionally, you can access the fields on any implementing type using GraphQL
[fragments](https://graphql.org/learn/queries/#fragments "https://graphql.org/learn/queries/#fragments"), as long as you specify the
type.

Let’s examine an example of a GraphQL query that uses the interface.

```
query {
  findEventsAtVenue(venueId: "Madison Square Garden") {
    id
    name
    minAgeRestriction
    startsAt

    ... on Festival {
      performers
    }

    ... on Concert {
      performingBand
    }

    ... on Conference {
      speakers
      workshops
    }
  }
}
```

The previous query yields a single list of results, and the server could sort the events by start date by
default.

```
{
  "data": {
    "findEventsAtVenue": [
      {
        "id": "Festival-2",
        "name": "Festival 2",
        "minAgeRestriction": 21,
        "startsAt": "2018-10-05T14:48:00.000Z",
        "performers": [
          "The Singers",
          "The Screamers"
        ]
      },
      {
        "id": "Concert-3",
        "name": "Concert 3",
        "minAgeRestriction": 18,
        "startsAt": "2018-10-07T14:48:00.000Z",
        "performingBand": "The Jumpers"
      },
      {
        "id": "Conference-4",
        "name": "Conference 4",
        "minAgeRestriction": null,
        "startsAt": "2018-10-09T14:48:00.000Z",
        "speakers": [
          "The Storytellers"
        ],
        "workshops": [
          "Writing",
          "Reading"
        ]
      }
    ]
  }
}
```

Since results are returned as a single collection of events, using interfaces to represent common
characteristics is very helpful for sorting results.

## Union examples

As stated earlier, unions don't define common sets of fields. A search result might represent many different
types. Using the `Event` schema, you can define a `SearchResult` union as follows:

```
type Query {
    # Retrieve Events at a specific Venue
    findEventsAtVenue(venueId: ID!): [Event]
    # Search across all content
    search(query: String!): [SearchResult]
}

union SearchResult = Conference | Festival | Concert | Venue
```

In this case, to query any field on our `SearchResult` union, you must use fragments:

```
query {
  search(query: "Madison") {
    ... on Venue {
      id
      name
      address
    }

    ... on Festival {
      id
      name
      performers
    }

    ... on Concert {
      id
      name
      performingBand
    }

    ... on Conference {
      speakers
      workshops
    }
  }
}
```

## Type resolution in AWS AppSync

Type resolution is the mechanism by which the GraphQL engine identifies a resolved value as a specific object
type.

Going back to the union search example, provided our query yielded results, each item in the results list must
present itself as one of the possible types that the `SearchResult` union defined (that is,
`Conference`, `Festival`, `Concert`, or `Venue`).

Because the logic to identify a `Festival` from a `Venue` or a `Conference`
is dependent on the application requirements, the GraphQL engine must be given a hint to identify our possible
types from the raw results.

With AWS AppSync, this hint is represented by a meta field named `__typename`, whose value
corresponds to the identified object type name. `__typename` is required for return types that are
interfaces or unions.

## Type resolution example

Let’s reuse the previous schema. You can follow along by navigating to the console and adding the following
under the **Schema** page:

```
schema {
    query: Query
}

type Query {
    # Retrieve Events at a specific Venue
    findEventsAtVenue(venueId: ID!): [Event]
    # Search across all content
    search(query: String!): [SearchResult]
}

union SearchResult = Conference | Festival | Concert | Venue

type Venue {
    id: ID!
    name: String!
    address: String
    maxOccupancy: Int
}

interface Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
}

type Festival implements Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
    performers: [String]
}

type Conference implements Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
    speakers: [String]
    workshops: [String]
}

type Concert implements Event {
    id: ID!
    name: String!
    startsAt: String
    endsAt: String
    venue: Venue
    minAgeRestriction: Int
    performingBand: String
}
```

Let’s attach a resolver to the `Query.search` field. In the `Resolvers` section, choose
**Attach**, create a new **Data Source** of type
_NONE_, and then name it _StubDataSource_. For the sake of this example,
we’ll pretend we fetched results from an external source, and hard code the fetched results in the request mapping
template.

In the request mapping template pane, enter the following:

```
{
    "version" : "2018-05-29",
    "payload":
    ## We are effectively mocking our search results for this example
    [
        {
            "id": "Venue-1",
            "name": "Venue 1",
            "address": "2121 7th Ave, Seattle, WA 98121",
            "maxOccupancy": 1000
        },
        {
            "id": "Festival-2",
            "name": "Festival 2",
            "performers": ["The Singers", "The Screamers"]
        },
        {
            "id": "Concert-3",
            "name": "Concert 3",
            "performingBand": "The Jumpers"
        },
        {
            "id": "Conference-4",
            "name": "Conference 4",
            "speakers": ["The Storytellers"],
            "workshops": ["Writing", "Reading"]
        }
    ]
}
```

If the application returns the type name as part of the `id` field, the type resolution logic must
parse the `id` field to extract the type name and then add the `__typename` field to each of
the results. You can perform that logic in the response mapping template as follows:

###### Note

You can also perform this task as part of your Lambda function, if you are using the Lambda data
source.

```
#foreach ($result in $context.result)
    ## Extract type name from the id field.
    #set( $typeName = $result.id.split("-")[0] )
    #set( $ignore = $result.put("__typename", $typeName))
#end
$util.toJson($context.result)
```

Run the following query:

```
query {
  search(query: "Madison") {
    ... on Venue {
      id
      name
      address
    }

    ... on Festival {
        id
      name
      performers
    }

    ... on Concert {
      id
      name
      performingBand
    }

    ... on Conference {
      speakers
      workshops
    }
  }
}
```

The query yields the following results:

```
{
  "data": {
    "search": [
      {
        "id": "Venue-1",
        "name": "Venue 1",
        "address": "2121 7th Ave, Seattle, WA 98121"
      },
      {
        "id": "Festival-2",
        "name": "Festival 2",
        "performers": [
          "The Singers",
          "The Screamers"
        ]
      },
      {
        "id": "Concert-3",
        "name": "Concert 3",
        "performingBand": "The Jumpers"
      },
      {
        "speakers": [
          "The Storytellers"
        ],
        "workshops": [
          "Writing",
          "Reading"
        ]
      }
    ]
  }
}
```

The type resolution logic varies depending on the application. For example, you could have a different
identifying logic that checks for the existence of certain fields or even a combination of fields. That is, you
could detect the presence of the `performers` field to identify a `Festival` or the
combination of the `speakers` and the `workshops` fields to identify a
`Conference`. Ultimately, it is up to you to define the logic you want to use.
