# Bulk upload instructions for Dedicated Hosts

You can use bulk upload to upload your machine configuration, operating system,
SQL server edition, quantity, vCPU, and memory in an excel file. Batch upload uploads
this excel file to the AWS Pricing Calculator. To do this, use the provided excel template
worksheet.

###### To download the excel worksheet template

1. Open AWS Pricing Calculator at [https://calculator.aws/#/](https://calculator.aws/#/ "https://calculator.aws/#/").
2. Choose **Create estimate**.
3. Do one of the following:
   - Under **Windows Server and SQL Server on Amazon EC2**, choose
     **Configure**.
   - Search for **Windows Server and SQL Server on Amazon EC2** from the **Find service** search bar.

4. On the **Configure Windows Server and SQL Server on Amazon EC2**
   page under the **Bulk upload instructions** sections, choose **Download template**.

For more information, see [Machine specifications](windows-workload-ec2.md#estimate-workload-configure-ec2 "windows-workload-ec2.md#estimate-workload-configure-ec2"). 5. Navigate to the downloaded file on your local machine.

###### Important

Don't remove any columns from the template.

Don't add any columns to the template.

Don't change the position of the template worksheet.

###### Tip

You can refer to the **Example** worksheet in the spreadsheet for an example data. 6. Choose **Upload file**. 7. Under the **Machine specifications** table, see the **Status** column to confirm if your template was uploaded correctly.

    * **Accepted** - The data that you entered is in
     the correct format. The data can be used for providing
     recommendations.
    * **Declined** - The data format isn't valid. You
     can see the upload fail reason from the same column. After you correct
     your file, upload again using the previous steps.


    If the declined fail reasons aren't addressed, these rows aren't
     included for recommendations on dedicated Hosts in the **Review
     dedicated hosts** table.

8. Use the Review dedicated hosts section to see details such as host family, host description,
   instances, license count, and used capacity. For more information, see [Review dedicated hosts](windows-workload-ec2.md#estimate-dedicatedhost-ec2 "windows-workload-ec2.md#estimate-dedicatedhost-ec2").
9. Use the Dedicated Host costs section to see details for your workload.

The costs table provides an itemized breakdown of the dedicated hosts with
hourly cost, monthly cost per unit, and cost for the first twelve months
included. All costs are shown in USD currency. 10. Use the **License(s) summary** section to clarify the list of licenses that
you need to bring to AWS for the recommended dedicated hosts. 11. Choose **Save and add service** to save your estimate prices, and add additional services to the AWS Pricing Calculator.
