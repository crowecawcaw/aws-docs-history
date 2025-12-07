# Bulk actions

## Import opportunities

1. To upload opportunities in bulk, choose the drop-down list for **Bulk Actions** and select **Import Opportunities**. Partners are prompted with an overview of the key steps involved.
2. Choose **Start Import**. Users must complete the following Download and Prepare CSV file for import steps prior to uploading files:
   - **Always download the latest Excel template:** The date in which the template was last updated will be displayed for user transparency. Note: it is the user's responsibility to ensure the latest template version is being used for upload.
   - **New changes:** Check the new section "Products and Offerings" for guidance on how to attach products and offerings on opportunities. Download the dynamic sheet to check the APN Product Codes and Offering IDs to add on the bulk excel template.
   - **Prepare the Excel file to import:** Fill in all the information in the required fields highlighted in yellow. There are guided boxes that appear by clicking on the cell. They support you through the process in order to insert the correct information. Some of the cells have drop-down lists where you can review and choose required fields.
   - **Additional columns are required if you select certain options:** Additional columns are highlighted in the Excel file and listed in the table.

3. Choose **Next**.
4. When your Excel template is ready, choose **Select File**, select your saved .csv file, and then choose **Upload**. If you receive an error message while resolving any missing fields, refer to the accompanying tables in this section.
5. Choose **Import** to continue, and then wait for the confirmation message. If you receive an error message, review the section Errors in the bulk upload.
6. Choose **Done**, and close bulk import to return to the ACE Opportunity page.

### Opportunity fields

The following table describes the required fields for creating opportunities:

| Fields                                             | **Field name (required)**                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Description** |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Customer/company name                              | Name can be 80 characters maximum.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Industry vertical (pick-list value)                | Customer company name:<br>• Choose an industry vertical from the pick list. If you copy data from another file, paste it as text.<br>• Needs to map to valid selection. Refer to Values sheet containing mapping.<br>• Industry Other (required if industry vertical is Other) (column C).<br>• Required field when Industry Vertical selected is Other.<br>• 255 characters maximum.<br>• Government requires the following: Does opportunity belong to NatSec? (column D) |
| Country (pick-list value)                          | Required conditional fields:<br>• Needs to map to valid selection. Refer to the Values sheet for mapping.<br>• If you copy data from another file, paste it as text.<br>• State/province (pick-list value) (column F).<br>• When country is set to United States, state/province (column F) is required.                                                                                                                                                                    |
| Postal code                                        | • Field is specific to the end customer's billing postal code.<br>• 20 characters maximum.<br>• If the postal code starts with a zero, reformat the cell to as text.<br>• Attention to the formatting according to each country. Refer to the values tab and follow the postal code format of the country selected. If your country does not have a postal code leave it blank.                                                                                             |
| Customer website                                   | • Must be a valid domain.<br>• No social media pages are allowed.<br>• 255 characters maximum.<br>• If the domain ends in .co, add a forward slash (/) to the end (e.g., www.domain.co/).                                                                                                                                                                                                                                                                                   |
| Partner primary need from AWS                      | • Required conditional field.<br>• Must map to a valid selection. Refer to the Values sheet for mapping.<br>• If you select Co-Sell, then Sales Activities is required (column W).                                                                                                                                                                                                                                                                                          |
| Partner project title                              | Project title can be 60 characters maximum.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Customer business problem                          | Describe the customer's pain point or business problem. The description must be 20 characters minimum.                                                                                                                                                                                                                                                                                                                                                                      |
| Solution offered                                   | Describe the solution in 255 characters maximum. Enter the Offering ID for the solution. If you don't have an Offering ID, enter Other. If you enter Other, then Other Solution Offered is required (Column M).                                                                                                                                                                                                                                                             |
| Other Solution Offered                             | Describe the solution in 255 characters maximum.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Use case (pick-list value)                         | • Must map to valid use case. Refer to the Values sheet for mapping.<br>• If you copy data from another file, paste it as text.                                                                                                                                                                                                                                                                                                                                             |
| Estimated AWS monthly recurring revenue            | Use only numbers and no special formatting. Remember to count revenues in dollars and use US decimal notation (0,000.00).                                                                                                                                                                                                                                                                                                                                                   |
| Target close date                                  | • Future date must be in mm/dd/yyyy format. Update column formatting prior to and after saving the .csv file.<br>• When formatting the column, don't use asterisks in the date format because it will respond to changes based on a user's location and operating system. Download a new template, transfer only its data, and format the target-launch date column using the steps in the next section.                                                                    |
| Opportunity type                                   | • Select from the list of valid values only to specify if the project is a net new business, renewal or expansion.<br>• If the opportunity is a renewal or expansion, you can add the Parent Opportunity ID on Column Y                                                                                                                                                                                                                                                     |
| Delivery model (pick-list value)                   | • Needs to map to valid selection. Refer to the Values sheet for mapping.<br>• If you copy data from another file, paste it as text.                                                                                                                                                                                                                                                                                                                                        |
| Is opportunity from marketing activity? (required) | • Choose Yes or No. If you choose Yes, the following field is mandatory: Were marketing development funds used? (required if Is opportunity from marketing activity? is set to Yes) (Column U).<br>• If you choose Yes, the following fields are also optional:<br>+ AWS Marketing Campaign (Column AK).<br>+ Marketing Activity Channel (Column AL).<br>+ Marketing Activity Use-Case (Column AM).<br>• Must map to a valid selection. Refer to Values sheet for mapping.  |
| Sales activities                                   | Describes the customer's sales activities. This is required if Partner Primary Need from AWS (column I) is set to Co-Sell.                                                                                                                                                                                                                                                                                                                                                  |
| Competitive tracking (column AI)                   | If Competitive Tracking is set to Other, then Other Competitors (column AJ) is required.                                                                                                                                                                                                                                                                                                                                                                                    |

###### Secondary Required Fields

The Secondary Required Fields (highlighted black) are required:

1. If Industry Vertical is set to Other, the vertical must be specified in column C.
2. If Industry Vertical is set to Government, the following field is requested: Does opportunity belong to NatSec? (column D).
3. If Country is set to United States, then State/province is required (column F).
4. If Solution offered is set to Other, then Other Solution Offered is required (Column M).
5. If you Choose Yes for Is Opportunity from Marketing Activity, Was Marketing Development Funds Used? is required (column U).
6. If Partner Primary Need From AWS is set to Co-Sell, then specify Sales Activities in (column W).
7. If Competitive Tracking is set to Other, then you must specify it in column AJ.
8. If the Excel template contains a Values tab, you can use it to complete the additional columns.

#### Optional fields

The following table describes the optional fields for creating opportunities:

| Optional fields                                         | **Field name (optional)**                                                                                                                                                                                   | **Description** |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| AWS products (column X)                                 | Add the AWS product code from the Excel file in step 1. If you have multiple IDs, separate each one with a semicolon (;).                                                                                   |
| Customer phone                                          | Only numbers are allowed.                                                                                                                                                                                   |
| Customer email                                          | Must be a valid email address.                                                                                                                                                                              |
| AWS account ID                                          | Must be a 12-digit number. If the ID starts with zero, reformat the cell as text.                                                                                                                           |
| Additional comments                                     | 255 characters maximum.                                                                                                                                                                                     |
| State/province (pick-list value)                        | • Required conditional field.<br>• State is a required field when country is set to United States.<br>• If you copy data from another file, paste it as text.                                               |
| Street address and city                                 | 255 alphanumeric characters maximum (each).                                                                                                                                                                 |
| Competitive tracking (pick-list value)                  | • Required conditional fields.<br>• Must map to a valid use case. Refer to the Values sheet for mapping.<br>• If Other Competitors (column AI) is selected, column AJ is required (255 characters maximum). |
| Marketing development funded (pick-list value)          | Must map to a valid use case. Refer to the Values sheet for mapping.                                                                                                                                        |
| Primary sales contact, first name, last name, and title | The contact referenced in this field is included in opportunity-related email notifications.                                                                                                                |
| Primary contact phone                                   | Only numbers allowed.                                                                                                                                                                                       |
| Primary contact email                                   | Must be a valid email address.                                                                                                                                                                              |
| Partner CRM unique identifier                           | Ensure that the value is unique for each opportunity or leave this field blank so other users can save and submit records.                                                                                  |

## Export opportunities

The Bulk Export functionality allows a user to export up to 1,500 opportunities into a .csv file. AWS Opportunity referrals that have not been accepted will not appear in the export. To generate a file with your opportunities, choose **Export Opportunities** from the bulk-import dropdown list.

###### Note

You will export all filtered opportunities in the currently selected opportunities back to 2021.

## Update opportunities

The bulk-update function can export validated opportunities in bulk. This feature is designed to be scalable and to provide visibility of each engagement.

1. From the bulk-actions drop-down list, choose **Update Opportunities**.
2. Prepare the opportunities you want to update and download. Use filters to narrow the scope.
3. Choose **Next**.
4. Choose **Download Prepared XLS file** to generate and download your AWS opportunities. Acknowledge that there is a limit of 1,500 opportunities that can be downloaded.
5. Open the file in Excel, make any necessary changes, and save the file as a .csv.
6. Choose **Upload File**, choose your saved .csv file, and then choose **Update**. A popup window confirms the process status.
7. Confirm that you have prepared the .csv and are ready to upload it, and then choose **Next**.
8. Choose the file you prepared, and then choose **Upload CSV File**.
9. You will be redirected to the ACE Opportunity Page.
10. When the bulk update completes, you will receive a notification.

###### Note

To review your history of bulk updates and get detailed information, choose **Go to Bulk Updates**.
