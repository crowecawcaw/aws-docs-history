# Creating a sensitive data discovery job

With Amazon Macie, you can create and run sensitive data discovery jobs to automate discovery, logging, and
reporting of sensitive data in Amazon Simple Storage Service (Amazon S3) general purpose buckets. A _sensitive data discovery job_ is a series of automated processing and analysis
tasks that Macie performs to detect and report sensitive data in Amazon S3 objects. As the
analysis progresses, Macie provides detailed reports of the sensitive data that it finds and
the analysis that it performs: _sensitive data findings_,
which report sensitive data that Macie finds in individual S3 objects, and _sensitive data discovery results_, which log details about the analysis of
individual S3 objects. For more information, see [Reviewing job
results](discovery-jobs-manage-results.md "discovery-jobs-manage-results.md").

When you create a job, you start by specifying which S3 buckets store objects that you want
Macie to analyze when the job runs—specific buckets that you select or buckets that
match specific criteria. Then you specify how often to run the job—once, or
periodically on a daily, weekly, or monthly basis. You can also choose options to refine the
scope of the job's analysis. The options include custom criteria that derive from properties
of S3 objects, such as tags, prefixes, and when an object was last modified.

After you define the schedule and scope of the job, you specify which managed data
identifiers and custom data identifiers to use:

- A _managed data identifier_ is a set of built-in criteria
  and techniques that are designed to detect a specific type of sensitive
  data—for example, credit card numbers, AWS secret access keys, or passport
  numbers for a particular country or region. These identifiers can detect a large and
  growing list of sensitive data types for many countries and regions, including
  multiple types of credentials data, financial information, and personally
  identifiable information (PII). For more information, see [Using managed data
  identifiers](managed-data-identifiers.md "managed-data-identifiers.md").
- A _custom data identifier_ is a set of criteria
  that you define to detect sensitive data. With custom data identifiers, you can
  detect sensitive data that reflects your organization's particular scenarios,
  intellectual property, or proprietary data—for example, employee IDs,
  customer account numbers, or internal data classifications. You can supplement the
  managed data identifiers that Macie provides. For more information, see [Building custom data
  identifiers](custom-data-identifiers.md "custom-data-identifiers.md").
  You then optionally select allow lists to use. In Macie, an _allow
  list_ specifies text or a text pattern to ignore. These are typically
  sensitive data exceptions for your particular scenarios or environment—for example,
  public names or phone numbers for your organization, or sample data that your organization
  uses for testing. For more information, see [Defining sensitive data exceptions with allow
  lists](allow-lists.md "allow-lists.md").

When you finish choosing these options, you're ready to enter general settings for the
job, such as the job's name and description. You can then review and save the job.

###### Tasks

- [Before you begin: Set up key
  resources](#discovery-jobs-create-prerequisites "#discovery-jobs-create-prerequisites")
- [Step 1: Choose S3 buckets](#discovery-jobs-create-step1 "#discovery-jobs-create-step1")
- [Step 2: Review your S3 bucket selections
  or criteria](#discovery-jobs-create-step2 "#discovery-jobs-create-step2")
- [Step 3: Define the schedule and refine the
  scope](#discovery-jobs-create-step3 "#discovery-jobs-create-step3")
- [Step 4: Select managed data
  identifiers](#discovery-jobs-create-step4 "#discovery-jobs-create-step4")
- [Step 5: Select custom data
  identifiers](#discovery-jobs-create-step5 "#discovery-jobs-create-step5")
- [Step 6: Select allow lists](#discovery-jobs-create-step6 "#discovery-jobs-create-step6")
- [Step 7: Enter general settings](#discovery-jobs-create-step7 "#discovery-jobs-create-step7")
- [Step 8: Review and create](#discovery-jobs-create-step8 "#discovery-jobs-create-step8")

## Before you begin: Set up key

resources

Before you create a job, it's a good idea to take the following steps:

- Verify that you configured a repository for your sensitive data discovery results. To do this, choose
  **Discovery results** in the navigation pane on the
  Amazon Macie console. To learn about these settings, see [Storing and retaining
  sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md").
- Create any custom data identifiers that you want the job to use. To learn how, see [Building custom data
  identifiers](custom-data-identifiers.md "custom-data-identifiers.md").
- Create any allow lists that you want the job to use. To learn how, see [Defining sensitive data exceptions with allow
  lists](allow-lists.md "allow-lists.md").
- If you want to analyze S3 objects that are encrypted, ensure that Macie can access and use
  the appropriate encryption keys. For more information, see [Analyzing encrypted S3
  objects](discovery-supported-encryption-types.md "discovery-supported-encryption-types.md").
- If you want to analyze objects in an S3 bucket that has a restrictive bucket policy,
  ensure that Macie is allowed to access the objects. For more information, see
  [Allowing Macie to access S3
  buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md").

If you do these things before you create a job, you streamline creation of the job and help
ensure that the job can analyze the data that you want.

## Step 1: Choose S3 buckets

When you create a job, the first step is to specify which S3 buckets store objects that you
want Macie to analyze when the job runs. For this step, you have two options:

- **Select specific buckets** – With this option, you explicitly
  select each S3 bucket to analyze. Then, when the job runs, Macie analyzes
  objects only in the buckets that you select.
- **Specify bucket criteria** – With this option, you define runtime
  criteria that determine which S3 buckets to analyze. The criteria consist of one
  or more conditions that derive from bucket properties. Then, when the job runs,
  Macie identifies buckets that match your criteria and analyzes objects in those
  buckets.

For detailed information about these options, see [Scope options for jobs](discovery-jobs-scope.md "discovery-jobs-scope.md").

The following sections provide instructions for choosing and configuring each option.
Choose the section for the option that you want.

If you choose to explicitly select each S3 bucket to analyze, Macie provides you with an
inventory of your general purpose buckets in the current AWS Region. You can
then use this inventory to select one or more buckets for the job. To learn
about this inventory, see [Selecting specific S3
buckets](discovery-jobs-scope.md#discovery-jobs-scope-buckets-select "discovery-jobs-scope.md#discovery-jobs-scope-buckets-select").

If you're the Macie administrator for an organization, the inventory includes buckets that are
owned by member accounts in your organization. You can select as many as 1,000
of these buckets, spanning as many as 1,000 accounts.

###### To select specific S3 buckets for the job

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Jobs**.
3. Choose **Create job**.
4. On the **Choose S3 buckets** page, choose **Select specific
   buckets**. Macie displays a table of all the general
   purpose buckets for your account in the current Region.
5. In the **Select S3 buckets** section, optionally
   choose refresh (
   ![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
   ) to retrieve the latest bucket metadata
   from Amazon S3.

If the information icon (
![The information icon, which is a blue circle that has a lowercase letter i in it.](images/icon-info-blue.png)
) appears next to any bucket
names, we recommend that you do this. This icon indicates that a bucket
was created during the past 24 hours, possibly after Macie last
retrieved bucket and object metadata from Amazon S3 as part of the [daily refresh
cycle](monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh "monitoring-s3-how-it-works.md#monitoring-s3-how-it-works-data-refresh"). 6. In the table, select the checkbox for each bucket that you want the job to analyze.

###### Tip

    * To find specific buckets more easily, enter filter criteria in the filter box above
     the table. You can also sort the table by choosing a column
     heading.
    * To determine whether you already configured a job to
     periodically analyze objects in a bucket, refer to the
     **Monitored by job** field. If
     **Yes** appears in a field, the bucket
     is explicitly included in a periodic job or the bucket
     matched the criteria for a periodic job within the past 24
     hours. In addition, the status of at least one of those jobs
     is not *Cancelled*. Macie
     updates this data on a daily basis.
    * To determine when an existing periodic or one-time job
     most recently analyzed objects in a bucket, refer to the
     **Latest job run** field. For
     additional information about that job, refer to the bucket's
     details.
    * To display a bucket's details, choose the bucket's name.
     In addition to job-related information, the details panel
     provides statistics and other information about the bucket,
     such as the bucket's public access settings. To learn more
     about this data, see [Reviewing your S3 bucket
     inventory](monitoring-s3-inventory-review.md "monitoring-s3-inventory-review.md").

7. When you finish selecting buckets, choose
   **Next**.
   In the next step, you'll review and verify your selections.

If you choose to specify runtime criteria that determine which S3 buckets to analyze,
Macie provides options to help you choose fields, operators, and values for
individual conditions in the criteria. To learn more about these options, see
[Specifying S3 bucket
criteria](discovery-jobs-scope.md#discovery-jobs-scope-buckets-criteria "discovery-jobs-scope.md#discovery-jobs-scope-buckets-criteria").

###### To specify S3 bucket criteria for the job

1.  Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2.  In the navigation pane, choose **Jobs**.
3.  Choose **Create job**.
4.  On the **Choose S3 buckets** page, choose
    **Specify bucket criteria**.
5.  Under **Specify bucket criteria**, do the following
    to add a condition to the criteria:
    1. Place your cursor in the filter box, and then choose the bucket property to use for
       the condition.
    2. In the first box, choose an operator for the condition,
       **Equals** or **Not
       equals**.
    3. In the next box, enter one or more values for the
       property.

    Depending on the type and nature of the bucket property, Macie
    displays different options for entering values. For example, if
    you choose the **Effective permission**
    property, Macie displays a list of values to choose from. If you
    choose the **Account ID** property, Macie
    displays a text box in which you can enter one or more
    AWS account IDs. To enter multiple values in a text box, enter
    each value and separate each entry with a comma. 4. Choose **Apply**. Macie adds the condition and displays it below the
    filter box.

    By default, Macie adds the condition with an include statement. This means that the
    job is configured to analyze (_include_) objects in buckets that match the
    condition. To skip (_exclude_)
    buckets that match the condition, choose
    **Include** for the condition, and then
    choose **Exclude**. 5. Repeat the preceding steps for each additional condition that
    you want to add to the criteria.

6.  To test your criteria, expand the **Preview the criteria results**
    section. This section displays a table of up to 25 general purpose
    buckets that currently match the criteria.
7.  To refine your criteria, do any of the following:

        * To remove a condition, choose **X** for the condition.
        * To change a condition, remove the condition by choosing **X** for the
         condition. Then add a condition that has the correct
         settings.
        * To remove all conditions, choose **Clear
         filters**.

    Macie updates the table of criteria results to reflect your
    changes.

8.  When you finish specifying bucket criteria, choose
    **Next**.
    In the next step, you'll review and verify your criteria.

## Step 2: Review your S3 bucket selections

or criteria

For this step, verify that you chose the correct settings in the preceding
step:

- Review your bucket selections ‐ If you
  selected specific S3 buckets for the job, review the table of buckets and change
  your bucket selections as necessary. The table provides insight into the
  projected scope and cost of the job's analysis. The data is based on the size
  and types of objects that are currently stored in a bucket.

In the table, the **Estimated cost** field indicates the total estimated
cost (in US dollars) of analyzing objects in an S3 bucket. Each estimate
reflects the projected amount of uncompressed data that the job will analyze in
a bucket. If any objects are compressed or archive files, the estimate assumes
that the files use a 3:1 compression ratio and the job can analyze all extracted
files. For more information, see [Forecasting and monitoring job
costs](discovery-jobs-costs.md "discovery-jobs-costs.md").

- Review your bucket criteria ‐ If you specified bucket
  criteria for the job, review each condition in the criteria. To change the
  criteria, choose **Previous**, and then use the filter options
  in the preceding step to enter the correct criteria. When you finish, choose
  **Next**.

When you finish reviewing and verifying the settings, choose
**Next**.

## Step 3: Define the schedule and refine the

scope

For this step, specify how often you want the job to run—once, or periodically
on a daily, weekly, or monthly basis. Also choose various options to refine the scope of
the job's analysis. To learn about these options, see [Scope options for jobs](discovery-jobs-scope.md "discovery-jobs-scope.md").

###### To define the schedule and refine the scope of the job

1. On the **Refine the scope** page, specify how often you want the job to
   run:
   - To run the job only once, immediately after you finish creating it,
     choose **One-time job**.
   - To run the job periodically on a recurring basis, choose
     **Scheduled job**. For **Update
     frequency**, choose whether to run the job daily, weekly,
     or monthly. Then use the **Include existing objects**
     option to define the scope of the job's first run:
     - Select this checkbox to analyze all existing objects immediately after you finish
       creating the job. Each subsequent run analyzes only those
       objects that are created or changed after the preceding
       run.
     - Clear this checkbox to skip analysis of all existing objects. The job's first run
       analyzes only those objects that are created or changed after
       you finish creating the job and before the first run starts.
       Each subsequent run analyzes only those objects that are created
       or changed after the preceding run.

     Clearing this checkbox is helpful for cases where you already analyzed the data and
     want to continue to analyze it periodically. For example, if you
     previously used another service or application to classify data
     and you recently started using Macie, you might use this option
     to ensure continued discovery and classification of your data
     without incurring unnecessary costs or duplicating
     classification data.

2. (Optional) To specify the percentage of objects that you want the job to
   analyze, enter the percentage in the **Sampling depth**
   box.

If this value is less than 100%, Macie selects the objects to analyze at
random, up to the specified percentage, and analyzes all the data in those
objects. The default value is 100%. 3. (Optional) To add specific criteria that determine which S3 objects are included or
excluded from the job's analysis, expand the **Additional
settings** section, and then enter the criteria. These criteria
consist of individual conditions that derive from properties of objects:

    * To analyze (*include*) objects that
     meet a specific condition, enter the condition type and value, and then
     choose **Include**.
    * To skip (*exclude*) objects that meet
     a specific condition, enter the condition type and value, and then
     choose **Exclude**.

Repeat this step for each include or exclude condition that you want.

If you enter multiple conditions, any exclude conditions take precedence over include
conditions. For example, if you include objects that have the .pdf file name
extension and exclude objects that are larger than 5 MB, the job analyzes any
object that has the .pdf file name extension, unless the object is larger than 5
MB. 4. When you finish, choose **Next**.

## Step 4: Select managed data

identifiers

For this step, specify which managed data identifiers you want the job to use when it
analyzes S3 objects. You have two options:

- Use recommended settings ‐ With this option, the job
  analyzes S3 objects by using the set of managed data identifiers that we
  recommend for jobs. This set is designed to detect common categories and types
  of sensitive data. To review a list of managed data identifiers that are
  currently in the set, see [Managed data identifiers recommended
  for jobs](discovery-jobs-mdis-recommended.md "discovery-jobs-mdis-recommended.md"). We update that list
  each time we add or remove a managed data identifier from the set.
- Use custom settings ‐ With this option, the job
  analyzes S3 objects by using managed data identifiers that you select. This can
  be all or only some of the managed data identifiers that are currently
  available. You can also configure the job to not use any managed data
  identifiers. The job can instead use only custom data identifiers that you
  select in the next step. To review a list of managed data identifiers that are
  currently available, see [Quick reference: Managed data identifiers by type](mdis-reference-quick.md "mdis-reference-quick.md"). We update that
  list each time we release a new managed data identifier.

When you choose either option, Macie displays a table of managed data identifiers. In the
table, the **Sensitive data type** field specifies the unique
identifier (ID) for a managed data identifier. This ID describes the type of sensitive
data that the managed data identifier is designed to detect, for example:
**USA_PASSPORT_NUMBER** for US passport numbers,
**CREDIT_CARD_NUMBER** for credit card numbers, and
**PGP_PRIVATE_KEY** for PGP private keys. To find specific
identifiers more quickly, you can sort and filter the table by sensitive data category
or type.

###### To select managed data identifiers for the job

1. On the **Select managed data identifiers** page, under
   **Managed data identifier options**, do one of the
   following:
   - To use the set of managed data identifiers that we recommend for jobs,
     choose **Recommended**.

   If you choose this option and you configured the job to run more than once, each run
   automatically uses all the managed data identifiers that are in the
   recommended set when the run starts. This includes new managed data
   identifiers that we release and add to the set. It excludes managed data
   identifiers that we remove from the set and no longer recommend for
   jobs.
   - To use only specific managed data identifiers that you select, choose
     **Custom**, and then choose **Use specific
     managed data identifiers**. Then, in the table, select the
     checkbox for each managed data identifier that you want the job to
     use.

   If you choose this option and you configured the job to run more than once, each run
   uses only the managed data identifiers that you select. In other words,
   the job uses these same managed data identifiers each time it
   runs.
   - To use all the managed data identifiers that Macie currently provides, choose
     **Custom**, and then choose **Use specific
     managed data identifiers**. Then, in the table, select the
     checkbox in the selection column heading to select all rows.

   If you choose this option and you configured the job to run more than once, each run
   uses only the managed data identifiers that you select. In other words,
   the job uses these same managed data identifiers each time it
   runs.
   - To not use any managed data identifiers and use only custom data
     identifiers, choose **Custom**, and then choose
     **Don't use any managed data identifiers**. Then,
     in the next step, select the custom data identifiers to use.

2. When you finish, choose **Next**.

## Step 5: Select custom data

identifiers

For this step, select any custom data identifiers that you want the job to use when it
analyzes S3 objects. The job will use the selected identifiers in addition to any
managed data identifiers that you configured the job to use. To learn more about custom
data identifiers, see [Building custom data
identifiers](custom-data-identifiers.md "custom-data-identifiers.md").

###### To select custom data identifiers for the job

1. On the **Select custom data identifiers** page, select the checkbox for
   each custom data identifier that you want the job to use. You can select as many
   as 30 custom data identifiers.

###### Tip

To review or test the settings for a custom data identifier before you
select it, choose the link icon (
![The link icon, which is a blue box that has an arrow in it.](images/icon-external-link.png)
) next to the
identifier's name. Macie opens a page that displays the identifier's
settings.

You can also use this page to test the identifier with sample data. To do
this, enter up to 1,000 characters of text in the **Sample
data** box, and then choose **Test**. Macie
evaluates the sample data by using the identifier, and then reports the
number of matches. 2. When you finish selecting custom data identifiers, choose
**Next**.

## Step 6: Select allow lists

For this step, select any allow lists that you want the job to use when it analyzes S3
objects. To learn more about allow lists, see [Defining sensitive data exceptions with allow
lists](allow-lists.md "allow-lists.md").

###### To select allow lists for the job

1. On the **Select allow lists** page, select the checkbox for each allow
   list that you want the job to use. You can select as many as 10 lists.

###### Tip

To review the settings for an allow list before you select it, choose the
link icon (
![The link icon, which is a blue box that has an arrow in it.](images/icon-external-link.png)
) next to the list's name. Macie opens a page
that displays the list's settings.

If the list specifies a regular expression (_regex_), you can also use this page to test the regex with
sample data. To do this, enter up to 1,000 characters of text in the
**Sample data** box, and then choose
**Test**. Macie evaluates the sample data by using the
regex, and then reports the number of matches. 2. When you finish selecting allow lists, choose
**Next**.

## Step 7: Enter general settings

For this step, specify a name and, optionally, a description of the job. You can also assign
tags to the job. A *tag* is a label that you define and assign to certain types of AWS resources. Each tag consists of a required tag key and an optional tag value. Tags can help you identify, categorize, and manage resources in different ways, such as by purpose, owner, environment, or other criteria. To learn more, see [Tagging Macie resources](tagging-resources.md "tagging-resources.md").

###### To enter general settings for the job

1. On the **Enter general settings** page, enter a name for the
   job in the **Job name** box. The name can contain as many as
   500 characters.
2. (Optional) For **Job description**, enter a brief description
   of the job. The description can contain as many as 200 characters.
3. (Optional) For **Tags**, choose **Add tag**,
   and then enter as many as 50 tags to assign to the job.
4. When you finish, choose **Next**.

## Step 8: Review and create

For this final step, review the job's configuration settings and verify that they're
correct. This is an important step. After you create a job, you can’t change any of
these settings. This helps ensure that you have an immutable history of sensitive data findings and discovery results for data privacy and protection audits or investigations that you perform.

Depending on the job's settings, you can also review the total estimated cost (in US
dollars) of running the job once. If you selected specific S3 buckets for the job, the
estimate is based on the size and types of objects in the buckets that you selected, and
how much of that data the job can analyze. If you specified bucket criteria for the job,
the estimate is based on the size and types of objects in as many as 500 buckets that
currently match the criteria, and how much of that data the job can analyze. To learn
about this estimate, see [Forecasting and monitoring job
costs](discovery-jobs-costs.md "discovery-jobs-costs.md").

###### To review and create the job

1. On the **Review and create** page, review each setting and verify that
   it's correct. To change a setting, choose **Edit** in the
   section that contains the setting, and then enter the correct setting. You can
   also use the navigation tabs to go to the page that contains a setting.
2. When you finish verifying the settings, choose **Submit** to
   create and save the job. Macie checks the settings and notifies you of any
   issues to address.

###### Note

If you haven’t configured a repository for your sensitive data discovery results, Macie displays a warning
and doesn't save the job. To address this issue, choose
**Configure** in the **Repository for sensitive
data discovery results** section. Then enter the configuration
settings for the repository. To learn how, see [Storing and retaining
sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md"). After you enter
the settings, return to the **Review and create** page and
choose refresh (
![The refresh button, which is a button that displays an empty blue circle with an arrow.](images/btn-refresh-data.png)
) in the **Repository for sensitive
data discovery results** section of the page.

Although we don't recommend it, you can temporarily override the repository requirement
and save the job. If you do this, you risk losing discovery results from the
job—Macie retains the results for only 90 days. To temporarily
override the requirement, select the checkbox for the override
option. 3. If Macie notifies you of issues to address, address the issues, and then
choose **Submit** again to create and save the job.

If you configured the job to run once, on a daily basis, or on the current day of the
week or month, Macie starts running the job immediately after you save it. Otherwise,
Macie prepares to run the job on the specified day of the week or month. To monitor the
job, you can [check the status of the
job](discovery-jobs-status-check.md "discovery-jobs-status-check.md").
