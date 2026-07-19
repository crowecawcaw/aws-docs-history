# Sensitive data detection and redaction output bucket structure

When you set the detection mode to DETECTION\_AND\_REDACTION, BDA creates a
`redacted/` directory for redacted output files, as shown in the following
example.

```
s3-bucket/
    ├── job-id/
       ├── job_metadata.json
       └── 0/
           └── standard_output/
               └── 0/
                   └── redacted/ # directory for redacted standard output
                              └── result.json
                   └── result.json # unredacted file with detected sensitive data
           └── custom_output/
               └── 0/
                   └── redacted/ # directory for redacted custom output
                              └── result.json
                   └── result.json # unredacted file with detected sensitive data
```

With DETECTION mode enabled, BDA does not create the `redacted/` directory. Instead,
BDA includes the detected sensitive data within the existing `result.json`.
