# Enable try it for an API Gateway product REST endpoint in your portal

Use try it to let an API consumer invoke your product endpoint from your portal. When an API consumer uses try
it, they enter method request parameters and invoke your product endpoint. Then, API Gateway invokes your API over the public
internet and returns the response in the try it window. You can use a
custom product page to provide any additional information about required parameters to access your API.

API Gateway uses the following limits to protect your APIs:

- API Gateway only allows 3 requests per second to your API.
- API Gateway uses a built-in timeout limit of 29000 ms. Your actual API might have a higher timeout limit, but
  API Gateway does not apply this timeout when a customer uses try it.
- API Gateway limits the response payload to 6MB.

## Considerations

The following considerations might impact how you use try it:

- Try it is not supported when you preview a portal.
- Try it is not supported for the REST APIs with the following features:

      + Private APIs
      + APIs that use mutual TLS
      + APIs that use private or self signed SSL certificates

  As the portal owner you are responsible for communicating with your API consumers the reasoning of the why
  try it button isn't there for any REST APIs that aren't supported. API Gateway does not explain this for you.

## Enable try it for a product REST endpoint

The following procedure shows how to enable try it for a product endpoint.

To learn how to use try it in a portal, see [Use an API Gateway portal](apigateway-portals-use-portal.md "apigateway-portals-use-portal.md").

###### Enable try it for a product REST endpoint

1. In the main navigation pane, choose
   **Portal products**.
2. Choose a product.
3. In the **Documentation** tab, under **API reference pages**, choose the name of a product REST endpoint, such as
   **/dogs - GET**.
4. Choose **Edit page**.
5. To let customers invoke your API in your portal, select
   **Try it functionality**.
6. Choose **Save changes**.
7. You must republish any portals that use this portal product for the changes to take effect.
