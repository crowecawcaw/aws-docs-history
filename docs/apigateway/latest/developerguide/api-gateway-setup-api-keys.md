

# Set up API keys for REST APIs in API Gateway
<a name="api-gateway-setup-api-keys"></a>

To set up API keys, do the following:
+ Configure API methods to require an API key.
+ Create or import an API key for the API in a Region.

Before setting up API keys, you must have created an API and deployed it to a stage. After you create an API key value, it cannot be changed.

For instructions on how to create and deploy an API by using the API Gateway console, see [Develop REST APIs in API Gateway](rest-api-develop.md) and [Deploy REST APIs in API Gateway](how-to-deploy-api.md), respectively.

After you create an API key, you must associate it with a usage plan. For more information, see [Set up usage plans for REST APIs in API Gateway](api-gateway-create-usage-plans.md).

**Note**  
For best practices to consider, see [Best practices for API keys and usage plans](api-gateway-api-usage-plans.md#apigateway-usage-plans-best-practices).

**Topics**
+ [Require an API key on a method](#api-gateway-usage-plan-configure-apikey-on-method)
+ [Create an API key](#api-gateway-usage-plan-create-apikey)
+ [Import API keys](#api-gateway-usage-pan-import-apikey)

## Require an API key on a method
<a name="api-gateway-usage-plan-configure-apikey-on-method"></a>

The following procedure describes how to configure an API method to require an API key.

------
#### [ AWS Management Console ]

**To configure an API method to require an API key**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose a REST API.

1. In the API Gateway main navigation pane, choose **Resources**.

1. Under **Resources**, create a new method or choose an existing one.

1. On the **Method request** tab, under **Method request settings**, choose **Edit**.  
![Add an API key to a method](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/api-gateway-new-console-add-key-to-method.png)

1. Select **API key required**.

1. Choose **Save**.

1. Deploy or redeploy the API for the requirement to take effect.

If the **API key required** option is set to `false` and you don't execute the previous steps, any API key that's associated with an API stage isn't used for the method.

------
#### [ AWS CLI ]

The following [put-method](https://docs.aws.amazon.com/cli/latest/reference/apigateway/put-method.html) command creates a `PUT` method that requires an API key:

```
aws apigateway put-method \
    --rest-api-id 1234123412 \
    --resource-id a1b2c3 \
    --http-method PUT \
    --authorization-type "NONE" \
    --api-key-required
```

The following [update-method](https://docs.aws.amazon.com/cli/latest/reference/apigateway/update-method.html) command updates an existing method to require an API key:

```
aws apigateway update-method \
    --rest-api-id 1234123412 \
    --resource-id a1b2c3 \
    --http-method PUT \
    --patch-operations op="replace",path="/apiKeyRequired",value="true"
```

------
#### [ REST API ]

To require an API key on a method, do one of the following:
+ Call [`method:put`](https://docs.aws.amazon.com/apigateway/latest/api/API_PutMethod.html) to create a method. Set `apiKeyRequired` to `true` in the request payload.
+ Call [`method:update`](https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateMethod.html) to set `apiKeyRequired` to `true`.

------

## Create an API key
<a name="api-gateway-usage-plan-create-apikey"></a>

The following procedure shows how to create an API key. If you want to import your API key, skip this step.

------
#### [ AWS Management Console ]

**To create an API key**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose a REST API.

1. In the API Gateway main navigation pane, choose **API keys**.

1. Choose **Create API key**.  
![Create API keys for usage plans](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/api-gateway-new-console-usage-plan-keys-choose-create-api-key-from-actions-menu.png)

1. For **Name**, enter a name.

1. (Optional) For **Description**, enter a description.

1. For **API key**, choose **Auto generate** to have API Gateway generate the key value, or choose **Custom** to create your own key value.

1. Choose **Save**.

------
#### [ AWS CLI ]

The following [create-api-key](https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-api-key.html) command creates an API key:

```
 aws apigateway create-api-key \
    --name 'Dev API key' \
    --description 'API key for Devs' \
    --enabled
```

------
#### [ REST API ]

Call [`apikey:create`](https://docs.aws.amazon.com/apigateway/latest/api/API_CreateApiKey.html) to create an API key.

------

## Import API keys
<a name="api-gateway-usage-pan-import-apikey"></a>

The following procedure describes how to import API keys. If you already created an API key, skip this step.

------
#### [ AWS Management Console ]

**To import API keys**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose a REST API.

1. In the main navigation pane, choose **API keys**.

1. Choose the **Actions** dropdown menu, and then choose **Import API keys**. 

1. To load a comma-separated key file, choose **Choose file**. You can also enter the keys in the text editor. For information about the file format, see [API Gateway API key file format](api-key-file-format.md).

1. Choose **Fail on warnings** to stop the import when there's an error, or choose **Ignore warnings** to continue to import valid key entries when there's an warning.

1. Choose **Import** to import your API keys.

------
#### [ AWS CLI ]

The following [import-api-keys](https://docs.aws.amazon.com/cli/latest/reference/apigateway/import-api-keys.html) command imports an API key:

```
aws apigateway import-api-key \
    a--body fileb://keys.csv \
    --format csv
```

------
#### [ REST API ]

Call [`apikey:import`](https://docs.aws.amazon.com/apigateway/latest/api/API_ImportApiKeys.html) to import an API key from a file. For the file format, see [API Gateway API key file format](api-key-file-format.md).

------

You cannot change the value of the new API key. After you create your API, you configure a usage plan. For more information, see [Set up usage plans for REST APIs in API Gateway](api-gateway-create-usage-plans.md).