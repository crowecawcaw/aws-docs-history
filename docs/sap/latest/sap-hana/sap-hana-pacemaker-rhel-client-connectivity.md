# Client Connectivity

For proper SAP HANA database connectivity:

- Ensure that the Overlay IP can be correctly resolved in all application servers
- DNS configuration or local host entries must be valid
- Network routing must be properly configured
- SAP HANA client libraries must be installed and up to date
  Ensure that the connectivity data for the SAP HANA Database references the hostname associated with the Overlay IP.
  For more information see SAP Documentation: [Setting Connectivity Data for the SAP HANA Database](https://help.sap.com/docs/SLTOOLSET/39c32e9783f6439e871410848f61544c/b7ed2d55b0a7f857e10000000a441470.html?version=CURRENT_VERSION_SWPM20 "https://help.sap.com/docs/SLTOOLSET/39c32e9783f6439e871410848f61544c/b7ed2d55b0a7f857e10000000a441470.html?version=CURRENT_VERSION_SWPM20")

Test database connectivity using R3trans utility:

```
 sidadm> R3trans -d
```

Review additional connections to SAP HANA that require High Availability. While application connectivity should use the overlay IP, administrative tools (SAP HANA Studio, hdbsql commands, monitoring tools) require direct connectivity to individual SAP HANA instances.
