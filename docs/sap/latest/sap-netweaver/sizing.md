# Sizing

[SAP Quick Sizer](https://www.sap.com/about/benchmark/measuring.html "https://www.sap.com/about/benchmark/measuring.html") is generally used to size the SAP environment for new implementations. However, if you are migrating your existing SAP applications based on SQL Server to AWS, consider using the following additional tools to right-size your SAP environment based on current use.

- **SAP Early Watch Alerts (EWA):** SAP EWA reports are provided by SAP regularly. These reports provide an overview of historical system use. Analyze these reports to see if your existing SAP system is overused or underused. You can use this information to right size your environment.
- **Windows native tools:** Gather and analyze historical use data for CPU/Memory with [Performance Monitor/Windows System Resource Manager](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc749154(v=ws.11)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc749154(v=ws.11)") to right size your environment.
- **AWS Application Discovery Service:**
  [AWS Application Discovery Service](../../../application-discovery/latest/userguide/what-is-appdiscovery.md "../../../application-discovery/latest/userguide/what-is-appdiscovery.md") helps with collecting usage and configuration data about your on-premises servers. You can use this information to analyze and right-size your environment.
  Since it is easy to scale up or scale down your Amazon EC2 instances on AWS, we recommend that you consider the following guidelines when sizing your SAP environment on AWS.

- Do not add too much capacity to meet future demand.
- Account for the SAP Quick Sizer buffer. SAP Quick Sizer tools provide sizing guidance based on assumptions that for 100% load (as per your inputs to tool) system use will not exceed 65%. Therefore, there is a fair amount of buffer already built into SAP Quick Sizer recommendation. See [SAP’s Quick Sizer guidance](<https://apps.support.sap.com/sap(bD1lbiZjPTAwMQ==)/bc/bsp/sap/qs_oberflaeche/pdf1.htm?area=QSDOC&filename=QS_for_beg_classic.pdf> "https://apps.support.sap.com/sap(bD1lbiZjPTAwMQ==)/bc/bsp/sap/qs_oberflaeche/pdf1.htm?area=QSDOC&filename=QS_for_beg_classic.pdf") for details.
