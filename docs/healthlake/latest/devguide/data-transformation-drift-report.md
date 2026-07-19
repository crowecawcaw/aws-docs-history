# Understanding drift reports

When drift detection is enabled, the bulk job writes an aggregate report named
`jobLevelDriftResult.json` to your output location. The report tells
you how much of your source data the profile actually captured, and what it missed:
so you know where to improve your mappings.

The report's structure depends on the source format: C-CDA reports are organized
around document sections and entries (identified by OIDs), while CSV reports are organized
around tables, columns, and rows. Both share the same coverage-rate concept (a fraction
from 0.0 to 1.0, where higher means more of your source was captured).

- [C-CDA drift report](#data-transformation-drift-report-ccda "#data-transformation-drift-report-ccda")
- [CSV drift report](#data-transformation-drift-report-csv "#data-transformation-drift-report-csv")
- [Improving coverage (both formats)](#data-transformation-drift-report-improving "#data-transformation-drift-report-improving")

## C-CDA drift report

```
{
  "jobId": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6",
  "profileId": "0f1e2d3c4b5a69788796a5b4c3d2e1f0",
  "profileVersion": 3,
  "timestamp": "2026-07-14T18:30:00Z",
  "filesProcessed": 500,
  "totalFilesFailed": 2,
  "avgSectionCoverageRate": 0.92,
  "avgEntryCoverageRate": 0.85,
  "avgOverallCoverageRate": 0.88,
  "avgResourceAccuracy": 0.97,
  "totalUnknownSections": 14,
  "totalUnknownEntries": 63,
  "documentOids": {
    "2.16.840.1.113883.10.20.22.1.2": 480
    },
  "unknownSectionOidCount": 2,
  "unknownSections": {
    "2.16.840.1.113883.10.20.22.2.14": 12
    },
  "unknownEntryOidCount": 5,
  "unknownEntries": {
    "2.16.840.1.113883.10.20.22.4.13": 40
    },
  "missingResources": {
    "2.16.840.1.113883.10.20.22.2.6.1": {
      "AllergyIntolerance": 8
      }
    },
  "perFileDrift": {
    "patient-001.xml": 0.95,
    "patient-002.xml": 0.61
    }
}
```

### How to read it

Start with the coverage rates. These are averages across all processed files,
expressed as a fraction from 0.0 to 1.0 (multiply by 100 for a percentage).
Higher is better: a higher rate means more of your source data made it
into the FHIR output.

| Field                    | What it means                                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `avgOverallCoverageRate` | The headline number. The average fraction of source content<br>(sections + entries) that the profile mapped to FHIR. 0.88<br>means ~88% of your source data was captured. |
| `avgSectionCoverageRate` | Average fraction of C-CDA sections (for example, Problems,<br>Medications, Allergies) that were mapped.                                                                   |
| `avgEntryCoverageRate`   | Average fraction of individual entries within sections (for<br>example, a single problem or medication) that were mapped.                                                 |
| `avgResourceAccuracy`    | Of the FHIR resources that were expected, the average<br>fraction that were actually produced.                                                                            |

Then find what was missed. These fields point you to the specific mappings to add:

| Field                                             | What it means                                                                                      | What to do                                                      |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `unknownSections`                                 | A map of source section OIDs the profile did not recognize,<br>and how many times each appeared.   | Add mappings for the high-count section OIDs.                   |
| `unknownEntries`                                  | A map of source entry OIDs the profile did not recognize,<br>and their frequency.                  | Add mappings for the high-count entry OIDs.                     |
| `missingResources`                                | A map of source OID → the FHIR resource types that<br>were expected but not produced, with counts. | Fix the mappings that should have generated those<br>resources. |
| `totalUnknownSections` /<br>`totalUnknownEntries` | Total counts of unmapped sections and entries across the<br>job.                                   | Use as a quick "how much is left" signal.                       |
| `documentOids`                                    | A map of the C-CDA document-type OIDs seen in the job, and<br>how many of each.                    | Confirms which document types your data contains.               |

Prioritize by frequency. The counts in `unknownSections`,
`unknownEntries`, and `missingResources` tell you which
gaps affect the most records. An OID that appears 40 times is a bigger win to
map than one that appears twice.

Drill into specific files. `perFileDrift` maps each source file to
its overall coverage rate. Sort by the lowest values to find the files the
profile handled worst: for example, `patient-002.xml`
at 0.61 is worth inspecting. For a full per-file breakdown (which specific OIDs
each file missed), see the individual reports under the
`driftDetectionPerFileResults/` folder.

### Improving coverage

1. Identify the highest-frequency entries in `unknownSections`,
   `unknownEntries`, and
   `missingResources`.
2. Use the Data Transformation AI agent (`UpdateProfileWithAgent`) to add
   mappings for those OIDs and resources: you can paste an OID and
   ask the agent to map it.
3. Publish a new profile version and re-run the job.
4. Compare the new `avgOverallCoverageRate` to confirm the
   gap closed.

## CSV drift report

For CSV jobs, the report is organized around tables (each CSV file is a table),
columns, and rows: not sections and OIDs.

```
{
  "jobId": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6",
  "profileId": "0f1e2d3c4b5a69788796a5b4c3d2e1f0",
  "profileVersion": 3,
  "summary": {
    "totalTablesInProfile": 4,
    "totalTablesInInput": 5,
    "tablesProcessed": 4,
    "tablesUnmapped": 1,
    "totalColumnsInInput": 42,
    "columnsMapped": 35,
    "columnsUnmapped": 7,
    "totalRowsScanned": 120000,
    "rowsConvertedSuccessfully": 119850,
    "rowsFailedCustomerError": 140,
    "rowsFailedServerError": 10,
    "totalResourcesGenerated": 245000,
    "tablesCoverageRate": 0.80,
    "columnsCoverageRate": 0.83,
    "overallCoverageRate": 0.83
  },
  "unmappedTables": [
    {
      "tableName": "billing",
      "fileName": "billing.csv",
      "reason": "No matching table declared in the mapping profile",
      "columns": ["invoice_id", "amount", "payer"]
    }
  ],
  "unmappedColumns": [
    {
      "tableName": "patients",
      "columns": ["preferred_language", "ethnicity_detail"],
      "reason": "Present in CSV but not referenced by any field mapping"
    }
  ]
}
```

### How to read it

Start with the summary. The coverage rates are fractions from 0.0 to 1.0
(higher is better):

| Field                 | What it means                                                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `overallCoverageRate` | The headline number: the fraction of all columns<br>across all input tables that your profile actually uses. 0.83<br>means ~83% of your source columns are mapped. |
| `tablesCoverageRate`  | Fraction of your input CSV files (tables) that the profile<br>maps (`tablesProcessed` /<br>`totalTablesInInput`).                                                  |
| `columnsCoverageRate` | Fraction of columns in the mapped tables that are referenced<br>by a field mapping.                                                                                |

Then check the counts to understand conversion outcomes:

| Field                                                             | What it means                                                       |
| ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| `totalTablesInInput` vs<br>`tablesProcessed`                      | How many of your CSV files were actually used vs.<br>found.         |
| `totalColumnsInInput` /<br>`columnsMapped` /<br>`columnsUnmapped` | How many source columns exist, were used, and were<br>ignored.      |
| `totalRowsScanned` /<br>`rowsConvertedSuccessfully`               | How many rows were read vs. successfully converted.                 |
| `rowsFailedCustomerError` /<br>`rowsFailedServerError`            | Rows that failed due to data-quality issues vs. internal<br>errors. |
| `totalResourcesGenerated`                                         | Total FHIR resources produced.                                      |

Then find what was missed:

| Field             | What it means                                                                                                | What to do                                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `unmappedTables`  | CSV files in your input that the profile does not declare<br>(with the reason and the columns in that file). | Add a table mapping if that file should be<br>converted.           |
| `unmappedColumns` | Per table, the columns present in the CSV but not used by<br>any field mapping.                              | Add field mappings for the columns you want in the FHIR<br>output. |

## Improving coverage (both formats)

1. Identify the highest-impact gaps: for C-CDA, the
   highest-frequency entries in
   `unknownSections`/`unknownEntries`/`missingResources`;
   for CSV, the entries in `unmappedTables`,
   `unmappedColumns`, and warnings.
2. Use the Data Transformation AI agent (`UpdateProfileWithAgent`) to add the
   missing mappings: you can paste an unmapped OID (C-CDA) or column
   name (CSV) and ask the agent to map it.
3. Publish a new profile version and re-run the job.
4. Compare the new `overallCoverageRate` to confirm the gap
   closed.

###### Note

Drift detection reports what a profile did not map; it does not indicate a
conversion error. Source data can be intentionally left unmapped if it is not
relevant to your use case. Use the report to decide what is worth
mapping.
