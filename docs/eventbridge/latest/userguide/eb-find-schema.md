# Finding an AWS service event schema in Amazon EventBridge

EventBridge includes [schemas](eb-schema.md "eb-schema.md") for all AWS services that
generate events. You can find these schemas in the EventBridge console, or you can find them by
using the API action [`SearchSchemas`](../schema-reference/v1-registries-name-registryname-schemas-search.md "../schema-reference/v1-registries-name-registryname-schemas-search.md").

###### To find schemas for AWS services in the EventBridge console

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Schemas**.
3. On the **Schemas** page, select **AWS event schema
   registry**.
4. To find a schema, in **Search AWS event schemas**, enter a
   search term**.**

A search returns matches for both the name and contents of the available schemas,
and then displays which versions of the schema contain matches. 5. Open an event schema by selecting the name of the schema.
