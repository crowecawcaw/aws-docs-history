

# Access control for the Custom Event Bus
<a name="eb-custom-bus-access"></a>

You control who can use a Custom Event Bus with IAM policies, the same way as for other AWS services. To let a role or user in your own account publish to a bus, manage subscribers, or administer buses, attach an identity-based policy to that role or user. For example, a producer's role needs `events:PutRawEvents` on the bus ARN. To let another account publish to your bus or attach subscribers to it, share the bus with that account through AWS Resource Access Manager (AWS RAM), or attach a resource policy to the bus; see [Sharing a Custom Event Bus with other accounts](eb-custom-bus-sharing.md). Every action name uses the `events:` prefix, for example `events:CreateSubscriber`; for the CLI, SDK, and endpoint names, see [Names, endpoints, and IAM permissions for the Custom Event Bus](eb-custom-bus-names.md).
+ [Actions, resources, and condition keys for the Custom Event Bus](eb-custom-bus-access-actions.md)
+ [Revoking a subscriber or an event source](eb-custom-bus-access-revoke.md)
+ [Permissions by scenario](eb-custom-bus-permissions.md)