AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Available programs in utility web

application

Utility web application provide support for various legacy platform utility
programs, such as IDCAMS, INFUTILB, SORT, and so on. To configure access to the
application, see [Configure access to utilities for managed
applications](applications-m2-ba-utilities.md "applications-m2-ba-utilities.md").

**List of programs**

- [JCLBCICS utility](#jclbcics "#jclbcics") - Used by batch to set bluesam dataset status to
  open/enabled or closed/disabled.

## JCLBCICS utility

JCLBCICS is a JCL utility program designed to set bluesam dataset to open/enabled or
closed/disabled. An open/enabled status will block access to the dataset from batch
programs while a closed/disabled status makes the dataset unavailable for accessing to
JICS online services.

**Usage**

- JCLBCICS changes STATUS column in Jics FILE_TABLE table and OPEN_STATUS column in
  Bluesam BLUESAM_STATUS table based on groovy configuration on DD name.

```
.open(ddName) -> ENABLED in Jics FILE_TABLE table, OPEN in Bluesam BLUESAM_STATUS table
.close(ddName) -> DISABLED in Jics FILE_TABLE table, CLOSED in Bluesam BLUESAM_STATUS table
```

- DD name size is configurable globally in `application-utility-pgm.yml`
  configuration file.

```
jclbcics.ddname.size: 7
```

- Global DD name size can be overridden in individual step by providing the
  overridden size with the following lines in groovy, then use stepParams as parameters for that step.

```
TreeMap stepMapTransfo = [:]
Map stepParams = ["MapTransfo":stepMapTransfo]
stepParams["MapTransfo"]["JCLBCICS_OVERRIDDEN_SIZE"] = '7'
...
.withParameters(stepParams)
.runProgram("JCLBCICS")
```

- When setting DD name size, max effective DD name size is 8.
- If ddName length is greater than the provided DD name size, it will be truncated
  from the end to match the DD name size.
- Wild card is supported in ddName If \* (asterisk) is appended to the end of
  ddName or ddName length is less than 8.

```
.open("DTSNAME*")
```

**Example code**

```
// DD name with overridden size of 7 bytes
 def stepSTEP007(Object shell, Map params, Map programResults) {
   shell.with {
     if (checkValidProgramResults(programResults)) {
       TreeMap stepMapTransfo = [:]
       Map stepParams = ["MapTransfo":stepMapTransfo]
       stepParams["MapTransfo"]["JCLBCICS_OVERRIDDEN_SIZE"] = '7'
       return execStep("STEP007", "JCLBCICS", programResults, {
         mpr
           .withDatasetsConfiguration(new DatasetsConfiguration()
           .close("DTSNAME"))
           .withParameters(stepParams)
           .runProgram("JCLBCICS")
        })
     }
   }
}
```
