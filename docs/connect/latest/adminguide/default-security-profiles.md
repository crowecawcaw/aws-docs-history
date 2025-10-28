# Default security profiles in Amazon Connect

Amazon Connect includes default security profiles for general roles. You can review the
permissions granted by these profiles and use them if they align with the permissions
that your users need. Otherwise, create a security profile that grants your users only
the permissions they need.

The following table lists the default security profiles.

| Security profile      | Description                                                                                     |
| --------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Admin**             | Grants administrators permission to perform a majority of actions.                              |
| **Agent**             | Grants agents permission to access the CCP.                                                     |
| **CallCenterManager** | Grants managers permission to perform actions related to user management, metrics, and routing. |
| **QualityAnalyst**    | Grants analysts permission to perform actions related to metrics.                               | ###### Note New permissions are added on a regular basis. We recommend revisiting your permission configurations to ensure your users can access the latest Amazon Connect features. |
