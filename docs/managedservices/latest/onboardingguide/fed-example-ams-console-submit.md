# Submitting the federation request to AMS

If this is your first account, work with your CSDM(s) and/or Cloud Architect(s) to
provide the metadata XML file for your identity provider.

If you are onboarding an additional account or Identity Provider and have access to
either the management account or the desired application account, follow these
steps.

1. Create a service request from the AMS console.

###### Note

    * If creating an identity provider for an application account, submit this
     request from either the application account itself or the
     management account.
    * If creating an identity provider for an AMS core account, submit this
     request from the management account.
    * If creating an identity provider for the management account, submit this
     request from the management account, or contact your CSDM for assistance.

In the service request, provide the details necessary to add the identity provider:

    * AccountId of the account where the new identity provider will be
     created.
    * Desired identity provider name, if not provided, the default will be
     **customer-saml**; typically, this must match the settings
     configured in your federation provider.
    * For existing accounts, include whether the new identity provider should be
     propagated to all existing console roles or provide a list of roles that should
     trust the new identity provider.
    * Attach the metadata XML file exported from your federation agent to the
     service request as a file attachment.

2. From the same account where you created the service request, create a new RFC
   using CT-ID ct-1e1xtak34nx76 (Management | Other | Other | Create) with the following
   information.
   - Title: "Onboard SAML IDP <Name> for Account <AccountId>".
   - AccountId of the account where the identity provider will be created.
   - Identity provider name.
   - For Existing Accounts: Whether the identity provider should be propagated to
     all existing console roles, or the list of roles which should trust the new
     identity provider.
   - Case ID of service request created in Step 1, where the metadata XML file is
     attached.
