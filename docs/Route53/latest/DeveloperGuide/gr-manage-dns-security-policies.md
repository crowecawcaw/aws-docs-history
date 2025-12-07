# Manage DNS security policies in Route 53 Global Resolver

## Managing global resolvers

After creating a global resolver, you can view its details, edit its configuration, and
manage associated resources from the Global Resolvers page.

### Viewing resolver details

The Global Resolvers page displays a list of all your resolvers with key information
including resolver name, deployed regions, associated DNS views, observability region, and
operational status.

### Editing global resolvers

You can modify the resolver name and description after creation. You cannot modify the
regions where a global resolver is deployed after creation.

## Managing firewall rules

After creating firewall rules, you can modify their priority, update their configuration,
or delete them as needed.

### Rule priority and evaluation order

Firewall rules are evaluated in priority order, with lower numbers processed first. When a
query matches multiple rules, only the first matching rule's action is applied.

### Updating firewall rules

You can update most aspects of a firewall rule after creation, including its priority,
action, and target domains.
