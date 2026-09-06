

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with Domain Management
<a name="working-with-domain-management"></a>

## Domain Management
<a name="domain-management"></a>

Partners can register and verify business domains through email validation to establish organizational identity and associate employees' training and certifications.

### API Summary
<a name="domain-api-summary"></a>

1. **SendEmailVerificationCode API:** Initiates email verification process by sending a verification code to the specified email address. Used for both new contact creation and email address updates.

1. **AssociateAwsTrainingCertificationEmailDomain API:** Associates an email domain with AWS training and certification for the partner account, enabling automatic verification of employee certifications.

1. **DisassociateAwsTrainingCertificationEmailDomain API:** Removes the association between an email domain and AWS training and certification for the partner account.