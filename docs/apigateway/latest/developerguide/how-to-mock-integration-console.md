# Enable mock integration using the API Gateway console

You must have a method available in API Gateway. Follow the instructions in [Tutorial: Create a REST API with an HTTP non-proxy integration](api-gateway-create-api-step-by-step.md "api-gateway-create-api-step-by-step.md").

1. Choose an API resource and choose **Create method**.

To create the method, do the following:

    1. For **Method type**, select a method.
    2. For **Integration type**, select **Mock**.
    3. Choose **Create method**.
    4. On the **Method request** tab, for **Method request settings**, choose **Edit**.
    5. Choose **URL query string parameters**. Choose **Add query string** and for **Name**, enter `scope`. This query
     parameter determines if the caller is internal or otherwise.
    6. Choose **Save**.

2. On the **Method
   response** tab, choose **Create response**, and then do the following:
   1. For **HTTP Status**, enter `500`.
   2. Choose **Save**.

3. On the **Integration request** tab, for **Integration request settings**, choose **Edit**.
4. Choose **Mapping templates**, and then do the following:
   1. Choose **Add mapping template**.
   2. For **Content type**, enter `application/json`.
   3. For **Template body**, enter the following:

   ```
   {
     #if( $input.params('scope') == "internal" )
       "statusCode": 200
     #else
       "statusCode": 500
     #end
   }
   ```

   4. Choose **Save**.

5. On the **Integration response** tab, for the **Default - Response** choose **Edit**.
6. Choose **Mapping templates**, and then do the following:
   1. For **Content type**, enter `application/json`.
   2. For **Template body**, enter the following:

   ```
   {
       "statusCode": 200,
       "message": "Go ahead without me"
   }
   ```

   3. Choose **Save**.

7. Choose **Create response**.

To create a 500 response, do the following:

    1. For **HTTP status regex**, enter `5\d{2}`.
    2. For
     **Method response status**, select
     `500`.
    3. Choose
     **Save**.
    4. For **5\d{2} - Response**, choose **Edit**.
    5. Choose **Mapping templates**, and then choose **Add mapping template**.
    6. For **Content type**, enter `application/json`.
    7. For **Template body**, enter the following:



    ```
    {
        "statusCode": 500,
        "message": "The invoked method is not supported on the API resource."
    }
    ```
    8. Choose **Save**.

8.  Choose the **Test** tab. You might need to choose the right arrow button to show the tab. To test your mock integration, do the following:

        1. Enter `scope=internal` under **Query strings**. Choose
         **Test**. The test result shows:



        ```

        **Request:** /?scope=internal
        Status: 200
        Latency: 26 ms
        **Response Body**

        {
          "statusCode": 200,
          "message": "Go ahead without me"
        }

        **Response Headers**

        {"Content-Type":"application/json"}


        ```
        2. Enter `scope=public` under `Query strings` or leave it blank.
         Choose **Test**. The test result shows:



        ```

        **Request:** /
        Status: 500
        Latency: 16 ms
        **Response Body**

        {
          "statusCode": 500,
          "message": "The invoked method is not supported on the API resource."
        }

        **Response Headers**

        {"Content-Type":"application/json"}


        ```

    You can also return headers in a mock integration response by first adding a header to
    the method response and then setting up a header mapping in the integration response. In
    fact, this is how the API Gateway console enables CORS support by returning CORS required
    headers.
