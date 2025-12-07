# Use the Amazon Location Service console to authenticate

###### Note

To learn more about authentication, see [Authenticate with Amazon Location Service](access.md "access.md").

To use Amazon Location Service, a user must be granted access to the resources and APIs that make up
Amazon Location. By default, the Amazon Location APIs require authentication to use. You can use
either Amazon Cognito or API keys to provide authentication and authorization for anonymous
users.

In the [Create your first Amazon Location Maps and Places
application](first-app.md "first-app.md") tutorial, the application has anonymous usage,
which means your users aren't required to sign in. In the tutorial, you create API keys
for use in the sample application.

Follow the procedures below to create your first API key.

1. In the [**Amazon Location
   console**](https://console.aws.amazon.com/location "https://console.aws.amazon.com/location") and choose **API keys** from
   the left menu.
2. On the **API keys** page, choose **Create API
   key**.
3. On the **Create API key** page, fill in the
   following information:
   - **Name** – A name for your API key, such as
     `MyHelloWorldApp`.
   - **Description** – An optional description for
     your API key.
   - **Actions** – Specify the actions you want to
     authorize with this API key. You must select at least
     **geo-maps:Get\*** and
     **geo-places:Search\***.
   - **Expiration time** – Optionally, add an
     expiration date and time for your API key. For more information, see
     [API key best practices](using-apikeys.md#api-keys-best-practices "using-apikeys.md#api-keys-best-practices").
   - **Client restrictions** – Optionally, add one
     or more web domains or one or more Android or Apple apps where you can
     use the API key. For example, if the API key is to allow an application
     running on the website `example.com`, then you could put
     `*.example.com/` as an allowed referrer.
   - **Tags** – Optionally, add tags to the API
     key.

###### Important

We recommend that you protect your API key usage by setting either an
expiration time or a referrer, if not both. 4. Choose **Create API key** to create the API key. 5. On the detail page for the API key, you can see information about the API key
that you have created.

Choose **Show API key** and copy the key value to use later
in the [Create your first Amazon Location Maps and Places
application](first-app.md "first-app.md") tutorial. The key value will have the format
`v1.public.`a1b2c3d4...``.
