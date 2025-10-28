# Metadata enforcement rules for subscription

requests

The metadata enforcement rules for subscription requests feature in Amazon DataZone
strengthens data governance by enabling domain unit owners to establish clear metadata
requirements for data consumers, streamlining access requests and enhancing data
governance. This feature enables organizations to align with organization’s metadata
standards, implement custom workflows, and provide a consistent, governed data access
experience.

The feature is supported in all the AWS commercial Regions where Amazon DataZone is
currently available.

Domain unit owners can can complete the following procedure to configure metadata
enforcement in Amazon DataZone:

1.  Navigate to the Amazon DataZone data portal using the data portal URL and log in
    using your SSO or AWS credentials. If you’re an Amazon DataZone administrator, you
    can obtain the data portal URL by accessing the Amazon DataZone console at
    https://console.aws.amazon.com/datazone in the AWS account where the
    Amazon DataZone domain was created.
2.  Choose **Domains**, navigate to the **Domain
    units** tab and choose the domain unit that you want to work
    with.
3.  Choose the **Rules** tab and then choose
    **Add**.
4.  On the **Create required metadata form rule** page, do the
    following and then choose **Add rule**:

        * Specify a name for your rule.
        * Under **Action**, choose **Subscription
         request**.
        * Under **Required forms**, choose **Add
         metadata form**, choose a metadata form within the domain /
         domain unit that you want to add to this rule, and then choose
         **Add**. You can add up to 5 metadata forms per
         rule.
        * Under **Scope**, specify with which data entities you
         want to associate these forms. You can choose data products and/or data
         assets.
        * Under **Data asset types**, specify whether the rule
         applies across all asset types or limit it to selected asset types.
        * Under **Projects**, specify whether the required
         forms will be associated with data products and/or assets published by
         all projects or only selected projects in this domain unit. Also, check
         **Cascade rule to child domain units** if you want
         child domain units to inherit this requirement.

    Once metadata enforcement is configured, data consumers can complete the following
    procedure to request access:

5.  Navigate to the Amazon DataZone data portal using the data portal URL and log in
    using your SSO or AWS credentials. If you’re an Amazon DataZone administrator, you
    can obtain the data portal URL by accessing the Amazon DataZone console at
    https://console.aws.amazon.com/datazone in the AWS account where the
    Amazon DataZone domain was created.
6.  Use the search bar to search for and choose the asset to which you want to
    subscribe, and then choose **Subscribe**.
7.  In the **Subscribe** pop up window, provide the following
    information:
    - The project that you want to subscribe to the asset.
    - A short justification for your subscription request.
    - Complete Required Metadata - specify the required metadata fields as
      specified by the domain unit. If mandatory fields are incomplete, they
      are highlighted, and submission is disabled until resolved. Once all the
      mandatory fields are entered, select **Apply**.

8.  Select **Request** to submit the subscription request. After
    submitting, an event is generated in EventBridge, which can be used in custom
    workflows outside of Amazon DataZone as needed. You receive a notification in the
    data portal when the publisher approves your request.
    Data producers can complete the following procedure to approve the subscription
    request:

###### To approve or reject a subscription request

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. In the data portal, choose **Browse projects list** and
   select the project that contains the asset with the subscription request.
3. Navigate to the **Data** tab, then choose **Incoming
   requests** from the left navigation pane.
4. Locate the request and choose **View request**. You can
   filter by **Pending** to see only requests that are still
   open.
5. Review the subscription request and reason for access, and decide whether to
   approve or reject it.

Data producers can review the provided metadata, including document links and
account IDs, to determine if the request meets compliance and workflow
requirements before granting access. 6. To approve, select between the two options:

    * **Full access**: If you choose to approve the
     subscription with full access option, the subscriber will get access to
     all the rows and columns in your data asset.
    * **Approve with row and column filters**: To limit
     access to specific rows and columns of data, you can choose the option
     to approve with row and column filters. For more information, see [Fine-grained access control to data in
     Amazon DataZone](fine-grained-access-control.md "fine-grained-access-control.md").




    	+ Select **Choose filters**, and then from the
    	 drop down select one or more available filters you want to apply
    	 to the subscription.
    	+ To create a new filter you can choose Create new filter
    	 option, which opens a new page to create a new row or column
    	 filter. For more information, see [Create column filters in Amazon DataZone](create-column-filter.md "create-column-filter.md") and [Create row filters in Amazon DataZone](create-row-filter.md "create-row-filter.md").

7. (Optional) Enter a response that explains your reason for accepting or
   rejecting the request.
8. Choose either **Approve**.
