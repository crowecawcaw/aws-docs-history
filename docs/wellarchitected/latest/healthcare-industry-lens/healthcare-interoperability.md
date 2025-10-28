# Healthcare interoperability

Healthcare interoperability refers to health data exchange between
information systems like electronic healthcare records (EHR),
pharmacy systems, diagnostic imaging systems, laboratory systems,
and claims systems. With interoperability, health data can be
communicated between electronic systems, between organizations,
and across geographical boundaries with standardized protocols.

Enabling interoperability requires that data be captured in
electronic systems, with standards for the content, transport,
vocabulary/terminology, privacy and security, and identifiers. The
Healthcare Information and Management Systems Society (HIMSS), a
globally recognized thought leader on healthcare interoperability,
[defines
four levels of interoperability](https://www.himss.org/resources/interoperability-healthcare "https://www.himss.org/resources/interoperability-healthcare") as:

- **Foundational**: Establishing interconnectivity so that
  systems can securely exchange data.
- **Structural**: Defining and adopting standards for the
  format, syntax, and organization of data.
- **Semantic**: Using standardized coding vocabularies so that
  the parties exchanging data can have a shared understanding of its meaning.
- **Organization**: Managing the governance and legal aspects
  of exchanging data between organizations and individuals. This level also covers consent
  for how an individual’s data will be shared.

Characteristics of functional interoperability solutions include:

- Using a published standard to structure and transmit health
  data. Many standards are currently used across healthcare,
  such as
  [Health
  Level Seven Version 2](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=185 "https://www.hl7.org/implement/standards/product_brief.cfm?product_id=185") (HL7 v2), HL7 Version 3 (HL7 v3),
  [HL7 Fast
  Healthcare Interoperability Resources](https://hl7.org/FHIR/summary.html "https://hl7.org/FHIR/summary.html") Version 4 (FHIR),
  [X12
  Electronic Data Interchange (EDI) transactions](https://x12.org/products/transaction-sets "https://x12.org/products/transaction-sets") used in
  healthcare benefits coordination and claims processing, and
  the Digital Imaging and Communications in Medicine (DICOM)
  standard for storing and transferring medical images.
- Exposing either an API or an integration server to other
  systems seeking to exchange data.
- Checking received data for conformance to the interoperability
  standard being used.
- Being able to apply transformations to data received or
  sent and mapping the internal formats of systems of record, like
  EHRs, to a structural and semantic form dictated by the
  standard.
- Facilitating secure authorization and launch of user-facing
  applications, often with protocols like
  [SMART
  on FHIR](http://www.hl7.org/fhir/smart-app-launch/ "http://www.hl7.org/fhir/smart-app-launch/").
