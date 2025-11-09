AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime APIs

The AWS Blu Age Runtime uses several web-applications to expose REST endpoints, providing ways to interact with the modernized applications using REST clients (e.g. calling jobs using a scheduler).

The purpose of this document is to list available REST endpoints, giving details about:

- Their role
- The way to use them properly
  The endpoints listing is organized into categories, depending on the nature of the provided service and the web-application exposing the endpoints.

We assume that you already have a basic knowledge of using REST endpoints using dedicated tools such as [POSTMAN](https://www.postman.com/ "https://www.postman.com/"),
[Thunder Client](https://www.thunderclient.com/ "https://www.thunderclient.com/"),
[CURL](https://curl.se/ "https://curl.se/"), web browsers, etc ...) or writing your own piece of code to make an API call.

###### Topics

- [Available endpoints for user when building URLs](ba-endpoints-build-urls.md "ba-endpoints-build-urls.md")
- [Endpoints for Gapwalk application in AWS Blu Age](ba-endpoints-gapwalk.md "ba-endpoints-gapwalk.md")
- [Blusam application console REST endpoints](ba-endpoints-bac.md "ba-endpoints-bac.md")
- [Manage JICS application console in AWS Blu Age](ba-endpoints-jac.md "ba-endpoints-jac.md")
- [Data structures for AWS Blu Age user](ba-endpoints-apx.md "ba-endpoints-apx.md")
