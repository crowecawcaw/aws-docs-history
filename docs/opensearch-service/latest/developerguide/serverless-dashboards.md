# Accessing OpenSearch Dashboards

After you create a collection with the AWS Management Console, you can navigate to the collection's
OpenSearch Dashboards URL. You can find the Dashboards URL by choosing
**Collections** in the left navigation pane and selecting the
collection to open its details page. The URL takes the format
`https://dashboards.`us-east-1`.aoss.amazonaws.com/_login/?collectionId=`07tjusf2h91cunochc``.
Once you navigate to the URL, you'll automatically log into Dashboards.

If you already have the OpenSearch Dashboards URL available but aren't on the AWS Management Console,
calling the Dashboards URL from the browser will redirect to the console. Once you enter
your AWS credentials, you'll automatically log in to Dashboards. For information about
accessing collections for SAML, see [Accessing
OpenSearch Dashboards with SAML](serverless-saml.md#serverless-saml-dashboards "serverless-saml.md#serverless-saml-dashboards").

The OpenSearch Dashboards console timeout is one hour and isn't configurable.

###### Note

On May 10, 2023, OpenSearch introduced a common global endpoint for
OpenSearch Dashboards. You can now navigate to OpenSearch Dashboards in the browser with a URL
that takes the format
`https://dashboards.`us-east-1`.aoss.amazonaws.com/_login/?collectionId=`07tjusf2h91cunochc``.
 To ensure backward compatibility, we'll continue to support the existing collection
 specific OpenSearch Dashboards endpoints with the format
 `https://`07tjusf2h91cunochc`.`us-east-1`.aoss.amazonaws.com/\_dashboards`.
