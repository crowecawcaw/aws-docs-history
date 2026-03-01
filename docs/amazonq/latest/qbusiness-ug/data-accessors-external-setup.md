# Completing the process to add a data accessor

After you grant a software provider (ISV) data accessor permissions, you'll need to
provide AWS or the ISV with the following configuration parameters. They will reach
out to you to source these configuration parameters. These values are required inputs
when the ISV uses the `SearchRelevantContent` API operation to perform
cross-account access of the data from your Amazon Q index.

###### Topics

- [Using the AWS Management Console](#data-accessors-completing-process-console "#data-accessors-completing-process-console")
- [Using the AWS CLI;](#data-accessors-completing-process-cli "#data-accessors-completing-process-cli")
  These parameters are all easily accessed from the AWS Management Console:

1. Amazon Q Business application ID — This is the unique identifier of the Amazon Q Business
   application environment. It tells the ISV what Amazon Q application environment is associated with the
   Amazon Q index.
2. The Amazon Q Business application Region — This is the AWS Region where the
   Amazon Q Business application environment is created.
3. Amazon Q Business retriever ID — This is the unique identifier for the retriever. The
   retriever gets the data from the Amazon Q index configured by the Amazon Q
   customer.
4. Data accessor application ARN — This is the ISV Amazon Resource Name (ARN). It
   is used to identify the ISV when it is accessing a customer's Amazon Q
   index.
5. The Region for the Identity and Access Management (IAM) Identity Center (IDC)
   instance — This is the AWS Region where the IDC instance of the customer has
   been created.
   The ISV can then begin retrieving content from the Amazon Q index by calling the
   `SearchRelevantContent` API. The `SearchRelevantContent` API
   follows Amazon Q Business access control standards by only retrieving data that the customer's
   end users have been given access to.

## Using the AWS Management Console

To access these variables in the Amazon Q Business console:

1. Sign in to the AWS Management Console and choose the **Amazon Q Business**
   console.
2. Choose **Applications**, then select the name of your
   application environment from the list.
3. In the **Application details** page, you will see the
   **Application id** on this page and the application environment
   **Region** on the top right corner of the console top
   navigation bar.
4. From the left navigation, choose **Data sources**.
5. In the **Data sources** page, you will see the
   **Retriever id** on this page.
6. From the left navigation, choose **Data
   accessors**.
7. Choose the **Data accessor** from the **Data
   accessor(s) list** section.
8. In the **Data accessor details** page, you will see the
   **Data accessor IDC application ARN** on this
   page.
9. To get the IAM Identity Center (IDC) Region, you will need to open the IAM
   IDC console, Choose **Dashboard** and you can find the IDC
   **Region** in the Summary Settings section on that
   page.

## Using the AWS CLI;

Amazon Q Business `applicationId` and the `dataAccessorArn` are
included in the response of `GetDataAccessor` API. To get the IDC Region
of your IDC instance and the IDC application environment, you need to visit IAM identity
center page in the AWS Management Console.

```

# To get qbusiness application id
aws qbusiness list-applications
{
    "applications": [
        {
            "displayName": "your_qbusiness_application",
            "applicationId": ${qbusiness_application_id},
            "createdAt": ...,
            "updatedAt": ...,
            "status": "ACTIVE",
            "identityType": "AWS_IAM_IDC"
        }
    ]
}

# To get IDC application arn
aws qbusiness list-data-accessors --application-id ${qbusiness_application_id}
{
    "dataAccessors": [
        {
            "displayName": "Miro-3ajmo",
            "dataAccessorId": "7493bad6-df69-487c-b2b3-cd55bf01434c",
            "idcApplicationArn": "your_idc_application_arn",
            "principal": "arn:aws:iam::419356813857:role/AwsQBusinessMiroRetrievalRole",
            ...
        }
    ]
}

# To get retriever id
aws qbusiness list-retrievers \
  --application-id ${qbusiness_application_id}
{
    "retrievers": [
        {
            "applicationId": ${qbusiness_application_id},
            "retrieverId": "your_retriever_id",
            "type": "NATIVE_INDEX",
            "status": "ACTIVE",
            "displayName": "..."
        }
    ]
}

```
