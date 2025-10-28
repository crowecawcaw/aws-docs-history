# Metadata enforcement rules for

publishing

The metadata enforcement rules for publishing in Amazon DataZone strengthen data governance
by enabling domain unit owners to establish clear metadata requirements for data
producers, streamlining access requests and enhancing data governance.

The feature is supported in all the AWS commercial Regions where Amazon DataZone is
currently available.

Domain unit owners can can complete the following procedure to configure metadata
enforcement in Amazon DataZone:

1. Navigate to the Amazon DataZone data portal using the data portal URL and log in
   using your SSO or AWS credentials. If you’re an Amazon DataZone administrator, you
   can obtain the data portal URL by accessing the Amazon DataZone console at
   https://console.aws.amazon.com/datazone in the AWS account where the
   Amazon DataZone domain was created.
2. Choose **Domains**, navigate to the **Domain
   units** tab and choose the domain unit that you want to work
   with.
3. Choose the **Rules** tab and then choose
   **Add**.
4. On the **Create required metadata form rule** page, do the
   following and then choose **Add rule**:
   - Specify a name for your rule.
   - Under **Action**, choose **Data asset and
     product publishing**.
   - Under **Required forms**, choose **Add
     metadata form**, choose a metadata form within the domain /
     domain unit that you want to add to this rule, and then choose
     **Add**. You can add up to 5 metadata forms per
     rule.
   - Under **Scope**, specify with which data entities you
     want to associate these forms. You can choose data products and/or data
     assets.
   - Under **Data asset types**, specify whether the rule
     applies across all asset types or limit it to selected asset types.
   - Under **Projects**, specify whether the required
     forms will be associated with data products and/or assets published by
     all projects or only selected projects in this domain unit. Also, check
     **Cascade rule to child domain units** if you want
     child domain units to inherit this requirement.
