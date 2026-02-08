# Troubleshoot multi-Region setup in AWS IAM Identity Center

This topic describes common multi-Region setup related errors you might encounter when
using AWS IAM Identity Center and provides troubleshooting steps to resolve them.

## The Region I want to replicate my IAM Identity Center instance to

is not available in the IAM Identity Center console

You must first create a replica key for your customer managed KMS key in the Region you
want to replicate your IAM Identity Center instance to. Once the replica key is created, you will see the
Region in the list of Regions available for replications. For more information, see [Step 1: Create a replica key in the additional Region](replicate-to-additional-region.md#replicate-kms-key "replicate-to-additional-region.md#replicate-kms-key").

## AWS managed application sign-in failures in an

additional Region

If no IAM Identity Center users can sign into AWS managed applications in an additional Region after
you added the Region in IAM Identity Center, confirm that you configured the additional Region's Assertion
Consumer Service (ACS) URL in the external identity provider as described in [Step 3: Update external IdP setup](replicate-to-additional-region.md#update-external-idp-setup "replicate-to-additional-region.md#update-external-idp-setup"). Also, confirm your users have connectivity to
the Region.
