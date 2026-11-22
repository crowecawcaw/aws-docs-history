

# How to set up Global Resiliency for quick responses

Set up Global Resiliency for quick responses so that agents can search for and use the same quick responses in either Region, even if one Region becomes unavailable. This task is part of setting up Connect Customer Global Resiliency for your instance. For more information, see [Set up Connect Customer Global Resiliency](setup-connect-global-resiliency.md).

To set up replication, make sure that your quick responses knowledge base is associated with your instance by using an integration association. Connect Customer finds the quick responses of an instance through this association, so your quick responses don't replicate until the association exists.

Before you begin, make sure that your instance meets the [Connect Customer Global Resiliency requirements](connect-global-resiliency-requirements.md). You also need permissions to create a knowledge base, create an integration association, and replicate your instance.

**To set up Global Resiliency for quick responses**

1. In the source Region, create your quick responses knowledge base. To create it in the Connect Customer admin website (https://{{instance name}}.my.connect.aws/), choose **Get started** on the **Quick responses** page. To use a customer managed key, call the [CreateKnowledgeBase](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateKnowledgeBase.html) API instead, with a `knowledgeBaseType` of `QUICK_RESPONSES`. For instructions on creating the knowledge base, see [Set up a Connect Customer knowledge base to store quick responses](setup-knowledgebase.md).

1. In the source Region, make sure that the knowledge base has a replica key for the replica Region if you encrypt it with a customer managed key. For instructions on setting up the replica key, see [Using customer managed keys with your knowledge base](global-resiliency-quick-responses-cmk.md).

1. Make sure that the knowledge base is associated with your instance. If you created it with **Get started** in the Connect Customer admin website, the association already exists. Otherwise, associate it by using the [CreateIntegrationAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html) API, with an `IntegrationType` of `WISDOM_QUICK_RESPONSES`. An instance can have only one quick responses knowledge base association. If the call fails because your instance already has one, use the [ListIntegrationAssociations](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListIntegrationAssociations.html) API to see which knowledge base is associated.

1. In the source Region, replicate your instance. If your instance isn't replicated yet, call the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API, as described in [Create a replica of your existing Connect Customer instance](create-replica-connect-instance.md). If the call fails, see [Why a ReplicateInstance call fails](create-replica-connect-instance.md#why-replicateinstance-fails). If your instance is already replicated, creating the integration association starts replicating your quick responses.

1. In the replica Region, use the [ListIntegrationAssociations](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListIntegrationAssociations.html) API to confirm that the instance has an integration association with an `IntegrationType` of `WISDOM_QUICK_RESPONSES`.

1. In the replica Region, use the [ListQuickResponses](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ListQuickResponses.html) API to confirm that your quick responses are present, with the same IDs as in the source Region.

You now have Global Resiliency configured for quick responses, and agents can use the same quick responses in either Region. For information about how changes replicate, see [Replicating changes](global-resiliency-quick-responses-resources.md#global-resiliency-quick-responses-how-changes-replicate).