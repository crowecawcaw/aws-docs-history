AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Create transfer tasks in File Transfer

Transfer tasks are used to specify the data sets to be transferred from the mainframe to
Amazon S3 and allow you to choose the code page conversion options.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md") and have created [Create data transfer endpoints for
File Transfer](filetransfer-data-transfer-endpoints.md "filetransfer-data-transfer-endpoints.md").

###### Topics

- [Create transfer tasks](#filetransfer-console-create-task "#filetransfer-console-create-task")
- [View transfer tasks](#filetransfer-console-view-task "#filetransfer-console-view-task")

## Create transfer tasks

To create transfer tasks in File Transfer, follow these steps in the AWS Mainframe Modernization console.

###### To create a transfer task

###### Important

You must have at least one data transfer endpoint to create new transfer
tasks.

1.  Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2.  In the AWS Region selector, choose the Region where you want to transfer
    files from your mainframe to an Amazon S3 bucket.
3.  On the **Transfer tasks** page, you can choose any data
    transfer endpoint to create transfer tasks.
4.  On the **Create transfer task** page, set up properties for
    your transfer task. If you have not created any transfer tasks previously, you
    can create your first one by choosing the **Create Transfer
    task** option.
    - On this page, enter the basic information of your transfer task,
      including the transfer task name, description, and secret key.

    ###### Note

        + Encrypt the secret using the KMS key defined with the
         data transfer endpoint. The secret should contain the
         mainframe credentials needed to access data sets on the
         mainframe using the `userId` and
         `password` keys. For more information, see
         the [AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md").
        + You must configure the secret key with the following
         resource-based policy so that AWS Mainframe Modernization service can access it to
         perform data transfer task.



        JSON





        ```
        `{
         "Version":"2012-10-17",
         "Statement" : [ {
         "Effect" : "Allow",
         "Principal" : {
         "Service" : "m2.amazonaws.com"
         },
         "Action" : [ "secretsmanager:GetSecretValue",
         "secretsmanager:DescribeSecret" ],
         "Resource" : "*"
         } ]
        }`

        ```

    ###### Note

    The current maximum supported dataset size for transfer is 90
    GB.
    - Next, select the target Amazon S3 bucket location where the target data
      sets from the mainframe will be transferred.
    - The previously chosen data transfer endpoint will be selected. You can
      also select another endpoint from the available endpoints.

5.  Choose **Next**.
6.  On the **Add data sets** page, in the **Transfer task configuration** section, you can choose to either
    configure your transfer task in binary mode or to convert and transfer your data
    sets.
    - **Transfer in binary mode** option allows
      you to transfer data sets by skipping code page conversions and
      retaining their Record Descriptor Word (RDW) bytes.
    - **Transfer and convert data sets** option
      allows you to transfer data sets by setting the source and target code
      pages for your data sets. You can see the available code pages for File Transfer
      on the [Supported source and target encodings in AWS Mainframe Modernization File Transfer](filetransfer-encodings.md "filetransfer-encodings.md") page.

7.  Enter your query in the **Search mainframe for data
    sets** to search the mainframe for data sets to be included in your
    transfer task. Choose **View data sets**.

The following wildcard symbols can be used as part of the data set search
criteria for mainframe:

    * A single asterisk (\*) as a qualifier (between periods or after the
     final period) matches a single qualifier in that position.
    * A single asterisk (\*) within a qualifier matches zero or more
     characters in that position.
    * A double asterisk (\*\*) as a qualifier (between periods or after the
     final period) matches zero or more qualifiers in that position.
    * A double asterisk (\*\*) within a qualifier is not a valid
     query.
    * A single percent sign (%) matches any single alphanumeric or national
     character in that position. You can use up to eight percent signs in
     each qualifier.

###### Note

We suggest always ending your search criteria with a period followed by a
double asterisk (.\*\*) and then refine the search further, if needed.

For more information on wildcard rules, see the [Filtering data set names](https://www.ibm.com/docs/en/zos/3.1.0?topic=processed-filtering-by-data-set-names "https://www.ibm.com/docs/en/zos/3.1.0?topic=processed-filtering-by-data-set-names") in the _IBM
documentation_. 8. These data sets will load under **Mainframe data
sets** section, where you can search or choose one or more data
sets you want to configure code page conversions for. These chosen data sets
will be displayed in the **Added data sets**
section. If no data sets are loaded, you need to revisit step 7.

###### Note

You can select data sets from multiple search queries and add them to your
transfer task. 9. In the **Added data sets** section, you will see
name, type, and volume name of your data sets.

###### Important

For **Transfer and convert data sets**
option, you need to manually enter the source code page and target code page
for each of your chosen data set. _Source code
page_ is the source data set format, and _target code page_ is the target data set format
used to convert the data sets and store them in the target Amazon S3
bucket. 10. After confirming the data sets in the **Added data
sets** section, (and source and target code pages for Transfer and
convert data sets option), choose **Next**. 11. On the **Review and create** page, you can review or edit information for your transfer task. 12. Then, choose **Create transfer task**.

###### Important

Choosing the **Create transfer task** button will start the data
transfer, which is billable per the [AWS Mainframe Modernization pricing](https://aws.amazon.com/mainframe-modernization/pricing/ "https://aws.amazon.com/mainframe-modernization/pricing/") page. This billing
is based on the amount of data (GB) transferred as measured by the data set
size.

## View transfer tasks

To view transfer tasks in File Transfer, you must follow these steps in the AWS Mainframe Modernization
console.

###### To view transfer tasks

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where you want to transfer
   files from your mainframe to an Amazon S3 bucket.
3. On the **Transfer tasks** page, select the data transfer
   endpoint to view your transfer tasks.
4. For endpoints that have pre-existing transfer tasks, these will be displayed
   under the **Transfer tasks** section. You can choose to view
   details of any transfer task from this list.
