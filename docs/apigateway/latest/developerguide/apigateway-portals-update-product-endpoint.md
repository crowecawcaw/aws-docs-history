

# Update a product REST endpoint in API Gateway
<a name="apigateway-portals-update-product-endpoint"></a>

When you update a product REST endpoint, you can change all the settings of the product endpoint except for the path and method of a REST API and the stage it's deployed to. Any changes to your product endpoints are updated automatically, but you need to republish any portals that use your products to see the changes reflected in a portal.

## Update a product REST endpoint
<a name="apigateway-portals-update-product-endpoint-update"></a>

The following procedure shows how to update a product REST endpoint to overwrite the current API documentation with custom API reference documentation.

**To update a product REST endpoint**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. In the main navigation pane, choose **Portal products**.

1. Choose a product.

1. In the **Documentation** tab, under **API reference pages**, choose the name of a product REST endpoint, such as **/dogs - GET**.

1. For **Preview**, choose **Edit page**.

1. For **Documentation source**, turn on **Override the documentation**.

1. For **Display content**, choose **Override the existing content**.

   If you choose **Remove all content**, the content is removed from the page, but you can choose **Override the existing content** to access the documentation again.

1. In **Page body**, enter custom API reference documentation using [GitHub Flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

   This documentation will not propagate back to API Gateway.

1. Choose **Save changes**.

1. You must republish any portals that use this portal product for the changes to take effect.