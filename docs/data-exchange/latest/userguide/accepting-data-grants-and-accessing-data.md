# Accepting data grants and accessing data on AWS Data Exchange

The following steps describe the process of accepting a data grant on AWS Data Exchange using the
AWS Data Exchange console:

###### Accepting a data grant

1. You must sign up for an AWS account and create a user before you can accept a data grant.
   For more information see [Sign up for an AWS account](setting-up.md#setting-up-aws-sign-up "setting-up.md#setting-up-aws-sign-up").
2. In the left navigation pane of the AWS Data Exchange console, under **Exchanged data
   grants**, choose **Received data grants**.
3. Any data grants in which your AWS account is the receiver of will appear in the table
   under the tab of **Pending data grants** showing the pending data grant details
   with the status of **Pending acceptance**.
4. To accept a data grant, select the check box next to the data grant you wish to approve,
   and choose **Accept data grant**.
5. When the acceptance of the data grant has completed processing, the data grant will appear under
   the **Accepted and expired data grants** tab showing the data grant details
   with the status of **Accepted**.
6. After the acceptance of the data grant, choose the data grant name from the**Entitled data sets** table to access the data. You can also navigate to the
   **Entitled data** page from **My data** to view your data
   grant and to view all data sets shared with your account.
7. Next, use the included data sets. You can take any of the following actions depending on
   the type of data set you have access to:
   1. Export the associated files to your Amazon Simple Storage Service (Amazon S3) or locally through a signed
      URL.
   2. Call the Amazon API Gateway API.
   3. Query the Amazon Redshift data share.
   4. Access the Amazon S3 data.
   5. Query the AWS Lake Formation data lake (Preview).

   ###### Note

   When you accept a data grant, you agree that your use of the underlying data set remains
   subject to the AWS Customer Agreement or other agreement with AWS governing your use of
   such services.

## Related topics

- [Access an AWS Data Exchange data set after accepting a data
  grant](data-grant-access-data-set.md "data-grant-access-data-set.md")
- [Access an AWS Data Exchange data set containing
  file-based data](data-grant-access-file-based-data.md "data-grant-access-file-based-data.md")
- [Access an AWS Data Exchange data set containing APIs](data-grant-access-apis.md "data-grant-access-apis.md")
- [Access an AWS Data Exchange data set containing Amazon Redshift
  data sets](data-grant-access-redshift-data-sets.md "data-grant-access-redshift-data-sets.md")
- [Access an AWS Data Exchange data set containing Amazon S3 data
  access](data-grant-access-s3-data-sets.md "data-grant-access-s3-data-sets.md")
- [Access an AWS Data Exchange data set containing
  AWS Lake Formation data sets (Preview)](data-grant-access-lake-formation-data-sets.md "data-grant-access-lake-formation-data-sets.md")
