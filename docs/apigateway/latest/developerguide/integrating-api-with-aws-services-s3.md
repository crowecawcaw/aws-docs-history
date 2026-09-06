

# Tutorial: Create a REST API as an Amazon S3 proxy
<a name="integrating-api-with-aws-services-s3"></a>

As an example to showcase using a REST API in API Gateway to proxy Amazon S3, this section describes how to create and configure a REST API to expose the following Amazon S3 operations: 
+ Expose GET on the API's root resource to [list all of the Amazon S3 buckets of a caller](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html).
+ Expose GET on a Folder resource to [view a list of all of the objects in an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html).
+ Expose GET on a Folder/Item resource to [view or download an object from an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html).

 You might want to import the sample API as an Amazon S3 proxy, as shown in [OpenAPI definitions of the sample API as an Amazon S3 proxy](api-as-s3-proxy-export-swagger-with-extensions.md). This sample contains more exposed methods. For instructions on how to import an API using the OpenAPI definition, see [Develop REST APIs using OpenAPI in API Gateway](api-gateway-import-api.md).

**Note**  
 To integrate your API Gateway API with Amazon S3, you must choose a region where both the API Gateway and Amazon S3 services are available. For region availability, see [Amazon API Gateway Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/apigateway.html). 

**Topics**
+ [Set up IAM permissions for the API to invoke Amazon S3 actions](#api-as-s3-proxy-iam-permissions)
+ [Create API resources to represent Amazon S3 resources](#api-as-s3-proxy-create-resources)
+ [Expose an API method to list the caller's Amazon S3 buckets](#api-root-get-as-s3-get-service)
+ [Expose API methods to access an Amazon S3 bucket](#api-folder-operations-as-s3-bucket-actions)
+ [Expose API methods to access an Amazon S3 object in a bucket](#api-items-in-folder-as-s3-objects-in-bucket)
+ [OpenAPI definitions of the sample API as an Amazon S3 proxy](api-as-s3-proxy-export-swagger-with-extensions.md)
+ [Call the API using a REST API client](api-as-s3-proxy-test-using-postman.md)

## Set up IAM permissions for the API to invoke Amazon S3 actions
<a name="api-as-s3-proxy-iam-permissions"></a>

 To allow the API to invoke Amazon S3 actions, you must have the appropriate IAM policies attached to an IAM role. In this step, you create a new IAM role.

**To create the AWS service proxy execution role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Roles**.

1. Choose **Create role**.

1.  Choose **AWS service** under **Select type of trusted entity**, and then select **API Gateway** and select **Allows API Gateway to push logs to CloudWatch Logs**.

1.  Choose **Next**, and then choose **Next**.

1. For **Role name**, enter **APIGatewayS3ProxyPolicy**, and then choose **Create role**.

1. In the **Roles** list, choose the role you just created. You may need to scroll or use the search bar to find the role.

1. For the selected role, select the **Add permissions** tab.

1. Choose **Attach policies** from the dropdown list.

1. In the search bar, enter **AmazonS3FullAccess** and choose **Add permissions**. 
**Note**  
This tutorial uses a managed policy for simplicity. As a best practice, you should create your own IAM policy to grant the minimum permissions required. 

1. Note the newly created **Role ARN**, you will use it later.

## Create API resources to represent Amazon S3 resources
<a name="api-as-s3-proxy-create-resources"></a>

You use the API's root (`/`) resource as the container of an authenticated caller's Amazon S3 buckets. You also create a `Folder` and `Item` resources to represent a particular Amazon S3 bucket and a particular Amazon S3 object, respectively. The folder name and object key will be specified, in the form of path parameters as part of a request URL, by the caller. 

**Note**  
When accessing objects whose object key includes `/` or any other special character, the character needs to be URL encoded. For example, `test/test.txt` should be encoded to `test%2Ftest.txt`.

**To create an API resource that exposes the Amazon S3 service features**

1.  In the same AWS Region you created your Amazon S3 bucket, create an API named **MyS3**. This API's root resource (**/**) represents the Amazon S3 service. In this step, you create two additional resources **/{folder}** and **/{item}**.

1. Choose **Create resource**.

1. Keep **Proxy resource** turned off. 

1. For **Resource path**, select `/`.

1. For **Resource name**, enter **{folder}**.

1. Keep **CORS (Cross Origin Resource Sharing)** unchecked.

1. Choose **Create resource**.

1. Select the **/{folder}** resource, and then choose **Create resource**.

1. Use the previous steps to create a child resource of **/{folder}** named **{item}**.

   Your final API should look similar to the following:

      
![Create an API in API Gateway as an Amazon S3 proxy](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/aws_proxy_s3_create_api-resources_new_console.png)

## Expose an API method to list the caller's Amazon S3 buckets
<a name="api-root-get-as-s3-get-service"></a>

Getting the list of Amazon S3 buckets of the caller involves invoking the [GET Service](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html) action on Amazon S3. On the API's root resource, (**/**), create the GET method. Configure the GET method to integrate with the Amazon S3, as follows. 

**To create and initialize the API's `GET /` method**

1. Select the **/** resource, and then choose **Create method**. 

1. For method type, select **GET**.

1. For **Integration type**, select **AWS service**.

1. For **AWS Region**, select the AWS Region where you created your Amazon S3 bucket. 

1. For **AWS service**, select **Amazon Simple Storage Service**.

1. Keep **AWS subdomain** blank.

1. For **HTTP method**, select **GET**.

1. For **Action type**, select **Use path override**.

   With path override, API Gateway forwards the client request to Amazon S3 as the corresponding [Amazon S3 REST API path-style request](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAPI.html), in which a Amazon S3 resource is expressed by the resource path of the `s3-host-name/bucket/key` pattern. API Gateway sets the `s3-host-name` and passes the client specified `bucket` and `key` from the client to Amazon S3.

1. For **Path override**, enter **/**.

1. For **Execution role**, enter the role ARN for **APIGatewayS3ProxyPolicy**.

1. Choose **Method request settings**.

   You use the method request settings to control who can call this method of your API.

1. For **Authorization**, from the dropdown menu, select `AWS_IAM`.

      
![Declare method response types](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/aws_proxy_s3_setup_method_request_authorization_new_console.png)

1. Choose **Create method**.

This setup integrates the frontend `GET https://{{your-api-host}}/{{stage}}/` request with the backend `GET https://{{your-s3-host}}/`.

 For your API to return successful responses and exceptions properly to the caller, you declare the 200, 400 and 500 responses in **Method response**. You use the default mapping for 200 responses so that backend responses of the status code not declared here will be returned to the caller as 200 ones. 

**To declare response types for the `GET /` method**

1.  On the **Method response** tab, under **Response 200**, choose **Edit**.

1. Choose **Add header** and do the following:

   1. For **Header name**, enter **Content-Type**.

   1. Choose **Add header**.

   Repeat these steps to create a **Timestamp** header and a **Content-Length** header.

1. Choose **Save**.

1. On the **Method response** tab, under **Method responses**, choose **Create response**.

1. For **HTTP status code**, enter **400**.

   You do not set any headers for this response.

1. Choose **Save**.

1. Repeat the following steps to create the 500 response.

   You do not set any headers for this response.

Because the successful integration response from Amazon S3 returns the bucket list as an XML payload and the default method response from API Gateway returns a JSON payload, you must map the backend Content-Type header parameter value to the frontend counterpart. Otherwise, the client will receive `application/json` for the content type when the response body is actually an XML string. The following procedure shows how to set this up. In addition, you also want to display to the client other header parameters, such as Date and Content-Length. 

**To set up response header mappings for the GET / method**

1. On the **Integration response** tab, under **Default - Response**, choose **Edit**.

1. For the **Content-Length** header, enter **integration.response.header.Content-Length** for the mapping value.

1. For the **Content-Type** header, enter **integration.response.header.Content-Type** for the mapping value.

1. For the **Timestamp** header, enter **integration.response.header.Date** for the mapping value.

1. Choose **Save**. The result should look similar to the following:

      
![Map integration response headers to method response headers](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/aws_proxy_s3_setup_integration_response_headers_new_console.png)

1. On the **Integration response** tab, under **Integration responses**, choose **Create response**.

1. For **HTTP status regex**, enter **4\\d{2}**. This maps all 4xx HTTP response status codes to the method response.

1. For **Method response status code**, select **400**.

1. Choose **Create**.

1. Repeat the following steps to create an integration response for the 500 method response. For **HTTP status regex**, enter **5\\d{2}**.

As a good practice, you can test the API you have configured so far.

**To test the `GET /` method**

1. Choose the **Test** tab. You might need to choose the right arrow button to show the tab.

1. Choose **Test**. The result should look like the following image:

      
![Test API root GET bucket result](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/aws_proxy_s3_test_root_get_result_new_console.png)

## Expose API methods to access an Amazon S3 bucket
<a name="api-folder-operations-as-s3-bucket-actions"></a>

To work with an Amazon S3 bucket, you expose the `GET` method on the /{folder} resource to list objects in a bucket. The instructions are similar to those described in [Expose an API method to list the caller's Amazon S3 buckets](#api-root-get-as-s3-get-service). For more methods, you can import the sample API here, [OpenAPI definitions of the sample API as an Amazon S3 proxy](api-as-s3-proxy-export-swagger-with-extensions.md).

**To expose the GET method on a folder resource**

1. Select the **/{folder}** resource, and then choose **Create method**. 

1. For method type, select **GET**.

1. For **Integration type**, select **AWS service**.

1. For **AWS Region**, select the AWS Region where you created your Amazon S3 bucket. 

1. For **AWS service**, select **Amazon Simple Storage Service**.

1. Keep **AWS subdomain** blank.

1. For **HTTP method**, select **GET**.

1. For **Action type**, select **Use path override**.

1. For **Path override**, enter **{bucket}**.

1. For **Execution role**, enter the role ARN for **APIGatewayS3ProxyPolicy**.

1. Choose **Create method**.

You set the `{folder}` path parameter in the Amazon S3 endpoint URL. You need to map the `{folder}` path parameter of the method request to the `{bucket}` path parameter of the integration request.

**To map `{folder}` to `{bucket}`**

1.  On the **Integration request** tab, under **Integration request settings**, choose **Edit**. 

1. Choose **URL path parameters**, and then choose **Add path parameter**.

1. For **Name**, enter **bucket**.

1. For **Mapped from**, enter **method.request.path.folder**.

1. Choose **Save**.

Now, you test your API. 

**To test the `/{folder} GET` method.**

1. Choose the **Test** tab. You might need to choose the right arrow button to show the tab.

1. Under **Path**, for **folder**, enter the name of your bucket.

1. Choose **Test**.

   The test result will contain a list of object in your bucket.

      
![Test the GET method to create an Amazon S3 bucket.](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/aws_proxy_s3_test_api_folder_get_new_console.png)

## Expose API methods to access an Amazon S3 object in a bucket
<a name="api-items-in-folder-as-s3-objects-in-bucket"></a>

Amazon S3 supports GET, DELETE, HEAD, OPTIONS, POST and PUT actions to access and manage objects in a given bucket. In this tutorial, you expose a `GET` method on the `{folder}/{item}` resource to get an image from a bucket. For more applications of the `{folder}/{item}` resource, see the sample API, [OpenAPI definitions of the sample API as an Amazon S3 proxy](api-as-s3-proxy-export-swagger-with-extensions.md).

**To expose the GET method on a item resource**

1. Select the **/{item}** resource, and then choose **Create method**. 

1. For method type, select **GET**.

1. For **Integration type**, select **AWS service**.

1. For **AWS Region**, select the AWS Region where you created your Amazon S3 bucket. 

1. For **AWS service**, select **Amazon Simple Storage Service**.

1. Keep **AWS subdomain** blank.

1. For **HTTP method**, select **GET**.

1. For **Action type**, select **Use path override**.

1. For **Path override**, enter **{bucket}/{object}**.

1. For **Execution role**, enter the role ARN for **APIGatewayS3ProxyPolicy**.

1. Choose **Create method**.

You set the `{folder}` and `{item}` path parameters in the Amazon S3 endpoint URL. You need to map the path parameter of the method request to the path parameter of the integration request.

In this step, you do the following:
+ Map the `{folder}` path parameter of the method request to the `{bucket}` path parameter of the integration request.
+ Map the `{item}` path parameter of the method request to the `{object}` path parameter of the integration request.

**To map `{folder}` to `{bucket}` and `{item}` to `{object}`**

1.  On the **Integration request** tab, under **Integration request settings**, choose **Edit**. 

1. Choose **URL path parameters**.

1. Choose **Add path parameter**.

1. For **Name**, enter **bucket**.

1. For **Mapped from**, enter **method.request.path.folder**.

1. Choose **Add path parameter**.

1. For **Name**, enter **object**.

1. For **Mapped from**, enter **method.request.path.item**.

1. Choose **Save**.

**To test the `/{folder}/{object} GET` method.**

1. Choose the **Test** tab. You might need to choose the right arrow button to show the tab.

1. Under **Path**, for **folder**, enter the name of your bucket.

1. Under **Path**, for **item**, enter the name of an item.

1. Choose **Test**.

   The response body will contain the contents of the item.

      
![Test the GET method to create an Amazon S3 bucket.](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/aws_proxy_s3_test_api_item_get_new_console.png)

   The request correctly returns the plain text of ("Hello world") as the content of the specified file (test.txt) in the given Amazon S3 bucket (amzn-s3-demo-bucket).

 To download or upload binary files, which in API Gateway is considered any thing other than utf-8 encoded JSON content, additional API settings are necessary. This is outlined as follows: 

**To download or upload binary files from S3**

1.  Register the media types of the affected file to the API's binaryMediaTypes. You can do this in the console: 

   1. Choose **API settings** for the API.

   1. Under **Binary media types**, choose **Manage media types**.

   1. Choose **Add binary media type**, and then enter the required media type, for example, `image/png`.

   1. Choose **Save changes** to save the setting.

1. Add the `Content-Type` (for upload) and/or `Accept` (for download) header to the method request to require the client to specify the required binary media type and map them to the integration request.

1. Set **Content Handling** to `Passthrough` in the integration request (for upload) and in a integration response (for download). Make sure that no mapping template is defined for the affected content type. For more information, see [Data transformations for REST APIs in API Gateway](rest-api-data-transformations.md).

The payload size limit is 10 MB. See [Quotas for configuring and running a REST API in API Gateway](api-gateway-execution-service-limits-table.md).

Make sure that files on Amazon S3 have the correct content types added as the files' metadata. For streamable media content, `Content-Disposition:inline` may also need to be added to the metadata.

For more information about the binary support in API Gateway, see [Content type conversions in API Gateway](api-gateway-payload-encodings-workflow.md).