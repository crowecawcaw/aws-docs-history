

# Resources that EDI Cloud Operations backs up
<a name="eco-backup-resources"></a>

The following table lists the AWS resources that ECO backs up for EDI with the default backup plan.


<table>
<thead>
  <tr><th>AWS resource</th><th>Purpose</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>Data Platform</b></td></tr>
  <tr><td>DynamoDB</td><td>Persistent storage for OSDU management data, reference data, and metadata</td></tr>
  <tr><td>Aurora PostgreSQL</td><td>Reservoir Domain Data Management Service (DDMS)</td></tr>
  <tr><td>Amazon S3 (optional)</td><td>Persistent storage for all data records</td></tr>
  <tr><td>Amazon EBS</td><td>Volume storage that Amazon EKS persistent volume claims use. Applications that run in Amazon EKS, such as MongoDB to store data entitlements for authorization, and Amazon OpenSearch Service to store indexes and saved searches, require persistent storage</td></tr>
</tbody>
</table>


**Note**  
By default, ECO doesn't back up the Amazon S3 data from your Data Platform account that contains OSDU data records.

If you require changes to the default backup plan, work with your E-SDM during onboarding. Or submit a service request from your account.