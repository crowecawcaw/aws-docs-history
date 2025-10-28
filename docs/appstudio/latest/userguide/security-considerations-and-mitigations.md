# Security considerations and mitigations

## Security considerations

When dealing with data connectors, data models, and published applications,
several security concerns arise related to data exposure, access control, and potential
vulnerabilities. The following list includes the primary security concerns.

### Improper configuration of IAM roles

Incorrect configuration of IAM roles for data connectors can lead to unauthorized access and data leaks.
Granting overly permissive access to a data connector's IAM role can allow unauthorized users to access and
modify sensitive data.

### Using IAM roles to perform data operations

Since end users of an App Studio app assume the IAM role provided in the connector
configuration to perform actions, those end users might get access to data to which they typically do not have access.

### Deleting data connectors of published applications

When a data connector is deleted, the associated secret credentials are not
automatically removed from published applications that are already using that connector.
In this scenario, if an application has been published with certain connectors, and one of
those connectors is deleted from App Studio, the published application will continue to
work using the previously stored connector credentials. It is important to note that the published
app will remain unaffected and operational despite the connector deletion.

### Editing data connectors on published applications

When a data connector is edited, the changes are not automatically reflected in
published applications that are using that connector. If an application has been published
with certain connectors, and one of those connectors is modified in App Studio,
the published application will continue to use the previously stored connector configuration and
credentials. To incorporate the updated connector changes, the application must be republished.
Until the app is republished, it will remain incorrect and non-operational, or unaffected and operational
but will not reflect the latest connector modifications.

## Security risk mitigation recommendations

This section lists mitigation recommendations to avoid security risks detailed in the
previous security considerations section.

1. **Proper IAM role configuration:** Ensure that IAM
   roles for data connectors are correctly configured with the principle of least privilege to prevent
   unauthorized access and data leaks.
2. **Restricted app access:** Only share your apps with
   users who are authorized to view or perform actions on the application data.
3. **App publishing:** Ensure that apps are republished
   whenever a connector is updated or deleted.
