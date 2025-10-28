# Open government methods, infrastructure, and tools

To maintain the trust of the people they serve, governments need to be transparent,
accountable, and truthful. This covers many different aspects of government operations such as
how and with whom taxpayer money is spent, how effective policy initiatives are, what the laws
are and the penalties for breaking them, and how decisions are taken. Being open is essential
to help avoid perceptions of corruption or unfairness in society. There are a number of open
government tools and approaches that can be used by governments as they develop public
services that can increase trust, improve outcomes and, in some cases, help verify that legal
or regulatory obligations are met.

Characteristics and principles of open government system
architectures include:

- High public trust and confidence in government systems and
  services
- Clear accountability and reporting measures
- Public visibility and participation of programs, projects,
  services, and policies
- Open feedback mechanisms for the public

## Working in the open

Working in the open has benefits to both government and society. It provides a scalable
mechanism for peer review, partnerships, and public participation as well as greater
opportunities for collaboration and reuse between government teams, departments, and
jurisdictions. Blogging, sharing tools and code, showcases, feedback opportunities, open
prototyping, and visible product management can all benefit the quality of delivery. AWS
architecture and delivery practices exemplify many of these open ways of working.

## Open-source software publication and reuse

Many governments have a policy of publishing code repositories that they have developed
under an open source license to increase transparency and allow for reuse by others. This
approach can also extend to infrastructure as code (IaC) configurations. It’s important to
understand if the government systems and services you work on will be published as open
source so that information not intended for the public domain isn’t published in the code
repository, and that no proprietary code is included. Increasingly, governments have
open-source software policies that encourage or require teams delivering new systems or
services to explore the reuse of existing open-source solutions before investing time or
money into building new ones. In some countries, these requirements are legislated. It is
therefore important to understand any open-source software policies when designing and
architecting new government systems and services, and to support government organizations to
evaluate open source offerings as part of these processes. AWS provides an [open source repository and guidance](https://aws.amazon.com/opensource "https://aws.amazon.com/opensource") to help.

## Algorithmic transparency

To maintain trust and fairness when using algorithms for automated or semi-automated
decision making, it’s important to consider whether the algorithms used can be published. A
number of government organizations maintain a public register of algorithms used within
their systems for this purpose. Not all algorithms will be appropriate for publication, for
example, some fraud detection measures, however, where automated decisions are taken that
directly affect people’s lives and livelihoods, consideration should be made around
publication of the algorithm and what mechanism is most appropriate for doing so.
Algorithmic transparency could also mean traceable explainability to the legislation or
rules used to make a decision, or providing transparency to end users on when they are
interacting with algorithms. Finally, it can be useful to test inputs/outputs of algorithmic
decision making against the relevant legislation/regulation as code, to work toward
compliance.

## Performance reporting

A key tool for government accountability is monitoring, measuring, and publishing
performance data of public services and policy initiatives through public facing dashboards.
Dashboards provide a simple way for the public and policymakers to visualize, and access the
data and insights around the performance of important government operations. Considerations
should be made around what metrics are useful indicators for performance, what mechanisms
are required to derive those metrics, and how this data can be published.

## Open government data

Government organizations generate and manage a wide array of data and information for
which they are the canonical source. While much of this data contains private information,
such as personal, confidential, or classified, there is a large amount of non-private data
and information that can provide significant value to society if openly shared and licensed
for reuse. This sharing allows others to build on this data to create innovative solutions.
Common examples of open data range from the large scale, such as geospatial information,
population statistics or weather data, to the smaller scale, such as locations of public
toilets, lists of local authorities, and academic institutions. You should consider if your
service holds data that is appropriate for open publication. If it does, you should explore
mechanisms for publishing and providing both programmatic and manual access to the data, and
that the data is licensed for reuse.
