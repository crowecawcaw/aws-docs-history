# Amazon Security Lake

Amazon Security Lake automatically centralizes security data from AWS environments,
software as a service (SaaS) providers, on premises and cloud sources into a purpose-built
data lake stored in your AWS account. With Security Lake, you can get a more complete
understanding of your security data across your entire organization. Security Lake has
adopted the Open Cybersecurity Schema Framework (OCSF), an open source security event
schema. With OCSF support, the service normalizes and combines security data from AWS and
a broad range of enterprise security data sources.

## AppFabric audit log ingestion considerations

You can get your SaaS audit logs into Amazon Security Lake in your AWS account by
adding a custom source to Security Lake. The following sections describe the AppFabric
output schema, output format, and output destinations to use with Security Lake.

### Schema and format

Security Lake supports the following AppFabric output schema and format:

- OCSF - JSON
  - AppFabric normalizes the data using the Open Cybersecurity Schema
    Framework (OCSF) and outputs the data in JSON format.

### Output locations

Security Lake supports AppFabric as a custom source using an Amazon Data Firehose delivery stream
as the AppFabric ingestion output location. To configure the AWS Glue table and Firehose
delivery stream, and to set up a custom source in Security Lake, use the following
procedures.

### Create an AWS Glue table

1. Navigate to Amazon Simple Storage Service (Amazon S3) and create a bucket with a name of your
   choice.
2. Navigate to the AWS Glue console.
3. For **Data Catalog**, go to the
   **Tables** section, and choose **Add
   Table**.
4. Enter a name of your choice for this table.
5. Select the Amazon S3 bucket that you created in step 1.
6. For the data format, select **JSON**, and choose
   **Next**.
7. On the **Choose or define schema** page, choose
   **Edit schema as JSON**.
8. Enter the following schema, and complete the AWS Glue table creation
   process.

```
[
    {
        "Name": "message",
        "Type": "string"
    },
    {
        "Name": "process",
        "Type": "struct<name:string,pid:int,user:struct<name:string,type:string,domain:string,uid:string,type_id:int,full_name:string,risk_level:string,risk_score:int>,group:struct<name:string,uid:string>,tid:int,cmd_line:string,container:struct<name:string,size:int,tag:string,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,parent_process:struct<name:string,pid:int,file:struct<name:string,owner:struct<name:string,type:string,uid:string,type_id:int,email_addr:string,risk_level:string,risk_level_id:int,risk_score:int>,type:string,version:string,path:string,uid:string,type_id:int,mime_type:string,parent_folder:string,data_classification:struct<confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,is_system:boolean,modified_time:bigint,xattributes:string>,user:struct<name:string,type:string,uid:string,org:struct<uid:string,ou_name:string>,type_id:int,uid_alt:string>,group:struct<name:string,uid:string,privileges:array<string>>,tid:int,uid:string,cmd_line:string,container:struct<name:string,uid:string,image:struct<name:string,path:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string,pod_uuid:string>,created_time:bigint,namespace_pid:int,auid:int,euid:int,egid:int>>"
    },
    {
        "Name": "status",
        "Type": "string"
    },
    {
        "Name": "time",
        "Type": "bigint"
    },
    {
        "Name": "device",
        "Type": "struct<name:string,owner:struct<name:string,type:string,uid:string,type_id:int,risk_level:string,risk_level_id:int>,type:string,ip:string,hostname:string,mac:string,image:struct<name:string,tag:string,uid:string>,type_id:int,container:struct<name:string,runtime:string,size:bigint,tag:string,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>>,instance_uid:string,interface_name:string,interface_uid:string,namespace_pid:int,network_interfaces:array<struct<name:string,type:string,hostname:string,mac:string,type_id:int>>,region:string,risk_score:int,modified_time_dt:string>"
    },
    {
        "Name": "metadata",
        "Type": "struct<version:string,product:struct<name:string,version:string,uid:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,url_string:string,vendor_name:string>,data_classification:struct<confidentiality:string,confidentiality_id:int>,event_code:string,log_name:string,log_provider:string,original_time:string,tenant_uid:string,processed_time_dt:string>"
    },
    {
        "Name": "severity",
        "Type": "string"
    },
    {
        "Name": "duration",
        "Type": "int"
    },
    {
        "Name": "type_name",
        "Type": "string"
    },
    {
        "Name": "activity_id",
        "Type": "int"
    },
    {
        "Name": "type_uid",
        "Type": "int"
    },
    {
        "Name": "observables",
        "Type": "array<struct<name:string,type:string,type_id:int,value:string>>"
    },
    {
        "Name": "category_name",
        "Type": "string"
    },
    {
        "Name": "class_uid",
        "Type": "int"
    },
    {
        "Name": "category_uid",
        "Type": "int"
    },
    {
        "Name": "class_name",
        "Type": "string"
    },
    {
        "Name": "timezone_offset",
        "Type": "int"
    },
    {
        "Name": "end_time",
        "Type": "bigint"
    },
    {
        "Name": "activity_name",
        "Type": "string"
    },
    {
        "Name": "cloud",
        "Type": "struct<account:struct<name:string,type:string,uid:string,type_id:int>,project_uid:string,provider:string,region:string>"
    },
    {
        "Name": "query_info",
        "Type": "struct<name:string,uid:string,query_string:string>"
    },
    {
        "Name": "query_result",
        "Type": "string"
    },
    {
        "Name": "query_result_id",
        "Type": "int"
    },
    {
        "Name": "severity_id",
        "Type": "int"
    },
    {
        "Name": "status_code",
        "Type": "string"
    },
    {
        "Name": "status_detail",
        "Type": "string"
    },
    {
        "Name": "status_id",
        "Type": "int"
    },
    {
        "Name": "network_interfaces",
        "Type": "array<struct<name:string,type:string,hostname:string,mac:string,type_id:int,ip:string>>"
    },
    {
        "Name": "file",
        "Type": "struct<attributes:int,name:string,type:string,path:string,type_id:int,accessor:struct<name:string,type:string,uid:string,groups:array<struct<name:string,domain:string,uid:string>>,type_id:int,email_addr:string>,creator:struct<name:string,type:string,uid:string,type_id:int,risk_level:string,risk_level_id:int>,parent_folder:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,security_descriptor:string,accessed_time_dt:string,modified_time_dt:string>"
    },
    {
        "Name": "actor",
        "Type": "struct<process:struct<pid:int,file:struct<name:string,size:bigint,type:string,version:string,path:string,type_id:int,parent_folder:string,accessed_time:bigint,confidentiality:string,data_classification:struct<category:string,category_id:int>,is_system:boolean,xattributes:string,modified_time_dt:string>,user:struct<name:string,type:string,uid:string,type_id:int,risk_score:int>,group:struct<name:string>,loaded_modules:array<string>,cmd_line:string,container:struct<name:string,size:int,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,pod_uuid:string>,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,pid:int,file:struct<name:string,type:string,version:string,path:string,type_id:int,parent_folder:string,confidentiality:string,confidentiality_id:int,created_time:bigint,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int,policy:struct<name:string,version:string,uid:string>>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>>,user:struct<name:string,type:string,uid:string,org:struct<name:string,uid:string,ou_name:string>,type_id:int,risk_level:string,uid_alt:string>,group:struct<name:string>,uid:string,cmd_line:string,container:struct<name:string,runtime:string,size:int,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string>,created_time:bigint,integrity:string,namespace_pid:int,parent_process:struct<name:string,file:struct<name:string,type:string,desc:string,modifier:struct<name:string,type:string,uid:string,type_id:int,email_addr:string>,type_id:int,created_time:bigint,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,xattributes:string,created_time_dt:string>,group:struct<name:string,uid:string>,uid:string,loaded_modules:array<string>,cmd_line:string,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>>,sandbox:string,egid:int,created_time_dt:string>,created_time_dt:string>,terminated_time:bigint,auid:int>,user:struct<name:string,type:string,uid:string,type_id:int,credential_uid:string,risk_level:string>,app_name:string,idp:struct<name:string,uid:string>,invoked_by:string>"
    },
    {
        "Name": "dst_endpoint",
        "Type": "struct<owner:struct<name:string,type:string,uid:string,type_id:int,full_name:string,risk_level:string,risk_level_id:int,uid_alt:string>,port:int,type:string,ip:string,location:struct<desc:string,city:string,country:string,coordinates:array<double>,continent:string>,hostname:string,uid:string,type_id:int,autonomous_system:struct<name:string,number:int>,container:struct<name:string,size:int,uid:string,image:struct<name:string,tag:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,orchestrator:string>,hw_info:struct<bios_date:string>,instance_uid:string,interface_name:string,interface_uid:string,namespace_pid:int,svc_name:string>"
    },
    {
        "Name": "src_endpoint",
        "Type": "struct<name:string,owner:struct<name:string,type:string,domain:string,uid:string,org:struct<name:string,uid:string,ou_name:string>,groups:array<struct<uid:string>>,type_id:int,credential_uid:string,email_addr:string,ldap_person:struct<deleted_time:bigint,hire_time:bigint,surname:string,last_login_time_dt:string,hire_time_dt:string,leave_time_dt:string>>,port:int,type:string,ip:string,location:struct<desc:string,city:string,country:string,coordinates:array<double>,continent:string>,hostname:string,uid:string,type_id:int,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,pod_uuid:string>,instance_uid:string,interface_name:string,interface_uid:string,intermediate_ips:array<string>,namespace_pid:int,svc_name:string,vpc_uid:string>"
    },
    {
        "Name": "user",
        "Type": "struct<name:string,type:string,groups:array<struct<name:string,uid:string>>,type_id:int>"
    },
    {
        "Name": "resource",
        "Type": "struct<version:string,uid:string,agent_list:array<struct<name:string,type:string,uid:string,type_id:int,policies:array<struct<name:string,version:string,uid:string>>>>,cloud_partition:string,data_classification:struct<category:string,category_id:int>>"
    },
    {
        "Name": "privileges",
        "Type": "array<string>"
    },
    {
        "Name": "action",
        "Type": "string"
    },
    {
        "Name": "action_id",
        "Type": "int"
    },
    {
        "Name": "protocol_ver",
        "Type": "string"
    },
    {
        "Name": "proxy",
        "Type": "struct<name:string,port:int,type:string,ip:string,hostname:string,uid:string,type_id:int,agent_list:array<struct<name:string,type:string,version:string,uid:string,type_id:int>>,autonomous_system:struct<name:string,number:int>,container:struct<name:string,runtime:string,size:int,uid:string,hash:struct<value:string,algorithm:string,algorithm_id:int>>,instance_uid:string,interface_name:string,interface_uid:string,intermediate_ips:array<string>,namespace_pid:int,proxy_endpoint:struct<name:string,port:int,type:string,ip:string,hostname:string,uid:string,type_id:int,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,uid:string,labels:array<string>>,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string,pod_uuid:string>,instance_uid:string,interface_name:string,interface_uid:string,namespace_pid:int,proxy_endpoint:struct<name:string,port:int,type:string,ip:string,hostname:string,uid:string,type_id:int,autonomous_system:struct<name:string,number:int>,container:struct<name:string,runtime:string,size:bigint,uid:string,image:struct<name:string,tag:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>>,intermediate_ips:array<string>,namespace_pid:int,svc_name:string>,subnet_uid:string,svc_name:string,zone:string>,svc_name:string>"
    },
    {
        "Name": "client_hassh",
        "Type": "struct<algorithm:string,fingerprint:struct<value:string,algorithm:string,algorithm_id:int>>"
    },
    {
        "Name": "authorizations",
        "Type": "array<string>"
    },
    {
        "Name": "proxy_tls",
        "Type": "struct<version:string,certificate:struct<version:string,uid:string,subject:string,issuer:string,fingerprints:array<struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,expiration_time:bigint,serial_number:string>,cipher:string,sni:string,certificate_chain:array<string>,client_ciphers:array<string>,ja3_hash:struct<value:string,algorithm:string,algorithm_id:int>,ja3s_hash:struct<value:string,algorithm:string,algorithm_id:int>>"
    },
    {
        "Name": "load_balancer",
        "Type": "struct<name:string,classification:string,dst_endpoint:struct<owner:struct<type:string,domain:string,uid:string,type_id:int,account:struct<name:string,type:string,uid:string,type_id:int>,credential_uid:string,ldap_person:struct<manager:struct<name:string,type:string,domain:string,uid:string,org:struct<name:string,uid:string,ou_uid:string>,type_id:int>,given_name:string,ldap_dn:string,leave_time:bigint,modified_time:bigint,surname:string>>,port:int,type:string,os:struct<name:string,type:string,type_id:int,edition:string>,ip:string,hostname:string,uid:string,type_id:int,instance_uid:string,interface_name:string,interface_uid:string,namespace_pid:int,svc_name:string,vlan_uid:string>,endpoint_connections:array<struct<code:int,network_endpoint:struct<name:string,owner:struct<name:string,type:string,uid:string,type_id:int,ldap_person:struct<labels:array<string>,created_time:bigint,hire_time:bigint,ldap_dn:string,surname:string,modified_time_dt:string,deleted_time_dt:string>,groups:array<struct<name:string,desc:string,uid:string,type:string>>,full_name:string,email_addr:string,risk_level:string,risk_level_id:int>,port:int,type:string,ip:string,hostname:string,type_id:int,container:struct<name:string,size:int,tag:string,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string>,instance_uid:string,interface_name:string,namespace_pid:int,proxy_endpoint:struct<name:string,owner:struct<name:string,type:string,uid:string,groups:array<struct<name:string,uid:string>>,type_id:int,full_name:string,email_addr:string,risk_score:int,uid_alt:string>,port:int,type:string,hostname:string,uid:string,type_id:int,autonomous_system:struct<name:string,number:int>,container:struct<name:string,size:bigint,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,orchestrator:string,pod_uuid:string>,hw_info:struct<cpu_count:int,cpu_speed:int,keyboard_info:struct<function_keys:int,keyboard_subtype:int>>,instance_uid:string,interface_name:string,interface_uid:string,namespace_pid:int,svc_name:string>,subnet_uid:string,svc_name:string,uid:string,interface_uid:string,intermediate_ips:array<string>>>>,metrics:array<struct<name:string,value:string>>>"
    },
    {
        "Name": "disposition_id",
        "Type": "int"
    },
    {
        "Name": "disposition",
        "Type": "string"
    },
    {
        "Name": "proxy_traffic",
        "Type": "struct<bytes:bigint,packets:int>"
    },
    {
        "Name": "auth_type_id",
        "Type": "int"
    },
    {
        "Name": "proxy_http_response",
        "Type": "struct<code:int,message:string,status:string,length:int>"
    },
    {
        "Name": "server_hassh",
        "Type": "struct<algorithm:string,fingerprint:struct<value:string,algorithm:string,algorithm_id:int>>"
    },
    {
        "Name": "auth_type",
        "Type": "string"
    },
    {
        "Name": "firewall_rule",
        "Type": "struct<version:string,uid:string>"
    },
    {
        "Name": "proxy_connection_info",
        "Type": "struct<direction:string,direction_id:int,protocol_num:int,protocol_ver:string>"
    },
    {
        "Name": "connection_info",
        "Type": "struct<direction:string,direction_id:int>"
    },
    {
        "Name": "api",
        "Type": "struct<request:struct<data:string,uid:string>,response:struct<error:string,code:int,message:string,error_message:string>,operation:string>"
    },
    {
        "Name": "attacks",
        "Type": "array<struct<version:string,tactics:array<struct<name:string,uid:string>>,technique:struct<name:string,uid:string>>>"
    },
    {
        "Name": "raw_data",
        "Type": "string"
    },
    {
        "Name": "email_uid",
        "Type": "string"
    },
    {
        "Name": "malware",
        "Type": "array<struct<name:string,path:string,uid:string,classification_ids:array<int>,cves:array<struct<title:string,uid:string,references:array<string>,created_time:bigint,cvss:array<struct<version:string,base_score:double,metrics:array<struct<name:string,value:string>>,overall_score:double,depth:string>>,modified_time_dt:string,created_time_dt:string,type:string>>,provider:string,classifications:array<string>>>"
    },
    {
        "Name": "start_time_dt",
        "Type": "string"
    },
    {
        "Name": "direction",
        "Type": "string"
    },
    {
        "Name": "smtp_hello",
        "Type": "string"
    },
    {
        "Name": "unmapped",
        "Type": "string"
    },
    {
        "Name": "direction_id",
        "Type": "int"
    },
    {
        "Name": "email_auth",
        "Type": "struct<spf:string,dkim:string,dkim_domain:string,dkim_signature:string,dmarc:string,dmarc_override:string,dmarc_policy:string>"
    },
    {
        "Name": "email",
        "Type": "struct<uid:string,from:string,to:array<string>,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,delivered_to:string,message_uid:string,reply_to:string,smtp_from:string>"
    },
    {
        "Name": "impact_id",
        "Type": "int"
    },
    {
        "Name": "resources",
        "Type": "array<struct<owner:struct<name:string,type:string,uid:string,type_id:int,full_name:string,ldap_person:struct<hire_time:bigint,ldap_cn:string,ldap_dn:string,surname:string,leave_time_dt:string>>,version:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,data:string,labels:array<string>,region:string>>"
    },
    {
        "Name": "finding_info",
        "Type": "struct<title:string,uid:string,attacks:array<struct<version:string,tactics:array<struct<name:string,uid:string>>,technique:struct<name:string,uid:string>>>,analytic:struct<name:string,type:string,version:string,desc:string,uid:string,type_id:int>,last_seen_time:bigint,first_seen_time_dt:string>"
    },
    {
        "Name": "evidences",
        "Type": "array<struct<process:struct<name:string,pid:int,file:struct<name:string,type:string,version:string,path:string,type_id:int,company_name:string,parent_folder:string,confidentiality:string,confidentiality_id:int,created_time:bigint,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,security_descriptor:string,owner:struct<name:string,type:string,uid:string,groups:array<struct<name:string,type:string,domain:string>>,type_id:int,account:struct<name:string,type:string,uid:string,type_id:int>,credential_uid:string,uid_alt:string>,desc:string,accessor:struct<name:string,type:string,uid:string,type_id:int,account:struct<name:string,type:string,uid:string,type_id:int>,email_addr:string>,creator:struct<name:string,type:string,domain:string,uid:string,org:struct<name:string,uid:string>,type_id:int,full_name:string>,modified_time:bigint,modified_time_dt:string>,user:struct<name:string,type:string,uid:string,type_id:int,risk_score:int,full_name:string>,group:struct<name:string,type:string,uid:string>,uid:string,loaded_modules:array<string>,cmd_line:string,container:struct<name:string,size:int,tag:string,uid:string,image:struct<name:string,path:string,uid:string,labels:array<string>>,hash:struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,session:struct<uid:string,issuer:string,created_time:bigint,is_remote:boolean,is_vpn:boolean>,file:struct<attributes:int,name:string,size:int,type:string,path:string,modifier:struct<name:string,type:string,uid:string,type_id:int,full_name:string,credential_uid:string,org:struct<name:string,uid:string,ou_name:string>>,product:struct<name:string,version:string,uid:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,vendor_name:string>,type_id:int,company_name:string,mime_type:string,parent_folder:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,modified_time_dt:string,created_time_dt:string,owner:struct<type:string,domain:string,uid:string,org:struct<name:string,uid:string>,groups:array<struct<name:string,type:string,uid:string,desc:string>>,type_id:int,credential_uid:string,email_addr:string,risk_level:string,risk_level_id:int>,accessed_time:bigint,confidentiality:string,confidentiality_id:int,xattributes:string>,user:struct<name:string,type:string,domain:string,uid:string,type_id:int,account:struct<name:string,type:string,uid:string,type_id:int>,org:struct<name:string,uid:string,ou_name:string>,risk_score:int>,group:struct<uid:string,privileges:array<string>,name:string,type:string,desc:string>,uid:string,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,tag:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,pod_uuid:string>,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,user:struct<name:string,type:string,uid:string,type_id:int,account:struct<name:string,type:string,uid:string,type_id:int>,credential_uid:string,domain:string,risk_level:string>,group:struct<name:string,uid:string,type:string,desc:string>,uid:string,cmd_line:string,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,uid:string,path:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,pod_uuid:string>,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,pid:int,file:struct<name:string,size:bigint,type:string,version:string,modifier:struct<name:string,type:string,type_id:int,risk_score:int>,type_id:int,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,owner:struct<type:string,type_id:int,account:struct<name:string,type:string,uid:string,type_id:int>>,path:string,parent_folder:string,is_system:boolean,security_descriptor:string,accessed_time_dt:string>,user:struct<name:string,org:struct<name:string,uid:string,ou_name:string,ou_uid:string>,type:string,domain:string,uid:string,groups:array<struct<name:string,uid:string>>,type_id:int,account:struct<name:string,type:string,type_id:int>,credential_uid:string,risk_score:int>,uid:string,cmd_line:string,container:struct<name:string,runtime:string,size:bigint,uid:string,image:struct<name:string,tag:string,uid:string,path:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,integrity:string,lineage:array<string>,namespace_pid:int,parent_process:struct<name:string,pid:int,file:struct<name:string,type:string,path:string,uid:string,type_id:int,parent_folder:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,xattributes:string,created_time_dt:string,signature:struct<certificate:struct<version:string,subject:string,issuer:string,fingerprints:array<struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,serial_number:string,created_time_dt:string>,algorithm:string,algorithm_id:int>,accessor:struct<name:string,type:string,uid:string,type_id:int,risk_level:string,risk_level_id:int,uid_alt:string>,company_name:string,mime_type:string,accessed_time:bigint,modified_time_dt:string>,user:struct<type:string,uid:string,type_id:int,credential_uid:string,email_addr:string,ldap_person:struct<labels:array<string>,deleted_time:bigint>,groups:array<struct<name:string,uid:string,desc:string>>,account:struct<name:string,type:string,uid:string,type_id:int>,risk_level:string,risk_score:int,uid_alt:string>,group:struct<name:string,uid:string,privileges:array<string>>,uid:string,cmd_line:string,container:struct<name:string,size:int,uid:string,image:struct<name:string,uid:string,labels:array<string>>,hash:struct<value:string,algorithm:string,algorithm_id:int>,pod_uuid:string>,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,pid:int,file:struct<name:string,type:string,path:string,uid:string,type_id:int,mime_type:string,parent_folder:string,confidentiality:string,confidentiality_id:int,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,security_descriptor:string,modified_time_dt:string>,user:struct<name:string,type:string,domain:string,uid:string,org:struct<uid:string,ou_name:string>,groups:array<struct<name:string,uid:string>>,type_id:int,email_addr:string,ldap_person:struct<labels:array<string>,manager:struct<name:string,type:string,uid:string,org:struct<name:string,uid:string,ou_name:string>,groups:array<struct<name:string,privileges:array<string>>>,type_id:int,full_name:string,risk_level:string,risk_level_id:int>,last_login_time_dt:string>,uid_alt:string>,group:struct<domain:string,uid:string,privileges:array<string>>,uid:string,loaded_modules:array<string>,cmd_line:string,container:struct<name:string,runtime:string,size:bigint,tag:string,uid:string,image:struct<uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,orchestrator:string>,created_time:bigint,integrity:string,namespace_pid:int,parent_process:struct<name:string,pid:int,session:struct<count:int,uid:string,uuid:string,issuer:string,created_time:bigint,is_remote:boolean,is_vpn:boolean,uid_alt:string>,file:struct<attributes:int,name:string,owner:struct<name:string,type:string,domain:string,uid:string,type_id:int,credential_uid:string,email_addr:string>,type:string,path:string,desc:string,uid:string,type_id:int,mime_type:string,parent_folder:string,confidentiality:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int,policy:struct<name:string,version:string,group:struct<name:string>,uid:string>>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,is_system:boolean>,user:struct<name:string,type:string,uid:string,type_id:int,credential_uid:string,risk_level:string>,group:struct<name:string,desc:string,uid:string,privileges:array<string>>,loaded_modules:array<string>,cmd_line:string,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,session:struct<uid:string,issuer:string,created_time:bigint,is_mfa:boolean,is_remote:boolean,created_time_dt:string>,file:struct<name:string,size:bigint,type:string,version:string,path:string,signature:struct<certificate:struct<version:string,uid:string,subject:string,issuer:string,fingerprints:array<struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,expiration_time:bigint,serial_number:string,expiration_time_dt:string>,algorithm:string,algorithm_id:int>,type_id:int,parent_folder:string,created_time:bigint,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,created_time_dt:string>,user:struct<uid:string,risk_level:string>,group:struct<name:string,domain:string>,uid:string,created_time:bigint,namespace_pid:int,auid:int,euid:int,egid:int>,terminated_time:bigint,xattributes:string,euid:int>>,auid:int,terminated_time_dt:string,created_time_dt:string,lineage:array<string>>,egid:int,group:struct<name:string,uid:string>,tid:int,loaded_modules:array<string>,sandbox:string,terminated_time:bigint,xattributes:string,euid:int>,terminated_time:bigint,xattributes:string,terminated_time_dt:string,created_time_dt:string,pid:int,session:struct<issuer:string,created_time:bigint,expiration_reason:string,is_remote:boolean,expiration_time_dt:string>,file:struct<name:string,type:string,path:string,desc:string,modifier:struct<name:string,type:string,uid:string,type_id:int,email_addr:string>,product:struct<name:string,version:string,uid:string,data_classification:struct<confidentiality:string,confidentiality_id:int>,url_string:string,vendor_name:string>,type_id:int,mime_type:string,parent_folder:string,confidentiality:string,created_time:bigint,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int,policy:struct<name:string,version:string,group:struct<type:string,uid:string>,uid:string>>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,modified_time:bigint,accessed_time_dt:string,modified_time_dt:string>,loaded_modules:array<string>,integrity:string,integrity_id:int,lineage:array<string>,egid:int>,terminated_time:bigint,xattributes:string,pid:int,cmd_line:string,auid:int,created_time_dt:string>,xattributes:string,tid:int,integrity:string,euid:int>,file:struct<name:string,type:string,path:string,desc:string,product:struct<name:string,version:string,uid:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,url_string:string,vendor_name:string>,type_id:int,creator:struct<name:string,type:string,uid:string,type_id:int,account:struct<name:string,type:string,uid:string,type_id:int>,credential_uid:string,uid_alt:string>,parent_folder:string,confidentiality:string,confidentiality_id:int,created_time:bigint,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,security_descriptor:string,accessor:struct<name:string,type:string,uid:string,type_id:int,account:struct<name:string,type:string,uid:string,type_id:int>,risk_level:string,risk_level_id:int>,company_name:string,accessed_time_dt:string,created_time_dt:string>,query:struct<type:string,hostname:string,class:string,opcode_id:int,packet_uid:int>,connection_info:struct<direction:string,direction_id:int,protocol_num:int,boundary:string,boundary_id:int,protocol_ver:string,protocol_ver_id:int,tcp_flags:int>,api:struct<request:struct<flags:array<string>,uid:string>,response:struct<error:string,code:int,flags:array<string>,message:string,error_message:string>,operation:string,version:string>,actor:struct<process:struct<name:string,pid:int,file:struct<name:string,type:string,path:string,type_id:int,creator:struct<name:string,type:string,uid:string,type_id:int,email_addr:string>,parent_folder:string,confidentiality:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,modified_time:bigint,xattributes:string,modified_time_dt:string,created_time_dt:string,version:string,desc:string,security_descriptor:string>,uid:string,cmd_line:string,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,uid:string,tag:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,pod_uuid:string,runtime:string,network_driver:string>,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,pid:int,file:struct<name:string,owner:struct<name:string,type:string,uid:string,type_id:int,full_name:string,risk_level:string>,type:string,path:string,desc:string,modifier:struct<name:string,type:string,uid:string,type_id:int>,uid:string,type_id:int,parent_folder:string,confidentiality:string,confidentiality_id:int,data_classification:struct<confidentiality:string,confidentiality_id:int,policy:struct<name:string,version:string,desc:string,uid:string>>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,created_time_dt:string,signature:struct<certificate:struct<version:string,subject:string,issuer:string,fingerprints:array<struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,expiration_time:bigint,serial_number:string>,algorithm:string,algorithm_id:int,created_time:bigint>,product:struct<name:string,uid:string,feature:struct<name:string,version:string,uid:string>,cpe_name:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,vendor_name:string>,accessed_time_dt:string>,user:struct<name:string,type:string,domain:string,uid:string,org:struct<name:string,uid:string,ou_name:string>,type_id:int,account:struct<name:string,uid:string>,ldap_person:struct<labels:array<string>,job_title:string,office_location:string,hire_time_dt:string>,risk_score:int>,group:struct<domain:string,desc:string,uid:string,name:string,type:string>,cmd_line:string,container:struct<name:string,size:int,uid:string,hash:struct<value:string,algorithm:string,algorithm_id:int>,image:struct<tag:string,uid:string>,network_driver:string>,created_time:bigint,integrity:string,integrity_id:int,namespace_pid:int,parent_process:struct<name:string,pid:int,file:struct<attributes:int,name:string,type:string,path:string,signature:struct<digest:struct<value:string,algorithm:string,algorithm_id:int>,algorithm:string,algorithm_id:int>,product:struct<name:string,version:string,uid:string,data_classification:struct<category:string,category_id:int>,vendor_name:string>,uid:string,type_id:int,accessor:struct<name:string,type:string,uid:string,type_id:int>,parent_folder:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,is_system:boolean,xattributes:string,accessed_time_dt:string,modified_time_dt:string>,user:struct<name:string,type:string,uid:string,type_id:int,uid_alt:string,credential_uid:string>,group:struct<name:string,uid:string,domain:string,desc:string>,uid:string,cmd_line:string,container:struct<name:string,size:int,tag:string,uid:string,hash:struct<value:string,algorithm:string,algorithm_id:int>,image:struct<name:string,path:string,uid:string>,orchestrator:string>,created_time:bigint,namespace_pid:int,auid:int,terminated_time_dt:string,integrity:string,integrity_id:int,parent_process:struct<name:string,pid:int,file:struct<attributes:int,name:string,owner:struct<type:string,uid:string,type_id:int,ldap_person:struct<labels:array<string>,cost_center:string,deleted_time:bigint,email_addrs:array<string>,ldap_dn:string,leave_time_dt:string>,risk_level:string,risk_score:int>,type:string,path:string,type_id:int,accessor:struct<name:string,type:string,uid:string>,mime_type:string,parent_folder:string,confidentiality:string,confidentiality_id:int,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,security_descriptor:string,modified_time_dt:string,created_time_dt:string>,user:struct<name:string,type:string,domain:string,uid:string,type_id:int,full_name:string>,loaded_modules:array<string>,cmd_line:string,container:struct<name:string,size:int,uid:string,image:struct<name:string,tag:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string>,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,pid:int,user:struct<name:string,type:string,domain:string,uid:string,type_id:int,account:struct<name:string,type:string,uid:string,labels:array<string>,type_id:int>,risk_level:string,risk_level_id:int>,uid:string,loaded_modules:array<string>,cmd_line:string,container:struct<name:string,runtime:string,size:int,uid:string,image:struct<name:string,uid:string>>,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,pid:int,session:struct<count:int,uid:string,issuer:string,created_time:bigint,is_remote:boolean>,file:struct<name:string,type:string,path:string,desc:string,modifier:struct<name:string,type:string,uid:string,type_id:int,email_addr:string>,type_id:int,creator:struct<name:string,type:string,uid:string,type_id:int,email_addr:string,risk_level:string,risk_level_id:int>,mime_type:string,parent_folder:string,accessed_time:bigint,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,accessed_time_dt:string>,group:struct<name:string,type:string,uid:string>,tid:int,uid:string,cmd_line:string,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,pid:int,file:struct<name:string,size:bigint,type:string,path:string,signature:struct<algorithm:string,algorithm_id:int>,modifier:struct<name:string,type:string,uid:string,type_id:int,account:struct<name:string,uid:string>,uid_alt:string>,type_id:int,mime_type:string,parent_folder:string,accessed_time:bigint,confidentiality:string,confidentiality_id:int,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,is_system:boolean,accessed_time_dt:string>,user:struct<name:string,type:string,domain:string,uid:string,type_id:int>,group:struct<name:string,uid:string,privileges:array<string>>,uid:string,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,tag:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string,orchestrator:string>,created_time:bigint,namespace_pid:int,parent_process:struct<name:string,pid:int,file:struct<name:string,size:bigint,type:string,path:string,signature:struct<certificate:struct<version:string,subject:string,issuer:string,fingerprints:array<struct<value:string,algorithm:string,algorithm_id:int>>,expiration_time:bigint,serial_number:string,created_time_dt:string>,algorithm:string,algorithm_id:int>,uid:string,type_id:int,parent_folder:string,accessed_time:bigint,confidentiality:string,confidentiality_id:int,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,accessed_time_dt:string,modified_time_dt:string,created_time_dt:string>,user:struct<name:string,type:string,domain:string,uid:string,type_id:int,ldap_person:struct<created_time:bigint,deleted_time:bigint,given_name:string,last_login_time:bigint,ldap_cn:string,surname:string>>,group:struct<type:string,domain:string,uid:string>,cmd_line:string,container:struct<name:string,runtime:string,size:int,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,integrity:string,integrity_id:int,lineage:array<string>,namespace_pid:int,parent_process:struct<name:string,pid:int,session:struct<uid:string,issuer:string,created_time:bigint,is_remote:boolean>,file:struct<name:string,type:string,path:string,type_id:int,company_name:string,parent_folder:string,accessed_time:bigint,data_classification:struct<category:string,category_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,security_descriptor:string,xattributes:string>,user:struct<name:string,type:string,uid:string,type_id:int>,group:struct<name:string,uid:string>,uid:string,cmd_line:string,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string>,created_time:bigint,lineage:array<string>,namespace_pid:int,parent_process:struct<name:string,pid:int,file:struct<name:string,type:string,path:string,type_id:int,accessor:struct<name:string,type:string,domain:string,uid:string,org:struct<name:string,uid:string>,type_id:int,risk_level:string>,creator:struct<name:string,type:string,domain:string,uid:string,type_id:int,full_name:string,risk_level:string,risk_level_id:int>,parent_folder:string,accessed_time:bigint,confidentiality:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,accessed_time_dt:string>,user:struct<name:string,type:string,uid:string,org:struct<name:string,uid:string,ou_name:string,ou_uid:string>,type_id:int,account:struct<name:string,type:string,uid:string,type_id:int>,credential_uid:string,risk_level:string>,group:struct<name:string,uid:string>,uid:string,cmd_line:string,container:struct<name:string,size:int,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,parent_process:struct<pid:int,file:struct<name:string,type:string,path:string,signature:struct<certificate:struct<version:string,uid:string,subject:string,issuer:string,fingerprints:array<struct<value:string,algorithm:string,algorithm_id:int>>,expiration_time:bigint,serial_number:string,expiration_time_dt:string>,algorithm:string,algorithm_id:int,created_time_dt:string>,uid:string,type_id:int,accessor:struct<name:string,type:string,uid:string,org:struct<name:string,uid:string,ou_name:string>,type_id:int,credential_uid:string,ldap_person:struct<location:struct<desc:string,city:string,country:string,coordinates:array<double>,continent:string>,deleted_time:bigint,job_title:string,modified_time:bigint,modified_time_dt:string,leave_time_dt:string>,risk_score:int>,parent_folder:string,accessed_time:bigint,data_classification:struct<category:string,confidentiality:string,confidentiality_id:int,policy:struct<name:string,version:string,uid:string>>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,is_system:boolean>,user:struct<name:string,type:string,uid:string,org:struct<name:string,uid:string,ou_name:string>,type_id:int,uid_alt:string>,group:struct<name:string,type:string,desc:string,uid:string,privileges:array<string>>,uid:string,cmd_line:string,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,path:string,uid:string,labels:array<string>>,hash:struct<value:string,algorithm:string,algorithm_id:int>,orchestrator:string,pod_uuid:string>,created_time:bigint,integrity:string,namespace_pid:int,created_time_dt:string>,auid:int>,created_time_dt:string>,sandbox:string>>,terminated_time:bigint,euid:int>,terminated_time:bigint,xattributes:string>>,terminated_time:bigint,egid:int>,auid:int,egid:int,uid:string>,terminated_time_dt:string,user:struct<name:string,uid:string,groups:array<struct<name:string,domain:string,uid:string>>,account:struct<name:string,type:string,uid:string,type_id:int>,email_addr:string,risk_level:string>,group:struct<name:string,uid:string>,integrity:string,integrity_id:int,egid:int>,user:struct<name:string,type:string,uid:string,groups:array<struct<name:string,type:string,privileges:array<string>,desc:string,uid:string>>,type_id:int,risk_level:string,risk_level_id:int,uid_alt:string,full_name:string,credential_uid:string,email_addr:string,ldap_person:struct<last_login_time:bigint,deleted_time_dt:string>>,app_uid:string,authorizations:array<struct<policy:struct<name:string,version:string,uid:string,is_applied:boolean>>>>,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string>,databucket:struct<name:string,type:string,uid:string,type_id:int,created_time:bigint,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,created_time_dt:string>,dst_endpoint:struct<name:string,owner:struct<type:string,uid:string,org:struct<name:string,uid:string,ou_name:string>,type_id:int,full_name:string,account:struct<name:string,type:string,uid:string,labels:array<string>,type_id:int>,credential_uid:string,name:string,groups:array<struct<name:string,type:string,desc:string,uid:string>>,risk_level:string,risk_level_id:int>,port:int,type:string,domain:string,ip:string,hostname:string,uid:string,type_id:int,agent_list:array<struct<name:string,type:string,uid:string,type_id:int,uid_alt:string,version:string,policies:array<struct<name:string,version:string>>>>,autonomous_system:struct<name:string,number:int>,container:struct<name:string,size:bigint,tag:string,uid:string,image:struct<name:string,uid:string,tag:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string,runtime:string,pod_uuid:string>,instance_uid:string,interface_name:string,interface_uid:string,namespace_pid:int,svc_name:string,vlan_uid:string,os:struct<name:string,type:string,type_id:int,lang:string,edition:string>,intermediate_ips:array<string>,proxy_endpoint:struct<name:string,owner:struct<name:string,domain:string,uid:string,groups:array<struct<name:string,uid:string,domain:string,privileges:array<string>>>>,port:int,type:string,ip:string,location:struct<desc:string,city:string,country:string,coordinates:array<double>,continent:string>,uid:string,mac:string,type_id:int,container:struct<name:string,uid:string,image:struct<name:string,path:string,uid:string,labels:array<string>>,hash:struct<value:string,algorithm:string,algorithm_id:int>>,instance_uid:string,interface_uid:string,intermediate_ips:array<string>,namespace_pid:int,svc_name:string,zone:string>>,src_endpoint:struct<name:string,owner:struct<type:string,groups:array<struct<name:string,domain:string,desc:string,uid:string,privileges:array<string>>>,type_id:int,full_name:string,email_addr:string,ldap_person:struct<deleted_time:bigint,ldap_dn:string,last_login_time_dt:string,created_time:bigint,modified_time:bigint,office_location:string>,name:string,uid:string,credential_uid:string>,port:int,type:string,os:struct<name:string,type:string,version:string,type_id:int,lang:string,cpu_bits:int>,domain:string,ip:string,hostname:string,type_id:int,agent_list:array<struct<name:string,type:string,version:string,uid:string,type_id:int>>,container:struct<name:string,size:int,uid:string,hash:struct<value:string,algorithm:string,algorithm_id:int>,network_driver:string>,instance_uid:string,interface_name:string,interface_uid:string,namespace_pid:int,svc_name:string,vlan_uid:string,uid:string,autonomous_system:struct<name:string,number:int>>,database:struct<name:string,type:string,uid:string,groups:array<struct<name:string,uid:string,domain:string,privileges:array<string>>>,type_id:int,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>>>>"
    },
    {
        "Name": "impact",
        "Type": "string"
    },
    {
        "Name": "count",
        "Type": "int"
    },
    {
        "Name": "confidence_id",
        "Type": "int"
    },
    {
        "Name": "enrichments",
        "Type": "array<struct<data:string,name:string,type:string,value:string,provider:string>>"
    },
    {
        "Name": "rcode",
        "Type": "string"
    },
    {
        "Name": "app_name",
        "Type": "string"
    },
    {
        "Name": "rcode_id",
        "Type": "int"
    },
    {
        "Name": "query",
        "Type": "struct<type:string,hostname:string,class:string,opcode_id:int,packet_uid:int>"
    },
    {
        "Name": "proxy_endpoint",
        "Type": "struct<name:string,owner:struct<name:string,type:string,domain:string,uid:string,groups:array<struct<name:string,desc:string,uid:string,privileges:array<string>>>,type_id:int,credential_uid:string,risk_score:int>,port:int,type:string,ip:string,hostname:string,uid:string,type_id:int,autonomous_system:struct<name:string,number:int>,container:struct<name:string,size:bigint,uid:string,image:struct<name:string,uid:string>,hash:struct<value:string,algorithm:string,algorithm_id:int>,pod_uuid:string>,instance_uid:string,interface_uid:string,namespace_pid:int,subnet_uid:string,svc_name:string>"
    },
    {
        "Name": "response_time",
        "Type": "bigint"
    },
    {
        "Name": "delay",
        "Type": "int"
    },
    {
        "Name": "start_time",
        "Type": "bigint"
    },
    {
        "Name": "proxy_http_request",
        "Type": "struct<version:string,url:struct<port:int,scheme:string,path:string,hostname:string,query_string:string,categories:array<string>,category_ids:array<int>,subdomain:string,url_string:string>,user_agent:string,http_headers:array<struct<name:string,value:string>>,referrer:string>"
    },
    {
        "Name": "version",
        "Type": "string"
    },
    {
        "Name": "stratum",
        "Type": "string"
    },
    {
        "Name": "stratum_id",
        "Type": "int"
    },
    {
        "Name": "dispersion",
        "Type": "int"
    },
    {
        "Name": "traffic",
        "Type": "struct<bytes_out:int,chunks:bigint,bytes:int,packets:int,packets_in:bigint>"
    },
    {
        "Name": "precision",
        "Type": "int"
    },
    {
        "Name": "size",
        "Type": "int"
    },
    {
        "Name": "actual_permissions",
        "Type": "int"
    },
    {
        "Name": "base_address",
        "Type": "string"
    },
    {
        "Name": "requested_permissions",
        "Type": "int"
    },
    {
        "Name": "end_time_dt",
        "Type": "string"
    },
    {
        "Name": "compliance",
        "Type": "struct<control:string,status:string,standards:array<string>,status_id:int>"
    },
    {
        "Name": "remediation",
        "Type": "struct<desc:string>"
    },
    {
        "Name": "kb_article_list",
        "Type": "array<struct<os:struct<name:string,type:string,type_id:int,cpe_name:string,edition:string>,title:string,uid:string,severity:string,classification:string,created_time:bigint,size:int,created_time_dt:string>>"
    },
    {
        "Name": "peripheral_device",
        "Type": "struct<name:string,class:string,uid:string,model:string,serial_number:string,vendor_name:string>"
    },
    {
        "Name": "time_dt",
        "Type": "string"
    },
    {
        "Name": "group",
        "Type": "struct<name:string,type:string,uid:string>"
    },
    {
        "Name": "users",
        "Type": "array<struct<name:string,type:string,uid:string,type_id:int,risk_level:string,risk_level_id:int,groups:array<struct<name:string,uid:string>>,uid_alt:string>>"
    },
    {
        "Name": "confidence_score",
        "Type": "int"
    },
    {
        "Name": "state",
        "Type": "string"
    },
    {
        "Name": "state_id",
        "Type": "int"
    },
    {
        "Name": "evidence",
        "Type": "string"
    },
    {
        "Name": "confidence",
        "Type": "string"
    },
    {
        "Name": "risk_level",
        "Type": "string"
    },
    {
        "Name": "risk_score",
        "Type": "int"
    },
    {
        "Name": "impact_score",
        "Type": "int"
    },
    {
        "Name": "risk_level_id",
        "Type": "int"
    },
    {
        "Name": "finding",
        "Type": "struct<title:string,uid:string,modified_time:bigint,modified_time_dt:string,first_seen_time_dt:string>"
    },
    {
        "Name": "user_result",
        "Type": "struct<name:string,type:string,uid:string,type_id:int,account:struct<name:string,uid:string,labels:array<string>>,risk_level:string>"
    },
    {
        "Name": "codes",
        "Type": "array<int>"
    },
    {
        "Name": "command",
        "Type": "string"
    },
    {
        "Name": "type",
        "Type": "string"
    },
    {
        "Name": "kernel",
        "Type": "struct<name:string,type:string,type_id:int>"
    },
    {
        "Name": "http_response",
        "Type": "struct<code:int,status:string,http_headers:array<struct<name:string,value:string>>>"
    },
    {
        "Name": "http_request",
        "Type": "struct<url:struct<scheme:string,path:string,hostname:string,query_string:string,category_ids:array<int>,resource_type:string,subdomain:string,url_string:string>,user_agent:string,http_headers:array<struct<name:string,value:string>>>"
    },
    {
        "Name": "tls",
        "Type": "struct<version:string,certificate:struct<subject:string,issuer:string,fingerprints:array<struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,expiration_time:bigint,serial_number:string>,cipher:string,sni:string,certificate_chain:array<string>,client_ciphers:array<string>,ja3s_hash:struct<value:string,algorithm:string,algorithm_id:int>>"
    },
    {
        "Name": "web_resources",
        "Type": "array<struct<name:string,type:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,url_string:string,data:string>>"
    },
    {
        "Name": "http_cookies",
        "Type": "array<struct<name:string,value:string,is_http_only:boolean,is_secure:boolean,samesite:string,expiration_time_dt:string,path:string>>"
    },
    {
        "Name": "type_id",
        "Type": "int"
    },
    {
        "Name": "databucket",
        "Type": "struct<name:string,type:string,file:struct<attributes:int,name:string,owner:struct<name:string,type:string,uid:string,type_id:int,account:struct<type:string,uid:string,type_id:int>,ldap_person:struct<email_addrs:array<string>,modified_time:bigint,modified_time_dt:string>,risk_score:int>,size:bigint,type:string,path:string,modifier:struct<name:string,type:string,uid:string,groups:array<struct<name:string,domain:string,desc:string,uid:string>>,type_id:int>,type_id:int,parent_folder:string,created_time:bigint,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,accessed_time_dt:string>,uid:string,groups:array<struct<name:string,type:string,uid:string>>,type_id:int,data_classification:struct<category:string,category_id:int,confidentiality:string,policy:struct<version:string,uid:string,is_applied:boolean>>,modified_time_dt:string,created_time_dt:string>"
    },
    {
        "Name": "table",
        "Type": "struct<uid:string,created_time_dt:string>"
    },
    {
        "Name": "session",
        "Type": "struct<count:int,uid:string,uuid:string,issuer:string,created_time:bigint,is_remote:boolean,is_vpn:boolean,uid_alt:string>"
    },
    {
        "Name": "certificate",
        "Type": "struct<version:string,uid:string,subject:string,issuer:string,fingerprints:array<struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,expiration_time:bigint,serial_number:string>"
    },
    {
        "Name": "is_mfa",
        "Type": "boolean"
    },
    {
        "Name": "logon_type_id",
        "Type": "int"
    },
    {
        "Name": "auth_protocol_id",
        "Type": "int"
    },
    {
        "Name": "logon_type",
        "Type": "string"
    },
    {
        "Name": "is_remote",
        "Type": "boolean"
    },
    {
        "Name": "is_cleartext",
        "Type": "boolean"
    },
    {
        "Name": "auth_protocol",
        "Type": "string"
    },
    {
        "Name": "is_renewal",
        "Type": "boolean"
    },
    {
        "Name": "lease_dur",
        "Type": "int"
    },
    {
        "Name": "relay",
        "Type": "struct<name:string,type:string,ip:string,mac:string,namespace:string,type_id:int>"
    },
    {
        "Name": "transaction_uid",
        "Type": "string"
    },
    {
        "Name": "file_result",
        "Type": "struct<name:string,size:int,type:string,path:string,desc:string,product:struct<name:string,version:string,uid:string,lang:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,vendor_name:string>,type_id:int,creator:struct<name:string,type:string,domain:string,uid:string,org:struct<name:string,uid:string,ou_name:string>,groups:array<struct<name:string,uid:string,desc:string>>,type_id:int,risk_level:string>,parent_folder:string,confidentiality:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,modified_time:bigint>"
    },
    {
        "Name": "file_diff",
        "Type": "string"
    },
    {
        "Name": "create_mask",
        "Type": "string"
    },
    {
        "Name": "web_resources_result",
        "Type": "array<struct<type:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,url_string:string>>"
    },
    {
        "Name": "app",
        "Type": "struct<name:string,version:string,uid:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,url_string:string,vendor_name:string>"
    },
    {
        "Name": "src_url",
        "Type": "string"
    },
    {
        "Name": "priority_id",
        "Type": "int"
    },
    {
        "Name": "verdict",
        "Type": "string"
    },
    {
        "Name": "desc",
        "Type": "string"
    },
    {
        "Name": "verdict_id",
        "Type": "int"
    },
    {
        "Name": "priority",
        "Type": "string"
    },
    {
        "Name": "finding_info_list",
        "Type": "array<struct<title:string,uid:string,attacks:array<struct<version:string,tactics:array<struct<name:string,uid:string>>,technique:struct<name:string,uid:string>>>,analytic:struct<name:string,type:string,uid:string,type_id:int>,created_time:bigint,src_url:string,last_seen_time_dt:string,created_time_dt:string,related_analytics:array<struct<name:string,type:string,uid:string,category:string,type_id:int>>,related_events:array<struct<type:string,uid:string,type_name:string,type_uid:bigint,kill_chain:array<struct<phase:string,phase_id:int>>>>,modified_time_dt:string>>"
    },
    {
        "Name": "expiration_time_dt",
        "Type": "string"
    },
    {
        "Name": "expiration_time",
        "Type": "bigint"
    },
    {
        "Name": "comment",
        "Type": "string"
    },
    {
        "Name": "entity",
        "Type": "struct<data:string,name:string,version:string,uid:string>"
    },
    {
        "Name": "entity_result",
        "Type": "struct<data:string,name:string,type:string,version:string,uid:string>"
    },
    {
        "Name": "module",
        "Type": "struct<type:string,file:struct<name:string,type:string,path:string,desc:string,type_id:int,company_name:string,creator:struct<name:string,type:string,domain:string,groups:array<struct<name:string,uid:string>>,type_id:int,risk_level:string>,parent_folder:string,data_classification:struct<confidentiality:string,confidentiality_id:int>,xattributes:string>,base_address:string,function_name:string,load_type:string,load_type_id:int,start_address:string>"
    },
    {
        "Name": "exit_code",
        "Type": "int"
    },
    {
        "Name": "injection_type",
        "Type": "string"
    },
    {
        "Name": "injection_type_id",
        "Type": "int"
    },
    {
        "Name": "request",
        "Type": "struct<uid:string>"
    },
    {
        "Name": "response",
        "Type": "struct<error:string,code:int,message:string,error_message:string>"
    },
    {
        "Name": "driver",
        "Type": "struct<file:struct<name:string,type:string,version:string,path:string,type_id:int,parent_folder:string,created_time:bigint,data_classification:struct<confidentiality:string,confidentiality_id:int,policy:struct<name:string,version:string,uid:string,is_applied:boolean>>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,security_descriptor:string,created_time_dt:string>>"
    },
    {
        "Name": "prev_security_states",
        "Type": "array<string>"
    },
    {
        "Name": "security_states",
        "Type": "array<string>"
    },
    {
        "Name": "folder",
        "Type": "struct<name:string,type:string,path:string,desc:string,type_id:int,mime_type:string,parent_folder:string,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,security_descriptor:string,accessed_time_dt:string>"
    },
    {
        "Name": "url",
        "Type": "struct<port:int,scheme:string,path:string,hostname:string,query_string:string,resource_type:string,url_string:string>"
    },
    {
        "Name": "tunnel_type_id",
        "Type": "int"
    },
    {
        "Name": "tunnel_type",
        "Type": "string"
    },
    {
        "Name": "protocol_name",
        "Type": "string"
    },
    {
        "Name": "job",
        "Type": "struct<name:string,file:struct<name:string,type:string,path:string,signature:struct<certificate:struct<version:string,subject:string,issuer:string,fingerprints:array<struct<value:string,algorithm:string,algorithm_id:int>>,created_time:bigint,expiration_time:bigint,serial_number:string>,algorithm:string,algorithm_id:int,developer_uid:string>,type_id:int,parent_folder:string,confidentiality:string,confidentiality_id:int,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,hashes:array<struct<value:string,algorithm:string,algorithm_id:int>>,security_descriptor:string>,desc:string,cmd_line:string,created_time:bigint,last_run_time:bigint,next_run_time:bigint,run_state:string,run_state_id:int>"
    },
    {
        "Name": "num_trusted_items",
        "Type": "int"
    },
    {
        "Name": "command_uid",
        "Type": "string"
    },
    {
        "Name": "num_registry_items",
        "Type": "int"
    },
    {
        "Name": "num_network_items",
        "Type": "int"
    },
    {
        "Name": "schedule_uid",
        "Type": "string"
    },
    {
        "Name": "num_resolutions",
        "Type": "int"
    },
    {
        "Name": "scan",
        "Type": "struct<name:string,type:string,type_id:int>"
    },
    {
        "Name": "num_detections",
        "Type": "int"
    },
    {
        "Name": "num_processes",
        "Type": "int"
    },
    {
        "Name": "num_files",
        "Type": "int"
    },
    {
        "Name": "total",
        "Type": "int"
    },
    {
        "Name": "num_folders",
        "Type": "int"
    },
    {
        "Name": "dce_rpc",
        "Type": "struct<command:string,flags:array<string>,command_response:string,opnum:int,rpc_interface:struct<version:string,uuid:string,ack_reason:int,ack_result:int>>"
    },
    {
        "Name": "share",
        "Type": "string"
    },
    {
        "Name": "client_dialects",
        "Type": "array<string>"
    },
    {
        "Name": "open_type",
        "Type": "string"
    },
    {
        "Name": "tree_uid",
        "Type": "string"
    },
    {
        "Name": "share_type_id",
        "Type": "int"
    },
    {
        "Name": "share_type",
        "Type": "string"
    },
    {
        "Name": "dialect",
        "Type": "string"
    },
    {
        "Name": "cis_benchmark_result",
        "Type": "struct<name:string>"
    },
    {
        "Name": "vulnerabilities",
        "Type": "array<struct<references:array<string>,severity:string,affected_packages:array<struct<name:string,version:string,architecture:string,path:string,release:string,package_manager:string>>,cve:struct<type:string,uid:string,references:array<string>,created_time:bigint,cvss:array<struct<version:string,depth:string,base_score:double,vector_string:string,severity:string,overall_score:double>>,epss:struct<version:string,created_time:bigint,score:string>,title:string,desc:string,cwe_url:string>,cwe:struct<uid:string,caption:string,src_url:string>,kb_articles:array<string>,kb_article_list:array<struct<os:struct<name:string,type:string,country:string,type_id:int,lang:string,edition:string,sp_name:string,cpe_name:string,build:string,sp_ver:int>,title:string,product:struct<name:string,version:string,feature:struct<name:string,version:string,uid:string>,url_string:string,vendor_name:string>,uid:string,severity:string,created_time:bigint,is_superseded:boolean,classification:string>>,related_vulnerabilities:array<string>,vendor_name:string>>"
    },
    {
        "Name": "service",
        "Type": "struct<name:string,uid:string>"
    },
    {
        "Name": "data_security",
        "Type": "struct<category:string,pattern_match:string,category_id:int,confidentiality:string,confidentiality_id:int,data_lifecycle_state:string,data_lifecycle_state_id:int,detection_system:string,detection_system_id:int,policy:struct<name:string,version:string,group:struct<type:string,uid:string>,desc:string,uid:string>>"
    },
    {
        "Name": "database",
        "Type": "struct<name:string,type:string,uid:string,type_id:int,data_classification:struct<category:string,category_id:int,confidentiality:string,confidentiality_id:int>,modified_time:bigint>"
    }
]
```

### Create a custom source in Security Lake

1. Navigate to the Amazon Security Lake console.
2. Select **Custom sources** in the navigation pane.
3. Choose **Create custom source**.
4. Enter a name for your custom source and select an applicable OCSF event
   class.

###### Note

AppFabric uses **Account Change**,
**Authentication**, **User Access
Management**, **Group Management**,
**Web Resources Activity**, and **Web
Resource Access Activity** event classes. 5. For both **AWS account ID** and **External
ID**, enter your AWS account ID. Then, choose
**Create**. 6. Save the Amazon S3 location of the custom source. You will use it to set up an
Amazon Data Firehose delivery stream.

### Create a delivery stream in Firehose

1. Navigate to the Amazon Data Firehose console.
2. Choose **Create a delivery stream**.
3. For **Source**, select **Direct
   PUT**.
4. For **Destination**, choose
   **S3**.
5. In the **Transform and convert records** section, choose
   **Enable record format conversion** and choose
   **Apache Parquet** as the output
   format.
6. For **AWS Glue table**, choose the AWS Glue table that
   you created in the previous procedure, and choose the latest version.
7. For **Destination settings**, choose the Amazon S3 bucket that
   you created with the Security Lake custom source.
8. For **Dynamic Partitioning**, choose
   **Enabled**.
9. For **Inline parsing for JSON**, choose
   **Enabled**.
   - For **Keyname**, enter
     `eventDayValue`.
   - For **JQ Expression**, enter
     `(.time/1000)|strftime("%Y%m%d")`.

10. For the **S3 bucket prefix**, enter the following
    value.

```
ext/`<custom source name>`/region=`<region>`/accountId=`<account_id>`/eventDay=!{partitionKeyFromQuery:eventDayValue}/
```

Replace `<custom source name>`, `<region>` and
`<account_id>` with your Security Lake custom source name, AWS Region and
AWS account ID. 11. For the **S3 bucket error output prefix**, enter the
following value.

```
ext/AppFabric/error/
```

12. For the **Retry duration**, select
    **300**.
13. For the **Buffer size**, select **128
    MiB**.
14. For the **Buffer interval**, select
    **60s**.
15. Complete the creation process for the Firehose delivery stream.

### Create AppFabric ingestions

To send data to Amazon Security Lake, you must create an ingestion in the AppFabric
console that uses the Firehose delivery stream that you created earlier as the output
location. For more information about configuring AppFabric ingestions to use Firehose as an
output location, see the [Create an output
location](prerequisites.md#create-output-location "prerequisites.md#create-output-location").
