

# Build customer segments in Connect Customer
<a name="customer-segments-building-segments"></a>

**Note**  
**Segmentation powered by SQL (Beta) requires Data store to be turned on. Please visit Customer Profiles home page screen and enable Data store from the top blue banner**

**Note**  
To navigate to the segmentation builder experience in the Connect Customer admin website, you need security profiles permissions for this feature. For more information, see [Assign security profile permissions to manage customer segments](security-profile-customer-profile-segmentation.md).
Before building segments, we recommend your Customer Profiles domain setup data integrations to populate profiles in your Customer Profiles Domain. For more information on how to configure data integrations with Customer Profiles, see [Integrate external applications with Connect Customer Customer Profiles](integrate-external-apps-customer-profiles.md).
Segments can include events you captured using Calculated Attributes. For more information on how to configure custom Calculated Attributes and review the default Calculated Attributes Customer Profiles offers, see [Set up calculated attributes in Connect Customer Customer Profiles](customerprofiles-calculated-attributes.md).

Connect Customer provides two ways to build customer segments: 1/ Define segments through Spark SQL (Beta; requires Data store to be enabled); 2/ Define segments through audience groups and filters (Classic Segmentation). For both, you can use natural language prompts through Generative AI-powered Segment AI assistant. If you define segments in one of the ways, you move that segment to the other and would have to start again.

## Classic segmentation with audience groups and filters
<a name="customer-segments-audience-groups-classic-segmentation"></a>

 When you create a customer segment, you choose starting audiences and refine that audiences by choosing the filters that define the segment. For example, you could create an audience group, then choose a filter of all customers who live in a specific country and who are frequent callers. Segments are recalculated on demand, such as during campaign execution, contact flow execution, and segment estimate or export. As a result, the size and membership of each segment changes over time. 

 Additionally, you can create a second audience group, and then create a relationship (AND, OR, or EXCLUDE) between the two audience groups to further narrow down, concatenate, or exclude customers from the first audience group. 

![Two audience groups.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-building-segments-1.png)


## Audience groups
<a name="customer-segments-audience-groups"></a>

 When you create a customer segment, you create one or more audience groups. An audience group consists of these components: 

![A conceptual diagram that shows the components of audience groups.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-audience-groups-1.png)

+  **Starting audiences**: The customer segments that define the initial user population. You can specify up to 5 starting audiences, or all of the profiles in your Customer Profiles domain. 
+  **Filter groups**: Categories of audience information that you apply on top of the starting audiences. You can add multiple groups of filters which are connected by OR relationships. 
+  **Filters**: Filters reduce the audience number that belong to the segment. You can add as many filters as you want to tailor the segment to your needs. 

 A customer segment has to have at least one audience group, but you can optionally create a second audience group, and then create a relationship (AND/OR/EXCLUDE) between the two audience groups. See [Step 5: Add the second audience group (optional)](#step-5-add-the-second-audience-group-optional) for more details about the relationship. 

## Creating a customer segment
<a name="creating-a-customer-segment"></a>

 The following steps describe creating and configuring a customer segment: 
+  Step 1: Build a new segment 
+  Step 2: Configure name and description 
+  Step 3: Choose the starting audiences to include in audience group 1 
+  Step 4: Choose and configure the filter groups (optional) 
+  Step 5: Add audience group 2 (optional) 
+  Step 6: Enable Sorting (optional) 

### Step 1: Build a new segment
<a name="step-1-build-a-new-segment"></a>

1.  To create a segment, make sure that you have created security profiles permissions as a prerequisite. For more information, see [Assign security profile permissions to manage customer segments](security-profile-customer-profile-segmentation.md). In addition, to best visualize the membership of your segment, we recommend data ingestion before segment creation. To ingest profiles through S3 or external applications, see [Create and ingest customer data into Customer Profiles](customer-profiles-object-type-mappings.md) or [Integrate external applications with Connect Customer Customer Profiles](integrate-external-apps-customer-profiles.md). 

1.  Choose **Create a segment** in the Customer segment table view.   
![The Create a segment button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-1-build-a-new-segment-1.png)

### Step 2: Specify a name and description
<a name="step-2-configure-specify-name-and-description"></a>
+  For **Name**, enter a name for the customer segment to make it easy to recognize later. 
**Note**  
The Connect Customer admin website uses the entered name as the `DisplayName` of the segment, and generates an identifier based on it. The generated identifier is used as the `SegmentDefinitionName` when you access the segment by using Customer Profiles APIs.
+  For **Description**, optionally enter a description for the customer segment. 

![A Segment name section.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-2-configure-specify-name-and-description-1.png)


### Step 3: Choose the starting audiences to include in audience group 1
<a name="step-3-choose-the-starting-audiences-to-include-in-audience-group"></a>

 You'll first choose how you want to define the starting audience for the audience group. 

1.  Under **Audience group 1**, for the **Starting audience** dropdown list, select one or more segments to include in the audience group, or choose **All profiles from Customer Profiles**. 
**Note**  
 When you choose multiple segments as the starting audience, the segments are connected by `OR` relationships. For example, if you choose **Premium membership customers** and **Basic membership customers** segments as the starting audiences, all profiles who are in either of the segments will be the included.   
![A Starting audience dropdown list.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-3-choose-the-starting-audiences-to-include-in-audience-group-1.png)

1. To create a segment with ProfileType, start by using **All Accounts from Customer Profiles** as your initial audience. With this approach, you can filter account-based profiles effectively. It's important to note that unless you specify otherwise, the segmentation process will automatically export all profiles within the customer profiles domain. This default behavior ensures comprehensive coverage but can be adjusted to meet specific targeting needs.

   The following is an example of how a segment definition can be created (either account- or standard-profiles based):

   **Filters all account-based profiles (ProfileType=ACCOUNT\_PROFILE)**  
![Filters all account-based profiles (ProfileType=ACCOUNT_PROFILE).](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-3-choose-the-starting-audiences-to-include-in-audience-group-1-5.png)
**Note**  
To create a segment only with sub-profiles, create a new audience that excludes account-based profiles. For example, profiles with `ProfileType` is PROFILE or where `ProfileType` is empty.  
![To create a segment only with sub-profiles, create a new audience that excludes account-based profiles.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-3-choose-the-starting-audiences-to-include-in-audience-group-1-6.png)

   **Sample Campaign that targets accounts to be reached out by using `Phone`**  
![Sample Campaign that targets accounts to be reached out by using Phone.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-3-choose-the-starting-audiences-to-include-in-audience-group-1-7.png)

   In this example, the campaign targets a single account with the following call sequence:

   1. First attempts to reach John (ID: 2)

   1. If John doesn't answer, then calls Sally (ID: 3) as a backup contact

1.  After you choose a starting audience, the **Estimated audience** section updates to display the eligible profiles. After you edit the audience groups, you can choose **Refresh** button in the Estimated audience section to re-fetch the estimate.  
![An Estimated audience section.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-3-choose-the-starting-audiences-to-include-in-audience-group-2.png)

### Step 4: Choose and apply audience filters (optional)
<a name="step-4-choose-and-apply-audience-filters-optional"></a>

 After you’ve chosen your starting audiences, you can further refine the audiences by applying conditional logic to attributes. Segments supports standard profile attributes, custom profile attributes, and calculated attributes.

![Audience filters.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-4-choose-and-apply-audience-filters-optional-1.png)


**To choose and configure the audience filters**

1.  For **Attribute**, you can choose an attribute of the following types

   1.  **Calculated attributes** - Filter the audience based on one of calculated attributes. 

      See [Set up calculated attributes in Connect Customer Customer Profiles](customerprofiles-calculated-attributes.md) to learn about the default Calculated Attributes and how to configure custom Calculated Attributes.

   1.  **Standard attributes** - Filter the audience based on one of standard profile attributes. 

      See [Standard profile definition in the Connect Customer Customer Profiles](standard-profile-definition.md) for the list of standard profile attributes.

   1.  **Custom attributes** - Filter the audience based on one of custom profile attributes. 
**Note**  
We store up to 1000 most recent profile attributes within the domain. If your domain contains a large amount of attributes the oldest attributes might not be displayed in this list.

1.  Choose the **Operator**. Operators determines the relationship of the attribute to a value you enter. The following describes the available operators. Available operators change based on the type of value of the attribute you selected. 



- ** Number **
  - **Operator:**  Greater than  / **Description:**  Used for numeric attributes only. This operator filters results that are greater than the number passed. For example, Customer’s average hold time is greater than 10 seconds. 
  - **Operator:**  Greater than or equal  / **Description:**  Used for numeric attributes only. This operator filters results that are greater than or equal to the number passed. For example, Customer’s average hold time is greater than or equal to 10 seconds. 
  - **Operator:**  Equals  / **Description:**  Used for numeric attributes only. This operator filters the audience by numeric value equality. For example, Customer’s average hold time equals 10 seconds. 
  - **Operator:**  Less than  / **Description:**  Used for numeric attributes only. This operator filters results that are less than the number passed. For example, Customer’s average hold time is less than 10 seconds. 
  - **Operator:**  Less than or equal  / **Description:**  Used for numeric attributes only. This operator filters results that are less than or equal to the number passed. For example, Customer’s average hold time is less than or equal to 10 seconds. 

- ** String**
  - **Operator:**  Is  / **Description:**  Filters the audience the matches to the given string. For example, customer’s Address.Country is USA. 
  - **Operator:**  Is not  / **Description:**  Filters the audience that does not match a given string. For example, customer’s Address.Country is not USA. 
  - **Operator:**  Contains  / **Description:**  Use this to filter the audience based on a substring within a string. For example, if you have a filter for Address.Country attribute, you could pass the US to return US or USA. 
  - **Operator:**  Begind with  / **Description:**  Filters the audience whose attribute begins with the given string. For example, customer’s Address.Country begins with US. 
  - **Operator:**  Ends with  / **Description:**  Filters the audience whose attribute ends with the given string. For example, customer’s EmailAddress ends with @amazon.com.

- ** Date**
  - **Operator:**  Before  / **Description:**  Filters the audience whose attribute has a date value that is before a specific date. For example, customer’s whose Attributes.NextReservation is before 2024/10/01. 
  - **Operator:**  On  / **Description:**  Filters the audience whose attribute value matches with a specific date. For example, customer’s whose Attributes.NextReservation is on 2024/10/01. 
  - **Operator:**  After  / **Description:**  Filters the audience whose attribute has a date value that is after a specific date. For example, customer’s whose Attributes.NextReservation is after 2024/10/01. 
  - **Operator:**  Time range is / **Description:**  Filters the audience whose attribute has a date value that is between a specific time range. You can either specify the time range in absolute time mode or relative time mode. 
  - **Description:**  Absolute time mode: you can specify an absolute time range. For example, between 2024/10/01 12:00 AM and 2024/10/07 12:00 AM. 
  - **Description:**  Relative time mode: you can specify the relative time range of furture or past X hours, days, weeks, months, or years.   - Future time direction: will filter audience whose attribute has a date value that is between now and a speficied future time. For example, within the next 2 days.   - Past time direction: will filter audience whose attribute has a date value that is between a speficied past time and now. For example, within the last 2 days. 
  - **Operator:**  Time range is not  / **Description:**  Filters the audience whose attribute has a date value that is not between a specific time range. You can either specify the time range in absolute time mode or relative time mode. See "Time range is" operator in this table for more details. 

- ** List**
  - **Operator:**  Contains any of  / **Description:**  Filters the audience whose list attribute contains any of the given values. For example, a customer’s calculated attribute contains US or USA. 
  - **Operator:**  Contains all of  / **Description:**  Filters the audience whose list attribute contains all of the given values. For example, a customer’s calculated attribute contains both US and USA. 



**Note**  
The **Contains any of** and **Contains all of** operators apply to list attributes. The admin website shows these operators for a calculated attribute only when its statistic is recent occurrences.

**Note**  
When you set the **Value** for a calculated attribute or profile attribute filter, you can choose one of the following options:  

**Static values**  
Compare against fixed values that you enter.

**Attribute references**  
Reference another attribute's value, evaluated individually for each customer. Choose the profile attribute or calculated attribute that you want to reference from the list.

![A filter group with the Value drop-down expanded, showing the Static values and Attribute references options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-building-segments-2.png)


**Note**  
Customer segments in the Connect Customer admin website uses UTC timezone and a default time of 00:00:00 UTC for all time-based filters. You can filter on dates but times are recorded as the same value. If you enter a date of 2024-01-01, the console passes the time as 2024-01-01T00:00:00Z.

**Note**  
When you specify a filter for a calculated attribute, you can override the time period of the calculated attribute definition. For example, the filter `Frequent caller is true for the event time period of 60 days` will override the *Frequent caller* [Default calculated attributes in Connect Customer Customer Profiles](customerprofiles-default-calculated-attributes.md) to evaluate the value within the past 60 days instead of the [time period configured in the calculated attribute definition](customerprofiles-calculated-attributes-apis.md). This override is specific to the segment, and does not affect the calculated attribute definition itself.  

![Attribute, Operator, and Value to be evaluated.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-4-choose-and-apply-audience-filters-optional-2.png)


1. Specify the Value. You can specify multiple values connected by `OR` relationships. For example, `Address.Country` is `USA` or `Mexico`. The value input shows suggestions in the dropdown for string operators based on the customer profiles stored in the domain.
**Note**  
Values are case-sensitive. For example, *Address.Country is US* returns different results than *Address.Country is us*.

1.  (Optional) To apply additional attributes to this filter group, choose **\+ Filter**. To create another group of filters, choose **\+ Group**. 

**Note**  
 When you have multiple filters in a filter group, the filters are connected by AND relationships. For example, a filter group containing 2 filters, “*Address.Country* is USA” and “*Customer’s average hold time* is more than 10 seconds”, the profiles whose *Address.Country* is USA **and** *average hold time* is more than 10 seconds will belong to the segment. 

 When you have multiple filter groups in an audience group, Customer segments in the Connect Customer admin website use OR relationships to connect between the filter groups. 

![Two audience filters.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-4-choose-and-apply-audience-filters-optional-3.png)


1. When you’re finished setting up the audience group, choose **Create segment**. 

### Step 5: Add the second audience group (optional)
<a name="step-5-add-the-second-audience-group-optional"></a>

 Optionally add the second audience group and define a relationship with audience group 1. When you create a customer segment by using the Connect Customer admin website, you can have a maximum of two audience groups per segment. If you add a second audience group to your segment, you can choose one of two ways to specify how the two audience groups are connected: 
+  **AND relationship** — If you use AND relationship to connect two audiences, your segment contains all profiles who meet the filters of both Audience group 1 and Audience group 2. 
+  **OR relationship** — If you use OR relationship to connect two audiences, your segment contains all profiles who meet the filters of either Audience group 1 or Audience group 2. 
+  **EXCLUDE relationship** — If you use EXCLUDE relationship to connect two audiences, the segment will contain profiles in Audience group 1 excluding the profiles in Audience group 2. 

**To configure second audience group**

1.  Choose **AND**, **OR**, or **EXCLUDE** relationship after configuring Audience group 1.   
![The AND, OR, or EXCLUDE options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-5-add-the-second-audience-group-optional-1.png)

1.  Choose the starting audience in Audience group 2. For reference, see [Step 3: Choose the starting audiences to include in audience group 1](#step-3-choose-the-starting-audiences-to-include-in-audience-group). 

1.  (Optional) Choose the filters by which you want to narrow down your segments. For reference, see [Step 4: Choose and apply audience filters (optional)](#step-4-choose-and-apply-audience-filters-optional) 

1.  When you finish setting up the segment, choose **Create segment**. Segment is created and you can now use the segment in outbound campaigns or flows.   
![A message that the segment was successfully created.](http://docs.aws.amazon.com/connect/latest/adminguide/images/step-5-add-the-second-audience-group-optional-2.png)

### Step 6: Enable Sorting (optional)
<a name="step-6-enable-sorting-optional"></a>

 Optionally configure sorting for your segment results. You can use sorting to control the order in which profiles appear in your segment output. You can sort by up to 10 attributes. Attributes are evaluated from top to bottom. When multiple profiles share the same value for an attribute, the next attribute in the list is used as a tiebreaker, and so on.

Outbound campaigns and journeys respect this sort order when executing, which means profiles are processed and dialed in the order defined by the segment. For more information about using sorted segments with outbound campaigns, see [Outbound campaign best practices](https://docs.aws.amazon.com/connect/latest/adminguide/outbound-campaign-best-practices.html). Sorting segments is useful when you want to:
+ Prioritize high-value customers by sorting on attributes such as lifetime value or account tier.
+ Contact customers with upcoming appointments first by sorting on appointment date.
+ Process time-sensitive communications in a specific order.

**Note**  
Segment sort order is respected only for voice campaigns and voice activities in journeys. Other communication channels process profiles in an unsorted order.

**To enable sorting**

1.  Enter the attribute name you want to sort by. You can use an attribute from either standard or calculated attributes. 

1.  Specify the sort order: choose either **Ascending** or **Descending**. 

1.  (Optional) Specify the data type by choosing **String**, **Numeric**, or **Date**. If you do not specify a type, it is automatically inferred based on sampled data. 

![The Enable Sorting configuration for segment results.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-enable-segment-sorting.png)


## Creating segments powered by Spark SQL
<a name="w2aac40c53c13c15"></a>

With segments powered by Spark SQL, you can use complete Customer Profile data and expanded functionality to define segments. You can use standard profile object attributes and custom object attributes. You can also used SQL-based functionality such as joining standard and custom objects together to use data from various objects, filtering segments with statistics such as percentiles and standardizing date fields to make comparisons. 

You can start by entering in a natural language prompt into Segment Assistant AI. Segment AI assistant will define the segment including its translation into Spark SQL. Segment Assistant AI will provide the steps it took to define the segment and you can validate it matches what you were aiming to create. You can also view the SQL, the SQL steps in natural language and a AI-generated summary of the Spark SQL to further help validate. If you want to make changes, you can update your natural language prompt or make edits to the Spark SQL directly. 

You also have the option to create the Spark SQL segment directly.

Like Classic segmentation, segments powered by Spark SQL can be used in segment membership calls and Flow blocks. To use Outbound Campaigns or Journeys with Spark SQL segments, contact AWS Support to request access.

When you use a Spark SQL segment in a segment membership call, Flow block, or Outbound Campaign initiated by a customer event, it uses the last exported segment (segment snapshot). The segment snapshot used for membership expires 1 year after creation. If you receive a 4XX error, make sure you have exported the segment (segment snapshot).

**Note**  
**SQL segmentation runs on Data store which has up to 10 years data. Classic segmentation uses latest data (data updated in past 3 years)**

### Step 1: Build a new segment
<a name="w2aac40c53c13c15c15"></a>

In the Segment AI assistant, select “How to create a segment” for more guidance on creating valuable segments or “I want to generate a segment” to enter a natural language prompt to create the segment. 

Alternatively, use SQL to define a new segment in the query editor. 

### Step 2: Specify a name and description
<a name="w2aac40c53c13c15c17"></a>

For Name, enter a name for the customer segment to make it easy to recognize later.

**Note**  
The Amazon Connect admin website uses the entered name as the `DisplayName` of the segment, and generates an identifier based on it. The generated identifier is used as the `SegmentDefinitionName` when you access the segment by using Customer Profiles APIs.

For Description, optionally enter a description for the customer segment.

### Step 3: Review and validate the segment
<a name="w2aac40c53c13c15c19"></a>

Review the data the Segment AI assistant used and the steps the AI model it took to generate your segment. You can also review the SQL it created to define the segment in the query editor. If it was not able to create the segment, address the feedback it provided to help it create an accurate segment. After it has generated a segment, Customer Profiles will automatically create a segment estimate for you. 

If you want to make edits, you can provide a new prompt by choosing “New conversation” or create/edit SQL in the query editor.

If you are not using the Segment AI assistant, you can validate the query and create the estimate by choosing on the “Validate and estimate query” button below the query editor. 

**Note**  
Segments powered by Spark SQL will take time depending on the amount of profile data you use in the segment and the SQL used, similar to other query engines (for example, multiple joins across objects usually take more time). 

### Step 4: Create segment
<a name="w2aac40c53c13c15c21"></a>

After you have build a segment and are satisfied, select “Create segment” button on the top right. After you have created the segment, you can select Actions - exporting to .csv, using the segment in Flows and using the segment in Outbound Campaigns.

**Note**  
If you use the segment in Outbound Campaigns or Flow blocks, it will check segment membership based on when the segment was last created. If you need real-time segment membership checks as the Flow or campaign is being executed, use Classic segmentation. 