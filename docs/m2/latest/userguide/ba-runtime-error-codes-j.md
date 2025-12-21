AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime Error Codes related to JICS

JICS error codes, prefixed with `BA-J`.

| Key        | Severity | Text                                                                                                                                                                                     | Additional details |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-J0001` | Fatal    | Wrong configuration for JICS XA DataSource. Either correctly configure `datasource.jicsDs.xa.data-source-class-name`<br>and other xa properties, or set `spring.jta.enabled` to `false`. |                    |
