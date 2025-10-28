# Listing records

The following procedure explains how to use the Amazon Route 53 console to list the records in a hosted zone.
For information about how to list records using the Route 53 API, see
[ListResourceRecordSets](../APIReference/API_ListResourceRecordSets.md "../APIReference/API_ListResourceRecordSets.md") in the _Amazon Route 53 API Reference_.

###### To list records

1.  Sign in to the AWS Management Console and open the Route 53 console at
    [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2.  In the navigation pane, choose **Hosted zones**.
3.  On the **Hosted Zones** page, choose the name of a hosted zone.
4.  To change the search mode, choose the gear icon on the upper right of the **Records**
    table. Choose one of:

        * **Automatic**


        In this mode, the service uses a filter based on a number of records. Full for less than
         2000 and fast for more than 2000 records.
        * **Full**


        In this mode, all the search filters are available, but the search performance might be
         slower.
        * **Fast**


        In this mode, some advanced features aren't available, but the search performance will be
         faster.

    To display only selected records, enter the applicable search criteria above the list of records. In the automatic mode the search behavior depends on whether
    the hosted zone contains up to 2,000 records or more than 2,000 records:

**Up to 2,000 records and full mode**

- To display the records that have specific values, enter a value in the search bar and press
  **Enter**. For example, to display the
  records that have an IP address beginning with
  **192.0**, enter that value in the
  **Search** field and press
  **Enter**.
- To display only the records that have the same DNS record type, select **Record type** in the dropdown list, and enter the record type.
- To display only alias records, select **Alias** in the dropdown list, and
  enter `Yes`.
- To display only weighted records, select **Routing policy** in the dropdown
  list, and enter `WEIGHTED`.

**More than 2,000 records and fast mode**

- You can search only on record names, not on record values. You also can't filter based on the record type, or
  on alias or weighted records.

To do this, put your cursor into the **Filter** textbox, select
**Properties** and then
**Record name**.

- For records that have three labels (three parts separated by dots), when you enter a value in the
  search field and press **Enter**, the Route 53 console automatically performs a wildcard search
  on the third label from the right in the record name. For example, suppose the hosted zone example.com contains
  100 records named record1.example.com through record100.example.com. (Record1 is the third label from the right.)
  Here's what happens when you search on the following values:
  - **record1** – The Route 53 console searches for
    **record1\*.example.com**, which returns **record1.example.com**,
    **record10.example.com** through **record19.example.com**, and
    **record100.example.com**.
  - **record1.example.com** – As in the preceding example, the console searches for
    **record1\*.example.com** and returns the same records.
  - **1** – The console searches for **1\*.example.com** and
    returns no records.
  - **example** – The console searches for **example\*.example.com**
    and returns no records.
  - **example.com** – In this example, the console doesn't perform a
    wildcard search. It returns all the records in the hosted zone.
  - **Automatic search mode** – When using this search mode, you must first provide a property, such as record name, to be able to search.

###### Note

If the third label from the right contains one or more hyphens (such as
`third-label.example.com`), and if you
search for the part of the third label immediately
before the hyphen (`third` in this example),
Route 53 won't return any records. Instead, either include
the hyphen (search for `third-`) or omit the
character immediately before the hyphen (search for
`third`).

- For records that have four or more labels, you must specify the exact name of the record. No wildcard searches
  are supported. For example, if the hosted zone includes a record named label4.record1.example.com, you can find that record
  only if you specify **label4.record1.example.com** in the search field.
