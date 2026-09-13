

# Managing feed policies
<a name="feed-policies"></a>

A feed policy is a resource-based policy that you attach to an Elemental Inference feed to grant cross-account access. When you attach a policy to a feed, other AWS accounts and services can call `GetMetadata` on that feed without needing IAM credentials in your account.

A common use case for feed policies is integration with AWS Elemental MediaTailor. After you attach a policy that grants MediaTailor access, MediaTailor retrieves contextual metadata from the feed at ad break time and forwards it to the ad-decision server for contextual ad targeting.

**Topics**
+ [Prerequisites](feed-policies-prerequisites.md)
+ [Policy requirements](feed-policies-requirements.md)
+ [Attaching a policy using the console](feed-policies-console.md)
+ [Managing policies using the CLI](feed-policies-cli.md)
+ [Example policy for MediaTailor access](feed-policies-example.md)
+ [Security considerations](feed-policies-security.md)