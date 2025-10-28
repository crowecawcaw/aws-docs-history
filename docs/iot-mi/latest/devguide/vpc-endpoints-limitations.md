# Limitations

- The [CreateAccountAssociation](../APIReference/API_CreateAccountAssociation.md "../APIReference/API_CreateAccountAssociation.md") API,
  is designed to perform OAuth with third-party cloud services,
  which requires the request to leave the Amazon network.
  This is important for customers using AWS PrivateLink to contain their traffic within the VPC,
  as AWS PrivateLink cannot provide complete end-to-end containment for this API call.
- VPC endpoints for AWS IoT Managed integrations are not available in AWS GovCloud (US) Regions.
  For general VPC endpoint limitations, see
  [Interface endpoint properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.
