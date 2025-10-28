# MASEC 1: How do you plan to manage user

and application identities across companies?

A well-defined plan is important to integrate identities from both
companies without any impact to the end users. It is critical to
have an integration plan to avoid security and compliance issues
after mergers and acquisitions.

## MASEC01-BP01 Use a

centralized identity provider

At any given time, you can have only one directory or one SAML 2.0 identity provider connected to IAM Identity Center. But, you can change the identity source that is connected to a different one.

## MASEC01-BP02 Use a common

authorization approach

Companies may have a very different approach to authorization. Companies need to use a common authorization platform and develop consistent authorization policies for the combined systems.

## MASEC01-BP03 Use AWS

temporary credentials

You can use the AWS Security Token Service to create and provide trusted users with temporary security credentials that can control access to your AWS resources.

## MASEC01-BP04 Store and use

secrets securely

Use AWS Secrets Manager to replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. The secret can't be compromised by someone examining your code because the secret no longer exists in the code.

## MASEC01-BP05 Create a common

policy for auditing and rotating credentials

Rotation is the process of periodically updating a secret. When you rotate a secret, you update the credentials in both the secret and the database or service. In Secrets Manager, you can set up automatic rotation for your secrets.
