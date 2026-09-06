

# Common Setup Issues
<a name="common-setup-issues"></a>

## Referential integrity errors: "product\_id values do not match any id in Product dataset"
<a name="common-setup-issues-referential-integrity-errors"></a>

 The most common cause is trailing whitespace in ID fields. Source systems that export from fixed-width databases often pad string fields with spaces. The product master may have clean IDs ("MAT604") while the order line file has padded IDs ("MAT604 "). The system does a strict string match, so these won't join. 

 **Fix:** Add TRIM() to all string ID fields in your data flow SQL transforms. Apply it to product\_id, ship\_from\_site\_id, customer\_tpartner\_id, and any other join key. Also check for quoting inconsistencies between files. When re-exporting CSVs, use QUOTE\_ALL to prevent type inference issues where numeric-looking IDs (e.g., "111613") get treated as integers in one file and strings in another. 

 **Prevention:** Always TRIM all ID fields in your SQL transforms as a default practice, even if you don't see the issue today. Source data can change between exports. 

## Products in order history missing from product master
<a name="common-setup-issues-products-missing-from-product-master"></a>

 Your order history will often contain products that aren't in the current product master (discontinued products, one-time items, test SKUs). The system will reject the entire order file if any product\_id doesn't have a matching product master record. 

 **Fix:** Either (a) create stub rows in the product master for missing products with minimal required fields (id, description, base\_uom), or (b) filter the order history to only include products present in the product master. Option (a) is preferred because it preserves demand history that may be useful for lineage and trend detection. 

## CSV parsing errors on product master upload
<a name="common-setup-issues-csv-parsing-errors"></a>

 Product descriptions containing commas, quotes, or special characters can break CSV parsing. You may see errors like "Expected 17 fields, saw 19" on specific rows. 

 **Fix:** Re-export the file with proper quoting (QUOTE\_ALL). Check the specific failing rows for embedded commas in description fields. 

## Data not appearing after upload
<a name="common-setup-issues-data-not-appearing-after-upload"></a>
+ Verify your file format hasn't changed (extension, column headers, encoding).
+ Check that file names and extensions match the expected pattern — renaming .csv to .csv000 or similar will break ingestion.
+ Allow up to 30 minutes for data ingestion to complete after upload.
+ If column headers change between loads (e.g., columns named by month/year), a pre-processing step is required before upload.

## PIV not updating after data refresh
<a name="common-setup-issues-piv-not-updating"></a>
+ PIV triggers approximately 15 minutes after ingestion completes and takes \~20-30 minutes to run.
+ End-to-end from data upload to fresh PIV: approximately 1–1.5 hours.
+ If PIV hasn't updated in 24\+ hours, contact support.

## Exception counts seem too high or too low
<a name="common-setup-issues-exception-counts"></a>
+ **Too high:** Threshold may be too loose, or a single product\+site may be generating multiple exceptions for different dates. Contact support to review rule configuration.
+ **Too low:** Threshold may be too restrictive, or required data (e.g., forecast, inventory levels) may be missing for some products.

 Spot-check a few products you know well and compare what the system shows vs your source system. 

## No financial impact showing on exceptions
<a name="common-setup-issues-no-financial-impact"></a>

 Financial impact requires unit cost to be populated in the product data. If cost is missing or zero for a product, no dollar value will display. Check with your support team on cost data coverage — a waterfall approach across multiple cost fields typically provides the best coverage. 