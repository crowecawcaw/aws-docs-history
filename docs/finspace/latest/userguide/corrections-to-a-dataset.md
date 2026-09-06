

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Corrections to a dataset
<a name="corrections-to-a-dataset"></a>

**Important**  
Amazon FinSpace Dataset Browser will be discontinued on {{March 26, 2025}}. Starting {{November 29, 2023}}, FinSpace will no longer accept the creation of new Dataset Browser environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/) will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/) or contact [AWS Support](https://aws.amazon.com/contact-us/) to assist with your transition.

A changeset can be ingested as a correction to an already created changeset. This action does not delete the prior ingested set but signifies that the replaced changeset will be used when a view is created if both changesets fall under the specified date and time of the view.

 **To create a changeset that is a replacement to an existing changeset** 

1. From the homepage, search for the dataset that you want to make corrections to.

1. Choose the dataset name to view the dataset details page.

1. Choose the **All Data Views** tab.

1. Under the **Dataset Update History** table, from the list of changesets identify the changeset to be replaced and then choose the corrections icon (![Two curved arrows forming a circular shape, indicating a refresh or sync operation.](http://docs.aws.amazon.com/finspace/latest/userguide/images/05-add-and-manage-data/corrections-icon.png)).

1. Choose **Choose CSV File** to select and upload a file from your desktop.

1. Once the file is uploaded, choose the input format for the ingested data from the following options:
   + **Delimiter** – Specifies the delimiter character. The default value is *Comma*.
   + **Escape Character** – Specifies a character to use for escaping. The default value is *None*.
   + **Quotes** – Specifies the character to use for quoting. The default value is *Double Quotes* (").
   + **Multiline Records** – Specifies whether a single record can span multiple lines. By default this option is disabled. Enable this option if you want any record to span multiple lines.
   + **Treat First Line As Header** – Specifies whether to treat the first line as a header. By default this option is disabled.
   + **Skip First Data Line** – Specifies whether to skip the first data line. By default this option is disabled.

1. Choose **Save**. The changeset is added to the **Dataset Update History** table with a **Pending** or **Running** status that changes to **Available** once the update is successful.