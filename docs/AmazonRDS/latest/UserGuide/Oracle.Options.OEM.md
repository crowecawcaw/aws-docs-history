# Oracle Enterprise Manager

Amazon RDS supports Oracle Enterprise Manager (OEM). OEM is the Oracle product line for integrated management of
enterprise information technology.

Amazon RDS supports OEM on Oracle Database 19c non-CDBs or CDBs, 21c CDBs, and 26ai CDBs. The following table describes
the supported OEM options.

| Option                                                                                                      | Option ID   | Supported OEM releases    |
| ----------------------------------------------------------------------------------------------------------- | ----------- | ------------------------- |
| [OEM Database Express](Appendix.Oracle.Options.OEM_DBControl.md "Appendix.Oracle.Options.OEM_DBControl.md") | `OEM`       | OEM Database Express 19c  |
| [OEM Management Agent](Oracle.Options.OEMAgent.md "Oracle.Options.OEMAgent.md")                             | `OEM_AGENT` | OEM Cloud Control for 13c |

###### Note

You can use OEM Database or OEM Management Agent, but not both. Use OEM Database Express for lightweight,
built-in monitoring of a single database without additional infrastructure. Use OEM Management Agent to manage
the DB instance centrally through an existing Oracle Enterprise Manager Cloud Control installation.
