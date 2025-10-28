# Best Practice 19.6 – Evaluate

archiving and offloading options

By considering options to archive infrequently accessed data or offload large objects
to near-line storage, you can reduce your infrastructure and backup costs.

**Suggestion 19.6.1 – Implement archiving for large tables with
infrequently accessed data**

Specifically for SAP HANA databases, there are cost benefits of managing your
database growth using archiving strategies.

- SAP Documentation: [Data
  Archiving](https://help.sap.com/viewer/6c8d90ed795242279e9103a8acad9cbe/LATEST "https://help.sap.com/viewer/6c8d90ed795242279e9103a8acad9cbe/LATEST")

**Suggestion 19.6.2 – Evaluate the archiving tools that support Amazon
S3 as a destination**

Amazon S3 is designed to be highly available and durable and offers a wide range of
cost-effective storage classes. This makes it ideal for storing SAP archive data with the
lowest total cost of ownership (TCO).

- AWS Documentation: [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes "https://aws.amazon.com/s3/storage-classes")
- SAP Documentation: [SAP
  Certified Archiving Solutions](https://www.sap.com/dmc/exp/2013_09_adpd/enEN/#/solutions?filters=v:296 "https://www.sap.com/dmc/exp/2013_09_adpd/enEN/#/solutions?filters=v:296")

**Suggestion 19.6.3 – Use a data management system for large
objects**

Understand the options and cost benefits for offloading and managing data outside of
the SAP database for large objects, such as invoices and images. Consider the business
requirements for accessing the data, the implementation effort and the ongoing management
complexity.

Large objects will increase your database size, inflating resource and backup costs.
Data management system options might provide a lower-cost storage solution.

- SAP Documentation: [SAP Document Management](https://help.sap.com/viewer/0f3e26f224d9419688b3d25d7c2e46fe/LATEST/en-US/4af6e75227db9972e10000000a4450e5.html "https://help.sap.com/viewer/0f3e26f224d9419688b3d25d7c2e46fe/LATEST/en-US/4af6e75227db9972e10000000a4450e5.html")
- SAP Documentation: [Search
  for Certified ILM Solutions](https://www.sap.com/dmc/exp/2013_09_adpd/enEN/#/solutions?search=BC-ILM "https://www.sap.com/dmc/exp/2013_09_adpd/enEN/#/solutions?search=BC-ILM")
