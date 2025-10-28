# Unsubscribing WebSocket connections

using filters in AWS AppSync

###### Important

As of Mar 13, 2025, you can build a real-time PubSub API powered by WebSockets using
AWS AppSync Events. For more information, see [Publish events via WebSocket](../eventapi/publish-websocket.md "../eventapi/publish-websocket.md") in the _AWS AppSync Events
Developer Guide_.

In AWS AppSync, you can forcibly unsubscribe and close (invalidate) a WebSocket
connection from a connected client based on specific filtering logic. This is useful in
authorization-related scenarios such as when you remove a user from a group.

Subscription invalidation occurs in response to a payload defined in a mutation. We
recommend that you treat mutations used to invalidate subscription connections as
administrative operations in your API and scope permissions accordingly by limiting
their use to an admin user, group, or backend service. For example, using schema
authorization directives such as `@aws_auth(cognito_groups:
 ["Administrators"])` or `@aws_iam`. For more information, see
[Using additional authorization modes](security-authz.md#using-additional-authorization-modes "security-authz.md#using-additional-authorization-modes").

Invalidation filters use the same syntax and logic as [enhanced
subscription filters](aws-appsync-real-time-enhanced-filtering.md "aws-appsync-real-time-enhanced-filtering.md"). Define these filters using the following
utilities:

- `extensions.invalidateSubscriptions()` – Defined in the
  GraphQL resolver's response handler for a mutation.
- `extensions.setSubscriptionInvalidationFilter()` – Defined
  in the GraphQL resolver's response handler of the subscriptions linked to the
  mutation.
  For more information about invalidation filtering extensions, see [JavaScript
  resolvers overview](resolver-reference-overview-js.md "resolver-reference-overview-js.md").

## Using

subscription invalidation

To see how subscription invalidation works in AWS AppSync, use the following
GraphQL schema:

```
type User {
  userId: ID!
  groupId: ID!
}

type Group {
  groupId: ID!
  name: String!
  members: [ID!]!
}

type GroupMessage {
  userId: ID!
  groupId: ID!
  message: String!
}

type Mutation {
    createGroupMessage(userId: ID!, groupId : ID!, message: String!): GroupMessage
    removeUserFromGroup(userId: ID!, groupId : ID!) : User @aws_iam
}

type Subscription {
    onGroupMessageCreated(userId: ID!, groupId : ID!): GroupMessage
        @aws_subscribe(mutations: ["createGroupMessage"])
}

type Query {
	none: String
}
```

Define an invalidation filter in the `removeUserFromGroup` mutation
resolver code:

```
import { extensions } from '@aws-appsync/utils';

export function request(ctx) {
	return { payload: null };
}

export function response(ctx) {
	const { userId, groupId } = ctx.args;
	extensions.invalidateSubscriptions({
		subscriptionField: 'onGroupMessageCreated',
		payload: { userId, groupId },
	});
	return { userId, groupId };
}

```

When the mutation is invoked, the data defined in the `payload` object
is used to unsubscribe the subscription defined in `subscriptionField`.
An invalidation filter is also defined in the `onGroupMessageCreated`
subscription's response mapping template.

If the `extensions.invalidateSubscriptions()` payload contains an ID
that matches the IDs from the subscribed client as defined in the filter, the
corresponding subscription is unsubscribed. In addition, the WebSocket connection is
closed. Define the subscription resolver code for the
`onGroupMessageCreated` subscription:

```
import { util, extensions } from '@aws-appsync/utils';

export function request(ctx) {
	// simplfy return null for the payload
	return { payload: null };
}

export function response(ctx) {
	const filter = { groupId: { eq: ctx.args.groupId } };
	extensions.setSubscriptionFilter(util.transform.toSubscriptionFilter(filter));

	const invalidation = { groupId: { eq: ctx.args.groupId }, userId: { eq: ctx.args.userId } };
	extensions.setSubscriptionInvalidationFilter(util.transform.toSubscriptionFilter(invalidation));

	return null;
}
```

Note that the subscription response handler can have both subscription filters and
invalidation filters defined at the same time.

For
example,
assume that client A subscribes a new user with the ID
`user-1` to the group with the ID
`group-1` using the following
subscription request:

```
onGroupMessageCreated(userId : "`user-1`", groupId: :"`group-1`"){...}
```

AWS AppSync runs the subscription resolver, which generates subscription and
invalidation filters as defined in the preceding `onGroupMessageCreated`
response mapping template. For client A, the subscription filters allow data to be
sent only to `group-1`, and the invalidation
filters are defined for both `user-1` and
`group-1`.

Now assume that client B subscribes a user with the ID
`user-2` to a group with the ID
`group-2` using the following
subscription request:

```
onGroupMessageCreated(userId : "`user-2`", groupId: :"`group-2`"){...}
```

AWS AppSync runs the subscription resolver, which generates subscription and
invalidation filters. For client B, the subscription filters allow data to be sent
only to `group-2`, and the invalidation
filters are defined for both `user-2` and
`group-2`.

Next, assume that a new group message with the ID
`message-1` is created using a
mutation request like in the following example:

```
createGroupMessage(id: "`message-1`", groupId :
      "`group-1`", message: "test message"){...}
```

Subscribed clients matching the defined filters automatically receive the
following data payload via WebSockets:

```
{
  "data": {
    "onGroupMessageCreated": {
      "id": "message-1",
      "groupId": "group-1",
      "message": "test message",
    }
  }
}
```

Client A receives the message because the filtering
criteria
match the defined subscription filter. However, client B doesn't
receive the message, as the user is not part of
`group-1`. Also, the request doesn't
match the subscription filter defined in the subscription resolver.

Finally, assume that `user-1` is removed
from `group-1` using the following mutation
request:

```
removeUserFromGroup(userId: "user-1", groupId : "group-1"){...}
```

The mutation initiates a subscription invalidation as defined in its
`extensions.invalidateSubscriptions()` resolver response handler
code. AWS AppSync then unsubscribes client A and closes its WebSocket connection.
Client B is unaffected, as the invalidation payload defined in the mutation doesn't
match its user or group.

When AWS AppSync invalidates a connection, the client receives a message confirming
that they are unsubscribed:

```
{
  "message": "Subscription complete."
}
```

## Using context variables

in subscription invalidation filters

As with enhanced subscription filters, you can use the [`context` variable](resolver-context-reference-js.md "resolver-context-reference-js.md") in the subscription invalidation
filter extension to access certain data.

For example, it's possible to configure an email address as the invalidation
payload in the mutation, then match it against the email attribute or claim from a
subscribed user authorized with Amazon Cognito user pools or OpenID Connect. The
invalidation filter defined in the
`extensions.setSubscriptionInvalidationFilter()` subscription
invalidator checks if the email address set by the mutation's
`extensions.invalidateSubscriptions()` payload matches the email
address retrieved from the user's JWT token in
`context.identity.claims.email`, initiating the invalidation.
