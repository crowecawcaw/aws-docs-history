

# Security considerations
<a name="feed-policies-security"></a>

When creating feed policies, follow these security best practices:
+ **Always include a source account condition** – Include the `aws:SourceAccount` condition in every statement that grants access to an AWS service principal. This prevents the *confused deputy* problem, where a service could be tricked into accessing your feed on behalf of an unauthorized account. Where possible, also include `aws:SourceArn` to restrict access to specific resources in your account.
+ **Do not use wildcard principals** – Elemental Inference rejects policies with wildcard (`*`) principals. Specify the exact AWS service or account principal that requires access.
+ **Scope permissions to specific actions** – Grant only the actions that the consuming service needs. For MediaTailor integration, `elemental-inference:GetMetadata` is the only supported action.
+ **Scope the resource** – Specify the exact feed ARN in the `Resource` field rather than using a wildcard. This ensures the policy grants access only to the intended feed.