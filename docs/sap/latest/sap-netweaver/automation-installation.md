# Automated SAP installation

Deploying an SAP system requires significant effort in building an infrastructure that conforms to SAP specifications. Installation, operating system configuration, and configuration of parameters based on the type of SAP workload must be repeated for the development, quality, and production landscape. You can automate this installation and configuration using AWS Systems Manager. Automating the installation and configuration of your SAP landscape helps your team stay compliant with auditable policies related to configuration as code. In addition, it turns the SAP installation into an easily repeatable process, which makes the quality of the outcome easier to improve because you can simulate it and run it multiple times using the same source of information.

The solution described here uses Systems Manager documents to install a distributed SAP landscape that contains the following:

- ABAP SAP Central Services (ASCS)
- Database instance
- Primary Application Server (PAS)
- Additional Application Servers (AAS)
