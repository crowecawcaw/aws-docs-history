# AWS CloudHSM in AWS GovCloud (US)

AWS CloudHSM offers secure cryptographic key storage for customers by providing managed hardware security modules in the AWS Cloud.

## Region availability

AWS CloudHSM is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-East)
- AWS GovCloud (US-West)

## How AWS CloudHSM differs

There are no differences for this service.

## Documentation

[AWS CloudHSM documentation](../../../cloudhsm/latest/userguide/introduction.md "../../../cloudhsm/latest/userguide/introduction.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- AWS CloudHSM metadata is not permitted to contain export-controlled data. This includes all configuration data that you enter when creating and maintaining your AWS CloudHSM config. Audit and syslogs should not contain export-controlled data.

## AWS CloudHSM Root Certificate

If you choose to [verify the identity of an HSM](../../../cloudhsm/latest/userguide/verify-hsm-identity.md "../../../cloudhsm/latest/userguide/verify-hsm-identity.md"), be sure to use the root certificate for the AWS GovCloud (US) Region rather than the root certificate that is available for commercial Regions. You can download the certificate from [AWS-US-GOV\_CloudHSM\_Root\_G1.zip](../../../cloudhsm/latest/userguide/samples/AWS_US_GOV_CloudHSM_Root-G1.zip.md "../../../cloudhsm/latest/userguide/samples/AWS_US_GOV_CloudHSM_Root-G1.zip.md"). Verification is an optional step that you can perform after you [create an HSM](../../../cloudhsm/latest/userguide/create-hsm.md "../../../cloudhsm/latest/userguide/create-hsm.md"). For more information about AWS CloudHSM, see the [AWS CloudHSM User Guide](../../../cloudhsm/latest/userguide/introduction.md "../../../cloudhsm/latest/userguide/introduction.md"). For more information about AWS CloudHSM Classic, see the [AWS CloudHSM Classic User Guide](../../../cloudhsm/classic/userguide.md "../../../cloudhsm/classic/userguide.md").
