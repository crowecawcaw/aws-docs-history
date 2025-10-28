# Data mesh

A _data mesh_ is an architectural framework that enables domain teams to perform cross-domain data analysis through distributed, decentralized ownership.

Organizations have multiple data sources from different lines of business that must be integrated for analytics. Managing all these data sources from a central data repository can be challenging. Similar to how application architecture has involved into building microservices rather than a single application entity, data teams are exploring ways to modularize their data platforms to become federated, decentralized solutions.

A data mesh is an analytics design pattern that effectively unites the disparate data sources and links them together through self-service data sharing and governance guidelines. Business functions can maintain control over how shared data is accessed, who can access it and when it can be accessed. Organizations that have built data lakes, data warehouses and other data repositories, and require these environments to be more connected, could benefit from a data mesh architecture.

The trade off to implementing a data mesh is that a data mesh adds complexities to architecture but also brings efficiency by improving data searchability, accessibility, security and scalability.

A data mesh transfers data control to domain experts who create meaningful data products within a decentralized governance framework. Data consumers request access to the data products and seek approvals or changes directly from data owners. As a result, everyone gets faster access to relevant data, and faster access improves business agility.

A data mesh may be suitable for customers who:

- Have a well-established data strategy
- Have a current implementation of a modern data architecture
- Have decoupled business units that operate autonomously
- Need to share data across business units, or with external partners
- Require consistent data governance across multiple teams that aren’t part of a single organization
- Need to have quick delivery cycles with well-defined agile practices, and are willing to iterate changes from lessons learned

Technology, people, and processes are the key principles that help deliver and maintain a successful data mesh. The people and processes can be identified as follows:

- **Data owner:** A data mesh features data domains as nodes, which exist in data lake accounts; it is founded in decentralization and distribution of data responsibility to people closest to the data, which become data domain owners.
- **Data steward:** Federated data governance is how data products are shared. Delivering discoverable metadata auditability based on federated decision-making and accountability structures falls to the data steward.
- **Data engineer:** A data producer contributes one or more data products to a central catalog in a data mesh account. Data products must be autonomous, discoverable, secure, and reusable.
- **Data consumer:** The platform streamlines the experience of data users to discover, access, and use data products. It streamlines the experience of data consumers to easily consume and drive value from the data.
