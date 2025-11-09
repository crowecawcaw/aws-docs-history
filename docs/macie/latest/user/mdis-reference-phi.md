# Managed data identifiers for PHI

Amazon Macie can detect multiple types of sensitive, personal health information (PHI) by using
managed data identifiers. The topics on this page specify each type and provide information about
the managed data identifier that's designed to detect the data. Each topic provides the following
information:

- Managed data identifier ID – Specifies the unique
  identifier (ID) for the managed data identifier that's designed to detect the data. When you [create a
  sensitive data discovery job](discovery-jobs-create.md "discovery-jobs-create.md") or [configure settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md"), you can use
  this ID to specify whether you want Macie to use the managed data identifier when it analyzes data.
- Supported countries and regions – Indicates which countries or
  regions the applicable managed data identifier is designed for. If the managed data identifier isn't
  designed for a particular country or region, this value is _Any_.
- Keyword required – Specifies whether detection
  requires a keyword to be in proximity of the data. If a keyword is required, the topic also
  provides examples of required keywords. For information about how Macie uses
  keywords when it analyzes data, see [Keyword requirements](managed-data-identifiers-keywords.md "managed-data-identifiers-keywords.md").
- Comments – Provides any relevant details that might
  affect your choice of managed data identifier or your investigation into reported occurrences of
  the sensitive data. The details include information such as supported standards, syntax
  requirements, and exceptions.
  The topics are listed in alphabetical order by sensitive data type.

###### Sensitive data types

- [Drug Enforcement
  Agency (DEA) Registration Number](#mdis-reference-DEA-registration-num "#mdis-reference-DEA-registration-num")
- [Health Insurance Claim
  Number (HICN)](#mdis-reference-HICN "#mdis-reference-HICN")
- [Health insurance or medical identification
  number](#mdis-reference-HI-ID "#mdis-reference-HI-ID")
- [Healthcare Common Procedure Coding
  System (HCPCS) code](#mdis-reference-HCPCS "#mdis-reference-HCPCS")
- [National Drug Code (NDC)](#mdis-reference-NDC "#mdis-reference-NDC")
- [National Provider
  Identifier (NPI)](#mdis-reference-NPI "#mdis-reference-NPI")
- [Unique device
  identifier (UDI)](#mdis-reference-UDI "#mdis-reference-UDI")

## Drug Enforcement Agency (DEA)

Registration Number

**Managed data identifier ID:** US_DRUG_ENFORCEMENT_AGENCY_NUMBER

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: _dea number,
dea registration_

**Comments:** None

## Health Insurance Claim Number (HICN)

**Managed data identifier ID:** USA_HEALTH_INSURANCE_CLAIM_NUMBER

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: _health
insurance claim number, hic no, hic no., hic number, hic#, hicn, hicn#.,
hicno#_

**Comments:** None

## Health insurance or medical identification number

Support includes European Health Insurance Card numbers for the EU and Finland, health
insurance numbers for France, Medicare Beneficiary Identifiers for the US, NHS numbers for the
UK, and Personal Health Numbers for Canada.

**Managed data identifier ID:** Depending on country or region, CANADA_HEALTH_NUMBER,
EUROPEAN_HEALTH_INSURANCE_CARD_NUMBER, FINLAND_EUROPEAN_HEALTH_INSURANCE_NUMBER,
FRANCE_HEALTH_INSURANCE_NUMBER, UK_NHS_NUMBER,
USA_MEDICARE_BENEFICIARY_IDENTIFIER

**Supported countries and regions:** Canada, EU, Finland, France, UK, US

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes
for specific countries and regions.

| Country or region | Keywords                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Canada            | canada healthcare number, msp number, personal healthcare number, phn, soins de<br>santé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| EU                | assicurazione sanitaria numero, carta assicurazione numero, carte d’assurance<br>maladie, carte européenne d'assurance maladie, ceam, ehic, ehic#,<br>finlandehicnumber#, gesundheitskarte, hälsokort, health card, health card number, health<br>insurance card, health insurance number, insurance card number, krankenversicherungskarte,<br>krankenversicherungsnummer, medical account number, numero conto medico, numéro d’assurance<br>maladie, numéro de carte d’assurance, numéro de compte medical, número de cuenta médica,<br>número de seguro de salud, número de tarjeta de seguro, sairaanhoitokortin,<br>sairausvakuutuskortti, sairausvakuutusnumero, sjukförsäkring nummer, sjukförsäkringskort,<br>suomi ehic-numero, tarjeta de salud, terveyskortti, tessera sanitaria assicurazione numero,<br>versicherungsnummer |
| Finland           | ehic, ehic#, finland health insurance card, finlandehicnumber#, finska<br>sjukförsäkringskort, hälsokort, health card, health card number, health insurance card,<br>health insurance number, sairaanhoitokortin, sairaanhoitokortin, sairausvakuutuskortti,<br>sairausvakuutusnumero, sjukförsäkring nummer, sjukförsäkringskort, suomen<br>sairausvakuutuskortti, suomi ehic-numero, terveyskortti                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| France            | carte d'assuré social, carte vitale, insurance card                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| UK                | national health service, NHS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| US                | mbi, medicare beneficiary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

**Comments:** None

## Healthcare Common Procedure Coding System (HCPCS)

code

**Managed data identifier ID:** USA_HEALTHCARE_PROCEDURE_CODE

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: _current
procedural terminology, hcpcs, healthcare common procedure coding
system_

**Comments:** None

## National Drug Code (NDC)

**Managed data identifier ID:** USA_NATIONAL_DRUG_CODE

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: _national drug
code, ndc_

**Comments:** None

## National Provider Identifier (NPI)

**Managed data identifier ID:** USA_NATIONAL_PROVIDER_IDENTIFIER

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: _hipaa, n.p.i,
national provider, npi_

**Comments:** None

## Unique device identifier (UDI)

**Managed data identifier ID:** MEDICAL_DEVICE_UDI

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: _blood, blood
bag, dev id, device id, device identifier, gs1, hibcc, iccbba, med, udi, unique device id,
unique device identifier_

**Comments:** Macie can detect unique device identifiers (UDIs) that comply
with formats approved by the US Food and Drug Administration. This includes standard formats
defined by GS1, HIBCC, and ICCBBA. ICCBA support is for the ISBT standard.
