# Connecting Amazon Q Business to Amazon S3 using the console

The following procedure outlines how to connect Amazon Q Business to
Amazon S3 using the AWS Management Console.

###### Connecting Amazon Q to Amazon S3

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation menu, choose **Data
   sources**.
3. From the **Data sources** page, choose
   **Add data source**.
4. Then, on the **Add data sources** page, from
   **Data sources**, add the **Amazon S3** data source to your Amazon Q application.
5. Then, on the **Amazon S3** data source page, enter
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

7. **IAM role** – Choose an existing
   IAM role or create an IAM role to access your
   repository credentials and index content.

###### Note

IAM roles used for applications can't be used for data
sources. If you are unsure if an existing role is used for an application,
choose **Create a new role** to avoid errors. 8. **Sync scope**, enter the following information:

    1. **Enter the data source location** – The path
     to the Amazon S3 bucket where your data is stored. Select
     **Browse S3** to find and choose your
     bucket.


    ###### Note

    Your bucket must be in the same AWS Region as your Amazon Q Business index.
    2. **Maximum file size -
     *optional*** – You can
     specify the file size limit in MB for Amazon Q crawling. Amazon Q
     crawls only files within the defined size limit. The default file
     size is 50MB. The maximum file size limit is 10 GB. Files must be
     larger than 0 MB and no larger than 10 GB. You can go up to 10 GB
     (10240 MB) if you enable **Video files** in
     **Multi-media content** configuration, and up
     to 2 GB (2048 MB) if you enable **Audio files** in
     **Multi-media content configuration**.
    3. **Access control list configuration file location -
     *optional*** – The path to
     the location of a file containing a JSON structure that specifies access
     settings for the files stored in your S3 data source. Select
     **Browse S3** to locate your ACL file.


    For more information, see [ACL crawling](s3-user-management.md "s3-user-management.md").
    4. **Metadata files folder location -
     *optional*** – The path to
     the folder in which your metadata is stored. Select **Browse
     S3** to locate your metadata folder.
    5. **Filter patterns** – Add regex patterns to
     include or exclude documents from your index. All paths are relative to
     the data source location Amazon S3 bucket. You can add up to 100
     patterns.


    You can include and exclude documents using file names, file types,
     file paths, and glob patterns (patterns that can expand a wildcard
     pattern into a list of path names that match the given pattern).


    Examples of glob patterns include:




    	* `/myapp/config/*` – All files inside config
    	 directory
    	* `/**/*.png` – All .png files in all
    	 directories
    	* `/**/*.{png,ico,md}` – All .png, .ico, or
    	 .md files in all directories
    	* `/myapp/src/**/*.ts` – All .ts files inside
    	 src directory (and all its subdirectories)
    	* `**/!(*.module).ts` – All .ts files but not
    	 `.module.ts`
    	* For the following examples, assume that the Amazon S3 bucket is
    	 structured like this:



    	```

    	                            S3 bucket:
    	                              - file1.txt
    	                              - file2.txt
    	                              - file3.txt
    	                              - certificate
    	                                - certificate0.cer
    	                                - extra
    	                                  - certificate-e.cer
    	                                  - extra1
    	                                    - certificate-e-1.cer
    	                              - folder1
    	                                - file1-1.txt
    	                                - file1-2.txt
    	                                - file1-3.txt
    	                                - certificate
    	                                  - certificate1.cer
    	                              - folder2
    	                                - folder2-1
    	                                  - file2-1-1.txt
    	                                  - file2-1-2.txt
    	                                  - file2-1-3.txt
    	                                  - certificate
    	                                     - certificate2.cer

    	```
    	* \*\* matches any level \* – only matches one level
    	* \*\*/certificate/\*\*– matches certificate folder at any
    	 level except root level (ex.
    	 folder2/folder2-1/certificate)
    	* \*/certificate/\*\*– matches certificate folder only one
    	 level under root level. (ex. like folder1/certificate)
    	* certificate/\*\*– matches certificate folder at root
    	 level. (ex. certificate/ , certificate/extra/ ,
    	 certificate/extra/extra1)
    	* To exclude everything inside any "certificate" folder,
    	 regardless of its location, use the following:


    	certificate/\*\* + \*\*/certificate/\*\*
    	* Note that `/certificate/**` matches nothing
    6. **Multi-media content configuration – optional** –
     To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**. For more information, see [Extracting semantic meaning from embedded images and visuals](extracting-meaning-from-images.md "extracting-meaning-from-images.md").


    To extract audio transcriptions and video content, enable **Audio Files**. To extract video content, enable **Video files**. For more information, see [Extracting semantic meaning from audio and video Content](Audio-video-extraction.md "Audio-video-extraction.md").
    7. **Advanced settings**


    **Document deletion safeguard** - *optional*–To safeguard
     your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
     the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
     delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
     [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard").

9. **Sync mode**, choose how you want to update your index when
   your data source content changes. When you sync your data source with Amazon Q for the first time, all content is synced by default.
   - **Full sync** – Sync all content regardless of
     the previous sync status.
   - **New, modified, or deleted content sync** –
     Sync only new, modified, and deleted documents.

10. In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
11. **Configure VPC and security group –
    _optional_** – You can choose to use
    a VPC if your Amazon S3 bucket is not accessible through the public
    internet. If you so, you must add **Subnets** and **VPC
    security groups** as well.

###### Important

Make sure you have:

    * Configured your VPC according to the steps in [Gateway endpoints for Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md").
    * Chosen a private subnet in an Amazon Q
     [supported availability zone](connector-vpc-steps.md#connector-vpc-prerequisites-1 "connector-vpc-steps.md#connector-vpc-prerequisites-1").
    * Configured your security group to allow Amazon Q to
     access the Amazon S3 endpoint.For more information, see [Using Amazon VPC](connector-vpc.md "connector-vpc.md") and [Using Amazon VPC with Amazon S3](s3-vpc-xample-1.md "s3-vpc-xample-1.md").

If you choose to use VPC, enter the following information:

    1. **Subnets** – Select up to 6 repository
     subnets that define the subnets and IP ranges the repository instance
     uses in the selected VPC.
    2. **VPC security groups** – Choose up to 10
     security groups that allow access to your data source. Ensure that the
     security group allows incoming traffic from Amazon EC2 instances
     and devices outside your VPC. For databases, security group instances
     are required.

12. **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
13. **Field mappings** – A list of data source document
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

14. In **Data source details**, choose **Sync
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
