# Requirements and

limitations

The following topic lists the requirements and limitations for Oracle APEX and
ORDS.

## Oracle APEX version

requirements

The `APEX` option uses storage on the DB instance class for your DB instance. Following
are the supported versions and approximate storage requirements for Oracle
APEX.

| Oracle APEX version         | Storage requirements | Supported Oracle Database versions | Notes                                                                                                                                                                                                                                                                                    |
| --------------------------- | -------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Oracle APEX version 24.2.v1 | 114 MiB              | All                                | This version includes patch 37885097: PSE BUNDLE FOR APEX 24.2<br>(PSES ON TOP OF 24.2.0), PATCH_VERSION 4.                                                                                                                                                                              |
| Oracle APEX version 24.1.v1 | 112 MiB              | All                                | This version includes patch 36695709: PSE BUNDLE FOR APEX 24.1<br>(PSES ON TOP OF 24.1.0), PATCH_VERSION 3. If you need exactly<br>the same APEX images version to install on your EC2 instance,<br>download patch 37544819: 24.1.3 PSE BUNDLE FOR APEX 24.1 (PSES<br>ON TOP OF 24.1.0). |
| Oracle APEX version 23.2.v1 | 110 MiB              | All                                | This version includes patch 35895964: PSE BUNDLE FOR APEX 23.2<br>(PSES ON TOP OF 23.2.0), PATCH_VERSION 6. If you need exactly<br>the same APEX images version to install on your EC2 instance,<br>download patch 37593125: 23.2.6 PSE BUNDLE FOR APEX 23.2 (PSES<br>ON TOP OF 23.2.0). |
| Oracle APEX version 23.1.v1 | 106 MiB              | All                                | This version includes patch 35283657: PSE BUNDLE FOR APEX 23.1<br>(PSES ON TOP OF 23.1.0), PATCH_VERSION 2.                                                                                                                                                                              |
| Oracle APEX version 22.2.v1 | 106 MiB              | All                                | This version includes patch 34628174: PSE BUNDLE FOR APEX 22.2<br>(PSES ON TOP OF 22.2.0), PATCH_VERSION 4.                                                                                                                                                                              |
| Oracle APEX version 22.1.v1 | 124 MiB              | All                                | This version includes patch 34020981: PSE BUNDLE FOR APEX 22.1<br>(PSES ON TOP OF 22.1.0), PATCH_VERSION 6.                                                                                                                                                                              |
| Oracle APEX version 21.2.v1 | 125 MiB              | All                                | This version includes patch 33420059: PSE BUNDLE FOR APEX 21.2<br>(PSES ON TOP OF 21.2.0), PATCH_VERSION 8.                                                                                                                                                                              |
| Oracle APEX version 21.1.v1 | 125 MiB              | All                                | This version includes patch 32598392: PSE BUNDLE FOR APEX<br>21.1, PATCH_VERSION 3.                                                                                                                                                                                                      |
| Oracle APEX version 20.2.v1 | 148 MiB              | All except Oracle Database 21c     | This version includes patch 32006852: PSE BUNDLE FOR APEX<br>20.2, PATCH_VERSION 2020.11.12. You can see the patch number and<br>date by running the following query:<br>`<br>SELECT PATCH_VERSION, PATCH_NUMBER<br>FROM   APEX_PATCHES;<br>`                                            |
| Oracle APEX version 20.1.v1 | 173 MiB              | All except Oracle Database 21c     | This version includes patch 30990551: PSE BUNDLE FOR APEX<br>20.1, PATCH_VERSION 2020.07.15.                                                                                                                                                                                             |
| Oracle APEX version 19.2.v1 | 149 MiB              | All except Oracle Database 21c     |                                                                                                                                                                                                                                                                                          |
| Oracle APEX version 19.1.v1 | 148 MiB              | All except Oracle Database 21c     |                                                                                                                                                                                                                                                                                          |

For downloadable Oracle APEX .zip files, see [Oracle APEX Prior Release Archives](https://www.oracle.com/tools/downloads/apex-all-archives-downloads.html "https://www.oracle.com/tools/downloads/apex-all-archives-downloads.html") on the Oracle website.

## Oracle APEX and ORDS

prerequisites

Note the following prerequisites for using Oracle APEX and ORDS:

- Your system must use the Java Runtime Environment (JRE).
- Your Oracle client installation must include the following:
  - SQL\*Plus or SQL Developer for administration tasks
  - Oracle Net Services for configuring connections to your RDS for Oracle
    DB instance

## Oracle APEX

limitations

You can't modify the `APEX_`version`` user
 account, which is managed by Amazon RDS. Thus, you can't apply database profiles or
 enforce password rules on this user. The profiles and password settings for
 `APEX_`version`` are predefined by
Oracle and AWS and are designed to meet the security requirements for
Amazon RDS.
