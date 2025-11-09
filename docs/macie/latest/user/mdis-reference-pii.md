# Managed data identifiers for PII

Amazon Macie can detect multiple types of sensitive, personally identifiable information (PII)
by using managed data identifiers. The topics on this page list each type and provide
information about the managed data identifiers that are designed to detect the data. Each topic
provides the following information:

- Managed data identifier ID – Specifies the unique
  identifier (ID) for one or more managed data identifiers that are designed to detect the data.
  When you [create a sensitive data discovery job](discovery-jobs-create.md "discovery-jobs-create.md") or [configure settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md"), you can use these
  IDs to specify which managed data identifiers you want Macie to use when it analyzes
  data.
- Supported countries and regions – Indicates which
  countries and regions the applicable managed data identifiers are designed for. If the managed
  data identifiers aren't designed for particular countries or regions, this value is
  _Any_.
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

- [Birth date](#mdis-reference-DATE_OF_BIRTH "#mdis-reference-DATE_OF_BIRTH")
- [Driver’s license identification
  number](#mdis-reference-DL-num "#mdis-reference-DL-num")
- [Electoral roll
  number](#mdis-reference-electoral-roll-num "#mdis-reference-electoral-roll-num")
- [Full name](#mdis-reference-full-name "#mdis-reference-full-name")
- [Global Positioning System (GPS)
  coordinates](#mdis-reference-GPS "#mdis-reference-GPS")
- [HTTP cookie](#mdis-reference-HTTP_COOKIE "#mdis-reference-HTTP_COOKIE")
- [Mailing address](#mdis-reference-mailing-address "#mdis-reference-mailing-address")
- [National identification number](#mdis-reference-national-id "#mdis-reference-national-id")
- [National Insurance
  Number (NINO)](#mdis-reference-NINO "#mdis-reference-NINO")
- [Passport number](#mdis-reference-passport-num "#mdis-reference-passport-num")
- [Permanent residence
  number](#mdis-reference-permanent-residence-num "#mdis-reference-permanent-residence-num")
- [Phone number](#mdis-reference-phone-num "#mdis-reference-phone-num")
- [Public transportation card number](#mdis-reference-public-transport-num "#mdis-reference-public-transport-num")
- [Social Insurance
  Number (SIN)](#mdis-reference-social-insurance-num "#mdis-reference-social-insurance-num")
- [Social Security
  number (SSN)](#mdis-reference-social-security-num "#mdis-reference-social-security-num")
- [Taxpayer identification or reference number](#mdis-reference-taxpayer-num "#mdis-reference-taxpayer-num")
- [Vehicle identification
  number (VIN)](#mdis-reference-vin "#mdis-reference-vin")

## Birth date

**Managed data identifier ID:** DATE_OF_BIRTH

**Supported countries and regions:** Any

**Keyword required:** Yes. Keywords include: _bday,
b-day, birth date, birthday, date of birth, dob_

**Comments:** Support includes most date formats, such as all digits and
combinations of digits and names of months. Date components can be separated by spaces,
slashes (/), or hyphens (‐).

## Driver’s license identification number

**Managed data identifier ID:** Depending on country or region, AUSTRALIA_DRIVERS_LICENSE,
AUSTRIA_DRIVERS_LICENSE, BELGIUM_DRIVERS_LICENSE, BULGARIA_DRIVERS_LICENSE,
CANADA_DRIVERS_LICENSE, CROATIA_DRIVERS_LICENSE, CYPRUS_DRIVERS_LICENSE,
CZECHIA_DRIVERS_LICENSE, DENMARK_DRIVERS_LICENSE, DRIVERS_LICENSE (for the US),
ESTONIA_DRIVERS_LICENSE, FINLAND_DRIVERS_LICENSE, FRANCE_DRIVERS_LICENSE,
GERMANY_DRIVERS_LICENSE, GREECE_DRIVERS_LICENSE, HUNGARY_DRIVERS_LICENSE,
INDIA_DRIVERS_LICENSE, IRELAND_DRIVERS_LICENSE, ITALY_DRIVERS_LICENSE,
LATVIA_DRIVERS_LICENSE, LITHUANIA_DRIVERS_LICENSE, LUXEMBOURG_DRIVERS_LICENSE,
MALTA_DRIVERS_LICENSE, NETHERLANDS_DRIVERS_LICENSE, POLAND_DRIVERS_LICENSE,
PORTUGAL_DRIVERS_LICENSE, ROMANIA_DRIVERS_LICENSE, SLOVAKIA_DRIVERS_LICENSE,
SLOVENIA_DRIVERS_LICENSE, SPAIN_DRIVERS_LICENSE, SWEDEN_DRIVERS_LICENSE,
UK_DRIVERS_LICENSE

**Supported countries and regions:** Australia, Austria, Belgium, Bulgaria, Canada, Croatia, Cyprus,
Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, India, Ireland,
Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia,
Slovenia, Spain, Sweden, UK, US

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes
for specific countries and regions.

| Country or region | Keywords                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Australia         | dl#, dl:, dlno#, driver licence, driver license, driver permit,<br>drivers lic., drivers licence, driver's licence, drivers license, driver's license,<br>drivers permit, driver's permit, drivers permit number, driving licence, driving<br>license, driving permit                                                                                                                                    |
| Austria           | führerschein, fuhrerschein, führerschein republik österreich, fuhrerschein<br>republik osterreich                                                                                                                                                                                                                                                                                                        |
| Belgium           | fuehrerschein, fuehrerschein<br>• nr, fuehrerscheinnummer, fuhrerschein,<br>führerschein, fuhrerschein<br>• nr, führerschein<br>• nr, fuhrerscheinnummer,<br>führerscheinnummer, numéro permis conduire, permis de conduire, rijbewijs,<br>rijbewijsnummer                                                                                                                                               |
| Bulgaria          | превозно средство, свидетелство за управление на моторно, свидетелство за<br>управление на мпс, сумпс, шофьорска книжка                                                                                                                                                                                                                                                                                  |
| Canada            | dl#, dl:, dlno#, driver licence, driver licences, driver license,<br>driver licenses, driver permit, drivers lic., drivers licence, driver's licence,<br>drivers licences, driver's licences, drivers license, driver's license, drivers<br>licenses, driver's licenses, drivers permit, driver's permit, drivers permit number,<br>driving licence, driving license, driving permit, permis de conduire |
| Croatia           | vozačka dozvola                                                                                                                                                                                                                                                                                                                                                                                          |
| Cyprus            | άδεια οδήγησης                                                                                                                                                                                                                                                                                                                                                                                           |
| Czech Republic    | číslo licence, císlo licence řidiče, číslo řidičského průkazu, ovladače<br>lic., povolení k jízdě, povolení řidiče, řidiči povolení, řidičský prúkaz, řidičský<br>průkaz                                                                                                                                                                                                                                 |
| Denmark           | kørekort, kørekortnummer                                                                                                                                                                                                                                                                                                                                                                                 |
| Estonia           | juhi litsentsi number, juhiloa number, juhiluba, juhiluba<br>number                                                                                                                                                                                                                                                                                                                                      |
| Finland           | ajokortin numero, ajokortti, förare lic., körkort, körkort nummer,<br>kuljettaja lic., permis de conduire                                                                                                                                                                                                                                                                                                |
| France            | permis de conduire                                                                                                                                                                                                                                                                                                                                                                                       |
| Germany           | fuehrerschein, fuehrerschein<br>• nr, fuehrerscheinnummer, fuhrerschein,<br>führerschein, fuhrerschein<br>• nr, führerschein<br>• nr, fuhrerscheinnummer,<br>führerscheinnummer                                                                                                                                                                                                                          |
| Greece            | δεια οδήγησης, adeia odigisis                                                                                                                                                                                                                                                                                                                                                                            |
| Hungary           | illesztőprogramok lic, jogosítvány, jogsi, licencszám, vezető engedély,<br>vezetői engedély                                                                                                                                                                                                                                                                                                              |
| India             | driver licence, driver licences, driver license, driver licenses, drivers<br>lic., drivers licence, driver's licence, drivers licences, driver's licences,<br>drivers license, driver's license, drivers licenses, driver's licenses, driving<br>licence, driving license                                                                                                                                |
| Ireland           | ceadúnas tiomána                                                                                                                                                                                                                                                                                                                                                                                         |
| Italy             | patente di guida, patente di guida numero, patente guida, patente guida<br>numero                                                                                                                                                                                                                                                                                                                        |
| Latvia            | autovadītāja apliecība, licences numurs, vadītāja apliecība, vadītāja<br>apliecības numurs, vadītāja atļauja, vadītāja licences numurs, vadītāji<br>lic.                                                                                                                                                                                                                                                 |
| Lithuania         | vairuotojo pažymėjimas                                                                                                                                                                                                                                                                                                                                                                                   |
| Luxembourg        | fahrerlaubnis, führerschäin                                                                                                                                                                                                                                                                                                                                                                              |
| Malta             | liċenzja tas-sewqan                                                                                                                                                                                                                                                                                                                                                                                      |
| Netherlands       | permis de conduire, rijbewijs, rijbewijsnummer                                                                                                                                                                                                                                                                                                                                                           |
| Poland            | numer licencyjny, prawo jazdy, zezwolenie na prowadzenie                                                                                                                                                                                                                                                                                                                                                 |
| Portugal          | carta de condução, carteira de habilitação, carteira de motorist, carteira<br>habilitação, carteira motorist, licença condução, licença de condução, número de<br>licença, número licença, permissão condução, permissão de condução                                                                                                                                                                     |
| Romania           | numărul permisului de conducere, permis de conducere                                                                                                                                                                                                                                                                                                                                                     |
| Slovakia          | číslo licencie, číslo vodičského preukazu, ovládače lic., povolenia<br>vodičov, povolenie jazdu, povolenie na jazdu, povolenie vodiča, vodičský<br>preukaz                                                                                                                                                                                                                                               |
| Slovenia          | vozniško dovoljenje                                                                                                                                                                                                                                                                                                                                                                                      |
| Spain             | carnet conducer, el carnet de conducer, licencia conducer, licencia de<br>manejo, número carnet conducer, número de carnet de conducer, número de permiso<br>conducer, número de permiso de conducer, número licencia conducer, número permiso<br>conducer, permiso conducción, permiso conducer, permiso de<br>conducción                                                                               |
| Sweden            | ajokortin numero, dlno# ajokortti, drivere lic., förare lic., körkort,<br>körkort nummer, körkortsnummer, kuljettajat lic.                                                                                                                                                                                                                                                                               |
| UK                | dl#, dl:, dlno#, driver licence, driver licences, driver license,<br>driver licenses, driver permit, drivers lic., drivers licence, driver's licence,<br>drivers licences, driver's licences, drivers license, driver's license, drivers<br>licenses, driver's licenses, drivers permit, driver's permit, drivers permit number,<br>driving licence, driving license, driving permit                     |
| US                | dl#, dl:, dlno#, driver licence, driver licences, driver license,<br>driver licenses, driver permit, drivers lic., drivers licence, driver's licence,<br>drivers licences, driver's licences, drivers license, driver's license, drivers<br>licenses, driver's licenses, drivers permit, driver's permit, drivers permit number,<br>driving licence, driving license, driving permit                     |

**Comments:** None

## Electoral roll number

**Managed data identifier ID:** UK_ELECTORAL_ROLL_NUMBER

**Supported countries and regions:** UK

**Keyword required:** Yes. Keywords include: _electoral
#, electoral number, electoral roll #, electoral roll no., electoral roll number,
electoralrollno_

**Comments:** None

## Full name

**Managed data identifier ID:** NAME

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** Macie can detect full names only. Support is limited to Latin
character sets.

## Global Positioning System (GPS) coordinates

**Managed data identifier ID:** LATITUDE_LONGITUDE

**Supported countries and regions:** Any, if the coordinates are in proximity of an English
keyword.

**Keyword required:** Yes. Keywords include: _coordinate,
coordinates, lat long, latitude longitude, position_

**Comments:** Macie can detect GPS coordinates if the latitude and longitude
coordinates are stored as a pair and they're in Decimal Degrees (DD) format, for example
`41.948614,-87.655311`. Support doesn't include detection of coordinates in:
Degrees Decimal Minutes (DDM) format, for example `41°56.9168'N 87°39.3187'W`; or
Degrees, Minutes, Seconds (DMS) format, for example `41°56'55.0104"N
 87°39'19.1196"W`.

## HTTP cookie

**Managed data identifier ID:** HTTP_COOKIE

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** Detection requires a complete `Cookie` or
`Set-Cookie` header. The header can include one or more name-value pairs, for
example: `Set-Cookie: id=TWlrZQ` and `Cookie: session=3948;
 lang=en`.

## Mailing address

**Managed data identifier ID:** ADDRESS (for Australia, Canada, France, Germany,
Italy, Spain, UK, and the US), BRAZIL_CEP_CODE (for Brazil's Código de
Endereçamento Postal)

**Supported countries and regions:** Australia, Brazil, Canada, France, Germany, Italy, Spain, UK,
US

**Keyword required:** Varies. Keywords aren't required by the ADDRESS
managed data identifier. Keywords are required by the BRAZIL_CEP_CODE managed
data identifier. Keywords include: _cep, código de endereçamento postal,
codigo de endereçamento postal, código postal, codigo postal_

**Comments:** Although a keyword isn't required by the
ADDRESS managed data identifier, detection requires an address to include the
name of a city or place and a corresponding ZIP or Postal Code in a supported country or
region. The BRAZIL_CEP_CODE managed data identifier can detect only the Código
de Endereçamento Postal (CEP) portion of an address.

## National identification number

Support includes: Aadhaar numbers for India; Cédula de Ciudadanía numbers for Colombia; Clave Única de Registro de Población (CURP) numbers for Mexico; Codice Fiscale numbers for Italy; Documento Nacional de Identidad (DNI) numbers for Argentina and Spain; French National Institute for Statistics and Economic Studies (INSEE) codes; German National Identity Card numbers; Registro Geral (RG) numbers for Brazil; and, Rol Único Nacional (RUN) numbers for Chile.

**Managed data identifier ID:** Depending on country or region, ARGENTINA_DNI_NUMBER, BRAZIL_RG_NUMBER, CHILE_RUT_NUMBER, COLOMBIA_CITIZENSHIP_CARD_NUMBER, FRANCE_NATIONAL_IDENTIFICATION_NUMBER, GERMANY_NATIONAL_IDENTIFICATION_NUMBER, INDIA_AADHAAR_NUMBER, ITALY_NATIONAL_IDENTIFICATION_NUMBER, MEXICO_CURP_NUMBER, SPAIN_DNI_NUMBER

**Supported countries and regions:** Argentina, Brazil, Chile, Colombia, France, Germany, India, Italy, Mexico, Spain

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes for specific countries and regions.

| Country or region | Keywords                                                                                                                                                                                                                                                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Argentina         | dni, dni#, d.n.i., documento nacional de identidad                                                                                                                                                                                                                                                                                                     |
| Brazil            | registro geral, rg                                                                                                                                                                                                                                                                                                                                     |
| Chile             | identidad número, nacional identidad, national unique role, nationaluniqueroleID#, número identificación, rol único nacional, rol único tributario, run, run#, r.u.n., rut, rut#, r.u.t., unique national number, unique national role, unique tax registry, unique tax role, unique tributary number, unique tributary role                           |
| Colombia          | cédula de ciudadanía, documento de identificación                                                                                                                                                                                                                                                                                                      |
| France            | assurance sociale, carte nationale d’identité, cni, code sécurité sociale, French social security number, fssn#, insee, insurance number, national id number, nationalid#, numéro d'assurance, sécurité sociale, sécurité sociale non., sécurité sociale numéro, social, social security, social security number, socialsecuritynumber, ss#, ssn, ssn# |
| Germany           | ausweisnummer, id number, identification number, identity number, insurance number, personal id, personalausweis                                                                                                                                                                                                                                       |
| India             | aadhaar, aadhar, adhaar, uidai                                                                                                                                                                                                                                                                                                                         |
| Italy             | codice fiscal, dati anagrafici, ehic, health card, health insurance card, p. iva, partita i.v.a., personal data, tax code, tessera sanitaria                                                                                                                                                                                                           |
| Mexico            | clave personal identidad, clave única, clave única de registro de población, clavepersonalIdentidad, curp, registration code, registry code,<br>personal identidad clave, population code                                                                                                                                                              |
| Spain             | dni, dni#, dninúmero#, documento nacional de identidad, identidad único, identidadúnico#, insurance number, national identification number, national identity, nationalid#, nationalidno#, número nacional identidad, personal identification number, personal identity no, unique identity number, uniqueid#                                          |

**Comments:** The managed data identifier for Chile (CHILE_RUT_NUMBER) is designed to detect both Rol Único Nacional (RUN) numbers and Rol Único Tributario (RUT) numbers. For either type of number, Macie doesn't report occurrences where all the digits are zeroes, such as `00000000-K`, because they're commonly used as examples.

Although DNI numbers for Argentina and Spain have different syntaxes, there are similarities between them. Therefore, Macie might report a DNI number for Argentina as a DNI number for Spain, or the other way around. In addition, Macie doesn't report occurrences of the following character sequences, which are commonly used as example DNI numbers: `99999999` and `99.999.999`. Macie also doesn't report occurrences that consist of only zeroes—for example, `000000000` and `00.000.000`.

## National Insurance Number (NINO)

**Managed data identifier ID:** UK_NATIONAL_INSURANCE_NUMBER

**Supported countries and regions:** UK

**Keyword required:** Yes. Keywords include: _insurance
no., insurance number, insurance#, national insurance number, nationalinsurance#,
nationalinsurancenumber, nin, nino_

**Comments:** None

## Passport number

**Managed data identifier ID:** Depending on country or region, CANADA_PASSPORT_NUMBER,
FRANCE_PASSPORT_NUMBER, GERMANY_PASSPORT_NUMBER, ITALY_PASSPORT_NUMBER,
SPAIN_PASSPORT_NUMBER, UK_PASSPORT_NUMBER, USA_PASSPORT_NUMBER

**Supported countries and regions:** Canada, France, Germany, Italy, Spain, UK, US

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes
for specific countries and regions.

| Country or region | Keywords                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Canada            | passeport, passeport#, passport, passport#, passportno,<br>passportno#                                                                                                         |
| France            | numéro de passeport, passeport, passeport #, passeport n °,<br>passeport non                                                                                                   |
| Germany           | ausstellungsdatum, ausstellungsort, geburtsdatum, passport, passports,<br>reisepass, reisepass–nr, reisepassnummer                                                             |
| Italy             | italian passport number, numéro passeport, numéro passeport italien,<br>passaporto, passaporto italiana, passaporto numero, passport number, repubblica<br>italiana passaporto |
| Spain             | españa pasaporte, libreta pasaporte, número pasaporte, pasaporte,<br>passport, passport book, passport no, passport number, spain<br>passport                                  |
| UK                | passeport #, passeport n °, passeport non, passeportn °,<br>passport #, passport no, passport number, passport#,<br>passportid                                                 |
| US                | passport, travel document                                                                                                                                                      |

**Comments:** None

## Permanent residence number

**Managed data identifier ID:** CANADA_NATIONAL_IDENTIFICATION_NUMBER

**Supported countries and regions:** Canada

**Keyword required:** Yes. Keywords include: _carte
résident permanent, numéro carte résident permanent, numéro résident permanent, permanent
resident card, permanent resident card number, permanent resident no, permanent resident
no., permanent resident number, pr no, pr no., pr non, pr number, résident permanent no.,
résident permanent non_

**Comments:** None

## Phone number

**Managed data identifier ID:** Depending on country or region, BRAZIL_PHONE_NUMBER,
FRANCE_PHONE_NUMBER, GERMANY_PHONE_NUMBER, ITALY_PHONE_NUMBER, PHONE_NUMBER (for Canada and
the US), SPAIN_PHONE_NUMBER, UK_PHONE_NUMBER

**Supported countries and regions:** Brazil, Canada, France, Germany, Italy, Spain, UK, US

**Keyword required:** Varies. If a keyword is in proximity of the data, the number
doesn’t have to include a country code. Keywords include: _cell,
contact, fax, fax number, mobile, phone, phone number, tel, telephone, telephone
number_. For Brazil, keywords also include: _cel, celular, fone, móvel, número residencial, numero residencial,
telefone_. If a keyword isn’t in proximity of the data, the number has
to include a country code.

**Comments:** For the US, support includes toll-free numbers.

## Public transportation card number

**Managed data identifier ID:** ARGENTINA_TARJETA_SUBE

**Supported countries and regions:** Argentina

**Keyword required:** Yes. Keywords include: _sistema
único de boleto electrónico, sube_

**Comments:**
Macie can detect 16‐digit Sistema Único de Boleto Electrónico (SUBE) card numbers that begin with `6061` and adhere to the Luhn check formula. Card number components can be separated by spaces or hyphens (‐), or not use a separator—for example, `6061 1234 1234 1234`, `6061‐1234‐1234‐1234`, and `6061123412341234`.

## Social Insurance

Number (SIN)

**Managed data identifier ID:** CANADA_SOCIAL_INSURANCE_NUMBER

**Supported countries and regions:** Canada

**Keyword required:** Yes. Keywords include: _canadian
id, numéro d'assurance sociale, sin, social insurance number_

**Comments:** None

## Social Security number (SSN)

**Managed data identifier ID:** Depending on country or region,
SPAIN_SOCIAL_SECURITY_NUMBER,
USA_SOCIAL_SECURITY_NUMBER

**Supported countries and regions:** Spain, US

**Keyword required:** Yes. For Spain, keywords include: _número de la seguridad social, social security no., social security number,
socialsecurityno#, ssn, ssn#_. For the US, keywords include:
_social security, ss#, ssn_.

**Comments:** None

## Taxpayer identification or reference number

Support includes: CUIL and CUIT codes for Argentina; CIF, NIE, and NIF numbers for Spain; CNPJ and CPF numbers for Brazil; Codice Fiscale numbers for Italy; ITINs for the US; NIT numbers for Colombia; PANs for India; RFC numbers for Mexico; RUN and RUT numbers for Chile; Steueridentifikationsnummer numbers for Germany; TFNs for Australia; TINs for France; and, TRN and UTR numbers for the UK.

**Managed data identifier ID:** Depending on country or region, ARGENTINA_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER, ARGENTINA_ORGANIZATION_TAX_IDENTIFICATION_NUMBER, AUSTRALIA_TAX_FILE_NUMBER, BRAZIL_CNPJ_NUMBER, BRAZIL_CPF_NUMBER, CHILE_RUT_NUMBER, COLOMBIA_INDIVIDUAL_NIT_NUMBER, COLOMBIA_ORGANIZATION_NIT_NUMBER, FRANCE_TAX_IDENTIFICATION_NUMBER, GERMANY_TAX_IDENTIFICATION_NUMBER, INDIA_PERMANENT_ACCOUNT_NUMBER, ITALY_NATIONAL_IDENTIFICATION_NUMBER, MEXICO_INDIVIDUAL_RFC_NUMBER, MEXICO_ORGANIZATION_RFC_NUMBER, SPAIN_NIE_NUMBER, SPAIN_NIF_NUMBER, SPAIN_TAX_IDENTIFICATION_NUMBER, UK_TAX_IDENTIFICATION_NUMBER, USA_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER

**Supported countries and regions:** Argentina, Australia, Brazil, Chile, Colombia, France, Germany, India, Italy, Mexico, Spain, UK, US

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes for specific countries and regions.

| Country or region | Keywords                                                                                                                                                                                                                                                                                                                     |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Argentina         | argentina taxpayer id, clave única de identificación tributaria, cuil, c.u.i.l, cuit, c.u.i.t, número de identificación fiscal, número de contribuyente, unified labor identification code                                                                                                                                   |
| Australia         | tax file number, tfn                                                                                                                                                                                                                                                                                                         |
| Brazil            | cadastro de pessoa física, cadastro de pessoa fisica, cadastro de pessoas físicas, cadastro de pessoas fisicas, cadastro nacional da pessoa jurídica, cadastro nacional da pessoa juridica, cnpj, cpf                                                                                                                        |
| Chile             | identidad número, nacional identidad, national unique role, nationaluniqueroleID#, número identificación, rol único nacional, rol único tributario, run, run#, r.u.n., rut, rut#, r.u.t., unique national number, unique national role, unique tax registry, unique tax role, unique tributary number, unique tributary role |
| Colombia          | nit, nit., nit#, n.i.t.                                                                                                                                                                                                                                                                                                      |
| France            | numéro d'identification fiscal, tax id, tax identification number, tax number, tin, tin#                                                                                                                                                                                                                                     |
| Germany           | identifikationsnummer, steuer id, steueridentifikationsnummer, steuernummer, tax id, tax identification number, tax number                                                                                                                                                                                                   |
| India             | e-pan, pan card, pan number, permanent account number                                                                                                                                                                                                                                                                        |
| Italy             | codice fiscal, dati anagrafici, ehic, health card, health insurance card, p. iva, partita i.v.a., personal data, tax code, tessera sanitaria                                                                                                                                                                                 |
| Mexico            | código del registro federal de contribuyentes, identificación de impuestos, identificacion de impuestos, impuesto al valor agregado, iva, iva#, i.v.a., registro federal de contribuyentes, rfc, rfc#, r.f.c.                                                                                                                |
| Spain             | cif, cif número, cifnúmero#, nie, nif, número de contribuyente, número de identidad de extranjero, número de identificación fiscal, número de impuesto corporativo, personal tax number, tax id, tax identification number, tax number, tin, tin#                                                                            |
| UK                | paye, tax id, tax id no., tax id number, tax identification, tax identification#, tax no., tax number, tax reference, tax#, taxid#, temporary reference number, tin, trn, unique tax reference, unique taxpayer reference, utr                                                                                               |
| US                | i.t.i.n., individual taxpayer identification number, itin                                                                                                                                                                                                                                                                    |

**Comments:** The managed data identifier for Chile (CHILE_RUT_NUMBER) is designed to detect both Rol Único Nacional (RUN) numbers and Rol Único Tributario (RUT) numbers. For Registro Federal de Contribuyentes (RFC) numbers for Mexico, Macie doesn't report occurrences of the following character sequences, which are commonly used as example RFC numbers: `XAXX010101000` and `XEXX010101000`.

For several types of taxpayer identification and reference numbers, Macie doesn't report occurrences where all the digits are zeroes—for example, `00000000-K`, `000000000`, and `00.000.000`. This is because the use of only zeroes is common in examples of certain types of taxpayer identification and reference numbers.

## Vehicle identification number (VIN)

**Managed data identifier ID:** VEHICLE_IDENTIFICATION_NUMBER

**Supported countries and regions:** Any, if the VIN is in proximity of a keyword in one of the
following languages: English, French, German, Lithuanian, Polish, Portuguese, Romanian, or
Spanish.

**Keyword required:** Yes. Keywords include: _Fahrgestellnummer, niv, numarul de identificare, numarul seriei de sasiu, numer
VIN, Número de Identificação do Veículo, Número de Identificación de Automóviles, numéro
d'identification du véhicule, vehicle identification number, vin, VIN
numeris_

**Comments:** Macie can detect VINs that consist of a 17-character sequence
and adhere to the ISO 3779 and 3780 standards. These standards were designed for worldwide
use.
