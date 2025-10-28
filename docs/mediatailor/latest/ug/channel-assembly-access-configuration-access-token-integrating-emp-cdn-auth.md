# Integrating with MediaPackage endpoints that use CDN authorization

If you use AWS Elemental MediaPackage as your source location origin, MediaTailor can integrate with
MediaPackage endpoints that use CDN authorization.

To integrate with a MediaPackage endpoint that uses CDN authorization, use the
following procedure.

###### To integrate with MediaPackage

1. Complete the steps in [Setting up CDN
   authorization](../../../mediapackage/latest/ug/cdn-auth-setup.md "../../../mediapackage/latest/ug/cdn-auth-setup.md") in the _AWS Elemental MediaPackage User Guide_, if you haven't already.
2. Complete the procedure in [Step 1: Create an AWS KMS symmetric customer managed key](channel-assembly-access-configuration-access-configuring.md#channel-assembly-access-configuration-access-token-how-to-create-kms "channel-assembly-access-configuration-access-configuring.md#channel-assembly-access-configuration-access-token-how-to-create-kms").
3. Modify the secret that you created when you set up MediaPackage CDN
   authorization. Modify the secret with the following values:
   - Update the `KmsKeyId` with the customer managed key ARN that
     you created in [Step 1: Create an AWS KMS symmetric customer managed key](channel-assembly-access-configuration-access-configuring.md#channel-assembly-access-configuration-access-token-how-to-create-kms "channel-assembly-access-configuration-access-configuring.md#channel-assembly-access-configuration-access-token-how-to-create-kms").
   - (Optional) For the `SecretString`, you can either
     rotate the UUID to a new value, or you can use the existing
     encrypted secret as long as it's a key and value pair in a
     standard JSON format, such as
     `{"MediaPackageCDNIdentifier":
"112233445566778899"}`.

4. Complete the steps in [Attaching a resource-based secret policy](channel-assembly-access-configuration-access-configuring.md#channel-assembly-access-configuration-access-token-secret-policy "channel-assembly-access-configuration-access-configuring.md#channel-assembly-access-configuration-access-token-secret-policy").
5. Complete the steps in [Step 3: Configure a MediaTailor source location with access token
   authentication](channel-assembly-access-configuration-access-configuring.md#channel-assembly-access-configuration-access-token-how-to-enable-access-token-auth "channel-assembly-access-configuration-access-configuring.md#channel-assembly-access-configuration-access-token-how-to-enable-access-token-auth").
