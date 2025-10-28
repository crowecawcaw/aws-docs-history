# Reviewing a SQL analysis template

After a collaboration member has created a SQLanalysis template, you can review and
approve it. After the analysis template and approved, it can be used in a query in
AWS Clean Rooms.

###### Note

When you bring your analysis code into a collaboration, be aware of the following:

- AWS Clean Rooms does not validate or guarantee the behavior of the analysis code.
  - If you need to ensure certain behavior, review the code of your collaboration
    partner directly or work with a trusted third-party auditor to review it.

- In the shared security model:
  - You (the customer) are responsible for the security of the code running in the
    environment.
  - AWS Clean Rooms is responsible for the security of the environment, ensuring that
    - only the approved code runs
    - only specified configured tables are accessible
    - the only output destination is the result receiver's S3 bucket.

###### To review a SQL analysis template using the AWS Clean Rooms console

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with the AWS account that will function as the
   collaboration creator.
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Templates** tab, go to the **Analysis templates
   created by other members** section.
5. Choose the analysis template that has the **Can run status** of
   **No requires your review**.
6. Choose **Review**.
7. Review the analysis rule **Overview**,
   **Definition**, and **Parameters** (if any).
8. Review the configured tables listed under **Tables referenced in
   definition**.

The **Status** next to each table will read **Template not
allowed**. 9. Choose a table.

| If you                              | Then choose                                                               |
| ----------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Approve the analysis template       | **Allow template on table**. Confirm your approval by choosing **Allow**. |
| Don't approve the analysis template | **Disallow**                                                              | You are now ready to query the configured table using a SQL analysis template. For more information, see [Running SQL queries](running-sql-queries.md "running-sql-queries.md"). |
