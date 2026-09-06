

# Managed Policies for Amazon IVS
<a name="security-iam-awsmanpol"></a>





An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.













## IVSReadOnlyAccess
<a name="security-iam-awsmanpol-ivsreadonlyaccess"></a>

Use the [IVSReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/IVSReadOnlyAccess.html) AWS managed policy to give your application developers access to all non-mutating IVS API operations (for both low-latency and real-time streaming).

## IVSFullAccess
<a name="security-iam-awsmanpol-ivsfullaccess"></a>

Use the [IVSFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/IVSFullAccess.html) AWS managed policy to give your users access to all IVS and IVS Chat API operations (for both low-latency and real-time streaming). This policy includes additional permissions for dependent services, to allow full access to the IVS console.

## Policy Updates
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Amazon IVS since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Amazon IVS Low-Latency Streaming [Document History](doc-history.md) page.




| Change | Description | Date | 
| --- | --- | --- | 
| [IVSReadOnlyAccess](#security-iam-awsmanpol-ivsreadonlyaccess) – Change | IVS added a new action to grant ListParticipantReplicas permission in support of the Participant Replication real-time-streaming release. | July 24, 2025 | 
| [IVSReadOnlyAccess](#security-iam-awsmanpol-ivsreadonlyaccess) – Change | IVS added new actions to grant the following permissions in support of two real-time-streaming releases, RTMP Ingest and Generate Participant Tokens with a Key Pair:+ GetIngestConfiguration<br />+ ListIngestConfigurations<br />+ GetPublicKey<br />+ ListPublicKeys | September 18, 2024 | 
| [IVSReadOnlyAccess](#security-iam-awsmanpol-ivsreadonlyaccess) – Change | IVS added new actions to grant the following permissions in support of Server-Side Composition, Real-Time Composite Recording, and Tokenless Playback Restrictions:+ GetComposition<br />+ ListCompositions<br />+ GetEncoderConfiguration<br />+ ListEncoderConfigurations<br />+ GetPlaybackRestrictionPolicy<br />+ ListPlaybackRestrictionPolicies<br />+ GetStorageConfiguration<br />+ ListStorageConfigurations | February 16, 2024 | 
| [IVSFullAccess](#security-iam-awsmanpol-ivsfullaccess) – New policy | IVS added a new policy to allow full access to IVS (both low-latency and real-time streaming) and IVS Chat. | December 5, 2023 | 
| [IVSReadOnlyAccess](#security-iam-awsmanpol-ivsreadonlyaccess) – New policy | IVS added a new policy to allow read-only access to IVS (both low-latency and real-time streaming). | December 5, 2023 | 
| Amazon IVS started tracking changes | Amazon IVS started tracking changes for its AWS managed policies. | December 5, 2023 | 