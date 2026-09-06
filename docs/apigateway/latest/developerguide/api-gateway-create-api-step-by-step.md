

# Tutorial: Create a REST API with an HTTP non-proxy integration
<a name="api-gateway-create-api-step-by-step"></a>

 In this tutorial, you create an API from scratch using the Amazon API Gateway console. You can think of the console as an API design studio and use it to scope the API features, to experiment with its behaviors, to build the API, and to deploy your API in stages. 

**Topics**
+ [Create an API with HTTP custom integration](#api-gateway-create-resource-and-methods)
+ [(Optional) Map request parameters](#api-gateway-create-resources-and-methods-next-steps)

## Create an API with HTTP custom integration
<a name="api-gateway-create-resource-and-methods"></a>

 This section walks you through the steps to create resources, expose methods on a resource, configure a method to achieve the desired API behaviors, and to test and deploy the API.

In this step, you create an empty API. In the following steps you create resources and methods to connect your API to the `http://petstore-demo-endpoint.execute-api.com/petstore/pets` endpoint, using a non-proxy HTTP integration. 

**To create an API**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. If this is your first time using API Gateway, you see a page that introduces you to the features of the service. Under **REST API**, choose **Build**. When the **Create Example API** popup appears, choose **OK**.

   If this is not your first time using API Gateway, choose **Create API**. Under **REST API**, choose **Build**.

1.  For **API name**, enter **HTTPNonProxyAPI**.

1. (Optional) For **Description**, enter a description.

1. Keep **API endpoint type** set to **Regional**.

1. For **IP address type**, select **IPv4**.

1. Choose **Create API**.

The **Resources** tree shows the root resource (`/`) without any methods. In this exercise, we will build the API with the HTTP custom integration of the PetStore website (http://petstore-demo-endpoint.execute-api.com/petstore/pets.) For illustration purposes, we will create a `/pets` resource as a child of the root and expose a GET method on this resource for a client to retrieve a list of available Pets items from the PetStore website.

**To create a /pets resource**

1. Choose **Create resource**.

1. Keep **Proxy resource** turned off.

1. Keep **Resource path** as `/`.

1. For **Resource name**, enter **pets**.

1. Keep **CORS (Cross Origin Resource Sharing)** turned off.

1. Choose **Create resource**.

In this step, you create a `GET` method on the **/pets** resource. The `GET` method is integrated with the `http://petstore-demo-endpoint.execute-api.com/petstore/pets` website. Other options for an API method include the following:
+ **POST**, primarily used to create child resources.
+ **PUT**, primarily used to update existing resources (and, although not recommended, can be used to create child resources).
+ **DELETE**, used to delete resources.
+ **PATCH**, used to update resources.
+ **HEAD**, primarily used in testing scenarios. It is the same as GET but does not return the resource representation.
+ **OPTIONS**, which can be used by callers to get information about available communication options for the target service.

 For the integration request's **HTTP method**, you must choose one supported by the backend. For `HTTP` or `Mock integration`, it makes sense that the method request and the integration request use the same HTTP verb. For other integration types the method request will likely use an HTTP verb different from the integration request. For example, to call a Lambda function, the integration request must use `POST` to invoke the function, whereas the method request may use any HTTP verb depending on the logic of the Lambda function. 

**To create a `GET` method on the **/pets** resource**

1. Select the **/pets** resource.

1. Choose **Create method**.

1. For **Method type**, select **GET**.

1. For **Integration type**, select **HTTP integration**.

1. Keep **HTTP proxy integration** turned off.

1. For **HTTP method**, select **GET**.

1. For **Endpoint URL**, enter **http://petstore-demo-endpoint.execute-api.com/petstore/pets**.

   The PetStore website allows you to retrieve a list of `Pet` items by the pet type, such as "Dog" or "Cat", on a given page.

1. For **Content handling**, select **Passthrough**.

1. Choose **URL query string parameters**.

   The PetStore website uses the `type` and `page` query string parameters to accept an input. You add query string parameters to the method request and map them into corresponding query string parameters of the integration request. 

1. To add the query string parameters, do the following:

   1. Choose **Add query string**.

   1. For **Name**, enter **type**

   1. Keep **Required** and **Caching** turned off.

   Repeat the previous steps to create an additional query string with the name **page**.

1. Choose **Create method**.

The client can now supply a pet type and a page number as query string parameters when submitting a request. These input parameters must be mapped into the integration's query string parameters to forward the input values to our PetStore website in the backend.

**To map input parameters to the Integration request**

1. On the **Integration request** tab, under **Integration request settings**, choose **Edit**.

1. Choose **URL query string parameters**, and then do the following: 

   1. Choose **Add query string parameter**.

   1. For **Name**, enter **type**.

   1. For **Mapped from**, enter **method.request.querystring.type**

   1. Keep **Caching** turned off. 

   1. Choose **Add query string parameter**.

   1. For **Name**, enter **page**.

   1. For **Mapped from**, enter **method.request.querystring.page**

   1. Keep **Caching** turned off. 

1. Choose **Save**.

**To test the API**

1. Choose the **Test** tab. You might need to choose the right arrow button to show the tab.

1. For **Query strings**, enter **type=Dog&page=2**.

1. Choose **Test**.

    The result is similar to the following:

      
![Test-invoke GET on pets method result](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/api-gateway-create-api-step-by-step-test-invoke-get-on-pets-result-new-console.png)

    Now that the test is successful, we can deploy the API to make it publicly available. 

1. Choose **Deploy API**.

1. For **Stage**, select **New stage**.

1. For **Stage name**, enter **Prod**.

1. (Optional) For **Description**, enter a description.

1. Choose **Deploy**.

1.  (Optional) Under **Stage details**, for **Invoke URL**, you can choose the copy icon to copy your API's invoke URL. You can use this with tools such as [Postman](https://www.postman.com) and [cURL](https://curl.se/) to test your API.

 If you use an SDK to create a client, you can call the methods exposed by the SDK to sign the request. For implementation details, see the [AWS SDK](https://aws.amazon.com/developer/tools/) of your choosing. 

**Note**  
 When changes are made to your API, you must redeploy the API to make the new or updated features available before invoking the request URL again. 

## (Optional) Map request parameters
<a name="api-gateway-create-resources-and-methods-next-steps"></a>

### Map request parameters for an API Gateway API
<a name="getting-started-mappings"></a>

 This tutorial shows how to create a path parameter of `{petId}` on the API's method request to specify an item ID, map it to the `{id}` path parameter in the integration request URL, and send the request to the HTTP endpoint.

**Note**  
 If you enter the incorrect case of a letter, such as lowercase letter instead of an uppercase letter, this will cause errors later in the walkthrough. 

#### Step 1: Create resources
<a name="getting-started-mappings-add-resources"></a>

In this step, you create a resource with a path parameter {petId}.

**To create the {petId} resource**

1. Select the **/pets** resource, and then choose **Create resource**.

1. Keep **Proxy resource** turned off.

1. For **Resource path**, select **/pets/**.

1. For **Resource name**, enter **{petId}**.

    Use the curly braces (`{ }`) around `petId` so that **/pets/{petId}** is displayed.

1. Keep **CORS (Cross Origin Resource Sharing)** turned off.

1. Choose **Create resource**.

#### Step 2: Create and test the methods
<a name="getting-started-mappings-set-methods"></a>

 In this step, you create a `GET` method with a `{petId}` path parameter. 

**To set up GET method**

1. Select the **/{petId}** resource, and then choose **Create method**.

1. For **Method type**, select **GET**.

1. For **Integration type**, select **HTTP integration**.

1. Keep **HTTP proxy integration** turned off.

1. For **HTTP method**, select **GET**.

1. For **Endpoint URL**, enter **http://petstore-demo-endpoint.execute-api.com/petstore/pets/{id}**

1. For **Content handling**, select **Passthrough**.

1. Keep the **Default timeout** turned on. 

1. Choose **Create method**.

Now you map the `{petId}` path parameter that you just created to the `{id}` path parameter in the HTTP endpoint URL of the integration request. The HTTP endpoint URL was **http://petstore-demo-endpoint.execute-api.com/petstore/pets/{id}**.

**To map the `{petId}` path parameter**

1. On the **Integration request** tab, under **Integration request settings**, choose **Edit**.

1. Choose **URL path parameters**.

1.  API Gateway creates a path parameter for the integration request named **petId**, however this path parameter isn't valid for the HTTP endpoint URL that you set as the backend integration. The HTTP endpoint uses `{id}` as the path parameter. For **Name**, delete **petId** and enter **id**.

   This maps the method request's path parameter of `petId` to the integration request's path parameter of `id`.

1. Choose **Save**.

Now you test the method.

**To test the method**

1. Choose the **Test** tab. You might need to choose the right arrow button to show the tab.

1. Under **Path** for **petId**, enter **4**.

1. Choose **Test**.

   If successful, **Response body** displays the following:

   ```
   {
     "id": 4,
     "type": "bird",
     "price": 999.99
   }
   ```

#### Step 3: Deploy the API
<a name="getting-started-mappings-deploy"></a>

In this step, you deploy the API so that you can begin calling it outside of the API Gateway console.

**To deploy the API**

1. Choose **Deploy API**.

1. For **Stage**, select **Prod**.

1. (Optional) For **Description**, enter a description.

1. Choose **Deploy**.

#### Step 4: Test the API
<a name="getting-started-mappings-test"></a>

In this step, you go outside of the API Gateway console and use your API to access the HTTP endpoint.

1. In the main navigation pane, choose **Stage**.

1. Under **Stage details**, choose the copy icon to copy your API's invoke URL.

   It should look something like this:

   ```
   https://{{my-api-id}}.execute-api.{{region-id}}.amazonaws.com/prod
   ```

1. Enter this URL in the address box of a new browser tab and append `/pets/4` to the URL before you submit your request.

1. The browser will return the following:

   ```
   {
     "id": 4,
     "type": "bird",
     "price": 999.99
   }
   ```

#### Next steps
<a name="api-gateway-create-resources-and-methods-next-steps"></a>

You can further customize your API by turning on request validation, transforming data, or creating custom gateway responses. 

To explore more ways to customize your API, see the following tutorials:
+ For more information about request validation, see [Set up basic request validation in API Gateway](api-gateway-request-validation-set-up.md).
+ For information about how to transform request and response payloads, see [Tutorial: Modify the integration request and response for integrations to AWS services](set-up-data-transformations-in-api-gateway.md).
+ For information about how to create custom gateway responses see, [Set up a gateway response for a REST API using the API Gateway console](set-up-gateway-response-using-the-console.md).