# Manage Amazon Connect Voice ID domains

###### Note

End of support notice: On May 20, 2026, AWS will end support for Amazon Connect
Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the
Amazon Connect console, access Voice ID features on the Amazon Connect admin website or Contact Control Panel, or access Voice ID
resources. For more information, visit [Amazon Connect
Voice ID end of support](amazonconnect-voiceid-end-of-support.md "amazonconnect-voiceid-end-of-support.md").

Amazon Connect Voice ID provides APIs for you manage Voice ID domains. You can find
equivalents for Create, Describe, List, and Update in the AWS Console.

1. [CreateDomain](../../../voiceid/latest/APIReference/API_CreateDomain.md "../../../voiceid/latest/APIReference/API_CreateDomain.md"): To create a new Voice ID domain, use the
   `CreateDomain` Voice ID API. When the Voice ID domain is
   created, a default fraudster watchlist to hold your fraudsters is created at
   the same time.

Note the following guidelines when using the `CreateDomain`
API:

    * You can only invoke this for your account after you have
     acknowledged the BIPA Consent in the AWS console.
    * You must also specify the KMS key for the Voice ID domain at
     the time of creation.
    * After creating a Voice ID domain, use the [Amazon Connect
     association APIs](../APIReference.md "../APIReference.md") to associate it with an Amazon Connect
     instance.

2. [DeleteDomain](../../../voiceid/latest/APIReference/API_DeleteDomain.md "../../../voiceid/latest/APIReference/API_DeleteDomain.md"): To delete a Voice ID domain, you must invoke the
   `DeleteDomain` Voice ID API and provide the domain ID. If
   this domain was associated with an Amazon Connect instance, Voice ID API calls, and
   Voice ID flow blocks will return runtime error. Deleting a Voice ID domain
   deletes all stored customer data such as audio recordings, voiceprints and
   speaker identifiers, as well as fraudster lists that you managed.
3. [DescribeDomain](../../../voiceid/latest/APIReference/API_DescribeDomain.md "../../../voiceid/latest/APIReference/API_DescribeDomain.md"): Use this API to return the name, description
   and encryption configuration of an existing domain identified by its
   `DomainID`.
4. [ListDomains](../../../voiceid/latest/APIReference/API_ListDomains.md "../../../voiceid/latest/APIReference/API_ListDomains.md"): Use this API to list all your Voice ID domains
   owned by your account in the Region.
5. [UpdateDomain](../../../voiceid/latest/APIReference/API_UpdateDomain.md "../../../voiceid/latest/APIReference/API_UpdateDomain.md"): To update the name and encryption configuration
   for a domain, you can use the `UpdateDomain` Voice ID API. This
   API clobbers existing attributes, and you must provide both these fields.

When you change the KMS key associated with the Voice ID domain,
following the `UpdateDomain` call your domain's existing data
will be asynchronously re-encrypted under the new KMS key. You can check
status of this process from your domain's
`ServerSideEncryptionUpdateDetails` attribute using the
`DescribeDomain` API. While this update process is in
progress, you must retain your old KMS key in an accessible state,
otherwise this process may fail. After this process completes, the old
KMS key may be safely retired.
