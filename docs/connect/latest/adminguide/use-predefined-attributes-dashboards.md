

# Use predefined attributes in dashboards
<a name="use-predefined-attributes-dashboards"></a>

Predefined attributes are available to use on dashboards for grouping and filtering different real-time and historical contact-related metrics. Some system defined attributes have been enabled by default for grouping and filtering. Filtering by user defined attributes is only available for historical contact metrics in instances that are enabled for Amazon Connect with unlimited AI capabilities. To set up analytics for filtering with user defined predefined attributes, see [Use contact segment attributes](use-contact-segment-attributes.md).

Historical contact metrics can be found in the [Metric definitions](metrics-definitions.md) page by looking for metrics that have a category of **Contact record-driven metric** and are available on the dashboard page.

Real time contact metrics include: [Contacts in queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-in-queue), [Contacts scheduled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#scheduled), [Oldest contact age](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#oldest-real-time).

**Topics**
+ [Group by predefined attributes](#group-by-predefined-attributes)
+ [Filter by predefined attributes](#filter-by-predefined-attribute)

## Group by predefined attributes
<a name="group-by-predefined-attributes"></a>

There are two system defined attributes that can be used for grouping:
+ Subtype (connect:Subtype)
+ Contact source (connect:ValidationTestType)

1. To group by one of the above attributes, navigate to **Dashboards and reports page** and select an existing template/report or create a custom one. 

1. In a widget that has only real-time or historical contact metrics, select the **Actions** icon and then choose **Edit**.

1. Choose on a groupings dropdown and select **Subtype** or **Contact source**.

   1. For real-time widgets, these grouping options will show up in the second grouping dropdown if the first grouping has been selected to be **Queue**.  
![The Analytics dashboards page, the grouping dropdown.](http://docs.aws.amazon.com/connect/latest/adminguide/images/predefined-attributes-groupings.png)

1. Choose **Save** to apply your changes to the widget.

## Filter by predefined attributes
<a name="filter-by-predefined-attribute"></a>

There are system defined attributes such as Subtype (connect:Subtype) or Contact source (connect:ValidationTestType) that can be used for filtering, along with any user defined attribute that has been enabled to be used for analytics. 

1. To group by one of the above attributes, navigate to **Dashboards and reports page** and select an existing template/report or create a custom one. 

1. In a widget that has only real-time or historical contact metrics, select the **Add filter** button. If enabled, user defined attributes will be displayed in the dropdown for historical widgets, either within the dropdown or under the business purpose associated with it.

   1. In the below example, **Department** and **Disposition** are both user defined attributes. **Department** was not associated with a business purpose and is displayed within the dropdown. **Disposition** shows up under **Proficiency**, because this is the business purpose associated with it.  
![The Analytics dashboards page, the Add filter dropdown.](http://docs.aws.amazon.com/connect/latest/adminguide/images/predefined-attributes-filters-1.png)

1. Once a filter has been selected, select one or more values to be filter by.  
![The Analytics dashboards page, the filter values dropdown.](http://docs.aws.amazon.com/connect/latest/adminguide/images/predefined-attributes-filters-2.png)

1. Choose **Apply** to apply your changes to the widget.