

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/). 

# Sample Schemas
<a name="schemas_sampleschemastopic"></a>

Cloud Directory comes ready with sample schemas for Organizations, Persons, and Devices. The following section lists the various sample schemas and lists the differences for each.

## Organizations
<a name="schemas_organizationsschema"></a>

The following tables list the facets that are included in the *Organizations* sample schema.

 



<table>
<thead>
  <tr><th><b>"Organization" Facet </b></th><th colspan="2"><b>Data Type </b></th><th colspan="2"><b>Length </b></th><th colspan="2"><b>Required Behavior? </b></th><th><b>Description </b></th></tr>
</thead>
<tbody>
  <tr><td>account_id </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Unique id for Organization </td></tr>
  <tr><td>account_name </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Name of Organization </td></tr>
  <tr><td>organization_status </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Status such as 'active', 'suspended', 'inactive', 'closed' </td></tr>
  <tr><td>mailing_address (street1) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical mailing address for this company/entity </td></tr>
  <tr><td>mailing_address (street2) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical mailing address for this company/entity </td></tr>
  <tr><td>mailing_address (city) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical mailing address for this company/entity </td></tr>
  <tr><td>mailing_address (state) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical mailing address for this company/entity </td></tr>
  <tr><td>mailing_address (country) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical mailing address for this company/entity </td></tr>
  <tr><td>mailing_address (postal_code) </td><td colspan="2">String </td><td colspan="2">1024</td><td colspan="2">N </td><td>A physical mailing address for this company/entity </td></tr>
  <tr><td>email </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Email id for Organization </td></tr>
  <tr><td>web_site </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Website URL </td></tr>
  <tr><td>telephone_number </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Telephone number for Organization </td></tr>
  <tr><td>description </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Description for Organization </td></tr>
</tbody>
</table>


 



<table>
<thead>
  <tr><th colspan="2"><b>"Legal_Entity" Facet </b></th><th><b>Data Type</b></th><th colspan="2"><b>Length</b> </th><th colspan="2"><b>Required Behavior?</b> </th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td>registered_company_name </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Legal entity name </td></tr>
  <tr><td>mailing_address (street1) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical registered address for this company/entity </td></tr>
  <tr><td>mailing_address (street2) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical registered address for this company/entity </td></tr>
  <tr><td>mailing_address (city) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical registered address for this company/entity </td></tr>
  <tr><td>mailing_address (state) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical registered address for this company/entity </td></tr>
  <tr><td>mailing_address (country) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical registered address for this company/entity </td></tr>
  <tr><td>mailing_address (postal_code) </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>A physical registered address for this company/entity </td></tr>
  <tr><td>industry_vertical </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Industry Segment </td></tr>
  <tr><td>billing_currency </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Billing currency </td></tr>
  <tr><td>tax_id </td><td colspan="2">String </td><td colspan="2">1024 </td><td colspan="2">N </td><td>Tax identification number </td></tr>
</tbody>
</table>


## Person
<a name="schemas_personschema"></a>

The following tables list the facets that are included in the *Person* sample schema.

 



<table>
<thead>
  <tr><th><b>"Person" Facet</b></th><th colspan="2"><b>Data Type</b></th><th colspan="2"><b>Length</b></th><th colspan="2"><b>Required Behavior?</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td>display_name</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>The name of the user, suitable for display to end-users.</td></tr>
  <tr><td>first_name</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>The given name of the User, or first name in most western languages</td></tr>
  <tr><td>last_name</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>The family name of the User, or last name in most western languages</td></tr>
  <tr><td>middle_name</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>The middle name(s) of the User</td></tr>
  <tr><td>nickname</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>The casual way to address the user in real life, such as, "Bob" or "Bobby" instead of "Robert"</td></tr>
  <tr><td>email</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>Email address for the user</td></tr>
  <tr><td>mobile_phone_number</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>Phone number for the user</td></tr>
  <tr><td>home_phone_number</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>Phone number for the user</td></tr>
  <tr><td>username</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">Y</td><td>unique identifier for the user</td></tr>
  <tr><td>profile</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A URI that is a uniform resource locator and that points to a location representing the user's online profile (such as a webpage)</td></tr>
  <tr><td>picture</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A URI that is a uniform resource locator that points to a resource location representing the user's image.</td></tr>
  <tr><td>website</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>URL</td></tr>
  <tr><td>timezone</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>The User's time zone</td></tr>
  <tr><td>locale</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>Used to indicate the User's default location for purposes of localizing such items as currency, date time format, or numerical representations.</td></tr>
  <tr><td>address (street1)</td><td colspan="3">String</td><td>1024</td><td>N</td><td colspan="2">A physical mailing address for this user.</td></tr>
  <tr><td>address (street2)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for this user.</td></tr>
  <tr><td>address (city)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for this user.</td></tr>
  <tr><td>address (state)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for this user.</td></tr>
  <tr><td>address (country)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for this user.</td></tr>
  <tr><td>address (postal_code)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for this user.</td></tr>
  <tr><td>user_status</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>Value indicating the user's administrative status</td></tr>
</tbody>
</table>


 



<table>
<thead>
  <tr><th><b>"Organization_Person" Facet</b></th><th colspan="2"><b>Data Type</b></th><th colspan="2"><b>Length</b></th><th colspan="2"><b>Required Behavior?</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td>title</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>Title in organization</td></tr>
  <tr><td>preferred_language</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>Indicates the user's preferred written or spoken languages and is generally used for selecting a localized user interface.</td></tr>
  <tr><td>employee_id</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A string identifier, typically numeric or alphanumeric, assigned to a person</td></tr>
  <tr><td>cost_center</td><td colspan="2">Integer</td><td colspan="2">1024</td><td>N</td><td colspan="2">Identifies the cost center</td></tr>
  <tr><td>department</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>Identifies the name of a department</td></tr>
  <tr><td>manager </td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>The user's manager</td></tr>
  <tr><td>company_name</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>Identifies the name of an organization</td></tr>
  <tr><td>company_address (street1)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for the organization</td></tr>
  <tr><td>company_address (street2)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for the organization</td></tr>
  <tr><td>company_address (city)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for the organization</td></tr>
  <tr><td>company_address (state)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for the organization</td></tr>
  <tr><td>company_address (country)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for the organization</td></tr>
  <tr><td>company_address (postalCode)</td><td colspan="2">String</td><td colspan="2">1024</td><td colspan="2">N</td><td>A physical mailing address for the organization</td></tr>
</tbody>
</table>


## Device
<a name="schemas_deviceschema"></a>

The following table lists the facet that is included in the *Device* sample schema.

 



<table>
<thead>
  <tr><th><b>"Device" Facet</b></th><th><b>Data Type</b></th><th colspan="2"><b>Length</b></th><th><b>Required Behavior?</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td>device_id</td><td>String</td><td colspan="2">1024</td><td>N</td><td>Alpha-numeric unique device id</td></tr>
  <tr><td>name</td><td>String</td><td colspan="2">1024</td><td>N</td><td>Friendly name for device</td></tr>
  <tr><td>description </td><td>String</td><td colspan="2">1024</td><td>N</td><td>Description for device </td></tr>
  <tr><td>X.509_certificates</td><td>String</td><td colspan="2">1024</td><td>N</td><td>X.509 Certificate</td></tr>
  <tr><td>device_version</td><td>String</td><td colspan="2">1024</td><td>N</td><td>Device version </td></tr>
  <tr><td>device_os_type</td><td>String</td><td colspan="2">1024</td><td>N</td><td>Operating System on device</td></tr>
  <tr><td>device_os_version</td><td>String</td><td colspan="2">1024</td><td>N</td><td>Operating System version number on device</td></tr>
  <tr><td>serial_number</td><td>String</td><td colspan="2">1024</td><td>N</td><td>Serial number of device</td></tr>
  <tr><td>device_status</td><td>String</td><td colspan="2">1024</td><td>N</td><td>Status for device (such as active, not_active, suspended, shutdown, off)</td></tr>
</tbody>
</table>
