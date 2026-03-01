# Connecting Amazon Q Business to Web Crawler using the console

The following procedure outlines how to connect Amazon Q Business to
Web Crawler using the AWS Management Console.

###### Note

Before you begin adding your data source, make sure you've created an Amazon Q Business application, and added an index and retriever to it.

###### Connecting Amazon Q to Web Crawler

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation menu, choose **Data
   sources**.
3. From the **Data sources** page, choose
   **Add data source**.
4. Then, on the **Add data sources** page, from
   **Data sources**, add the **Web Crawler** data source to your Amazon Q application.
5. Then, on the **Web Crawler** data source page, enter
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

7. In **Source** choose from the following options:
   - **Source URLs** – Add up to 10 seed/starting
     point URLs of the websites you want to crawl. You can also include
     website subdomains.
   - **Source sitemaps** – Add up to 3 sitemap URLs
     of the websites you want to crawl.
   - **Source URLs file** – Add up to 100
     seed/starting point URLs listed in a text file in Amazon S3.
     Each URL should be on a separate line in the text file.
   - **Source sitemaps file** – Add up to 3 sitemap
     XML files stored in Amazon S3. You can also zip the XML
     files.

###### Note

If you choose to use a text file that includes a list of up to 100 seed
URLs or to use a sitemap XML file, you specify the path to the Amazon S3 bucket where your file is stored.

You can also combine multiple sitemap XML files into a .zip file.
Otherwise, you can manually enter up to 10 seed or starting point URLs, and
up to three sitemap URLs.

###### Note

If you want to crawl a sitemap, check that the base or root URL is the
same as the URLs listed on your sitemap page. For example, if your sitemap
URL is
*https://example.com/sitemap-page.html*,
the URLs listed on this sitemap page should also use the base URL
"https://example.com/".

###### Note

If you want to later edit your data source to change your seed URLs with
authentication to sitemaps, you must create a new data source.

Amazon Q configures the data source using the seed URLs
endpoint information in the Secrets Manager secret for authentication.
Therefore, Amazon Q can't reconfigure the data source when
changing to sitemaps. 8. In **Authentication**, choose the type of authentication you
want to use and enter the following information in your AWS
Secrets Manager secret:

    * **No authentication** – Choose to crawl a
     public website without any authentication.
    * **Basic authentication** – Enter a name for
     the secret, and the username and password you use to access the website
     you want to crawl.
    * **NTLM/Kerberos authentication** – Enter a
     name for the secret, and the username and password you use to access the
     website you want to crawl. NTLM authentication protocol includes
     password hashing, and Kerberos authentication protocol includes password
     encryption.
    * **Form authentication** – Enter a name for the
     secret, and the username and password you use to access the website you
     want to crawl. Also add the following values:




    	+ **User name field Xpath** – Enter the
    	 XPath for your user name field. For example,
    	 `//input[@id='username']`.
    	+ **Password field Xpath** – Enter the
    	 XPath for your password field. For example,
    	 `//input[@id='password']`.
    	+ **User name button Xpath –
    	 *Optional*** –
    	 Provide the XPath for the button associated with the username
    	 input field, typically found on a login page. For example,
    	 `//button[@id='login-submit']`. This XPath helps
    	 the automation script identify and interact with the button to
    	 proceed with the login process. You can find this XPath using
    	 your browser’s developer tools.
    	+ **Password button Xpath** – Provide
    	 the XPath for the button associated with the password input
    	 field, typically used to submit the login form. For example,
    	 `//button[@id='login-submit']`. This XPath is
    	 essential for automating the interaction with the button after
    	 the password has been entered. You can find this XPath using
    	 your browser’s developer tools.
    ###### Note

    You can find the XPaths (XML Path Language) of elements using your
     web browser's developer tools. XPaths usually follow this format:
     `//tagname[@Attribute='Value']`. To learn how to
     retrieve XPaths, see [Retrieving XPaths (XML Path Language) for
     Web Crawler](webcrawler-retrieving-credentials.md "webcrawler-retrieving-credentials.md").
    * **SAML authentication** – Enter a name for the
     secret, and the username and password you use to access the website you
     want to crawl. Also add the following values:




    	+ **User name field Xpath** – Enter the
    	 XPath for your user name field. For example,
    	 `//input[@id='username']`.
    	+ **Password field Xpath** – Enter the
    	 XPath for your password field. For example,
    	 `//input[@id='password']`.
    	+ **User name button Xpath –
    	 *Optional*** –
    	 Provide the XPath for the button associated with the username
    	 input field, typically found on a login page. For example,
    	 `//button[@id='login-submit']`. This XPath helps
    	 the automation script identify and interact with the button to
    	 proceed with the login process. You can find this XPath using
    	 your browser’s developer tools.
    	+ **Password button Xpath** – Provide
    	 the XPath for the button associated with the password input
    	 field, typically used to submit the login form. For example,
    	 `//button[@id='login-submit']`. This XPath is
    	 essential for automating the interaction with the button after
    	 the password has been entered. You can find this XPath using
    	 your browser’s developer tools.
    ###### Note

    You can find the XPaths (XML Path Language) of elements using your
     web browser's developer tools. XPaths usually follow this format:
     `//tagname[@Attribute='Value']`. To learn how to
     retrieve XPaths, see [Retrieving XPaths (XML Path Language) for
     Web Crawler](webcrawler-retrieving-credentials.md "webcrawler-retrieving-credentials.md").

9. **Web proxy – _optional_** –
   Enter the host name and the port number of the proxy server that you want to use
   to connect to internal websites. For example, the host name of
   *https://a.example.com/page1.html* is
   "a.example.com" and the port number is 443, the standard port
   for HTTPS. If web proxy credentials are required to connect to a website host,
   you can create an AWS Secrets Manager secret that stores the following
   credentials: the username and password required for the web proxy to log into
   the host URL.
10. **Configure VPC and security group –
    _optional_** – Choose
    whether you want to use a VPC. If you do, enter the following
    information:
    1. **Subnets** – Select up to 6
       repository subnets that define the subnets and IP ranges
       the repository instance uses in the selected VPC.
    2. **VPC security groups** –
       Choose up to 10 security groups that allow access to
       your data source. Ensure that the security group allows
       incoming traffic from Amazon EC2 instances and
       devices outside your VPC. For databases, security group
       instances are required.For more information, see [VPC](connector-concepts.md#connector-vpc "connector-concepts.md#connector-vpc").

11. **IAM role** – Choose
    an existing IAM role or create an IAM role to access your repository credentials and
    index content.

###### Note

Creating a new service IAM role is recommended.

For more information, see [IAM role](webcrawler-connector.md#webcrawler-iam "webcrawler-connector.md#webcrawler-iam"). 12. In **Sync scope**, enter the following information:

    1. **Sync domain range** – Choose whether to sync
     website domains with subdomains only, or also crawl other domains that
     the webpages link to (**Sync everything**). By default,
     Amazon Q only syncs the domains of the websites that you
     want to crawl.
    2. For **Maximum file size** – Specify the file
     size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only
     the files within the size limit you define. The default file size is
     50MB. The maximum file size should be greater than 0MB and less than or
     equal to 50MB.
    3. In **Additional configuration –
     *optional*** – Configure the
     following settings:




    	* **Scope settings**, choose from the
    	 following:




    		+ **Crawl depth** – The depth,
    		 or number, of levels from the seed level to crawl. For
    		 example, the seed URL page is depth 0 and any hyperlinks
    		 on this page that are also crawled are depth 1.
    		+ **Maximum links per page** –
    		 The maximum number of URLs on a single webpage to
    		 crawl.
    		+ **Maximum throttling** – The
    		 maximum number of URLs crawled per website host per
    		 minute.
    	* **Include files that web pages link to**
    	 – Select this option to allow Amazon Q Business to
    	 crawl and index files that are linked from webpages.
    	* **Crawl URL patterns** – Add regular
    	 expression patterns to specify which URLs should be included or
    	 excluded during the crawling process. This allows you to control
    	 which pages on a website are crawled and which hyperlinks on
    	 those pages are indexed.
    	* **URL pattern to index** – Add regular
    	 expression patterns to define which URLs or files should be
    	 included or excluded from indexing. This helps you focus the
    	 indexing process on specific URLs or files, ensuring that only
    	 the desired content is indexed.
    4. **Multi-media content configuration – optional** –
     To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**.


    To extract audio transcriptions and video content, enable processing for the following file types:
    5. **Advanced settings**


    **Document deletion safeguard** - *optional*–To safeguard
     your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
     the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
     delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
     [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard").

13. In **Sync mode**, choose how you want to update your index
    when your data source content changes. When you sync your data source with
    Amazon Q for the first time, all content is synced by
    default.
    - **Full sync** – Sync all content regardless of
      the previous sync status.
    - **New, modified, or deleted content sync** –
      Sync only new, modified, and deleted documents.

14. In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
15. **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
16. **Field mappings** – A list of data source document
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

17. In **Data source details**, choose **Sync
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
