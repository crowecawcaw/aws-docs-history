# Configuring multi-year and granular data

Using the management account, you can enable multi-year data and granular data in
Cost Explorer. You do this in the Cost Management preferences in the console.

However, in order to enable multi-year and granular data, you first need to manage
access to view and edit your Cost Management preferences. See [Controlling access using IAM](ce-iam-access.md "ce-iam-access.md").

###### Note

Granular data visibility is only available for billing views that show chargeable data. When you use Billing Conductor as an account in a standard billing group or billing transfer billing group, you can't view granular data in Cost Explorer.

###### To set up multi-year and granular data

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management
   preferences**.
3. To get historical data for up to 38 months, select **Multi-year data
   at monthly granularity**.
4. To enable resource-level or hourly granular data, consider the following
   options:

###### Note

The hourly data as well as daily resource-level data is available for the
past 14 days.

    * Hourly granularity




    	+ Select **Cost and usage data for all AWS services at
    	 hourly granularity** to get hourly data for all
    	 AWS services without resource-level data.
    	+ Select **EC2-Instances (Elastic Compute Cloud)
    	 resource-level data** to track EC2 cost and usage
    	 at instance level at hourly granularity.
    * Daily granularity




    	+ Select **Resource-level data at daily
    	 granularity** to get resource-level data for
    	 individual or all AWS services.
    	+ Choose services from the **AWS services at daily
    	 granularity** dropdown list that you want to enable
    	 resource-level data for.


    	###### Note

    	The dropdown list contains only those services that were
    	 used in your organization in the last six months. They are
    	 ranked starting with the costliest.

5. Choose **Save preferences**.

###### Note

It can take up to 48 hours for changes to your data settings to reflect in
Cost Explorer. Also, after saving your preferences, you won’t be able to make any
additional changes for 48 hours.

If the estimated data volume for your preferences is above the Cost Explorer
limit, you'll receive an error stating that you have reached the data threshold
limit and you won’t be able to save your preferences. See "Understanding
Cost Explorer data threshold limits".
