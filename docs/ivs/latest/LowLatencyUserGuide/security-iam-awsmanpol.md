# Managed Policies for Amazon IVS

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## IVSReadOnlyAccess

Use the [IVSReadOnlyAccess](../../../aws-managed-policy/latest/reference/IVSReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/IVSReadOnlyAccess.md")
AWS managed policy to give your application developers access
to all non-mutating IVS API operations (for both low-latency and real-time streaming).

## IVSFullAccess

Use the [IVSFullAccess](../../../aws-managed-policy/latest/reference/IVSFullAccess.md "../../../aws-managed-policy/latest/reference/IVSFullAccess.md")
AWS managed policy to give your users access to all IVS and IVS Chat API operations (for both low-latency and real-time streaming).
This policy includes additional permissions for dependent services, to allow full access to the IVS console.

## Policy Updates

View details about updates to AWS managed policies for Amazon IVS since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Amazon IVS Low-Latency Streaming [Document History](doc-history.md "doc-history.md") page.

| Change                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                     | Date               |
| ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [IVSReadOnlyAccess](#security-iam-awsmanpol-ivsreadonlyaccess "#security-iam-awsmanpol-ivsreadonlyaccess") – Change     | IVS added a new action to grant ListParticipantReplicas permission in support of the Participant Replication<br>real-time-streaming release.                                                                                                                                                                                                                                                                    | July 24, 2025      |
| [IVSReadOnlyAccess](#security-iam-awsmanpol-ivsreadonlyaccess "#security-iam-awsmanpol-ivsreadonlyaccess") – Change     | IVS added new actions to grant the following permissions in support of two real-time-streaming releases,<br>RTMP Ingest and Generate Participant Tokens with a Key Pair:<br>• GetIngestConfiguration<br>• ListIngestConfigurations<br>• GetPublicKey<br>• ListPublicKeys                                                                                                                                        | September 18, 2024 |
| [IVSReadOnlyAccess](#security-iam-awsmanpol-ivsreadonlyaccess "#security-iam-awsmanpol-ivsreadonlyaccess") – Change     | IVS added new actions to grant the following permissions in support of Server-Side Composition,<br>Real-Time Composite Recording, and Tokenless Playback Restrictions:<br>• GetComposition<br>• ListCompositions<br>• GetEncoderConfiguration<br>• ListEncoderConfigurations<br>• GetPlaybackRestrictionPolicy<br>• ListPlaybackRestrictionPolicies<br>• GetStorageConfiguration<br>• ListStorageConfigurations | February 16, 2024  |
| [IVSFullAccess](#security-iam-awsmanpol-ivsfullaccess "#security-iam-awsmanpol-ivsfullaccess") – New policy             | IVS added a new policy to allow full access to IVS<br>(both low-latency and real-time streaming) and IVS Chat.                                                                                                                                                                                                                                                                                                  | December 5, 2023   |
| [IVSReadOnlyAccess](#security-iam-awsmanpol-ivsreadonlyaccess "#security-iam-awsmanpol-ivsreadonlyaccess") – New policy | IVS added a new policy to allow read-only access to IVS<br>(both low-latency and real-time streaming).                                                                                                                                                                                                                                                                                                          | December 5, 2023   |
| Amazon IVS started tracking changes                                                                                     | Amazon IVS started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                               | December 5, 2023   |
