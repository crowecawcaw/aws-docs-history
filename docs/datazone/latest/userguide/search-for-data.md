# Search for and view assets in the Amazon DataZone

catalog

Amazon DataZone provides a streamlined way to search for data. Any Amazon DataZone user with
permissions to access the data portal can search for assets in the Amazon DataZone catalog
and view asset names and the metadata assigned to them. You can take a closer look at an
asset by examining its details page.

###### Note

To view the actual data that an asset contains, you must first subscribe to the
asset and have your subscription request approved and access granted.

Search in Amazon DataZone (in new and existing domains) includes results based on keyword
and semantic matches. The search algorithm prioritizes keyword matches and then appends
those with semantic matches.

The semantic search functionality empowers users across different roles and functions
to more effectively discover, access, and leverage their organization's data assets,
leading to improved decision-making, collaboration, and overall data-driven
capabilities. With semantic search, keyword inputs produce synonym-based and
meaning-based search results in addition to simple keyword match results. For example,
with semantic search, if you type in 'flower' as your search input, a data asset with
the word 'rose' in its name is returned in search results. If you type in 'movie' as
your search input, a data asset with the word 'film' in its name is returned in search
results. If you type in 'football' as your search input, a data asset with the word
'soccer' in its name can be returned in search results.

With keyword search, you can input various keywords while searching for your
subscribed assets. For example, if you have an asset called `Catalog Sales
 Data`, it is returned in the search results if you input any of the following
keywords: `catalog_sales`, `Catalog Sales`,
`CatalogSales`, or `catalogsales`.

Amazon DataZone also enhances the search experience by enabling precise exact-match and
partial-match functionality for technical identifiers such as column and table names.
With this new capability, you can perform searches by enclosing your keywords in double
quotes (" "), ensuring results that match technical names exactly or partially. This
functionality builds upon the keyword and semantic search capabilities, which empower
you to discover assets by concepts and related terms. By adding a layer of precision for
technical identifiers, this enhancement enables you to manage large data catalogs with
complex technical naming conventions.

As you search through your data, you might need to locate specific technical assets to
support your use cases. With the ability to search for technical identifiers, you can
retrieve assets with accuracy, saving time and streamlining the discovery process. For
instance, a query like "customer_id" returns columns or tables with the exact
identifier, while a partial query such as "sales\_" can identify related assets like
sales_summary and sales_data_2024. This enhancement ensures data consumers can
efficiently find the assets they need, enhancing productivity.

###### To search for assets in the catalog

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. You can type the name of the asset that you are looking for in the search bar
   on the home page of the data portal.
3. To browse namespaces, choose **Catalog** from the top right
   of the page to open the catalog. The catalog provides a faceted search
   experience for you to find assets by searching on criteria such as
   , data owner, and glossary terms.
4. Enter your search term in one of the search boxes. After you run a search, you
   can apply various ﬁlters to narrow the results. The ﬁlters include
   asset type, source account, and the AWS Region to which the
   asset belongs.
5. To view details about a specific asset, choose the asset to open its details
   page. The details page includes the following information:
   - The asset name, data source (AWS Glue, Amazon Redshift, or Amazon S3), type (table,
     view, or S3 object), number of columns, and size.
   - A description of the asset.
   - The current published revision of the asset, the owner, whether
     approval is required for subscriptions, the namepace, and update
     history.
   - An **Overview** tab which includes glossary terms and
     metadata forms.
   - A **Schema** tab which displays the schema of the
     asset, including business and technical column names, data types, and
     business descriptions of the columns. The schema tab is visible only for
     tables and views (not for Amazon S3 objects).
   - A **Subscriptions** tab which includes a list of
     subscribers to the domain.
   - A **History** tab which includes a list of past
     revisions of the asset.
