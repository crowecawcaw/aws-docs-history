# Digital Sovereignty Lens - AWS Well-Architected

Framework

Publication date: **January 26, 2026** ([Document revisions](document-revisions.md "document-revisions.md"))

This paper describes the Digital Sovereignty Lens for the AWS Well-Architected Framework.
It provides AWS customers with a set of Well-Architected best practices and guidance on
digital sovereignty.

As organizations worldwide accelerate their cloud adoption, many face increasing regulatory
pressures and stakeholder demands to maintain control over their digital assets and data.

While there is no single definition of digital sovereignty and specific requirements may
vary by country, it is broadly understood as a term used by nation states to _assert
sovereignty_ over the _digital assets_ they _own or
regulate_.

## Digital sovereignty in practice

In practice, digital sovereignty manifests as requirements aligned to three broad areas.

1. **Compliance:** We find nations asserting digital sovereignty
   through legislations, standards, or by empowering their regulatory agencies to come up
   with compliance requirements. Compliance requirements originate from:
   - Cybersecurity related directives, standards, and guidelines (for example, [NIS 2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive "https://digital-strategy.ec.europa.eu/en/policies/nis2-directive")
     is a directive, and [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final") is a standard and a guideline).
   - Data privacy legislations (for example, [Regulation (EU) 2016/679](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679#tit_1 "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679#tit_1"), also known as the European Union General Data
     Protection Regulation (GDPR)).
   - Industry or sectoral regulations (for example, the [Health Insurance Portability and Accountability Act (HIPAA)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act "https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act") is a US federal
     law that protects sensitive patient health information (PHI)).
   - Emerging regulations (for example, the [European Union AI Act](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence "https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence")).
     Compliance is a key driver when it comes to sovereign workloads.

2. **Control**: Beyond standard compliance, some nations now
   mandate additional controls, driving towards more stringent data security and data
   residency related outcomes. These requirements translate to technical measures including:
   - Confidential compute solutions [(for example, AWS Nitro Enclaves)](https://aws.amazon.com/ec2/nitro/nitro-enclaves/ "https://aws.amazon.com/ec2/nitro/nitro-enclaves/")
   - Externally managed key stores [(for example, AWS KMS external
     key stores)](../../../kms/latest/developerguide/keystore-external.md "../../../kms/latest/developerguide/keystore-external.md")
   - Dedicated data security solutions
   - Privacy enhancing technologies
   - Data residency controls
   - Hybrid compute environments at the edge [(for example, AWS Outposts)](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/")

3. **Continuity**: Some nations seek to exercise more
   independence and choice while making technology decisions. They don't want to be locked
   into proprietary technologies or punitive license terms. This also extends to having
   uninterrupted access to infrastructure, services and skills required to support their
   digital footprint. Achieving continuity through greater self-sufficiency and resiliency is
   therefore a key outcome of digital sovereignty initiatives.

Together, the _three Cs_ form a mental model of the outcomes expected
from a digital sovereignty initiative. Be aware that there is an alternative viewpoint on
digital sovereignty, described as a combination of data sovereignty, operational sovereignty,
and technology sovereignty. The three Cs align with that viewpoint but are anchored towards
clear business-focused outcomes rather than on abstract notions.

## Scope

Sovereign workloads must be compliance-aligned, auditable, transparent, interoperable,
portable, and survivable. However, not every system needs to exhibit each of those qualities.
For example, you may not want to invest in interoperability and portability initially choosing
instead to focus on the compliance and control related measures.

The Digital Sovereignty Lens provides a framework to assist in designing workloads that
address sovereignty requirements while still using the flexibility of the AWS Cloud.

## Lens availability

Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you
to create your own [custom lenses](../userguide/lenses-custom.md "../userguide/lenses-custom.md"), or to use
lenses created by others that have been shared with you.

To begin reviewing your digital sovereignty workload, download and import the [Digital Sovereignty Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/digital-sovereignty-lens/digital-sovereignty-lens.json "https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/digital-sovereignty-lens/digital-sovereignty-lens.json") into AWS Well-Architected Tool from the public [AWS
Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens "https://github.com/aws-samples/sample-well-architected-custom-lens").
