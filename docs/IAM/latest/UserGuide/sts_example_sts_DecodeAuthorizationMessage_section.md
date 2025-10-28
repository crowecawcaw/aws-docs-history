# Use `DecodeAuthorizationMessage` with a CLI

The following code examples show how to use `DecodeAuthorizationMessage`.

CLI

**AWS CLI**

**To decode an encoded authorization message returned in response to a request**

The following `decode-authorization-message` example decodes additional information about the authorization status of a request from an encoded message returned in response to an Amazon Web Services request.

```
`aws sts decode-authorization-message \
 --encoded-message `EXAMPLEWodyRNrtlQARDip-eTA6i6DrlUhHhPQrLWB_lAbl5pAKxl9mPDLexYcGBreyIKQC1BGBIpBKr3dFDkwqeO7e2NMk5j_hmzAiChJN-8oy3EwiCjkUW5fdRNjcRvscGlUo_MhqHqHpR-Ojau7BMjOTWwOtHPhV_Zaz87yENdipr745EjQwRd5LaoL3vN8_5ZfA9UiBMKDgVh1gjqZJFUiQoubv78V1RbHNYnK44ElGKmUWYa020I1y6TNS9LXoNmc62GzkfGvoPGhD13br5tXEOo1rAm3vsPewRDFNkYL-4_1MWWezhRNEpqvXBDXLI9xEux7YYkRtjd45NJLFzZynBUubV8NHOevVuighd1Mvz3OiA-1_oPSe4TBtjfN9s7kjU1z70WpVbUgrLVp1xXTK1rf9Ea7t8shPd-3VzKhjS5tLrweFxNOKwV2GtT76B_fRp8HTYz-pOu3FZjwYStfvTb3GHs3-6rLribGO9jZOktkfE6vqxlFzLyeDr4P2ihC1wty9tArCvvGzIAUNmARQJ2VVWPxioqgoqCzMaDMZEO7wkku7QeakEVZdf00qlNLMmcaVZb1UPNqD-JWP5pwe_mAyqh0NLw-r1S56YC_90onj9A80sNrHlI-tIiNd7tgNTYzDuPQYD2FMDBnp82V9eVmYGtPp5NIeSpuf3fOHanFuBZgENxZQZ2dlH3xJGMTtYayzZrRXjiq_SfX9zeBbpCvrD-0AJK477RM84vmtCrsUpJgx-FaoPIb8LmmKVBLpIB0iFhU9sEHPqKHVPi6jdxXqKaZaFGvYVmVOiuQdNQKuyk0p067POFrZECLjjOtNPBOZCcuEKEXAMPLE``

```

Output:

```
{
    "DecodedMessage": "{\"allowed\":false,\"explicitDeny\":true,\"matchedStatements\":{\"items\":[{\"statementId\":\"VisualEditor0\",\"effect\":\"DENY\",\"principals\":{\"items\":[{\"value\":\"AROA123456789EXAMPLE\"}]},\"principalGroups\":{\"items\":[]},\"actions\":{\"items\":[{\"value\":\"ec2:RunInstances\"}]},\"resources\":{\"items\":[{\"value\":\"*\"}]},\"conditions\":{\"items\":[]}}]},\"failures\":{\"items\":[]},\"context\":{\"principal\":{\"id\":\"AROA123456789EXAMPLE:Ana\",\"arn\":\"arn:aws:sts::111122223333:assumed-role/Developer/Ana\"},\"action\":\"RunInstances\",\"resource\":\"arn:aws:ec2:us-east-1:111122223333:instance/*\",\"conditions\":{\"items\":[{\"key\":\"ec2:MetadataHttpPutResponseHopLimit\",\"values\":{\"items\":[{\"value\":\"2\"}]}},{\"key\":\"ec2:InstanceMarketType\",\"values\":{\"items\":[{\"value\":\"on-demand\"}]}},{\"key\":\"aws:Resource\",\"values\":{\"items\":[{\"value\":\"instance/*\"}]}},{\"key\":\"aws:Account\",\"values\":{\"items\":[{\"value\":\"111122223333\"}]}},{\"key\":\"ec2:AvailabilityZone\",\"values\":{\"items\":[{\"value\":\"us-east-1f\"}]}},{\"key\":\"ec2:ebsOptimized\",\"values\":{\"items\":[{\"value\":\"false\"}]}},{\"key\":\"ec2:IsLaunchTemplateResource\",\"values\":{\"items\":[{\"value\":\"false\"}]}},{\"key\":\"ec2:InstanceType\",\"values\":{\"items\":[{\"value\":\"t2.micro\"}]}},{\"key\":\"ec2:RootDeviceType\",\"values\":{\"items\":[{\"value\":\"ebs\"}]}},{\"key\":\"aws:Region\",\"values\":{\"items\":[{\"value\":\"us-east-1\"}]}},{\"key\":\"ec2:MetadataHttpEndpoint\",\"values\":{\"items\":[{\"value\":\"enabled\"}]}},{\"key\":\"aws:Service\",\"values\":{\"items\":[{\"value\":\"ec2\"}]}},{\"key\":\"ec2:InstanceID\",\"values\":{\"items\":[{\"value\":\"*\"}]}},{\"key\":\"ec2:MetadataHttpTokens\",\"values\":{\"items\":[{\"value\":\"required\"}]}},{\"key\":\"aws:Type\",\"values\":{\"items\":[{\"value\":\"instance\"}]}},{\"key\":\"ec2:Tenancy\",\"values\":{\"items\":[{\"value\":\"default\"}]}},{\"key\":\"ec2:Region\",\"values\":{\"items\":[{\"value\":\"us-east-1\"}]}},{\"key\":\"aws:ARN\",\"values\":{\"items\":[{\"value\":\"arn:aws:ec2:us-east-1:111122223333:instance/*\"}]}}]}}}"
}
```

For more information, see [Policy evaluation logic](reference_policies_evaluation-logic.md "reference_policies_evaluation-logic.md") in the _AWS IAM User Guide_.

- For API details, see
  [DecodeAuthorizationMessage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/decode-authorization-message.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/decode-authorization-message.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Decodes the additional information contained in the supplied encoded message content that was returned in response to a request. The additional information is encoded because details of the authorization status can constitute privileged information that the user who requested the action should not see.**

```
Convert-STSAuthorizationMessage -EncodedMessage "...encoded message..."

```

- For API details, see
  [DecodeAuthorizationMessage](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Decodes the additional information contained in the supplied encoded message content that was returned in response to a request. The additional information is encoded because details of the authorization status can constitute privileged information that the user who requested the action should not see.**

```
Convert-STSAuthorizationMessage -EncodedMessage "...encoded message..."

```

- For API details, see
  [DecodeAuthorizationMessage](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
