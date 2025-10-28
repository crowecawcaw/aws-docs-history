# Voice ID and Amazon Connect

Integration Association APIs

###### Note

End of support notice: On May 20, 2026, AWS will end support for Amazon Connect
Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the
Amazon Connect console, access Voice ID features on the Amazon Connect admin website or Contact Control Panel, or access Voice ID
resources. For more information, visit [Amazon Connect
Voice ID end of support](amazonconnect-voiceid-end-of-support.md "amazonconnect-voiceid-end-of-support.md").

You can use the following APIs to manage associations with Amazon Connect instances. You
can perform these operations on the AWS Console as well.

1. [CreateIntegrationAssociation](../APIReference/API_CreateIntegrationAssociation.md "../APIReference/API_CreateIntegrationAssociation.md"): To enable Voice ID on an Amazon Connect
   instance, you will need to associate a Voice ID domain with a Amazon Connect
   instance using a `CreateIntegrationAssociation` request. You can
   only associate one Voice ID domain to an Amazon Connect instance. If the instance is
   already associated with a domain, the API returns the following error:

`DuplicateResourceException` (409) - Request is trying to
created a duplicate resource.

###### Note

When you enable Voice ID for an Amazon Connect instance (by using either the
Amazon Connect console or the [CreateIntegrationAssociation](../APIReference/API_CreateIntegrationAssociation.md "../APIReference/API_CreateIntegrationAssociation.md") API), Amazon Connect creates a managed
Amazon EventBridge rule in your account. This rule is used to ingest Voice ID
events for creating contact records related to Voice ID. Additionally,
Amazon Connect adds [Voice ID permissions](connect-slr.md "connect-slr.md") to
the service-linked role for Amazon Connect. 2. [DeleteIntegrationAssociation](../APIReference/API_DeleteIntegrationAssociation.md "../APIReference/API_DeleteIntegrationAssociation.md"): To delete an existing association
between an Amazon Connect instance and a Voice ID domain, you will need to call the
`DeleteIntegrationAssociation` APIs along with the Amazon Connect
InstanceID and the `IntegrationAssociationID` returned by
`CreateIntegrationAssociation`. This is a required step if
you want to associate a different Voice ID domain to this Amazon Connect instance.
We do not recommend deleting associations in a production setup as it can
cause unpredictable behavior for Voice ID in your Amazon Connect instance. 3. [ListIntegrationAssociations](../APIReference/API_ListIntegrationAssociations.md "../APIReference/API_ListIntegrationAssociations.md"): To list all the associations
between Amazon Connect instance and Voice ID domains for your account in this
Region, you can invoke `ListIntegrationAssociations` API.
