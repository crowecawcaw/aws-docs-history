

# Managed data identifiers for PHI
<a name="mdis-reference-phi"></a>

Amazon Macie can detect multiple types of sensitive, personal health information (PHI) by using managed data identifiers. The topics on this page specify each type and provide information about the managed data identifier that's designed to detect the data. Each topic provides the following information:<a name="mdi-ref-fields-singular"></a>
+ **Managed data identifier ID** – Specifies the unique identifier (ID) for the managed data identifier that's designed to detect the data. When you [create a sensitive data discovery job](discovery-jobs-create.md) or [configure settings for automated sensitive data discovery](discovery-asdd-account-configure.md), you can use this ID to specify whether you want Macie to use the managed data identifier when it analyzes data.
+ **Supported countries and regions** – Indicates which countries or regions the applicable managed data identifier is designed for. If the managed data identifier isn't designed for a particular country or region, this value is *Any*.
+ **Keyword required** – Specifies whether detection requires a keyword to be in proximity of the data. If a keyword is required, the topic also provides examples of required keywords. For information about how Macie uses keywords when it analyzes data, see [Keyword requirements](managed-data-identifiers-keywords.md).
+ **Comments** – Provides any relevant details that might affect your choice of managed data identifier or your investigation into reported occurrences of the sensitive data. The details include information such as supported standards, syntax requirements, and exceptions.

The topics are listed in alphabetical order by sensitive data type.

**Topics**
+ [Drug Enforcement Agency (DEA) Registration Number](#mdis-reference-DEA-registration-num)
+ [Health Insurance Claim Number (HICN)](#mdis-reference-HICN)
+ [Health insurance or medical identification number](#mdis-reference-HI-ID)
+ [Healthcare Common Procedure Coding System (HCPCS) code](#mdis-reference-HCPCS)
+ [National Drug Code (NDC)](#mdis-reference-NDC)
+ [National Provider Identifier (NPI)](#mdis-reference-NPI)
+ [Unique device identifier (UDI)](#mdis-reference-UDI)

## Drug Enforcement Agency (DEA) Registration Number
<a name="mdis-reference-DEA-registration-num"></a>

**Managed data identifier ID:** US\_DRUG\_ENFORCEMENT\_AGENCY\_NUMBER

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: *dea number, dea registration*

**Comments:** None

## Health Insurance Claim Number (HICN)
<a name="mdis-reference-HICN"></a>

**Managed data identifier ID:** USA\_HEALTH\_INSURANCE\_CLAIM\_NUMBER

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: *health insurance claim number, hic no, hic no., hic number, hic\#, hicn, hicn\#., hicno\#*

**Comments:** None

## Health insurance or medical identification number
<a name="mdis-reference-HI-ID"></a>

Support includes European Health Insurance Card numbers for the EU and Finland, health insurance numbers for France, Medicare Beneficiary Identifiers for the US, NHS numbers for the UK, and Personal Health Numbers for Canada.

**Managed data identifier ID:** Depending on country or region, CANADA\_HEALTH\_NUMBER, EUROPEAN\_HEALTH\_INSURANCE\_CARD\_NUMBER, FINLAND\_EUROPEAN\_HEALTH\_INSURANCE\_NUMBER, FRANCE\_HEALTH\_INSURANCE\_NUMBER, UK\_NHS\_NUMBER, USA\_MEDICARE\_BENEFICIARY\_IDENTIFIER

**Supported countries and regions:** Canada, EU, Finland, France, UK, US

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes for specific countries and regions.


| Country or region | Keywords | 
| --- | --- | 
| Canada | canada healthcare number, msp number, personal healthcare number, phn, soins de santé | 
| EU | assicurazione sanitaria numero, carta assicurazione numero, carte d’assurance maladie, carte européenne d'assurance maladie, ceam, ehic, ehic\#, finlandehicnumber\#, gesundheitskarte, hälsokort, health card, health card number, health insurance card, health insurance number, insurance card number, krankenversicherungskarte, krankenversicherungsnummer, medical account number, numero conto medico, numéro d’assurance maladie, numéro de carte d’assurance, numéro de compte medical, número de cuenta médica, número de seguro de salud, número de tarjeta de seguro, sairaanhoitokortin, sairausvakuutuskortti, sairausvakuutusnumero, sjukförsäkring nummer, sjukförsäkringskort, suomi ehic-numero, tarjeta de salud, terveyskortti, tessera sanitaria assicurazione numero, versicherungsnummer | 
| Finland | ehic, ehic\#, finland health insurance card, finlandehicnumber\#, finska sjukförsäkringskort, hälsokort, health card, health card number, health insurance card, health insurance number, sairaanhoitokortin, sairaanhoitokortin, sairausvakuutuskortti, sairausvakuutusnumero, sjukförsäkring nummer, sjukförsäkringskort, suomen sairausvakuutuskortti, suomi ehic-numero, terveyskortti | 
| France | carte d'assuré social, carte vitale, insurance card | 
| UK | national health service, NHS | 
| US | mbi, medicare beneficiary | 

**Comments:** None

## Healthcare Common Procedure Coding System (HCPCS) code
<a name="mdis-reference-HCPCS"></a>

**Managed data identifier ID:** USA\_HEALTHCARE\_PROCEDURE\_CODE

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: *current procedural terminology, hcpcs, healthcare common procedure coding system*

**Comments:** None

## National Drug Code (NDC)
<a name="mdis-reference-NDC"></a>

**Managed data identifier ID:** USA\_NATIONAL\_DRUG\_CODE

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: *national drug code, ndc*

**Comments:** None

## National Provider Identifier (NPI)
<a name="mdis-reference-NPI"></a>

**Managed data identifier ID:** USA\_NATIONAL\_PROVIDER\_IDENTIFIER

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: *hipaa, n.p.i, national provider, npi*

**Comments:** None

## Unique device identifier (UDI)
<a name="mdis-reference-UDI"></a>

**Managed data identifier ID:** MEDICAL\_DEVICE\_UDI

**Supported countries and regions:** US

**Keyword required:** Yes. Keywords include: *blood, blood bag, dev id, device id, device identifier, gs1, hibcc, iccbba, med, udi, unique device id, unique device identifier*

**Comments:** Macie can detect unique device identifiers (UDIs) that comply with formats approved by the US Food and Drug Administration. This includes standard formats defined by GS1, HIBCC, and ICCBBA. ICCBA support is for the ISBT standard.