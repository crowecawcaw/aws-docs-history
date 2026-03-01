# Defining enhanced subscriptions filters in AWS AppSync

###### Important

As of Mar 13, 2025, you can build a real-time PubSub API powered by WebSockets using
AWS AppSync Events. For more information, see [Publish events via WebSocket](../eventapi/publish-websocket.md "../eventapi/publish-websocket.md") in the _AWS AppSync Events
Developer Guide_.

In AWS AppSync, you can define and enable business logic for data filtering on the
backend directly in the GraphQL API subscription resolvers by using filters that support
additional logical operators. You can configure these filters, unlike the subscription
arguments that are defined on the subscription query in the client. For more information
about using subscription arguments, see [Using subscription arguments](aws-appsync-real-time-data.md#using-subscription-arguments "aws-appsync-real-time-data.md#using-subscription-arguments"). For a list of operators, see [AWS AppSync resolver mapping template utility reference](resolver-util-reference.md "resolver-util-reference.md").

For the purpose of this document, we divide real-time data filtering into the
following categories:

- **Basic filtering** - Filtering based on
  client-defined arguments in the subscription query.
- **Enhanced filtering** - Filtering based on logic
  defined centrally in the AWS AppSync service backend.
  The following sections explain how to configure enhanced subscription filters and show
  their practical use.

## Defining subscriptions in your GraphQL schema

To use enhanced subscription filters, you define the subscription in the GraphQL
schema then define the enhanced filter using a filtering extension. To illustrate
how enhanced subscription filtering works in AWS AppSync, use the following GraphQL
schema, which defines a ticket management system API, as an example:

```
type Ticket {
	id: ID
	createdAt: AWSDateTime
	content: String
	severity: Int
	priority: Priority
	category: String
	group: String
	status: String

}

type Mutation {
	createTicket(input: TicketInput): Ticket
}

type Query {
	getTicket(id: ID!): Ticket
}

type Subscription {
	onSpecialTicketCreated: Ticket @aws_subscribe(mutations: ["createTicket"])
	onGroupTicketCreated(group: String!): Ticket @aws_subscribe(mutations: ["createTicket"])
}



enum Priority {
	none
	lowest
	low
	medium
	high
	highest
}

input TicketInput {
	content: String
	severity: Int
	priority: Priority
	category: String
	group: String

```

Suppose you create a `NONE` data source for your API, then attach a
resolver to the `createTicket` mutation using this data source. Your
handlers may look like this:

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
	return {
		payload: {
			id: util.autoId(),
			createdAt: util.time.nowISO8601(),
			status: 'pending',
			...ctx.args.input,
		},
	};
}

export function response(ctx) {
	return ctx.result;
}

```

###### Note

Enhanced filters are enabled in the GraphQL resolver's handler in a given
subscription. For more information, see [Resolver
reference](resolver-reference-js-version.md "resolver-reference-js-version.md").

To implement the behavior of the enhanced filter, you must use the
`extensions.setSubscriptionFilter()` function to define a filter
expression evaluated against published data from a GraphQL mutation that the
subscribed clients might be interested in. For more information about the filtering
extensions, see [Extensions](extensions-js.md "extensions-js.md").

The following section explains how to use filtering extensions to implement
enhanced filters.

## Creating enhanced subscription filters using filtering extensions

Enhanced filters are written in JSON in the response handler of the subscription's
resolvers. Filters can be grouped together in a list called a
`filterGroup`. Filters are defined using at least one rule, each with
fields, operators, and values. Let’s define a new resolver for
`onSpecialTicketCreated` that sets up an enhanced filter. You can
configure multiple rules in a filter that are evaluated using AND logic, while
multiple filters in a filter group are evaluated using OR logic:

```
import { util, extensions } from '@aws-appsync/utils';

export function request(ctx) {
	// simplfy return null for the payload
	return { payload: null };
}

export function response(ctx) {
	const filter = {
		or: [
			{ severity: { ge: 7 }, priority: { in: ['high', 'medium'] } },
			{ category: { eq: 'security' }, group: { in: ['admin', 'operators'] } },
		],
	};
	extensions.setSubscriptionFilter(util.transform.toSubscriptionFilter(filter));

  // important: return null in the response
	return null;
}
```

Based
on the filters defined in the preceding example, important tickets are automatically
pushed to subscribed API clients if a ticket is created with:

- `priority` level `high` or
  `medium`

AND

- `severity` level greater than or equal to `7`
  (`ge`)

OR

- `classification` ticket set to `Security`

AND

- `group` assignment set to `admin` or
  `operators`

![Example showing a ticket filtering query](images/aws-priority-example.png)

Filters defined in the subscription resolver (enhanced filtering) take precedence
over filtering based only on subscription arguments (basic filtering). For more
information about using subscription arguments, see [Using subscription arguments](aws-appsync-real-time-data.md#using-subscription-arguments "aws-appsync-real-time-data.md#using-subscription-arguments")).

If an argument is defined and required in the GraphQL schema of the subscription,
filtering based on the given argument takes place only if the argument is defined as
a rule in the resolver's `extensions.setSubscriptionFilter()` method.
However, if there are no `extensions` filtering methods in the
subscription resolver, arguments defined in the client are used only for basic
filtering. You can't use basic filtering and enhanced filtering concurrently.

You can use the [`context` variable](resolver-context-reference-js.md "resolver-context-reference-js.md") in the subscription's filter
extension logic to access contextual information about the request. For example,
when using Amazon Cognito User Pools, OIDC, or Lambda custom authorizers for authorization,
you can retrieve information about your users in `context.identity` when
the subscription is established. You can use that information to establish filters
based on your users’ identity.

Now assume that you want to implement the enhanced filter behavior for
`onGroupTicketCreated`. The `onGroupTicketCreated`
subscription requires a mandatory `group` name as an argument. When
created, tickets are automatically assigned a `pending` status. You can
set up a subscription filter to only receive newly created tickets that belong to
the provided group:

```
import { util, extensions } from '@aws-appsync/utils';

export function request(ctx) {
	// simplfy return null for the payload
	return { payload: null };
}

export function response(ctx) {
	const filter = { group: { eq: ctx.args.group }, status: { eq: 'pending' } };
	extensions.setSubscriptionFilter(util.transform.toSubscriptionFilter(filter));

	return null;
}
```

When data is published using a mutation like in the following example:

```
mutation CreateTicket {
  createTicket(input: {priority: medium, severity: 2, group: "aws"}) {
    id
    priority
    severity
    status
    group
    createdAt
  }
}
```

Subscribed clients listen for the data to be automatically pushed via WebSockets
as soon as a ticket is created with the `createTicket` mutation:

```
subscription OnGroup {
  onGroupTicketCreated(group: "aws") {
    category
    status
    severity
    priority
    id
    group
    createdAt
    content
  }
}
```

Clients can be subscribed without arguments because the filtering logic is
implemented in the AWS AppSync service with enhanced filtering, which simplifies the
client code. Clients receive data only if the defined filter criteria is met.

## Defining enhanced filters for nested schema fields

You can use enhanced subscription filtering to filter nested schema fields.
Suppose we modified the schema from the previous section to include location and
address types:

```
type Ticket {
	id: ID
	createdAt: AWSDateTime
	content: String
	severity: Int
	priority: Priority
	category: String
	group: String
	status: String
	location: ProblemLocation
}

type Mutation {
	createTicket(input: TicketInput): Ticket
}

type Query {
	getTicket(id: ID!): Ticket
}

type Subscription {
	onSpecialTicketCreated: Ticket @aws_subscribe(mutations: ["createTicket"])
	onGroupTicketCreated(group: String!): Ticket @aws_subscribe(mutations: ["createTicket"])
}

type ProblemLocation {
	address: Address
}

type Address {
	country: String
}

enum Priority {
	none
	lowest
	low
	medium
	high
	highest
}

input TicketInput {
	content: String
	severity: Int
	priority: Priority
	category: String
	group: String
	location: AWSJSON
```

With this schema, you can use a `.` separator to represent nesting. The
following example adds a filter rule for a nested schema field under
`location.address.country`. The subscription will be triggered if the
ticket's address is set to `USA`:

```
import { util, extensions } from '@aws-appsync/utils';

export const request = (ctx) => ({ payload: null });

export function response(ctx) {
	const filter = {
		or: [
			{ severity: { ge: 7 }, priority: { in: ['high', 'medium'] } },
			{ category: { eq: 'security' }, group: { in: ['admin', 'operators'] } },
			{ 'location.address.country': { eq: 'USA' } },
		],
	};
	extensions.setSubscriptionFilter(util.transform.toSubscriptionFilter(filter));
	return null;
}
```

In the example above, `location` represents nesting level one,
`address` represents nesting level two, and `country`
represents nesting level three, all of which are separated by the `.`
separator.

You can test this subscription by using the `createTicket`
mutation:

```
mutation CreateTicketInUSA {
  createTicket(input: {location: "{\"address\":{\"country\":\"USA\"}}"}) {
    category
    content
    createdAt
    group
    id
    location {
      address {
        country
      }
    }
    priority
    severity
    status
  }
}
```

## Defining enhanced filters from the client

You can use basic filtering in GraphQL with [subscriptions arguments](aws-appsync-real-time-data.md#using-subscription-arguments "aws-appsync-real-time-data.md#using-subscription-arguments"). The client that makes the call in the
subscription query defines the arguments' values. When enhanced filters are enabled
in an AWS AppSync subscription resolver with the `extensions` filtering,
backend filters defined in the resolver take precedence and priority.

Configure dynamic, client-defined enhanced filters using a `filter`
argument in the subscription. When you configure these filters, you must update the
GraphQL schema to reflect the new argument:

```
...
type Subscription {
    onSpecialTicketCreated(filter: String): Ticket
        @aws_subscribe(mutations: ["createTicket"])
}
...
```

The client can then send a subscription query like in the following
example:

```
subscription onSpecialTicketCreated($filter: String) {
     onSpecialTicketCreated(filter: $filter) {
        id
        group
        description
        priority
        severity
     }
 }
```

You can configure the query variable like the following example:

```
{"filter" : "{\"severity\":{\"le\":2}}"}
```

The `util.transform.toSubscriptionFilter()` resolver utility can be
implemented in the subscription response mapping template to apply the filter
defined in the subscription argument for each client:

```
import { util, extensions } from '@aws-appsync/utils';

export function request(ctx) {
	// simplfy return null for the payload
	return { payload: null };
}

export function response(ctx) {
	const filter = ctx.args.filter;
	extensions.setSubscriptionFilter(util.transform.toSubscriptionFilter(filter));
	return null;
}
```

With this strategy, clients can define their own filters that use enhanced
filtering logic and additional operators. Filters are assigned when a given client
invokes the subscription query in a secure WebSocket connection. For more
information about the transform utility for enhanced filtering, including the format
of the `filter` query variable payload, see [JavaScript
resolvers overview](resolver-reference-overview-js.md "resolver-reference-overview-js.md").

## Additional enhanced filtering restrictions

Below are
several use cases where additional restrictions are placed on enhanced
filters:

- Enhanced filters don't support filtering for top-level object lists. In
  this use case, published data from the mutation will be ignored for enhanced
  subscriptions.
- AWS AppSync supports up to five levels of nesting. Filters on schema fields
  past nesting level five will be ignored. Take the GraphQL response below.
  The `continent` field in
  `venue.address.country.metadata.continent` is allowed because
  it's a level five nest. However, `financial` in
  `venue.address.country.metadata.capital.financial` is a level
  six nest, so the filter won't work:

```
{
    "data": {
        "onCreateFilterEvent": {
            "venue": {
                "address": {
                    "country": {
                        "metadata": {
                            "capital": {
                                **"financial": "New York"**
                            },
                            **"continent" : "North America"**
                        }
                    },
                    "state": "WA"
                },
                "builtYear": 2023
            },
            "private": false,
        }
    }
}
```
