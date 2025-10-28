# Business Continuity

AWS recommends that you periodically schedule business continuity process validations by executing disaster recovery (DR) tests. This planned activity will help to flush out any potential unknowns and help the organization to deal with any real disaster in a streamlined manner. Depending on your disaster recovery architecture, business continuity may include:

- Backup/recovery of database from AmazonS3
- Creation of systems from AMI and point-in-time recovery via snapshots
- Changing the EC2 instance size of pilot light system
- Validation of integration (AD/DNS, email, third party, and so on.)
