Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Supported SARIF properties

Static Analysis Results Interchange Format (SARIF) is an output file format which is available in
software composition analysis (SCA) and static analysis reports in Amazon CodeCatalyst. The following example shows how to manually
configure SARIF in a static analysis report:

```
Reports:
MySAReport:
Format: SARIFSA
IncludePaths:
    - output/sa_report.json
SuccessCriteria:
    StaticAnalysisFinding:
    Number: 25
    Severity: HIGH
```

CodeCatalyst supports the following SARIF properties which can be used to optimize how the analysis results will appear in your reports.

###### Topics

- [sarifLog object](#test.sarif.sarifLog "#test.sarif.sarifLog")
- [run object](#test.sarif.run "#test.sarif.run")
- [toolComponent object](#test.sarif.toolComponent "#test.sarif.toolComponent")
- [reportingDescriptor object](#test.sarif.reportingDescriptor "#test.sarif.reportingDescriptor")
- [result object](#test.sarif.result "#test.sarif.result")
- [location object](#test.sarif.location "#test.sarif.location")
- [physicalLocation object](#test.sarif.physicalLocation "#test.sarif.physicalLocation")
- [logicalLocation object](#test.sarif.logicalLocation "#test.sarif.logicalLocation")
- [fix object](#test.sarif.fix "#test.sarif.fix")

## `sarifLog` object

| Name      | Required | Description                                                                                                                                             |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$schema` | Yes      | The URI of the SARIF JSON schema for version<br>[2.1.0](https://json.schemastore.org/sarif-2.1.0.json "https://json.schemastore.org/sarif-2.1.0.json"). |
| `version` | Yes      | CodeCatalyst only supports SARIF version 2.1.0.                                                                                                         |
| `runs[]`  | Yes      | A SARIF file contains an array of one or more runs, each of which represents a<br>single run of the analysis tool.                                      |

## `run` object

| Name          | Required | Description                                                              |
| ------------- | -------- | ------------------------------------------------------------------------ |
| `tool.driver` | Yes      | A `toolComponent` object that describes the analysis tool.               |
| `tool.name`   | No       | A property that indicates the name of the tool used to perform analysis. |
| `results[]`   | Yes      | The results of the analysis tool that are displayed on CodeCatalyst.     |

## `toolComponent` object

| Name                         | Required | Description                                                                                                                                             |
| ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                       | Yes      | The name of the analysis tool.                                                                                                                          |
| `properties.artifactScanned` | No       | A total number of artifacts analyzed by the tool.                                                                                                       |
| `rules[]`                    | Yes      | An array of `reportingDescriptor` objects that represent rules. Based on<br>these rules, the analysis tool finds problems in the code that is analyzed. |

## `reportingDescriptor` object

| Name                             | Required | Description                                                                                                                                                                                   |
| -------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                             | Yes      | The unique identifier for the rule that is used to reference a finding.<br>Maximum length: 1,024 characters                                                                                   |
| `name`                           | No       | The display name of the rule.<br>Maximum length: 1,024 characters                                                                                                                             |
| `shortDescription.text`          | No       | A shortened description of the rule.<br>Maximum length: 3,000 characters                                                                                                                      |
| `fullDescription.text`           | No       | A complete description of the rule.<br>Maximum length: 3,000 characters                                                                                                                       |
| `helpUri`                        | No       | A string that can be localized to contain the absolute URI of the primary documentation for the rule.<br>Maximum length: 3,000 characters                                                     |
| `properties.unscore`             | No       | A flag that indicates if the scan finding has been scored.                                                                                                                                    |
| `properties.score.severity`      | No       | A fixed set of strings that specify the severity level of the finding.<br>Maximum length: 1,024 characters                                                                                    |
| `properties.cvssv3_baseSeverity` | No       | A qualitative severity rating of [Common Vulnerability Scoring System v3.1](https://www.first.org/cvss/v3.1/specification-document "https://www.first.org/cvss/v3.1/specification-document"). |
| `properties.cvssv3_baseScore`    | No       | A CVSS v3 Base Score ranging from [0.0<br>• 10.0](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss").                                                           |
| `properties.cvssv2_severity`     | No       | If CVSS v3 values are not available, CodeCatalyst searches for CVSS v2 values.                                                                                                                |
| `properties.cvssv2_score`        | No       | A CVSS v2 Base Score ranging from [0.0<br>• 10.0](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss").                                                           |
| `properties.severity`            | No       | A fixed set of strings that specify the severity level of the finding.<br>Maximum length: 1,024 characters                                                                                    |
| `defaultConfiguration.level`     | No       | The default severity of a rule.                                                                                                                                                               |

## `result` object

| Name                             | Required | Description                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ruleId`                         | Yes      | The unique identifier for the rule that is used to reference a finding.<br>Maximum length: 1,024 characters                                                                                                                                                                                                         |
| `ruleIndex`                      | Yes      | The index of the associated rule in the tool component `rules[]`.                                                                                                                                                                                                                                                   |
| `message.text`                   | Yes      | A message that describes the result and displays the message for each finding.<br>Maximum length: 3,000 characters                                                                                                                                                                                                  |
| `rank`                           | No       | A value between 0.0 to 100.0 inclusive that represents the priority or importance of<br>the result. This scale values 0.0 being the lowest priority and 100.0 being the highest priority.                                                                                                                           |
| `level`                          | No       | The severity of the result.<br>Maximum length: 1,024 characters                                                                                                                                                                                                                                                     |
| `properties.unscore`             | No       | A flag that indicates if the scan finding has been scored.                                                                                                                                                                                                                                                          |
| `properties.score.severity`      | No       | A fixed set of strings that specify the severity level of the finding.<br>Maximum length: 1,024 characters                                                                                                                                                                                                          |
| `properties.cvssv3_baseSeverity` | No       | A qualitative severity rating of [Common Vulnerability Scoring System v3.1](https://www.first.org/cvss/v3.1/specification-document "https://www.first.org/cvss/v3.1/specification-document").                                                                                                                       |
| `properties.cvssv3_baseScore`    | No       | A CVSS v3 Base Score ranging from [0.0<br>• 10.0](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss").                                                                                                                                                                                 |
| `properties.cvssv2_severity`     | No       | If CVSS v3 values are not available, CodeCatalyst searches for CVSS v2 values.                                                                                                                                                                                                                                      |
| `properties.cvssv2_score`        | No       | A CVSS v2 Base Score ranging from [0.0<br>• 10.0](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss").                                                                                                                                                                                 |
| `properties.severity`            | No       | A fixed set of strings that specify the severity level of the finding.<br>Maximum length: 1,024 characters                                                                                                                                                                                                          |
| `locations[]`                    | Yes      | The set of locations where the result was detected. Only one location should be included<br>unless the problem can only be corrected by making a change at every specified location. CodeCatalyst<br>uses the first value in the location array to annotate the result.<br>Maximum number of `location` objects: 10 |
| `relatedLocations[]`             | No       | A list of additional locations references in the finding.<br>Maximum number of `location` objects: 50                                                                                                                                                                                                               |
| `fixes[]`                        | No       | An array of `fix` objects that represent the recommendation provided by the scanning tool. CodeCatalyst uses the first recommendation in the `fixes` array.                                                                                                                                                         |

## `location` object

| Name                 | Required | Description                                                               |
| -------------------- | -------- | ------------------------------------------------------------------------- |
| `physicalLocation`   | Yes      | Identifies the artifact and region.                                       |
| `logicalLocations[]` | No       | The set of locations described by name without reference to the artifact. |

## `physicalLocation` object

| Name                   | Required | Description                                                                                                          |
| ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
| `artifactLocation.uri` | Yes      | The URI indicating the location of an artifact, usually a file either in the repository or generated during a build. |
| `fileLocation.uri`     | No       | The fall back URI indicating the location of the file. This is used if `artifactLocation.uri` returns empty.         |
| `region.startLine`     | Yes      | The line number of the first character in the region.                                                                |
| `region.startColumn`   | Yes      | The column number of the first character in the region.                                                              |
| `region.endLine`       | Yes      | The line number of the last character in the region.                                                                 |
| `region.endColumn`     | Yes      | The column number of the last character in the region.                                                               |

## `logicalLocation` object

| Name                 | Required | Description                                                                                           |
| -------------------- | -------- | ----------------------------------------------------------------------------------------------------- |
| `fullyQualifiedName` | No       | Additional information that describes the location of the result.<br>Maximum length: 1,024 characters |

## `fix` object

| Name                                       | Required | Description                                                                                    |
| ------------------------------------------ | -------- | ---------------------------------------------------------------------------------------------- |
| `description.text`                         | No       | A message that displays a recommendation for each finding.<br>Maximum length: 3,000 characters |
| `artifactChanges.[0].artifactLocation.uri` | No       | The URI indicating the location of the artifact that needs to be updated.                      |
