# Authoring temporal policies

You author a temporal policy in the Dogwood policy language and add it to a policy engine, the same way
you create any other policy for Policy in AgentCore. A temporal policy is a `permit` or `forbid` rule
whose session-aware conditions are placed in a `temporal` block; the principal, action, and resource
the rule applies to are written using the standard `(principal, action, resource)` scope, the same as any other policy. The following sections show how to create a temporal
policy and walk through common patterns you can express.

###### Topics

- [Create a temporal policy](#policy-temporal-authoring-create "#policy-temporal-authoring-create")
- [Event schema: fields you can reference](#policy-temporal-authoring-event-schema "#policy-temporal-authoring-event-schema")
- [Use cases](#policy-temporal-authoring-use-cases "#policy-temporal-authoring-use-cases")

## Create a temporal policy

You create a temporal policy with the `create-policy` operation, the same operation you use for other
policies, and attach it to a policy engine. A temporal policy’s statement goes under `policy` in the definition, rather than under `cedar` as for a
stateless Cedar policy.

The following AWS CLI example creates a temporal policy on a policy engine:

```
aws bedrock-agentcore-control create-policy \
  --policy-engine-id my-policy-engine-id \
  --name TransferToLookedUpAccount \
  --validation-mode FAIL_ON_ANY_FINDINGS \
  --definition '{
    "policy": {
      "statement": "permit (principal, action == AgentCore::Action::\"FundsTarget___transfer_funds\", resource == AgentCore::Gateway::\"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway\") when temporal { formerly within 1h AgentCore::Action::\"FundsTarget___get_account_balance\"::response{ eventResource: resource, output.accountId: context.input.toAccount } };"
    }
  }'
```

You can also create a temporal policy by describing it in natural language instead of writing the
Dogwood statement yourself.

## Event schema: fields you can reference

Conditions inside a `temporal { }` block use _temporal event predicates_ to match specific events that
were recorded in the session so far (up to and including the action that is currently being authorized). A predicate names a time window, an action and event kind, and a
set of field constraints on the matched event. The `create-policy` example in the previous section used
one predicate, `formerly within 1h AgentCore::Action::"FundsTarget___get_account_balance"::response{
eventResource: resource, output.accountId: context.input.toAccount }`, which matches a
`get_account_balance`
`response` recorded within the last hour whose `output.accountId` equals the
current request’s `toAccount`.

To write a predicate, you need to know which events an action produces and which fields each event
carries, because those are the fields a predicate can constrain and correlate against. This section
describes that event schema.

Each action produces up to three kinds of event, named after the event kind in the predicate
(`::request`, `::response`, `::error`):

- `request` — recorded for each authorized request. Carries the action’s input fields.
- `response` — recorded when the tool returns successfully. Carries the action’s input and output
  fields.
- `error` — recorded when the request is denied or the tool returns an error. Carries the action’s
  input fields. This event is history-only.

The temporal event schema defines these events for each action `A`. `…​inputs(A)` and `…​outputs(A)`
expand to the action’s declared input and output fields:

```
// Recorded for each authorized request.
decision event <A>::request {
    ...inputs(A),
    eventPrincipal: principalType(A),
    eventResource:  resourceType(A),
    requestId:      String,
    pin sessionId:  String = context.sessionId,
}

// Recorded when the tool returns successfully; carries inputs and outputs.
event <A>::response {
    ...inputs(A),
    ...outputs(A),
    eventPrincipal: principalType(A),
    eventResource:  resourceType(A),
    requestId:      String,
    pin sessionId:  String = context.sessionId,
}

// Recorded when the request is denied or the tool returns an error; history-only.
event <A>::error {
    ...inputs(A),
    eventPrincipal: principalType(A),
    eventResource:  resourceType(A),
    requestId:      String,
    pin sessionId:  String = context.sessionId,
}
```

Within a predicate body, you can reference the following fields of the matched event:

| Field            | Description                                                                                                                                                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `input.<name>`   | An input field of the action. Available on `request`, `response`, and `error` events.                                                                                                                                                                                           |
| `output.<name>`  | An output field of the action. Available on `response` events only.                                                                                                                                                                                                             |
| `eventPrincipal` | The principal that made the recorded request.                                                                                                                                                                                                                                   |
| `eventResource`  | Always set this to `resource` (as `eventResource: resource`) so it refers to the resource in the policy scope, that is, the `resource` in the `permit` or `forbid` head. This scopes the match to the current request’s resource, and every temporal predicate must include it. |

To correlate a recorded event with the current request, compare one of these fields against a value
from the current request, such as `context.input.<name>`.

## Use cases

The following are a few examples of temporal policies.

### Available tools

The examples in this section use a gateway target named `FundsTarget` that exposes three tools. In a
policy, each tool is referenced by its action name, `FundsTarget___<tool-name>`, and by the input and
output fields listed here.

`FundsTarget___get_account_balance`

Retrieves the current account balance for a customer.

- Input: `customerId` (string, required).
- Output: `status` (string), `customerId` (string), `accountId` (string), `balance` (integer).

`FundsTarget___transfer_funds`

Transfers funds between accounts.

- Input: `fromAccount` (string, required), `toAccount` (string, required), `amount` (integer, required).
- Output: `status` (string), `fromAccount` (string), `toAccount` (string), `amount` (integer).

`FundsTarget___get_transaction_history`

Retrieves transaction history for an account.

- Input: `accountId` (string, required), `startDate` (string, optional), `endDate` (string, optional).
- Output: `status` (string), `accountId` (string).

### Example: output-to-input integrity

This example lets an agent transfer funds only to an account it looked up earlier in the same session,
preventing it from transferring to an account it fabricated. The policy permits `transfer_funds` only
when a `get_account_balance` response earlier in the session returned the same account:

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 1h AgentCore::Action::"FundsTarget___get_account_balance"::response{
        eventResource: resource,
        output.accountId: context.input.toAccount
    }
};
```

The `::response` predicate matches the recorded response of a prior `get_account_balance`.
`output.accountId` is a field that the tool returns, and `context.input.toAccount` is the destination
account on the current `transfer_funds` request; requiring them to be equal ties the transfer to a
prior lookup.

Because a policy engine denies by default, and because an action is recorded as a `response` only if it
was permitted, you also grant a plain `permit` for `get_account_balance` so the lookup is allowed and
recorded as a response in the session:

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___get_account_balance",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
);
```

With both policies in place, requests in a session are decided as follows:

| Request sequence in a session                                                       | Decision |
| ----------------------------------------------------------------------------------- | -------- |
| `transfer_funds` with no prior lookup                                               | DENY     |
| `get_account_balance` for an account, then `transfer_funds` to the same account     | ALLOW    |
| `get_account_balance` for one account, then `transfer_funds` to a different account | DENY     |

### Example: tool sequencing

This example permits an action only after a prerequisite action ran earlier in the same session. The
following policy permits `get_account_balance` only if a `transfer_funds` request occurred within the
last five minutes:

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___get_account_balance",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 5m AgentCore::Action::"FundsTarget___transfer_funds"::request{
        eventResource: resource
    }
};
```

The `::request` predicate matches a prior `transfer_funds` request in the session. Pair this with a
`permit` for `transfer_funds` so that action is allowed and recorded. With both policies in place,
`get_account_balance` is denied until a `transfer_funds` has run in the session:

| Request sequence in a session                     | Decision |
| ------------------------------------------------- | -------- |
| `get_account_balance` before any `transfer_funds` | DENY     |
| `transfer_funds`, then `get_account_balance`      | ALLOW    |

### Example: data freshness

This example permits an action only if a prerequisite completed **successfully** within a tight window,
so that stale results expire the permission. It permits `get_account_balance` only if a
`transfer_funds` completed within the last five minutes:

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___get_account_balance",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 5m AgentCore::Action::"FundsTarget___transfer_funds"::response{
        eventResource: resource
    }
};
```

Matching on `::response` rather than `::request` is the difference from tool sequencing: a `response`
event is recorded only when the action completes successfully, so this policy requires a recent
successful completion, not merely a prior request. The window length sets how fresh that completion
must be; once the window passes, the permission lapses until the prerequisite runs again.

| Request sequence in a session                                            | Decision |
| ------------------------------------------------------------------------ | -------- |
| `get_account_balance` before any completed `transfer_funds`              | DENY     |
| `transfer_funds` completes, then `get_account_balance` within the window | ALLOW    |
| `get_account_balance` after the window elapses                           | DENY     |

### Example: session-based rate limiting

This example caps a tool at a fixed number of calls within a session. The following policy forbids
`transfer_funds` once it has been called more than three times within five minutes in the session:

```
forbid (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    exists (n: Long).
        (count for (t: Timepoint).
            where (formerly within 5m (AgentCore::Action::"FundsTarget___transfer_funds"::request{ eventResource: resource } && tp(t)))) == n
        && n > 3
};
```

The `count` expression counts the `transfer_funds` requests recorded in the session within the last
five minutes, including the current request; when that count exceeds three, the forbid applies. Pair
it with a `permit` for `transfer_funds` so calls are allowed up to the limit. With both policies in
place, the first three `transfer_funds` calls within any five-minute window are allowed, and the
fourth (or later) call in that window is denied.

###### Important

This limit applies only within a single session, so it is not a security control against a determined
caller. Because the caller supplies the session ID, they can reset the count by starting a new session.
Use this pattern to shape behavior within a cooperative session, not to enforce a hard limit against a
caller who controls their own session ID. For more information, see
[Security considerations](policy-temporal.md#policy-temporal-security "policy-temporal.md#policy-temporal-security").

### Example: one-time-use approval

This example makes each approval good for a single use. A `transfer_funds` is permitted only if no
`transfer_funds` has completed since the most recent `get_account_balance` (the approval) in the
session. Once a transfer completes, it consumes the approval, and the next transfer is denied until a
new approval occurs:

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    !AgentCore::Action::"FundsTarget___transfer_funds"::response{ eventResource: resource }
    since within 1h AgentCore::Action::"FundsTarget___get_account_balance"::response{ eventResource: resource }
};
```

This `since` condition holds when a completed `get_account_balance` (the approval) occurred within the
last hour and no completed `transfer_funds` has occurred since that approval. Matching on
`::response` is essential: a transfer counts as completed only after it succeeds, so the request being
authorized does not block itself. Pair this with a `permit` for `get_account_balance` so approvals are
recorded.

Requests in a session are decided as follows:

| Request sequence in a session                           | Decision |
| ------------------------------------------------------- | -------- |
| `get_account_balance` (approval), then `transfer_funds` | ALLOW    |
| a second `transfer_funds` with no new approval          | DENY     |
| a new `get_account_balance`, then `transfer_funds`      | ALLOW    |

###### Note

A tool’s `response` event is recorded shortly after the call completes. Wait for the
`get_account_balance` (the approval) request to complete and its `response` to be recorded before you
issue the next `transfer_funds`, rather than issuing them back to back. For more information, see
[Sequencing actions that depend on a prior response](policy-temporal.md#policy-temporal-response-delay "policy-temporal.md#policy-temporal-response-delay").

### Example: cumulative budget

This example caps the total value of an action within a window. The following policy forbids
`transfer_funds` once the sum of the `amount` input across the session’s transfers in the last five
minutes reaches 3000:

```
forbid (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    exists (total: Long).
        (sum amt for (amt: Long), (t: Timepoint).
            where (formerly within 5m (AgentCore::Action::"FundsTarget___transfer_funds"::request{ eventResource: resource, input.amount: amt } && tp(t)))) == total
        && total >= 3000
};
```

The `sum` expression adds up the `amount` input field across the matching `transfer_funds` requests in
the window, including the current request; when the total reaches the threshold, the forbid applies.
The summed field is an input field of the action. Pair the policy with a `permit` for `transfer_funds`.
For example, with a 3000 threshold and transfers of 1000, the first two are allowed and the third,
which would reach 3000, is denied.

As with rate limiting, the sum is scoped to the current session and does not aggregate across sessions.

### Example: cool-down

This example enforces a cool-down: an action cannot be repeated within a fixed period of its last
completion. It forbids `transfer_funds` if a `transfer_funds` completed within the last minute:

```
forbid (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 1m AgentCore::Action::"FundsTarget___transfer_funds"::response{
        eventResource: resource
    }
};
```

This condition is self-referential: it matches the same action being authorized. Matching on
`::response` is what makes it work, because the request being authorized has not produced a response
yet, so it does not match itself. Matching on `::request` here would make the current request match its
own event, and the action would be permanently forbidden. After the window elapses with no new
completion, the action is allowed again.

| Request sequence in a session               | Decision |
| ------------------------------------------- | -------- |
| first `transfer_funds`                      | ALLOW    |
| another `transfer_funds` within 1 minute    | DENY     |
| `transfer_funds` after 1 minute has elapsed | ALLOW    |

### Example: continuous precondition

This example permits an action only while a precondition holds: a positive confirmation occurred
recently and nothing has invalidated it since. It permits `transfer_funds` only if a
`get_account_balance` (the confirmation) completed within the last five minutes and no
`get_transaction_history` (the invalidation) has completed since:

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    !AgentCore::Action::"FundsTarget___get_transaction_history"::response{ eventResource: resource }
    since within 5m AgentCore::Action::"FundsTarget___get_account_balance"::response{ eventResource: resource }
};
```

This `since` condition holds when a completed `get_account_balance` occurred within the last five
minutes and no completed `get_transaction_history` has occurred since. The completed
`get_account_balance` confirms the precondition, and requiring that no `get_transaction_history` has
happened since ensures nothing invalidated it afterward. Grant permits for both `get_account_balance`
and `get_transaction_history` so they are recorded.

| Request sequence in a session                           | Decision |
| ------------------------------------------------------- | -------- |
| `transfer_funds` before any `get_account_balance`       | DENY     |
| `get_account_balance`, then `transfer_funds`            | ALLOW    |
| `get_transaction_history` occurs, then `transfer_funds` | DENY     |
| a new `get_account_balance`, then `transfer_funds`      | ALLOW    |

### Example: multi-hop chain

You can compose several sequencing policies to require a chain of actions, each permitted only after
the previous one completed. This example requires the chain `get_account_balance` →
`get_transaction_history` → `transfer_funds`, using two policies (one per link):

```
// Link 1: permit get_transaction_history only after get_account_balance completed
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___get_transaction_history",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 5m AgentCore::Action::"FundsTarget___get_account_balance"::response{ eventResource: resource }
};

// Link 2: permit transfer_funds only after get_transaction_history completed
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 5m AgentCore::Action::"FundsTarget___get_transaction_history"::response{ eventResource: resource }
};
```

Each policy enforces one link, and the chain emerges from their composition: `transfer_funds` requires
`get_transaction_history`, which requires `get_account_balance`. Grant a `permit` for the first action
in the chain so it can start. A step attempted out of order is denied until its prerequisite completes.

| Request sequence in a session                                                | Decision           |
| ---------------------------------------------------------------------------- | ------------------ |
| `transfer_funds` or `get_transaction_history` before `get_account_balance`   | DENY               |
| `get_account_balance`, then `get_transaction_history`, then `transfer_funds` | ALLOW at each step |

### Example: mutual exclusion

This example makes two actions mutually exclusive within a window: whichever runs first blocks the
other. It uses two symmetric forbid policies so the exclusion holds in both directions. Here,
`transfer_funds` and `get_transaction_history` cannot both occur within two minutes:

```
// Forbid get_transaction_history if a transfer_funds was requested within 2m
forbid (
    principal,
    action == AgentCore::Action::"FundsTarget___get_transaction_history",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 2m AgentCore::Action::"FundsTarget___transfer_funds"::request{ eventResource: resource }
};

// Forbid transfer_funds if a get_transaction_history was requested within 2m
forbid (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 2m AgentCore::Action::"FundsTarget___get_transaction_history"::request{ eventResource: resource }
};
```

Because each policy matches on `::request`, even requesting one action blocks the other — the block
does not wait for the first action to complete. You need two symmetric `forbid` policies, one per
direction: one forbids `get_transaction_history` after a `transfer_funds` request, and the other
forbids `transfer_funds` after a `get_transaction_history` request. A single forbid would block only
one order. Pair both with permits for the two actions.

| Request sequence in a session                    | Decision                     |
| ------------------------------------------------ | ---------------------------- |
| `transfer_funds`, then `get_transaction_history` | transfer ALLOW, history DENY |
| `get_transaction_history`, then `transfer_funds` | history ALLOW, transfer DENY |

### Example: combining temporal, guardrail, and Cedar conditions

A single policy can combine a temporal condition with guardrail and standard Cedar conditions; all of
them must be satisfied for the policy to apply. This example permits `transfer_funds` only when the
cumulative transfer amount stays under a cap (temporal), the request contains no sensitive information
(guardrail), and the caller is not in a blocked group (Cedar):

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    exists (total: Long).
        (sum amt for (amt: Long), (t: Timepoint).
            where (formerly within 24h (AgentCore::Action::"FundsTarget___transfer_funds"::request{ eventResource: resource, input.amount: amt } && tp(t)))) == total
        && total < 60000
}
when {
    BedrockGuardrails::SensitiveInformation(["ACCOUNT_NUMBER"], [context.input.body]).count() == 0
}
unless {
    principal in Group::"blocked_users"
};
```

The temporal block enforces the cumulative cap, the guardrail block blocks requests that contain the
listed sensitive information, and the Cedar `unless` block excludes blocked principals. Each condition
type is evaluated independently and the permit applies only when all of them hold. For the guardrail
condition syntax, see [Guardrails in policies](policy-guardrails-in-policies.md "policy-guardrails-in-policies.md"); the temporal block
behaves as described in the preceding examples.

### Example: parallel prerequisites

This example requires two prerequisites to have completed, in any order, before an action is permitted.
It permits `get_account_balance` only if both `transfer_funds` and `get_transaction_history` completed
within the last hour, combining two `formerly` conditions with `&&`:

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___get_account_balance",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 1h AgentCore::Action::"FundsTarget___transfer_funds"::response{ eventResource: resource }
    && formerly within 1h AgentCore::Action::"FundsTarget___get_transaction_history"::response{ eventResource: resource }
};
```

Both prerequisites must have completed (`::response`) within the window, and the order does not matter.
Grant permits for both prerequisite actions so they are recorded. Completing only one leaves the action
denied until the other also completes.

| Request sequence in a session                               | Decision |
| ----------------------------------------------------------- | -------- |
| `get_account_balance` before both prerequisites             | DENY     |
| only one prerequisite completed, then `get_account_balance` | DENY     |
| both prerequisites completed, then `get_account_balance`    | ALLOW    |

### Example: approval threshold

This example permits an action only after a threshold number of qualifying events. It permits
`get_account_balance` for a customer only if at least two `transfer_funds` completed to that customer’s
account, correlating the transfer’s `toAccount` with the balance request’s `customerId`:

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___get_account_balance",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    exists (n: Long).
        (count for (t: Timepoint).
            where (formerly within 5m (AgentCore::Action::"FundsTarget___transfer_funds"::response{ eventResource: resource, input.toAccount: context.input.customerId } && tp(t)))) == n
        && n >= 2
};
```

The `count` expression counts the matching completed events in the window, and the action is permitted
once the count reaches the threshold.

###### Note

`count` counts matching events, not distinct principals. It cannot enforce that the events came from
different callers, so it expresses an "N events" threshold rather than a multi-party approval by N
distinct parties.

| Matching completed transfers to the account | `get_account_balance` |
| ------------------------------------------- | --------------------- |
| fewer than 2                                | DENY                  |
| 2 or more                                   | ALLOW                 |

### Example: block an action after a prior denial

This example blocks a sensitive action when an earlier tool call in the same session was denied. A
denied request is recorded as an `error` event, and the `::error` predicate matches such an event. The
following policy forbids `transfer_funds` whenever a `get_account_balance` in the session was denied
within the last three minutes:

```
forbid (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
)
when temporal {
    formerly within 3m AgentCore::Action::"FundsTarget___get_account_balance"::error{
        eventResource: resource
    }
};
```

A `forbid` rule overrides any `permit`, so pair it with a `permit` that allows `transfer_funds` under
normal conditions:

```
permit (
    principal,
    action == AgentCore::Action::"FundsTarget___transfer_funds",
    resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gateway"
);
```

With both policies in place, requests in a session are decided as follows:

| Request sequence in a session                          | Decision |
| ------------------------------------------------------ | -------- |
| `transfer_funds` with no prior denial                  | ALLOW    |
| `get_account_balance` is denied, then `transfer_funds` | DENY     |
