

# Automated Deployment
<a name="sap-hana-pacemaker-sles-automation"></a>

You can set up a cluster manually using the instructions provided here. You can also automate parts of this process to ensure consistent and repeatable deployments.

Use AWS Launch Wizard for SAP to automated deployments of SAP Hana Platform, SAP NetWeaver, SAP S/4 HANA, SAP BW/4HANA, and Solution Manager. Launch Wizard uses AWS CloudFormation templates and advanced scripts to quickly provision the required resources. The automation handles SAP HANA Installation, HANA System Replication and Pacemaker setup, requiring only post-deployment validation and testing. For more information, see [AWS Launch Wizard for SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap.html).

**Important**  
For reliable cluster operations, thoroughly test your system regardless of setup method. Testing helps identify system anomalies, validate changing requirements, and build operational understanding. See [Testing](sap-hana-pacemaker-sles-testing.md) for more details.