# DataZone IAM Credentials

Provider

An authentication mechanism that uses IAM credentials to connect to
DataZone-governed data in Athena.

## DataZone

domain identifier

Identifier of the DataZone domain to use.

| Parameter name           | Alias           | Parameter type | Default value |
| ------------------------ | --------------- | -------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DataZoneDomainId         | none            | Required       | none          | ## DataZone environment identifier Identifier of the DataZone environment to use.                                                                                                                                                      |
| Parameter name           | Alias           | Parameter type | Default value |
| ---                      | ---             | ---            | ---           |
| DataZoneEnvironmentId    | none            | Required       | none          | ## DataZone domain region The AWS Region where your DataZone domain is provisioned.                                                                                                                                                    |
| Parameter name           | Alias           | Parameter type | Default value |
| ---                      | ---             | ---            | ---           |
| DataZoneDomainRegion     | none            | Required       | none          | ## DataZone endpoint override The DataZone API endpoint to use instead of the endpoint default for the provided AWS Region.                                                                                                            |
| Parameter name           | Alias           | Parameter type | Default value |
| ---                      | ---             | ---            | ---           |
| DataZoneEndpointOverride | none            | Optional       | none          | ## User Your AWS access key ID. For more information about access keys, see [AWS security credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md") in the _IAM User Guide_.     |
| Parameter name           | Alias           | Parameter type | Default value |
| ---                      | ---             | ---            | ---           |
| User                     | AccessKeyId     | Optional       | none          | ## Password Your AWS secret key ID. For more information about access keys, see [AWS security credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md") in the _IAM User Guide_. |
| Parameter name           | Alias           | Parameter type | Default value |
| ---                      | ---             | ---            | ---           |
| Password                 | SecretAccessKey | Optional       | none          |
