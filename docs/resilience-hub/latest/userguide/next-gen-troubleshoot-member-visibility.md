

# Member account visibility gaps
<a name="next-gen-troubleshoot-member-visibility"></a>

**Symptom:** The delegated administrator cannot see services in a member account.

The following table lists possible causes and solutions.


| Cause | Solution | 
| --- | --- | 
| Service-linked role not yet created | For large organizations, service-linked role creation may take time. Wait and check again. | 
| Account was suspended during setup | Unsuspend the account. The 12-hour reconciliation job will create the service-linked role. | 
| Account recently joined organization | New accounts receive service-linked roles automatically, but there may be a brief delay. | 
| Service trust disabled | Re-enable trusted access from the management account. | 