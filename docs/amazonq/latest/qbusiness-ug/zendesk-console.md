# Connecting Amazon Q Business to

Zendesk using the console

The following procedure outlines how to connect Amazon Q Business to
Zendesk using the AWS Management Console.

###### Connecting Amazon Q to Zendesk

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation menu, choose **Data
   sources**.
3. From the **Data sources** page, choose
   **Add data source**.
4. Then, on the **Add data sources** page, from
   **Data sources**, add the **Zendesk** data source to your Amazon Q application.
5. Then, on the **Zendesk** data source page, enter
   the following information:
6. **Name and description**, do the following:
   - For **Data source name** – Name your data
     source for easy tracking.

   ###### Note

   You can include hyphens (-) but
   not spaces. Maximum of 1,000 alphanumeric characters.
   - **Description –
     _optional_** – Add an optional
     description for your data source. This text is viewed only by Amazon Q Business administrators and can be edited later.

7. **Source** – Enter your **Zendesk
   URL**. For example,
   `https://{sub-domain}.zendesk.com/`.
8. **Authorization** – Amazon Q Business crawls ACL information by default to ensure responses are generated only from
   documents your end users have access to. If supported for your connector, you can manage ACLs by selecting **Enable ACLs** to enable ACLs or **Disable ACLs** to disable them.
   To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs disabled](setting-up.md#DisableAclOnDataSource "setting-up.md#DisableAclOnDataSource") for more details.

See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details. 9. Authentication for existing Zendesk customers: Enter a name for your secret, a client
ID, client secret, username, and password. 10. Authentication for new customers since 30 July 2024:

    1. Register the application with Zendesk and follow their procedure: [Using OAuth authentication with your application](https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application "https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application")
    2. Set Client kind to Confidential.
    3. For Redirect URL Enter the URL that Zendesk should use to grant access to the
     application. The URLs must be absolute and not relative. You can use localhost:
     `http://localhost` or `http://127.0.0.1`.
    4. Implement an OAuth authorization flow:




    	1. Zendesk supports the authorization code grant flow to get access tokens.
    	 (Other grant flows have been deprecated.)
    	2. The flow doesn't use refresh tokens. The access token doesn't expire.
    5. To get an authorization code, register users on the Zendesk authorization page:
     `https://{subdomain}.zendesk.com/oauth/authorizations/new`. Use the
     following parameters:




    	1. `response_type` - Zendesk returns an authorization code in the
    	 response, so specify code as the response type. For example:
    	 response\_type=code.
    	2. `redirect_url` - The URL, which can be local, that Zendesk should
    	 use to send the user's decision to grant access to your application. For example:
    	 `http://localhost` or `http://127.0.0.1`.
    	3. `client_id` - The unique identifier obtained after registering the
    	 application with Zendesk.
    	4. `scope` - A space-separated list of scopes that control access to
    	 the Zendesk resources.
    6. After this, Zendesk will ask for user approval. Once approved it will respond with
     an authorization code.
    7. Obtain an access token from Zendesk. Include the following parameters in the
     request:




    	1. `grant_type` - Specify `authorization_code` as the
    	 value.
    	2. `code` - Use the authorization code received from Zendesk after the
    	 user has been granted access.
    	3. `client_id` - Use the unique identifier specified in an OAuth
    	 client in the Support admin interface Admin > Channels > API > OAuth
    	 Clients.
    	4. `client_secret` - Use the secret specified in an OAuth client in
    	 the Support admin interface Admin > Channels > API > OAuth Clients).
    	5. `redirect_uri` - The URL, which can be local, that Zendesk should
    	 use to send the user's decision to grant access to your application. For example:
    	 `http://localhost` or `http://127.0.0.1`.
    	6. `scope` – A space-separated list of scopes that control access to
    	 the Zendesk resources.
     For example:



    ```
    `curl https://{subdomain}.zendesk.com/oauth/tokens \
     -H "Content-Type: application/json" \
     -d '{"grant_type": "authorization_code", "code": "{your_code}",
     "client_id": "{your_client_id}", "client_secret": "{your_client_secret}",
     "redirect_uri": "{your_redirect_url}", "scope": "read" }' \
     -X POST`
    ```
    8. Use the access token in API calls.

11. **Configure VPC and security group –
    _optional_** – Choose
    whether you want to use a VPC. If you do, enter the following
    information:
    1.  **Subnets** – Select up to 6
        repository subnets that define the subnets and IP ranges
        the repository instance uses in the selected VPC.
    2.  **VPC security groups** –
        Choose up to 10 security groups that allow access to
        your data source. Ensure that the security group allows
        incoming traffic from Amazon EC2 instances and
        devices outside your VPC. For databases, security group
        instances are required.For more information, see [VPC](connector-concepts.md#connector-vpc "connector-concepts.md#connector-vpc").

12. **IAM role** – Choose
    an existing IAM role or create an IAM role to access your repository credentials and
    index content.

###### Note

Creating a new service IAM role is recommended.

For more information, see [IAM role](zendesk-connector.md#zendesk-iam "zendesk-connector.md#zendesk-iam"). 13. **Sync scope** – Set the content that you want to sync. 14. For **Maximum file size** – Specify the file size limit in MBs
that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you
define. The default file size is 50MB. The maximum file size should be greater than 0MB
and less than or equal to 50MB. 15. **Additional configuration – optional** – Configure the
following settings:

    * **Change log** – Select to update your index instead of
     syncing all your files.
    * **Organization name** – Enter the Zendesk
     organization names to filter your sync.
    * **Sync start date** – The date from which you want to
     index your content.
    * **Regex patterns** – Regular expression patterns to
     include or exclude certain files. You can add up to 100 patterns.

16. **Advanced settings**

**Document deletion safeguard** - _optional_–To safeguard
your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
[Document deletion
safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard"). 17. In **Sync run schedule**, for
**Frequency** – Choose how often
Amazon Q will sync with your data
source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs"). 18. **Tags - _optional_** –
Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details. 19. **Field mappings** – A list of data source document
attributes to map to your index fields.

###### Note

Add or update the fields from the **Data
source details** page after you finish adding your data source.

You can choose from two types of fields:

    1. **Default** – Automatically created by
     Amazon Q on your behalf based on common fields in your data source. You
     can't edit these.
    2. **Custom** – Automatically created by
     Amazon Q on your behalf based on common fields in your data source. You
     can edit these. You can also create and add new custom fields.


    ###### Note

    Support for adding custom fields varies by connector. You
     won't see the **Add field** option if your
     connector doesn't support adding custom fields.For more information, see [Field mappings](connector-concepts.md#connector-field-mappings "connector-concepts.md#connector-field-mappings").

20. In **Data source details**, choose **Sync
    now** to allow Amazon Q to begin syncing (crawling and
    ingesting) data from your data source. When the sync job finishes, your data
    source is ready to use.

###### Note

View CloudWatch logs for your data source sync job by selecting **View
CloudWatch logs**. If you encounter a `Resource not found
 exception` error, wait and try again as logs may not be available
immediately.

You can also view a detailed document-level report by selecting
**View Report**. This report shows the status of each
document during the crawl, sync, and index stages, including any errors. If
the report is empty for an in-progress job, check back later as data is
emitted to the report as events occur during the sync process.

For more information, see [Troubleshooting data source
connectors](troubleshooting-data-sources.md#troubleshooting-data-sources-not-indexed "troubleshooting-data-sources.md#troubleshooting-data-sources-not-indexed").
