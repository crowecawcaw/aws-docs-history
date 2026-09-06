

# Assign permissions to view dashboards and reports in Connect Customer
<a name="dashboard-required-permissions"></a>

The following security profile permissions control access to dashboards and reports in Connect Customer. These permissions are in the **Analytics and Optimization** section of the **Security profiles** page.

## Access metrics permission
<a name="access-metrics-permission"></a>

When you select **Access metrics - Access**:
+ Connect Customer automatically assigns the following permissions:
  + **Real-time metrics - Access**
  + **Historical metrics - Access**
  + **Agent activity audit - Access**

  These permissions are shown in the following image:  
![The Access option is selected for Access metrics, Real-time metrics, Historical metrics, and Agent activity audit.](http://docs.aws.amazon.com/connect/latest/adminguide/images/permissions-create-and-share-reports.png)
+ **Saved reports - View** permission.
+ You gain access to:
  + All tabs on the **Dashboards and reports** page.
  + All real-time and historical metrics reports.

![The Dashboards and reports page, access is granted to all the tabs on the page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/dashboard-access-all.png)


## Individual feature permissions
<a name="individual-permissions"></a>

You can also assign permissions for individual features:

### Real-time metrics permission
<a name="realtime-metrics-permissions"></a>

When you select only **Real-time metrics - Access**:
+ You can access only real-time metrics reports.
+ You cannot access other analytics pages or reports.

### Historical metrics permission
<a name="historical-metrics-permissions"></a>

When you select only **Historical metrics - Access**:
+ You can access only historical metrics reports.
+ You cannot access other analytics pages or reports.

### Dashboard permissions
<a name="dashboard-permissions"></a>

When you select only **Dashboards - Access**:
+ You can access only the **Dashboards** tab.
+ You can view historical metrics displayed on dashboards.
+ You must have the **Real-time metrics - Access** permission to view real-time metrics on dashboards.

![The Dashboards - Access permission on the Security profiles page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_dashboards_access.png)


The following image shows that you only have access to the **Dashboards** tab on the **Dashboards and reports** page. 

![The Dashboards and reports page, access is granted to the Dashboards tab only.](http://docs.aws.amazon.com/connect/latest/adminguide/images/dashboard-access.png)


## Custom metrics and permissions
<a name="custom-sl-permissions"></a>
+ **Analytics and Optimization - Access metrics** - Access permission or the **Dashboard - Access** permission.
+ **Analytics and Optimization - Custom metrics**: 
  + This permission enables users to view, create and manage custom metrics.
  + In [Connect Customer](enable-nextgeneration-amazonconnect.md) instances, you will have the ability to view, create, and manage custom metrics with custom filters and functions in addition to custom customer service level metric calculations.