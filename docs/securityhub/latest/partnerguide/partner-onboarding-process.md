# Partner onboarding process

As a partner, you can expect to complete several high-level steps as part of your onboarding
process. You must complete these steps before you can send security findings to AWS Security Hub CSPM.

1. You initiate an engagement with the APN Partner team or the Security Hub CSPM team and express interest
   in becoming a partner with Security Hub CSPM. You identify the email addresses to add to Security Hub CSPM communication
   channels.
2. AWS gives you the Security Hub CSPM partner onboarding materials.
3. You are invited to the Security Hub CSPM partner Slack channel, where you can ask questions related to
   your integration.
4. You provide APN Partner contacts with a draft product integration manifest for
   review.

The product integration manifest contains information that is used to create the partner
product Amazon Resource Name (ARN) for the integration with AWS Security Hub CSPM.

It provides the Security Hub CSPM team with information that appears on the partner provider page in
the Security Hub CSPM console. It is also used to propose new managed insights related to the integration to
add to the Security Hub CSPM insight library.

This initial version of the product integration manifest does not have to have the complete
details. But it should at least contain the use case and dataset information.

For details about the manifest and the required information, see [Product integration manifest](integration-manifest.md "integration-manifest.md"). 5. The Security Hub CSPM team gives you a product ARN for your product. You use the ARN to send findings
to Security Hub CSPM. 6. You build your integration to send findings to or receive findings from Security Hub CSPM.

**Mapping findings to ASFF**

To send findings to Security Hub CSPM, you must map your findings to the AWS Security Finding
Format (ASFF).

The ASFF provides a consistent description of findings that can be shared among AWS
security services, partners, and customer security systems. This reduces integration efforts,
encourages a common language, and provides a blueprint for implementers.

ASFF is the required wire protocol format to use to send findings to AWS Security Hub CSPM. Findings
are represented as JSON documents that adhere to the ASFF JSON Schema and RFC-7493 The I-JSON
Message Format. For details on the ASFF schema, see [AWS Security Finding
Format (ASFF)](../userguide/securityhub-findings-format.md "../userguide/securityhub-findings-format.md") in the _AWS Security Hub CSPM User Guide_.

See [Guidelines for mapping findings into the AWS Security
Finding Format (ASFF)](guidelines-asff-mapping.md "guidelines-asff-mapping.md").

**Building and testing the integration**

You can complete all of the testing for your integration using an AWS account that you
own. Doing so gives you full visibility into how the findings appear in Security Hub CSPM. It also helps
you understand the customer's experience with your security findings.

You use the [`BatchImportFindings`](../../1.0/APIReference/API_BatchImportFindings.md "../../1.0/APIReference/API_BatchImportFindings.md") API operation to send new and updated findings to
Security Hub CSPM.

Throughout the build of a Security Hub CSPM integration, AWS encourages you to keep your APN
Partner contacts informed about the progress of your integration. You can also ask your APN
Partner contacts for help with integration questions.

See [Guidelines for using the
BatchImportFindings API](guidelines-batchimportfindings.md "guidelines-batchimportfindings.md"). 7. You demonstrate the integration to the Security Hub CSPM product team. This integration must be
demonstrated using an account that the Security Hub CSPM team owns.

If they are comfortable with the integration, the Security Hub CSPM team gives approval to move forward
to list you as a provider. 8. You provide AWS with a final manifest for review. 9. The Security Hub CSPM team creates the provider integration in the Security Hub CSPM console. Customers can then
discover and enable the integration. 10. (Optional) You engage in additional marketing efforts to promote your Security Hub CSPM integration.
See [Go-to-market activities](go-to-market-activities.md "go-to-market-activities.md").

At a minimum, Security Hub CSPM recommends that you provide the following assets.

    * A demonstration video (3 minutes at most) of the working integration. The video is used
     for marketing purposes and is posted to the AWS YouTube channel.
    * A one-slide architecture diagram to add to the Security Hub CSPM first call slide deck.
