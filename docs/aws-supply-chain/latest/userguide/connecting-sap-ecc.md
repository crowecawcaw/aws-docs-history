# Connecting to SAP ECC 6.0

To extract your data from SAP ECC 6.0, follow the procedure below.

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose
   **Data Lake**.
2. On the **Data lake** page, choose **Add New Source**.

The **Select your supply chain data source** page appears. 3. Choose **SAP ECC**. 4. Under **SAP ECC Connection Details**, enter the
following:

    * **Connection name** – Enter a name for your
     connection. Connection names can only contain letters, numbers, and
     dashes.
    * **Connection description** – Enter a
     description for your connection.

5. Under **Amazon S3 Bucket Billing**, review the Amazon S3 billing
   information, and then select **Acknowledge**.
6. Choose **Next**.
7. Under **Data Mapping**, choose **Get
   started**.
8. ###### Note

The required fields are already mapped. Perform this step only if you want
to make specific changes to the default transformation recipe.

On the **Mapping Recipe** page, you can view the default
transformation recipe under **Field mappings**.

Choose **Add mapping** to map any additional destination
field. The **Required Destination Fields** are mandatory.
Choose **Destination field** to add an additional custom
destination field. 9. ###### Note

You can only use AWS Glue DataBrew to edit the recipes for transactional entities.
Use AWS Supply Chain to download your recipes, and edit them in DataBrew. Then upload
the recipes back into AWS Supply Chain. You can't use the AWS Supply Chain web application
to edit the transactional data fields in a recipe.

(Optional) Under **Recipe Actions**, you can do the
following:

    * **Download recipe file** - Select
     **Download** to edit your recipe files offline with
     DataBrew.
    * **Upload recipe file** - Choose
     **browse files**, or move (drag and drop) your
     edited recipe files. Select **Confirm upload** to
     upload the edited recipe file and modify your data field
     mappings.
    * **Reset to default recipe** - Select
     **Yes, reset my recipe** to remove all your custom
     mappings and revert to the default recipe recommended by
     AWS Supply Chain.

10. To edit your source field mappings and validate your transformation recipe,
    you can upload sample data. On the **Mapping Recipe** page,
    under **Upload sample data**, choose **browse
    files**, or move (drag and drop) files. The sample data file
    must contain the required parameters and include the source field
    names.
11. Choose **Accept all and continue**.
12. Under **Review and confirm**, you can view the data
    connection summary. To edit your data field mapping, choose **Go back to
    Data Mapping**.
13. To review the Amazon S3 paths where you must upload your SAP source data for
    ingestion, choose **Confirm and configure data ingestion**.
    Alternatively, you can choose **Confirm and configure data ingestion
    later**. You can view the data ingestion information anytime. From
    the AWS Supply Chain dashboard, select **Connections**. Select
    the connection dataflow that you want to ingest data, choose the vertical
    ellipsis, and select **Ingestion setup**.
14. If you're not using the Amazon S3 API to ingest data, create the Amazon S3 path manually
    on the Amazon S3 console. For more information about how to create paths, see
    [Uploading data to an Amazon S3 bucket](manually-uploading-data.md "manually-uploading-data.md").
15. Review the following table to map the AWS Supply Chain data entity with SAP
    source.

###### Important

On the **Amazon S3 path** page, you must upload the
parent entity before the child entity. You can first upload all the parent
entities and then upload all the child entities together.

| Data entity                                                                                                                                               | SAP source      | Hierarchy | Data entity action |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --------- | ------------------ | -------------------- | ------ | ------- |
| Company – [company](organization-company-entity.md "organization-company-entity.md")                                                                      | 0COMP_CODE_TEXT | Parent    | Replace            |
| Geography – [geography](organization-geography-entity.md "organization-geography-entity.md")                                                              | ADRC            | Parent    | Replace            |
| Inventory – [inv_level](inventory_mgmnt-inv-level-entity.md "inventory_mgmnt-inv-level-entity.md")                                                        | MARD            | Parent    | Update             |
| MCHB                                                                                                                                                      | Parent          | Update    |                    | VBBE                 | Child  | Update  |
| Inventory – [inv_policy](planning-inv-policy-entity.md "planning-inv-policy-entity.md")                                                                   | MARC            | Parent    | Replace            |
| 0MATERIAL_ATTR                                                                                                                                            | Child           | Update    |
| Outbound – [outbound_order_line](outbound-fulfillment-order-line-entity.md "outbound-fulfillment-order-line-entity.md")                                   | 2LIS_11_VAITM   | Parent    | Update             |
| 0BP_DEF_ADDRESS_ATTR                                                                                                                                      | Child           | Update    |                    | 0MATERIAL_ATTR       | Child  | Update  |
| 2LIS_11_VAHDR                                                                                                                                             | Child           | Update    |
| Outbound – [outbound_shipment](outbound-fulfillment-shipment-entity.md "outbound-fulfillment-shipment-entity.md")                                         | 2LIS_08TRTLP    | Parent    | Update             |
| 2LIS_08TRFKP                                                                                                                                              | Child           | Update    |                    | 2LIS_08TRTK          | Child  | Update  |
| 2LIS_12_VCITM                                                                                                                                             | Child           | Update    |
| Product – [product](product-product-entity.md "product-product-entity.md")                                                                                | 0MATERIAL_ATTR  | Parent    | Replace            |
| 0MATERIAL_TEXT                                                                                                                                            | Child           | Update    |
| Product – [product_hierarchy](product-hierarchy-entity.md "product-hierarchy-entity.md")                                                                  | T179            | Parent    | Replace            |
| Purchase order – [inbound_order](replenishment-inbound-order-entity.md "replenishment-inbound-order-entity.md")                                           | 2LIS_02_HDR     | Parent    | Update             |
| CDHDR                                                                                                                                                     | Child           | Update    |                    | EKKO                 | Child  | Update  |
| Purchase order – [inbound_order_line](replenishment-inbound-order-line-entity.md "replenishment-inbound-order-line-entity.md")                            | 2LIS_02_ITM     | Parent    | Update             |
| 0MATERIAL_ATTR                                                                                                                                            | Child           | Update    |                    | 2LIS_03_BF           | Child  | Update  |
| EKPO                                                                                                                                                      | Child           | Update    |                    | LIPS                 | Child  | Update  |
| LIKP                                                                                                                                                      | Child           | Update    |                    | INB-SHIPMENT         | Child  | Update  |
| Purchase order – [inbound_order_line_schedule](replenishment-inbound-order-line-schedule-entity.md "replenishment-inbound-order-line-schedule-entity.md") | 2LIS_02_SCL     | Parent    | Update             |
| 2LIS_02_SCN                                                                                                                                               | Child           | Update    |
| Production order – [inbound_order](replenishment-inbound-order-entity.md "replenishment-inbound-order-entity.md")                                         | 2LIS_04_P_MATNR | Parent    | Update             |
| Production order – [inbound_order_line](replenishment-inbound-order-line-entity.md "replenishment-inbound-order-line-entity.md")                          | 2LIS_04_P_MATNR | Parent    | Update             |
| 0CO_PC_ACT_05                                                                                                                                             | Child           | Update    |                    | 0MATERIAL_ATTR       | Child  | Update  |
| Reference – [reference_field](reference-fields-entity.md "reference-fields-entity.md")                                                                    | 0PURCH_ORG_TEXT | Parent    | Update             |
| MDRP_NODTT                                                                                                                                                | Parent          | Update    |                    | T005T                | Parent | Update  |
| T141T                                                                                                                                                     | Parent          | Update    |                    | T173T                | Parent | Update  |
| T179T                                                                                                                                                     | Parent          | Update    |                    | T370U                | Parent | Update  |
| T618T                                                                                                                                                     | Parent          | Update    |
| Shipment – [shipment](replenishment-shipment-entity.md "replenishment-shipment-entity.md")                                                                | INB-SHIPMENT    | Parent    | Replace            |
| EQUI                                                                                                                                                      | Parent          | Replace   |                    | LIKP                 | Parent | Replace |
| LIPS                                                                                                                                                      | Parent          | Replace   |                    | 0MATERIAL_TEXT       | Parent | Replace |
| 0MAT_VEND_ATTR                                                                                                                                            | Parent          | Replace   |                    | 0MATERIAL_ATTR       | Parent | Replace |
| EKPO                                                                                                                                                      | Parent          | Replace   |                    | T001W                | Parent | Replace |
| ADRC                                                                                                                                                      | Parent          | Replace   |                    | 0VENDOR_ATTR         | Parent | Replace |
| BUT021_FS                                                                                                                                                 | Parent          | Replace   |
| Site – [site](network-site-entity.md "network-site-entity.md")                                                                                            | T001W           | Parent    | Replace            |
| ADRC                                                                                                                                                      | Child           | Update    |                    | GEOLOC               | Child  | Update  |
| Trading partner – [trading_partner](organization-trading-partner-entity.md "organization-trading-partner-entity.md")                                      | 0BPARTNER_ATTR  | Parent    | Update             |
| 0BPARTNER_TEXT                                                                                                                                            | Child           | Update    |                    | 0VENDOR_ATTR         | Child  | Update  |
| 0CUSTOMER_ATTR                                                                                                                                            | Child           | Update    |                    | 0BP_DEF_ADDRESS_ATTR | Child  | Update  |
| Transfer order – [inbound_order_line](replenishment-inbound-order-line-entity.md "replenishment-inbound-order-line-entity.md")                            | 2LIS_03_BF      | Parent    | Update             |
| 0MATERIAL_ATTR                                                                                                                                            | Child           | Update    |
| Transportation – [transportation_lane](network-transporation-lane-entity.md "network-transporation-lane-entity.md")                                       | TVRO            | Parent    | Replace            |
| TVRAB                                                                                                                                                     | Child           | Update    |                    | VALW                 | Child  | Update  |
| Vendor management – [vendor_lead_time](vendor-management-lead-time-entity.md "vendor-management-lead-time-entity.md")                                     | EINA            | Parent    | Replace            |
| EINE                                                                                                                                                      | Child           | Update    |                    | 0MATERIAL_ATTR       | Child  | Update  |
| Vendor management – [vendor_product](vendor-management-product-entity.md "vendor-management-product-entity.md")                                           | EINA            | Parent    | Replace            |
| 0MATERIAL_ATTR                                                                                                                                            | Child           | Update    |
