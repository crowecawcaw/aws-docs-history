# Ingest NF packages into AWS TNB function catalog

CSPs ingest their 5G network function (NF) packages (for example, vCU, vUPF and vAMF)
into the AWS TNB function catalog. These packages are in the form of a Cloud Service Archive
(CSAR) file containing the NF descriptor, Helm charts, and custom scripts.

**Recommendation:** Work closely with NF vendors to verify
the packages adhere to cloud design principles and meet the packaging requirements of
AWS TNB. Establish a CI/CD pipeline to automate the ingestion of updated NF packages.

**Practical advice:** Thoroughly test the NF packages in a
non-production environment before ingesting them into the production catalog. Maintain
version control and cataloging of the NF packages to enable rollbacks and updates.
