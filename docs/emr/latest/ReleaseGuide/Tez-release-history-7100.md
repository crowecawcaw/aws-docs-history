# Amazon EMR 7.10.0 - Tez

release notes

## Amazon EMR 7.10.0 -

Tez changes

| Type    | Description                                                                                                                                                                                                                                                                                                                 |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bug Fix | [TEZ-4595](https://issues.apache.org/jira/browse/TEZ-4595 "https://issues.apache.org/jira/browse/TEZ-4595"): Fixed a bug where Tez would crash when trying to process a new DAG while it was still recovering from a previous failure, causing both DAGs to interfere with each other and throw an INVALID_EVENT exception. | **Tez release notes** Bug fix notes – The issue occurred when recovery files were present and the Application Master transitioned through RECOVERING → IDLE → RUNNING → IDLE states, creating a brief window where Hive could submit new DAGs during the IDLE → RUNNING transition. Modified the state transition logic to skip IDLE state when recovery files are present. The AM now follows RECOVERING → RUNNING → IDLE flow, ensuring new DAG submission only occurs after the recovered DAG is fully cleaned up. |
