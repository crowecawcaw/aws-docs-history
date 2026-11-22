

# Remediating exposures for GCP Firestore databases

AWS Security Hub can generate exposure findings for GCP Firestore databases.

On the Security Hub console, the GCP Firestore database involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the `GetFindingsV2` operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Google Cloud resources. 

**Contents**
+ [Misconfiguration traits for GCP Firestore databases](#gcp-firestore-misconfiguration)
  + [The Firestore database has deletion protection disabled](#deletion-protection-disabled)
  + [The Firestore database has point-in-time recovery disabled](#point-in-time-recovery-disabled)

## Misconfiguration traits for GCP Firestore databases
<a name="gcp-firestore-misconfiguration"></a>

Here are misconfiguration traits for GCP Firestore databases and suggested remediation steps.

### The Firestore database has deletion protection disabled
<a name="deletion-protection-disabled"></a>

 Delete protection prevents accidental deletion of a Firestore database, and it's off by default. When it's off, anyone with the `datastore.databases.delete` permission can delete the database and all its documents in one operation, even by mistake. Following data protection best practices, turn on delete protection for your Firestore databases. 

**Remediation: Turn on delete protection**  
 Turn on delete protection for the database. To delete the database later, you must first turn off delete protection. For more information, see [Update the delete protection setting](https://docs.cloud.google.com/firestore/native/docs/manage-databases#update-dp) on the Google Cloud website. 

### The Firestore database has point-in-time recovery disabled
<a name="point-in-time-recovery-disabled"></a>

 Point-in-time recovery (PITR) keeps one version of your data per minute for up to 7 days, so you can recover from accidental deletions or writes. Without PITR, Firestore keeps earlier versions of your data for only 1 hour. Following data protection best practices, turn on PITR for your Firestore databases. 

**Remediation: Turn on point-in-time recovery**  
 Turn on PITR for the database. Firestore keeps PITR data only from the time that you turn it on, and PITR storage has no free tier. For more information, see [Point-in-time recovery (PITR) overview](https://docs.cloud.google.com/firestore/native/docs/pitr) on the Google Cloud website. 