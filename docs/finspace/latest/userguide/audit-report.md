After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Generating dataset browser audit report in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

You can generate audit reports to support your governance processes right from the FinSpace
dataset browser by using the web application. FinSpace captures all activity within a FinSpace
environment.

###### Note

- The audit report functionality only applies to FinSpace dataset browser. It does
  not apply for activity in Managed kdb Insights.
- In order to generate an audit report, you must be a superuser or a member of a
  group with necessary permissions - **View Audit
  Data**.

**Use the following procedure to generate an audit report**

1. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
2. On the left navigation bar of the home page, choose **Audit Report**.
3. On the **Generate Audit Report** page, choose one or more
   activity type.
4. Choose the period over which the report should be run.
5. (Optional) Filter the report by a user by specifying their email.
6. (Optional) Specify Dataset ID to filter the activity by a specific dataset.
7. Choose **RUN REPORT**.
8. (Optional) Export the audit report to Comma-separated values (CSV) file by
   choosing **DOWNLOAD FULL REPORT (.CSV)**.

## Definitions of columns in

the audit report

| Audit report column | Description                                                                    |
| ------------------- | ------------------------------------------------------------------------------ |
| Timestamp           | The date and time of the event                                                 |
| Event Type          | Type of the event. For example<br>• user login, user accessing data<br>content |
| Event               | Details of the event                                                           |
| User                | Email of the user related to the audit activity                                |
| Dataset ID          | Dataset ID related to the event when applicable                                |

## Event types

| Event type            | Description                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------- |
| Authentication        | Events related to user sign in or accessing temporary credentials to<br>use the API         |
| Dataset Content       | Events related to accessing and using a dataset                                             |
| Dataset Definition    | Events related to associating and updating an attribute set to a<br>dataset                 |
| Categories            | Events related to creating, editing, and removing categories                                |
| Attribute Sets        | Events related to creating, editing, and removing attribute<br>sets                         |
| Users and Permissions | Events related to creating, editing, and removing users and permission<br>group permissions |
| Spark Clusters        | Events related to creating, scaling, and terminating spark<br>clusters                      |
| Notebooks             | Events related to creating, modifying, and terminating<br>notebooks                         |
| Search                | Events related to searching for datasets or browsing for datasets via<br>data browser       |
| Audit                 | Events related to generating, viewing, and downloading audit<br>reports                     |
