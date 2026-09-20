

# Constructing an Amazon Resource Name (ARN) for AWS DMS
<a name="CHAP_Introduction.AWS.ARN"></a>

If you use the AWS CLI or AWS DMS API to automate your database migration, then you work with Amazon Resource Name (ARNs). Each resource that is created in Amazon Web Services is identified by an ARN, which is a unique identifier. If you use the AWS CLI or AWS DMS API to set up your database migration, you supply the ARN of the resource that you want to work with. 

An ARN for an AWS DMS resource uses the following syntax:

`arn:aws:dms:{{region}}:{{account number}}:{{resourcetype}}:{{resourcename}}`

In this syntax, the following apply:
+ {{`region`}} is the ID of the AWS Region where the AWS DMS resource was created, such as `us-west-2`.

  The following table shows AWS Region names and the values that you should use when constructing an ARN.


<table>
<thead>
  <tr><th>Region</th><th>Name</th></tr>
</thead>
<tbody>
  <tr><td>Asia Pacific (Tokyo) Region</td><td>ap-northeast-1</td></tr>
  <tr><td>Asia Pacific (Seoul) Region</td><td>ap-northeast-2</td></tr>
  <tr><td>Asia Pacific (Mumbai) Region</td><td>ap-south-1</td></tr>
  <tr><td>Asia Pacific (Singapore) Region</td><td>ap-southeast-1</td></tr>
  <tr><td>Asia Pacific (Sydney) Region</td><td>ap-southeast-2</td></tr>
  <tr><td>Canada (Central) Region</td><td>ca-central-1</td></tr>
  <tr><td>China (Beijing) Region</td><td>cn-north-1 </td></tr>
  <tr><td>China (Ningxia) Region</td><td>cn-northwest-1</td></tr>
  <tr><td>Europe (Stockholm) Region</td><td>eu-north-1</td></tr>
  <tr><td>Europe (Milan) Region</td><td>eu-south-1</td></tr>
  <tr><td>EU (Frankfurt) Region</td><td>eu-central-1</td></tr>
  <tr><td>Europe (Ireland) Region</td><td>eu-west-1</td></tr>
  <tr><td>EU (London) Region</td><td>eu-west-2</td></tr>
  <tr><td>EU (Paris) Region</td><td>eu-west-3</td></tr>
  <tr><td>South America (São Paulo) Region</td><td>sa-east-1</td></tr>
  <tr><td>US East (N. Virginia) Region</td><td>us-east-1</td></tr>
  <tr><td>US East (Ohio) Region</td><td>us-east-2</td></tr>
  <tr><td>US West (N. California) Region</td><td>us-west-1</td></tr>
  <tr><td>US West (Oregon) Region</td><td>us-west-2</td></tr>
</tbody>
</table>

+ `{{account number}}` is your account number with dashes omitted. To find your account number, sign in to your AWS account at http://aws.amazon.com, choose **My Account/Console**, and then choose **My Account**.
+ *{{`resourcetype`}}* is the type of AWS DMS resource.

  The following table shows the resource types to use when constructing an ARN for a particular AWS DMS resource. 


<table>
<thead>
  <tr><th>AWS DMS resource type</th><th>ARN format</th></tr>
</thead>
<tbody>
  <tr><td>Replication instance </td><td><code>arn:aws:dms:region: account:rep: resourcename </code></td></tr>
  <tr><td>Endpoint</td><td><code>arn:aws:dms:region:account:endpoint: resourcename </code></td></tr>
  <tr><td>Replication task</td><td><code>arn:aws:dms:region:account:task:resourcename </code></td></tr>
  <tr><td>Subnet group</td><td><code>arn:aws:dms:region:account:subgrp:resourcename </code></td></tr>
</tbody>
</table>

+ {{`resourcename`}} is the resource name assigned to the AWS DMS resource. This is a generated arbitrary string.

The following table shows examples of ARNs for AWS DMS resources. Here, we assume an AWS account of 123456789012, which were created in the US East (N. Virginia) Region, and has a resource name. 


| Resource type | Sample ARN | 
| --- | --- | 
| Replication instance  | arn:aws:dms:us-east-1:123456789012:rep:QLXQZ64MH7CXF4QCQMGRVYVXAI   | 
| Endpoint  | arn:aws:dms:us-east-1:123456789012:endpoint:D3HMZ2IGUCGFF3NTAXUXGF6S5A  | 
| Replication task | arn:aws:dms:us-east-1:123456789012:task:2PVREMWNPGYJCVU2IBPTOYTIV4  | 
| Subnet group | arn:aws:dms:us-east-1:123456789012:subgrp:test-tag-grp  | 