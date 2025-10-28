# Using Deterministic Easy DKIM (DEED)

in Amazon SES

Deterministic Easy DKIM (DEED) offers a solution for managing DKIM configurations across
multiple AWS Regions. By simplifying DNS management and ensuring consistent DKIM signing,
DEED helps you streamline your multi-region email sending operations while maintaining
robust email authentication practices.

## What is Deterministic Easy DKIM (DEED)?

Deterministic Easy DKIM (DEED) is a feature that generates consistent DKIM tokens
across all AWS Regions based on a parent domain that is configured with [Easy DKIM](send-email-authentication-dkim-easy.md "send-email-authentication-dkim-easy.md"). This enables you to
replicate identities in different AWS Regions that automatically inherit and maintain
the same DKIM signing configuration as a parent identity that is currently configured
with Easy DKIM. With DEED, you only need to publish DNS records once for the parent
identity, and replica identities will use the same DNS records to verify domain
ownership and manage DKIM signing.

By simplifying DNS management and ensuring consistent DKIM signing, DEED helps you
streamline your multi-region email sending operations while maintaining best email
authentication practices.

Terminology used when talking about DEED:

- **Parent identity** – A verified
  identity configured with Easy DKIM that serves as the source for DKIM
  configuration for a replica identity.
- **Replica identity** – A copy of a
  parent identity that shares the same DNS setup and DKIM signing
  configuration.
- **Parent region** – The AWS Region
  where a parent identity is set up.
- **Replica region** – An AWS Region
  where a replica identity is set up.
- **DEED identity** – Any identity that
  is used as either a parent identity or a replica identity. (When a new
  identity is created, it is initially treated as a regular (non-DEED)
  identity. However, once a replica is created, the identity is then
  considered a DEED identity.)

Key benefits of using DEED include:

- **Simplified DNS management** –
  Publish DNS records only once for the parent identity.
- **Easier multi-region operations** –
  Simplify the process of expanding email sending operations to new
  regions.
- **Reduced administrative overhead** –
  Manage DKIM configurations centrally from the parent identity.

## How Deterministic Easy DKIM (DEED) works

When you create a replica identity, Amazon SES automatically replicates the DKIM signing
key from the parent identity to the replica identity. Any subsequent DKIM key rotations
or key length changes made to the parent identity are automatically propagated to all
replica identities.

The process involves the following workflow:

1. Create a parent identity in an AWS Region using Easy DKIM.
2. Set up the required DNS records for the parent identity.
3. Create replica identities in other AWS Regions, specifying the parent
   identity's domain name and DKIM signing region.
4. Amazon SES automatically replicates the parent's DKIM configuration to the replica
   identities.

Important considerations:

- You cannot create a replica of an identity that is already a
  replica.
- The parent identity must have [Easy DKIM](send-email-authentication-dkim-easy.md "send-email-authentication-dkim-easy.md")
  enabled—you cannot create replicas of BYODKIM or manually signed
  identities.
- Parent identities cannot be deleted until all replica identities are
  deleted.

## Setting up a replica identity using

DEED

This section will provide examples showing you how to create and verify a replica
identity using DEED along with the necessary permissions required.

###### Topics

- [Creating a replica identity](#creating-replica-identity "#creating-replica-identity")
- [Verifying replica identity
  configuration](#verifying-replica-identity "#verifying-replica-identity")
- [Required Permissions to use DEED](#required-permissions "#required-permissions")

### Creating a replica identity

To create replica identity:

1. In the AWS Region where you want to create a replica identity, open the
   SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").

(In the SES console, replica identities are referred to as
_Global identities_.) 2. In the navigation pane, choose **Identities**. 3. Choose **Create identity**. 4. Select **Domain** under **Identity
type** and enter the domain name of an existing identity
configured with Easy DKIM that you want to replicate and serve as the
parent. 5. Expand **Advanced DKIM settings** and select
**Deterministic Easy DKIM**. 6. From the **Parent region** dropdown menu, select a parent
region where an Easy DKIM-signed identity with the same name as you entered
for your Global (replica) identity resides. (Your replica region defaults to
the region you signed into the SES console with.) 7. Ensure **DKIM signatures** is enabled. 8. (Optional) Add one or more **Tags** to your domain
identity. 9. Review the configuration and choose **Create
identity**.

Using the AWS CLI:

To create a replica identity based on a parent identity configured with Easy DKIM,
you need to specify the parent's domain name, the region where you want to create
the replica identity, and the parent's DKIM signing region as shown in this
example:

```
aws sesv2 create-email-identity --email-identity `example.com` --region `us-west-2` --dkim-signing-attributes '{"DomainSigningAttributesOrigin": "`AWS_SES_US_EAST_1`"}'
```

In the preceding example:

1. Replace `example.com` with the parent domain
   identity being replicated.
2. Replace `us-west-2` with the region where the
   replica domain identity will be created.
3. Replace `AWS_SES_US_EAST_1` with the parent's
   DKIM signing region that represents its Easy DKIM signing configuration that
   will be replicated to the replica identity.

###### Note

The `AWS_SES_` prefix indicates that DKIM was configured
for the parent identity by using Easy DKIM, and `US_EAST_1`
is the AWS Region where it was created.

### Verifying replica identity

configuration

After creating the replica identity, you can verify that it was configured
correctly with the parent identity's DKIM signing configuration.

###### To verify a replica identity:

1. In the AWS Region where you created the replica identity, open the
   SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane, choose **Identities** and select
   the identity you want to verify from the **Identities**
   table.
3. Under the **Authentication** tab, the **DKIM
   configuration** field will indicate the status, and the
   **Parent region** field will indicate the region being
   used for the identity's DKIM signing configuration utilizing DEED.

Using the AWS CLI:

Use the `get-email-identity` command specifying the replica's domain
name and region:

```
aws sesv2 get-email-identity --email-identity `example.com` --region `us-west-2`
```

The response will include the value of the parent region in the
`SigningAttributesOrigin` parameter signifying that the replica
identity has been successfully configured with the parent identity's DKIM signing
configuration:

```
{
  "DkimAttributes": {
    "SigningAttributesOrigin": "AWS_SES_US_EAST_1"
  }
}
```

### Required Permissions to use DEED

To use DEED, you need:

1. Standard permissions for creating email identities in the replica
   region.
2. Permission to replicate the DKIM signing key from the parent
   region.

#### Example IAM policy for DKIM

replication

The following policy allows DKIM signing key replication from a parent
identity to specified replica regions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDKIMReplication",
 "Effect": "Allow",
 "Action": "ses:ReplicateEmailIdentityDKIMSigningKey",
 "Resource": "arn:aws:ses:us-east-1:123456789124:identity/example.com",
 "Condition": {
 "ForAllValues:StringEquals": {
 "ses:ReplicaRegion": ["us-west-2", "eu-west-1"]
 }
 }
 }
 ]
}`

```

## Best practices

The following best practices are recommended:

- **Plan your parent and replica regions** –
  Give consideration to the parent region you choose, as it will be the source of
  truth for the DKIM configuration used in replica regions.
- **Use consistent IAM policies** – Ensure
  that your IAM policies allow for DKIM replication across all intended
  regions.
- **Keep parent identities active** –
  Remember that your replica identities inherit the DKIM signing configuration of
  the parent identity, because of this dependency, you cannot delete a parent
  identity until all replica identities are deleted.

## Troubleshooting

If you encounter issues with DEED, consider the following:

- **Verification errors** – Ensure that you
  have the necessary permissions for DKIM replication.
- **Replication delays** – Allow some time
  for replication to complete, especially when creating new replica
  identities.
- **DNS issues** – Verify that the DNS
  records for the parent identity are correctly set up and propagated.
