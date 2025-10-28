# Creating an Amazon Q Business custom

plugin

###### Note

To validate accuracy before deploying to end users, we recommend creating a
Amazon Q Business test application to configure and test new features. To
create a new custom plugin, first ensure that you have a test application with the
same settings and configurations as your production application (the one deployed
for your end users). Using the console, configure a custom plugin in the test
application following the steps below. After you finish configuring your custom
plugin, launch a test web experience and login as an end user. Issue a number of
expected user prompts and confirm you are getting the expected results. If you are
not getting the expected results, return to the console page and modify the OpenAPI
specification to ensure it follows [best practices](plugins-api-schema-best-practices.md "plugins-api-schema-best-practices.md") for configuring OpenAPI
specifications. Repeat this process until you are satisfied with the test
application results and then replicate the same custom plugins settings in your
production application before you share it with your end users.

You use the [`CreatePlugin`](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") action to create an Amazon Q
custom plugin for your web experience chat. The following tabs provide a procedure for
the AWS Management Console and code examples for the AWS CLI.

**To create a custom plugin,** choose a tab based on your
access preference for Amazon Q.

Console
**To create a application-name plugin**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the Amazon Q Business console, in
   **Applications**, click on the name of your
   application from the list of applications.
3. From the left navigation menu, choose
   **Actions**, and then choose
   **Plugins**.
4. In **Plugins**, choose **Add
   plugin**.
5. In **Add plugins**, choose **Custom
   plugin**.
6. In **Custom plugin**, enter the following
   information:
   1. In **Name and description**, for
      **Plugin name** – A name for
      your Amazon Q plugin. The name can include hyphens (-) but
      not spaces and can have a maximum of 1000 alphanumeric
      characters.
   2. In **API schema**, for **API
      schema source**, choose from the following
      options:
      - **Select from Amazon S3** –
        Choose this to select an existing API schema from an
        Amazon S3 bucket. Your API schema must have an API
        description, structure, and parameters for your
        custom plugin. Then, enter the **Amazon S3
        URL** to your API schema.
      - **Define with in-line OpenAPI schema
        editor** – Choose this to write
        your custom plugin API schema in the inline OpenAPI
        schema editor in the Amazon Q console. A sample
        schema appears that you can edit. Then, you can
        choose to do the following:
        - Select the format for the schema, whether
          **JSON** or
          **YAML**.
        - To import an existing schema from S3 to
          edit, select **Import schema**,
          provide the S3 URL, and select
          **Import**.
        - To restore the schema to the original sample
          schema, select **Reset** and then
          confirm the message that appears by selecting
          **Reset** again.

   3. **Authentication** – Choose
      between **Authentication required** or
      **No authentication required**. If no
      authentication is required, there is no further action
      needed. If authentication is required, choose to
      **Create and add a new secret** or
      **Use an existing one**. Your secret
      must contain:
      1. **Secret name** – A name
         for your Secrets Manager secret.
      2. **Client ID** – The client
         ID you copied from your third-party
         application.
      3. **Client secret** – The
         client secret you copied from your third-party
         application.
      4. **OAuth callback URL** –
         The URL to which user needs to be redirected after
         authentication. If your deployed web url is
         `<q-endpoint>`, use
         `<q-endpoint>/oauth/callback` .
         Amazon Q Business will handle OAuth tokens
         in this URL. This callback URL needs to be
         allowlisted in your third-party application.
      5. In **Choose a method to authorize Amazon Q Business** – Choose to
         **Create and add a new service
         role** or **Use an existing
         service role**. Make sure your service
         role has the necessary permissions.

      The console will generate a **Service role
      name**.

7. **Tags – _optional_**
   – An optional tag to track your plugin.
8. Select **Add plugin** to add your plugin.

CLI
**To create a custom plugin**

```

aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type `CUSTOM` \
--auth-configuration basicAuthConfiguration="'{"noAuthConfiguration": {}}' \
--custom-plugin-configuration '{"description":"`description`, "apiSchemaType": "`OPEN_API_V3`", "apiSchema": {"s3": {"bucket": `s3_bucket_with_openapi_schema` "key":`s3_key_with_openapi_schema`}}}'"
```
