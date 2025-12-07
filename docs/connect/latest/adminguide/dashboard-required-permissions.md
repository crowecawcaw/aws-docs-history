# Assign permissions to view dashboards

and reports in Amazon Connect

The following security profile permissions control access to dashboards and reports in
Amazon Connect. These permissions are in the **Analytics and Optimization**
section of the **Security profiles** page.

## Access metrics permission

When you select **Access metrics - Access**:

- Amazon Connect automatically assigns the following permissions:

      + **Real-time metrics - Access**
      + **Historical metrics - Access**
      + **Agent activity audit - Access**

  These permissions are shown in the following image:

![The Access option is selected for Access metrics, Real-time metrics, Historical metrics, and Agent activity audit.](images/permissions-create-and-share-reports.png)

- **Saved reports - View** permission.
- You gain access to:
  - All tabs on the **Dashboards and reports**
    page.
  - All real-time and historical metrics reports.

![The Dashboards and reports page, access is granted to all the tabs on the page.](images/dashboard-access-all.png)

## Individual feature permissions

You can also assign permissions for individual features:

### Real-time metrics

permission

When you select only **Real-time metrics - Access**:

- You can access only real-time metrics reports.
- You cannot access other analytics pages or reports.

### Historical metrics

permission

When you select only **Historical metrics - Access**:

- You can access only historical metrics reports.
- You cannot access other analytics pages or reports.

### Dashboard permissions

When you select only **Dashboards - Access**:

- You can access only the **Dashboards** tab.
- You can view historical metrics displayed on dashboards.
- You must have the **Real-time metrics - Access**
  permission to view real-time metrics on dashboards.

![The Dashboards - Access permission on the Security profiles page.](images/dashboards-edit-security-profiles-2.png)

The following image shows that you only have access to the
**Dashboards** tab on the **Dashboards and
reports** page.

![The Dashboards and reports page, access is granted to the Dashboards tab only.](images/dashboard-access.png)

## Custom metrics and permissions

- **Analytics and Optimization - Access metrics** - Access
  permission or the **Dashboard - Access** permission.
- **Analytics and Optimization - Custom metrics**:
  - This permission enables users to view, create and manage custom
    metrics.
  - If you have enabled Next Generation Amazon Connect in your instance, you
    will have the ability to view, create, and manage custom metrics
    with custom filters and functions in addition to custom customer
    service level metric calculations.
