# Configure FedRAMP authorization or DoD SRG

compliance for WorkSpaces Pools

To comply with the [Federal Risk and
Authorization Management Program (FedRAMP)](https://aws.amazon.com/compliance/fedramp/ "https://aws.amazon.com/compliance/fedramp/") or the [Department of Defense (DoD) Cloud Computing
Security Requirements Guide (SRG)](https://aws.amazon.com/compliance/dod/ "https://aws.amazon.com/compliance/dod/"), you must configure Amazon WorkSpaces Pools to use
Federal Information Processing Standards (FIPS) endpoint encryption at the directory
level. You must also use a US AWS Region that has FedRAMP authorization or is DoD SRG
compliant.

The level of FedRAMP authorization (Moderate or High) or DoD SRG Impact Level (2, 4, or 5) depends on the US AWS Region in which Amazon WorkSpaces is being used. For the levels of FedRAMP
authorization and DoD SRG compliance that apply to each Region, see [AWS Services in Scope by
Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").

###### Requirements

- The WorkSpaces Pools directory must be configured to use **FIPS 140-2
  Validated Mode** for endpoint encryption.

###### Note

To use the **FIPS 140-2 Validated Mode** setting, ensure
the following:

    + The WorkSpaces Pools directory is either:




    	- New and not associated with a Pool
    	- Associated with an existing Pool that is in the STOPPED state

    + The Pool directory has [`StreamingExperiencePreferredProtocol`](../api/API_ModifyStreamingProperties.md "../api/API_ModifyStreamingProperties.md") set to TCP.

- You must create your WorkSpaces Pools in a [US AWS Region that has
  FedRAMP authorization or is DoD SRG-compliant](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- Users must access their WorkSpaces from one of the following WorkSpaces client
  applications:
  - macOS: 5.20.0 or later
  - Windows: 5.20.0 or later
  - Web Access

###### To use FIPS endpoint encryption

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories** then choose
   the directory that you want to use for FedRAMP authorization and DoD SRG
   compliance.
3. On the **Directory Details** page, choose the directory that
   you want to configure for FIPS encryption mode.
4. In the **Endpoint encryption** section, choose
   **Edit** and then select **FIPS 140-2 Validated
   Mode**.
5. Choose **Save**.
