

# AWS CloudHSM in AWS GovCloud (US)
<a name="govcloud-cloudhsm"></a>

AWS CloudHSM offers secure cryptographic key storage for customers by providing managed hardware security modules in the AWS Cloud.

## Region availability
<a name="region-availability"></a>

 AWS CloudHSM is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-East) 
+  AWS GovCloud (US-West) 

## How AWS CloudHSM differs
<a name="feature-diffs"></a>

There are no differences for this service.

## Documentation
<a name="documentation"></a>

 [AWS CloudHSM documentation](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html).

## Export-controlled content
<a name="itar-boundary"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  AWS CloudHSM metadata is not permitted to contain export-controlled data. This includes all configuration data that you enter when creating and maintaining your AWS CloudHSM config. Audit and syslogs should not contain export-controlled data.

## AWS CloudHSM Root Certificate
<a name="govcloud-hsmv2-root-cert"></a>

If you choose to [verify the identity of an HSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/verify-hsm-identity.html), be sure to use the root certificate for the AWS GovCloud (US) Region rather than the root certificate that is available for commercial Regions. You can download the certificate from [AWS-US-GOV\_CloudHSM\_Root\_G1.zip](https://docs.aws.amazon.com/cloudhsm/latest/userguide/samples/AWS_US_GOV_CloudHSM_Root-G1.zip). Verification is an optional step that you can perform after you [create an HSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-hsm.html). For more information about AWS CloudHSM, see the [AWS CloudHSM User Guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html). For more information about AWS CloudHSM Classic, see the [AWS CloudHSM Classic User Guide](https://docs.aws.amazon.com/cloudhsm/classic/userguide/).