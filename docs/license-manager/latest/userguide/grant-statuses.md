# License status for grants in License Manager

Licenses have two statuses: The **License status**, which shows the
overall availability and sharability of the license, and the **Grant
status**, which shows the ability to use the license.

The follow table shows the various statuses for a granted license:

| Status            | Description                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------- |
| AVAILABLE         | The license is available to use and share.                                                    |
| PENDING_AVAILABLE | The license is not available to use as it is still processing.                                |
| DEACTIVATED       | The license is not available to use because it has been deactivated by the<br>license issuer. |
| SUSPENDED         | The license is not available to use as it is suspended.                                       |
| EXPIRED           | The license is not available to use because it has reached the end of<br>term.                |
| PENDING_DELETE    | The license is not available to use as it is in the process of being<br>deleted.              |
| DELETED           | The license is not available to use because the license agreement has<br>been canceled.       |

The following table shows the various statuses for a grant:

| Status            | Description                                                                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PENDING_WORKFLOW  | The grant is in the process of being distributed.                                                                                                         |
| PENDING_ACCEPT    | The grant has been created and the grant recipient has not yet accepted<br>it.                                                                            |
| REJECTED          | The grant has been rejected by the grant recipient.                                                                                                       |
| ACTIVE            | The grant has been accepted and activated for use by the grant recipient.<br>The licensed resource can be used.                                           |
| FAILED_WORKFLOW   | The grant failed to distribute.                                                                                                                           |
| DELETED           | The grant has been deleted by the grantor.                                                                                                                |
| PENDING_DELETE    | The grant that was distributed is in the process of being deleted.                                                                                        |
| DISABLED          | The grant has been accepted by the grant recipient, but has not been<br>activated for use.                                                                |
| WORKFLOW_COMPLETE | The grant to an organization has been distributed or recalled. The grant<br>details show the status of sub-grants to each account in the<br>organization. |
