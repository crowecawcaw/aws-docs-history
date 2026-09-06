

# Manage DNS security policies in Route 53 Global Resolver
<a name="gr-manage-dns-security-policies"></a>

## Managing global resolvers
<a name="gr-managing-resolvers"></a>

After creating a global resolver, you can view its details, edit its configuration, and manage associated resources from the Global Resolvers page.

### Viewing resolver details
<a name="gr-viewing-resolver-details"></a>

The Global Resolvers page displays a list of all your resolvers with key information including resolver name, deployed regions, associated DNS views, observability region, and operational status.

### Editing global resolvers
<a name="gr-editing-resolvers"></a>

You can modify the resolver name and description after creation. You cannot modify the regions where a global resolver is deployed after creation.

## Managing firewall rules
<a name="gr-managing-firewall-rules"></a>

After creating firewall rules, you can modify their priority, update their configuration, or delete them as needed.

### Rule priority and evaluation order
<a name="gr-rule-priority"></a>

Firewall rules are evaluated in priority order, with lower numbers processed first. When a query matches multiple rules, only the first matching rule's action is applied.

### Updating firewall rules
<a name="gr-updating-rules"></a>

You can update most aspects of a firewall rule after creation, including its priority, action, and target domains.