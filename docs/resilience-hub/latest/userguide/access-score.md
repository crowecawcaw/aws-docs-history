# Accessing the Resiliency score of your

applications

You can view the Resiliency score of your application by choosing
**Dashboard** or **Applications** from the
navigation menu.

###### Accessing the Resiliency score from Dashboard

1. In the left navigation menu, choose **Dashboard**.
2. In **Application resiliency score over time**,
   choose one or more applications in the **Choose up to 4
   applications** dropdown list.
3. The **Resiliency score** chart displays the resiliency score
   for all the chosen applications.

###### Accessing the Resiliency score from Applications

1. In the left navigation menu, choose **Applications**.
2. In **Applications**, open an application.
3. Choose **Summary**.

The **Resiliency score** chart displays the trend of your
application's resiliency score for up to one year. AWS Resilience Hub displays action
items, resiliency policy breaches, and operational recommendations that need to
be addressed for improving and achieving the maximum possible resiliency score
using the following:

    * To view the action items that need to be completed for improving and
     achieving the maximum possible resiliency score, choose **Action
     items** tab. When selected, AWS Resilience Hub displays the
     following:




    	+ **RTO/RPO** – Indicates the number of
    	 recovery times (RTO/RPOs) that need to be fixed to resolve the
    	 breaches in your application's resiliency policy. Choose the
    	 value to view the RTO/RPO details in the assessment report of
    	 your application.
    	+ **Alarms** – Indicates the number of
    	 recommended Amazon CloudWatch alarms that need to be implemented in your
    	 application. Choose the value to view the Amazon CloudWatch alarms that
    	 need to be fixed in the assessment report of your
    	 application.
    	+ **SOPs** – Indicates the number of
    	 recommended SOPs that need to be implemented in your
    	 application. Choose the value to view the SOPs that need to be
    	 fixed in the assessment report of your application.
    	+ **FIS**  – Indicates the number of
    	 recommended tests that need to be implemented in your
    	 application. Choose the value to view the tests that need to be
    	 fixed in the assessment report of your application.
    * To view the score of each component that affects your resiliency
     score, choose **Score breakdown**. When selected,
     AWS Resilience Hub displays the following:




    	+ **RTO/RPO compliance** – Indicates how
    	 compliant the Applications Components (AppComponents) are with
    	 the estimated workload recovery times, and the target recovery
    	 times that are defined in your application’s resiliency policy.
    	 Choose the value to view the RTO/RPO estimations in the
    	 assessment report of your application.
    	+ **Alarms implemented** – Indicates the
    	 actual contribution of the implemented Amazon CloudWatch alarms compared
    	 to its maximum possible contribution towards the resiliency
    	 score of your application. Choose the value to view the
    	 implemented Amazon CloudWatch alarms in the assessment report of your
    	 application.
    	+ **SOPs implemented** – Indicates the
    	 actual contribution of the implemented SOPs compared to its
    	 maximum possible contribution towards the resiliency score of
    	 your application. Choose the value to view the implemented SOPs
    	 in the assessment report of your application.
    	+ **FIS experiments implemented** –
    	 Indicates the actual contribution of the implemented tests
    	 compared to its maximum possible contribution towards the
    	 resiliency score of your application. Choose the value to view
    	 the implemented tests in the assessment report of your
    	 application.
    * To view the resiliency policy breaches and operational
     recommendations, choose the right arrow to expand the **Policy
     breach and operational recommendations breakdown** section.
     When expanded, AWS Resilience Hub displays the following:




    	+ **Resiliency policy breaches** –
    	 Indicates the number of Application Components that breaches
    	 your application's resiliency policy. Choose the value next to
    	 **RTO/RPO** to view the details in the
    	 **Resiliency recommendations** tab of your
    	 application's assessment report.
    	+ **Operational recommendations** –
    	 Indicates the operational recommendations that have not been
    	 implemented or executed to enhance the resiliency of your
    	 application using **Outstanding** and
    	 **Excluded** tabs. Operational
    	 recommendations include all the recommendations that are
    	 inactive and the ones that have not been implemented.


    	To view the operational recommendations that need to be
    	 implemented, choose **Outstanding** tab. When
    	 selected, AWS Resilience Hub displays the following:




    		- **Alarms** – Indicates the
    		 number of recommended Amazon CloudWatch alarms that need to be
    		 implemented.
    		- **SOPs** – Indicates the
    		 number of recommended SOPs that need to be
    		 implemented.
    		- **FIS** – Indicates the number
    		 of recommended tests that need to be implemented.
    	To view the operational recommendations that are excluded from
    	 your application, choose **Excluded** tab. When
    	 selected AWS Resilience Hub displays the following:




    		- **Alarms** – Indicates the
    		 number of recommended Amazon CloudWatch alarms that are excluded
    		 from your application.
    		- **SOPs** – Indicates the
    		 number of recommended SOPs that are excluded from your
    		 application.
    		- **FIS** – Indicates the number
    		 of recommended tests that are excluded from your
    		 application.
