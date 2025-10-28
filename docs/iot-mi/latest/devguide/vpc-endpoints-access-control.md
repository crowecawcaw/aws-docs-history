# Controlling access to services over VPC endpoints

A VPC endpoint policy is an IAM resource policy that you attach to an interface VPC endpoint when you create or modify the endpoint.
If you don't attach a policy when you create an endpoint, we attach a default policy for you that allows full access to the service.
An endpoint policy doesn't override or replace IAM user policies or service-specific policies.
It's a separate policy for controlling access from the endpoint to the specified service.

Endpoint policies must be written in JSON format. For more information,
see [Controlling access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

## Example: VPC endpoint policy for AWS IoT Managed integrations actions

The following is an example of an endpoint policy for AWS IoT Managed integrations.
This policy allows users connecting to AWS IoT Managed integrations through the VPC endpoint to access destinations but denies access to credential lockers.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "iotmanagedintegrations:ListDestinations",
                "iotmanagedintegrations:GetDestination",
                "iotmanagedintegrations:CreateDestination",
                "iotmanagedintegrations:UpdateDestination",
                "iotmanagedintegrations:DeleteDestination"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": [
                "iotmanagedintegrations:ListCredentialLockers",
                "iotmanagedintegrations:GetCredentialLocker",
                "iotmanagedintegrations:CreateCredentialLocker",
                "iotmanagedintegrations:UpdateCredentialLocker",
                "iotmanagedintegrations:DeleteCredentialLocker"
            ],
            "Resource": "*"
        }
    ]
}
```

## Example: VPC endpoint policy that restricts access to a specific IAM role

The following VPC endpoint policy allows access to AWS IoT Managed integrations only for IAM principals that have the specified IAM role in their trust chain.
All other IAM principals are denied access.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalArn": "arn:aws:iam::123456789012:role/IoTManagedIntegrationsVPCRole"
                }
            }
        }
    ]
}
```
