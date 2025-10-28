# Updating the AWS Load Balancer resource

details in the ServiceNow CMDB

AWS Load Balancer resources map to the ServiceNow table: Cloud Load Balancer
(`cmdb_ci_cloud_load_balancer`).

The previous table in the Connector was Load Balancer Service
(`cmdb_ci_lb_service`). This change aligns with ServiceNow’s
cloud resource best practices.

###### Note

The following transition steps are required only if you are upgrading from version 3 of the
Connector to version 4.

**Fix Scripts to address changes to ELB mappings in
ServiceNow CMDB**

If you are using AWS Config integration before version 4, the Connector
includes two fix scripts that migrate existing Connector resources in the Load
Balancer Service (`cmdb_ci_lb_service`) table to the Cloud Load Balancer
(`cmdb_ci_cloud_load_balancer`) table.

**Fix Script 1: AWS SMC - Migrate ELB
data**

This fix script migrates ELBv2 data from the legacy Load Balancer Service
(`cmdb_ci_lb_service`) table with `discovery_source`
_AWS Service Management Connector_ to the new
Cloud Load Balancer (`cmdb_ci_cloud_load_balancer`) table with all
the relationships. (Legacy records remain undeleted for audit).

###### Note

The **AWS SMC - Migrate ELB data fix script**
migrates all existing relationships of the ELBv2 resource in Load Balancer
Service (`cmdb_ci_lb_service`), where the discovery source is
_AWS Service Management Connector_ to
the newly created resource in the Cloud Load Balancer
(`cmdb_ci_cloud_load_balancer`) table.

**Fix Script 2: AWS SMC - Delete ELB legacy relationship
(optional)**

This fix script deletes the relationships where a child or parent is a
resource in the original Load Balancer Service (`cmdb_ci_lb_service`)
table, and the discovery source of the resource is _AWS
Service Management Connector_.

###### Note

We recommend you execute **AWS SMC - Delete ELB legacy
relationship fix**
**script** after executing **AWS SMC - Migrate ELB data fix**
**script**, and receiving approvals from your
ServiceNow admin based on your organization’s data retention policies.

###### **To run a fix script in ServiceNow**

1. Log in to your ServiceNow instance as an admin user (for example,
   System Administrator) in the fulﬁller view (Standard user interface
   view).
2. In the filter navigator, enter `System
Definition`.
3. Choose **Fix Scripts**.
4. To migrate resources to the new Cloud Load Balancer table, choose
   **AWS SMC - Migrate ELB data**.

To delete relationships from the Load Balancer Service table, choose
**AWS SMC - Delete ELB legacy relationship fix
script**. 5. Open the fix script to execute. 6. Choose **Run Fix Script**.
