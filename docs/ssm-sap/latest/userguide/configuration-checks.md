# Run Configuration Checks with Systems Manager for SAP

You can run configuration checks on your registered SAP applications to validate their setup and ensure they follow best practices. Configuration checks are organized to help you execute checks and understand their results:

- **Configuration Check** - The top level at which checks are executed. Each check comprehensively answers a question such as "Have I chosen the right instance?" or "Is my storage configured correctly?"
- **SubCheck** - A logical grouping used to organize and view results. SubChecks group related information based on how it is gathered or defined. For example, all package status checks or parameters for a specific resource might be grouped into one subcheck.
- **Results** - Individual findings that evaluate a single parameter or configuration point in the system. Results can apply to a resource or be evaluated against the application. For example, "This package is installed on the primary HANA instance" or "Timezone is consistent across both the primary and secondary instances".
  You start configuration checks at the check level, while subchecks and results provide structured ways to view and understand the findings.

###### Topics

- [Run Configuration Checks](#executing-checks "#executing-checks")
- [Reviewing Configuration Check Results](#reviewing-results "#reviewing-results")

## Run Configuration Checks

### Step 1: View Available Checks

View the list of available configuration checks to determine which checks you wish to evaluate for your SAP application.

**Command template**

```
 aws ssm-sap list-configuration-check-definitions --region <REGION_ID>
```

**Example command with sample values**

```
 aws ssm-sap list-configuration-check-definitions --region us-east-1
```

**Example JSON response**

```
 {
    "ConfigurationChecks": [
        {
            "Id": "SAP_CHECK_01",
            "Name": "SAP EC2 Instance Type Selection",
            "Description": "Checks any EC2 Instances Associated with this HANA Application, and evaluates whether the Instance Type complies with SAP Certification requirements and that necessary hardware settings are in place.",
            "ApplicableApplicationTypes": [
                "HANA"
            ]
        },
        {
            "Id": "SAP_CHECK_02",
            "Name": "SAP HANA EBS Storage Configuration",
            "Description": "Application SAP HANA EBS Storage Configuration on Amazon EC2 Instances",
            "ApplicableApplicationTypes": [
                "HANA"
            ]
        },
        {
            "Id": "SAP_CHECK_03",
            "Name": "SAP HANA Pacemaker Configuration",
            "Description": "Application SAP HANA Resilience - Pacemaker Cluster Configuration",
            "ApplicableApplicationTypes": [
                "HANA"
            ]
        }
    ]
}
```

1. Use the check IDs (such as SAP_CHECK_01) when you want to start specific checks rather than running all available checks.

### Step 2: Start Configuration Checks

Start the configuration checks for your application. You can run all available checks specify individual check ids.
If no configuration-check-ids are specified, all checks will be run.

**Command template**

```
 aws ssm-sap start-configuration-checks \
--application-id <APPLICATION_ID> \
--configuration-check-ids <CHECK_ID> \
--region <REGION_ID>
```

**Example command with sample values**

```
 aws ssm-sap start-configuration-checks \
--application-id myHanaApplication \
--configuration-check-ids SAP_CHECK_03 \
--region us-east-1
```

**Example JSON response**

```
 {
    "ConfigurationCheckOperations": [
        {
            "Id": "af3142c1-f178-49e7-a390-ad047e2d518d", //(1)
            "ApplicationId": "myHanaApplication",
            "ConfigurationCheckId": "SAP_CHECK_03",
            "ConfigurationCheckName": "SAP HANA Pacemaker Configuration",
            "ConfigurationCheckDescription": "Application SAP HANA Resilience - Pacemaker Cluster Configuration"
        }
    ]
}
```

1. Take note of this operation ID. You’ll need it to check the status and view results.

### Step 3: Monitor Check Status

The configuration checks may take several minutes to complete. Use the following command to check the status.

**Command template**

```
 aws ssm-sap get-configuration-check-operation --operation-id <OPERATION_ID> --region <REGION_ID>
```

**Example command with sample values**

```
 aws ssm-sap get-configuration-check-operation \
--operation-id 6bd44104-d63c-449d-8007-6c1b471e3e5e \
--region us-east-1
```

**Example JSON response in progress**

```
 {
    "ConfigurationCheckOperation": {
        "Id": "12345678-abcd-efab-cdef-123456789abc",
        "ApplicationId": "HANA_H4H",
        "Status": "INPROGRESS",
        "ConfigurationCheckId": "SAP_CHECK_03",
        "ConfigurationCheckName": "SAP HANA Pacemaker Configuration",
        "ConfigurationCheckDescription": "Application SAP HANA Resilience - Pacemaker Cluster Configuration",
        "StartTime": "2025-08-25T14:11:39.080000+10:00"
    }
}
```

**Example JSON response successful**

```
 {
    "ConfigurationCheckOperation": {
        "Id": "12345678-abcd-efab-cdef-123456789abc",
        "ApplicationId": "HANA_H4H",
        "Status": "SUCCESS",
        "StatusMessage": "Configuration Check operation completed successfully",
        "ConfigurationCheckId": "SAP_CHECK_03",
        "ConfigurationCheckName": "SAP HANA Pacemaker Configuration",
        "ConfigurationCheckDescription": "Application SAP HANA Resilience - Pacemaker Cluster Configuration",
        "StartTime": "2025-08-25T14:11:39.080000+10:00",
        "EndTime": "2025-08-25T14:14:32.262000+10:00",
        "RuleStatusCounts": {
            "Failed": 6,
            "Warning": 5,
            "Info": 10,
            "Passed": 144,
            "Unknown": 0
        }
    }
}
```

## Reviewing Configuration Check Results

Configuration check results are organized hierarchically. Start by identifying the check operation you want to review, then drill down through subchecks to view individual rule results.

### Step 1: List Check Operations

View the history of configuration check operations. Each operation represents a complete execution of one or more configuration checks. You can list all operations or just the latest operation for each check type.

**Command template**

```
 aws ssm-sap list-configuration-check-operations \
--application-id <APPLICATION_ID> \
--region <REGION_ID> \
--list-mode <LIST_MODE>
```

The `--list-mode` parameter accepts two values:

- `ALL_OPERATIONS` (default) - Lists all configuration check operations
- `LATEST_PER_CHECK` - Lists only the most recent operation for each check type

**Example command with sample values**

```
 aws ssm-sap list-configuration-check-operations \
--application-id myHanaApplication \
--region us-east-1 \
--list-mode LATEST_PER_CHECK
```

**Example JSON response**

```
 {
    "ConfigurationCheckOperations": [
        {
            "Id": "12345678-abcd-efab-cdef-123456789abc",
            "ApplicationId": "HANA_H4H",
            "Status": "SUCCESS",
            "StatusMessage": "Configuration Check operation completed successfully",
            "ConfigurationCheckId": "SAP_CHECK_03",
            "ConfigurationCheckName": "SAP HANA Pacemaker Configuration",
            "ConfigurationCheckDescription": "Application SAP HANA Resilience - Pacemaker Cluster Configuration",
            "StartTime": "2025-08-25T14:11:39.080000+10:00",
            "EndTime": "2025-08-25T14:14:32.262000+10:00",
            "RuleStatusCounts": {
                "Failed": 6,
                "Warning": 5,
                "Info": 10,
                "Passed": 144,
                "Unknown": 0
            }
        },
        {
            "Id": "98765432-dcba-abcd-efab-987654321def",
            "ApplicationId": "HANA_H4H",
            "Status": "SUCCESS",
            "StatusMessage": "Configuration Check operation completed successfully",
            "ConfigurationCheckId": "SAP_CHECK_02",
            "ConfigurationCheckName": "SAP HANA EBS Storage Configuration",
            "ConfigurationCheckDescription": "Application SAP HANA EBS Storage Configuration on Amazon EC2 Instances",
            "StartTime": "2025-08-25T14:11:38.961000+10:00",
            "EndTime": "2025-08-25T14:12:35.030000+10:00",
            "RuleStatusCounts": {
                "Failed": 7,
                "Warning": 20,
                "Info": 43,
                "Passed": 40,
                "Unknown": 0
            }
        },
        {
            "Id": "11223344-aabb-ccdd-eeff-112233445566",
            "ApplicationId": "HANA_H4H",
            "Status": "SUCCESS",
            "StatusMessage": "Configuration Check operation completed successfully",
            "ConfigurationCheckId": "SAP_CHECK_01",
            "ConfigurationCheckName": "SAP EC2 Instance Type Selection",
            "ConfigurationCheckDescription": "Checks any EC2 Instances Associated with this HANA Application, and evaluates whether the Instance Type complies with SAP Certification requirements and that necessary hardware settings are in place",
            "StartTime": "2025-08-25T14:11:38.807000+10:00",
            "EndTime": "2025-08-25T14:12:25.237000+10:00",
            "RuleStatusCounts": {
                "Failed": 0,
                "Warning": 2,
                "Info": 8,
                "Passed": 36,
                "Unknown": 0
            }
        }
    ]
}
```

### Step 2: View Sub-Check Results

Each configuration check is divided into subchecks that group related rules together. For example, a subcheck might focus on package status checks or parameters for a specific resource.
list-sub-check-results provides the subcheck-ids which allow you to view the detailed reuslts.

**Command template**

```
 aws ssm-sap list-sub-check-results --operation-id <OPERATION_ID> --region <REGION_ID>
```

**Example command with sample values**

```
 aws ssm-sap list-sub-check-results \
--operation-id 6bd44104-d63c-449d-8007-6c1b471e3e5e \
--region us-east-1
```

**Example JSON response**

```
 {
    "SubCheckResults": [
        {
            "Id": "55667788-1122-3344-5566-778899aabbcc",
            "Name": "Operating System Package Prerequisites",
            "Description": "Validates required Operating System packages for SAP HANA High Availability are installed and aligned between cluster nodes. Requirements are based on known restrictions for Operating System, Version and SAP HANA Revision",
            "References": [
                "[SAP on AWS Hana High Availability Configuration / Red Hat / Prerequisites / Operating System Requirements / Packages](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-os-settings.html#packages)",
                "[SAP on AWS Hana High Availability Configuration / SUSE / Prerequisites / Operating System Requirements / Packages](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-os-settings.html#packages)"
            ]
        },
        {
            "Id": "abcdef12-3456-7890-abcd-ef1234567890",
            "Name": "Linux Systemd Service Configuration",
            "Description": "Validates systemd service status and enablement for required High Availability services including Corosync and Pacemaker",
            "References": [
                "[SAP on AWS Hana High Availability Configuration / Red Hat / Prerequisites / Operating System Requirements](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-os-settings.html)",
                "[SAP on AWS Hana High Availability Configuration / SUSE / Prerequisites / Operating System Requirements](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-sles-os-settings.html)"
            ]
        },
        // additional subchecks
    ]

}
```

**Note** Take note of the sub-check result IDs. You’ll need them to view detailed rule results.

### Step 3: View Rule Results

View the detailed results for each rule within a sub-check.

**Command template**

```
 aws ssm-sap list-sub-check-rule-results --sub-check-result-id <SUB_CHECK_RESULT_ID> --region <REGION_ID>
```

**Example command with sample values**

```
 aws ssm-sap list-sub-check-rule-results \
--sub-check-result-id 197fad22-aa0a-4fbf-a26a-1d2f034ffa46 \
--region us-east-1
```

**Example JSON response**

```
 {
    "RuleResults": [
        {
            "Id": "52df02e1-511d-4023-ba61-617a71c5f0c9",
            "Description": "Pacemaker cluster property 'stonith-enabled' matches SAP HANA cluster recommendations",
            "Status": "PASSED",
            "Message": "STONITH is enabled for cluster fencing",
            "Metadata": {
                "ActualValue": "true",
                "ClusterParameter": "stonith-enabled",
                "Component": "H4H-HDB00",
                "ExpectedValue": "true"
            }
        },
        {
            "Id": "d3501b51-c675-467c-8fd6-76741fafe32a",
            "Description": "Pacemaker cluster property 'stonith-action' matches SAP HANA cluster recommendations",
            "Status": "PASSED",
            "Message": "STONITH action configured for controlled node recovery",
            "Metadata": {
                "ActualValue": "off",
                "ClusterParameter": "stonith-action",
                "Component": "H4H-HDB00",
                "ExpectedValue": "off"
            }
        },
        {
            "Id": "281bbdf3-65c8-4b44-bdef-109190ee6201",
            "Description": "Pacemaker cluster property 'stonith-timeout' matches SAP HANA cluster recommendations",
            "Status": "PASSED",
            "Message": "STONITH timeout configured to allow sufficient time for fencing operations",
            "Metadata": {
                "ActualValue": "600",
                "ClusterParameter": "stonith-timeout",
                "Component": "H4H-HDB00",
                "ExpectedValue": "600"
            }
        },
        // additional rules
    ]
}
```
