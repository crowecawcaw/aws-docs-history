

# Monitoring authentications with IAM Roles Anywhere subjects
<a name="monitoring-subjects"></a>

You can use the **Subject Activity** tab in the IAM Roles Anywhere console to visualize and audit activities for certificates that are authenticated with IAM Roles Anywhere. A *subject* represents a unique identity defined by the X.509 subject of any certificates you use to authenticate with IAM Roles Anywhere. IAM Roles Anywhere creates a subject for you at the time of authentication if there isn't one already for the X.509 subject. Each subject contains the most recent certificates you have used with IAM Roles Anywhere.

**To view the history of an X.509 subject**

1. Sign in to the [IAM Roles Anywhere console](https://console.aws.amazon.com/rolesanywhere/home). 

1. Navigate to the **Subject activity** tab. 

1. In the list of certificates records grouped by X.509 **Subject**, choose the **Subject** record that you want to check. 

1. On the **Subject details** page, view the details of the subject record. 

1. In the **Certificates** section, you can see the most recent record for certificates authenticated with IAM Roles Anywhere that have the same certificate subject. 

1. Choose the **Serial number** record to view or copy the certificate body. 