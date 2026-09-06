

# Managed data identifiers for PII
<a name="mdis-reference-pii"></a>

Amazon Macie can detect multiple types of sensitive, personally identifiable information (PII) by using managed data identifiers. The topics on this page list each type and provide information about the managed data identifiers that are designed to detect the data. Each topic provides the following information:<a name="mdi-ref-fields-plural"></a>
+ **Managed data identifier ID** – Specifies the unique identifier (ID) for one or more managed data identifiers that are designed to detect the data. When you [create a sensitive data discovery job](discovery-jobs-create.md) or [configure settings for automated sensitive data discovery](discovery-asdd-account-configure.md), you can use these IDs to specify which managed data identifiers you want Macie to use when it analyzes data.
+ **Supported countries and regions** – Indicates which countries and regions the applicable managed data identifiers are designed for. If the managed data identifiers aren't designed for particular countries or regions, this value is *Any*.
+ **Keyword required** – Specifies whether detection requires a keyword to be in proximity of the data. If a keyword is required, the topic also provides examples of required keywords. For information about how Macie uses keywords when it analyzes data, see [Keyword requirements](managed-data-identifiers-keywords.md).
+ **Comments** – Provides any relevant details that might affect your choice of managed data identifier or your investigation into reported occurrences of the sensitive data. The details include information such as supported standards, syntax requirements, and exceptions.

The topics are listed in alphabetical order by sensitive data type.

**Topics**
+ [Birth date](#mdis-reference-DATE_OF_BIRTH)
+ [Driver’s license identification number](#mdis-reference-DL-num)
+ [Electoral roll number](#mdis-reference-electoral-roll-num)
+ [Full name](#mdis-reference-full-name)
+ [Global Positioning System (GPS) coordinates](#mdis-reference-GPS)
+ [HTTP cookie](#mdis-reference-HTTP_COOKIE)
+ [Mailing address](#mdis-reference-mailing-address)
+ [National identification number](#mdis-reference-national-id)
+ [National Insurance Number (NINO)](#mdis-reference-NINO)
+ [Passport number](#mdis-reference-passport-num)
+ [Permanent residence number](#mdis-reference-permanent-residence-num)
+ [Phone number](#mdis-reference-phone-num)
+ [Public transportation card number](#mdis-reference-public-transport-num)
+ [Social Insurance Number (SIN)](#mdis-reference-social-insurance-num)
+ [Social Security number (SSN)](#mdis-reference-social-security-num)
+ [Taxpayer identification or reference number](#mdis-reference-taxpayer-num)
+ [Vehicle identification number (VIN)](#mdis-reference-vin)

## Birth date
<a name="mdis-reference-DATE_OF_BIRTH"></a>

**Managed data identifier ID:** DATE\_OF\_BIRTH

**Supported countries and regions:** Any

**Keyword required:** Yes. Keywords include: *bday, b-day, birth date, birthday, date of birth, dob*

**Comments:** Support includes most date formats, such as all digits and combinations of digits and names of months. Date components can be separated by spaces, slashes (/), or hyphens (‐).

## Driver’s license identification number
<a name="mdis-reference-DL-num"></a>

**Managed data identifier ID:** Depending on country or region, AUSTRALIA\_DRIVERS\_LICENSE, AUSTRIA\_DRIVERS\_LICENSE, BELGIUM\_DRIVERS\_LICENSE, BULGARIA\_DRIVERS\_LICENSE, CANADA\_DRIVERS\_LICENSE, CROATIA\_DRIVERS\_LICENSE, CYPRUS\_DRIVERS\_LICENSE, CZECHIA\_DRIVERS\_LICENSE, DENMARK\_DRIVERS\_LICENSE, DRIVERS\_LICENSE (for the US), ESTONIA\_DRIVERS\_LICENSE, FINLAND\_DRIVERS\_LICENSE, FRANCE\_DRIVERS\_LICENSE, GERMANY\_DRIVERS\_LICENSE, GREECE\_DRIVERS\_LICENSE, HUNGARY\_DRIVERS\_LICENSE, INDIA\_DRIVERS\_LICENSE, IRELAND\_DRIVERS\_LICENSE, ITALY\_DRIVERS\_LICENSE, LATVIA\_DRIVERS\_LICENSE, LITHUANIA\_DRIVERS\_LICENSE, LUXEMBOURG\_DRIVERS\_LICENSE, MALTA\_DRIVERS\_LICENSE, NETHERLANDS\_DRIVERS\_LICENSE, POLAND\_DRIVERS\_LICENSE, PORTUGAL\_DRIVERS\_LICENSE, ROMANIA\_DRIVERS\_LICENSE, SLOVAKIA\_DRIVERS\_LICENSE, SLOVENIA\_DRIVERS\_LICENSE, SPAIN\_DRIVERS\_LICENSE, SWEDEN\_DRIVERS\_LICENSE, UK\_DRIVERS\_LICENSE

**Supported countries and regions:** Australia, Austria, Belgium, Bulgaria, Canada, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, India, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, UK, US

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes for specific countries and regions.


| Country or region | Keywords | 
| --- | --- | 
| Australia | dl\#, dl:, dlno\#, driver licence, driver license, driver permit, drivers lic., drivers licence, driver's licence, drivers license, driver's license, drivers permit, driver's permit, drivers permit number, driving licence, driving license, driving permit | 
| Austria | führerschein, fuhrerschein, führerschein republik österreich, fuhrerschein republik osterreich | 
| Belgium | fuehrerschein, fuehrerschein- nr, fuehrerscheinnummer, fuhrerschein, führerschein, fuhrerschein- nr, führerschein- nr, fuhrerscheinnummer, führerscheinnummer, numéro permis conduire, permis de conduire, rijbewijs, rijbewijsnummer | 
| Bulgaria | превозно средство, свидетелство за управление на моторно, свидетелство за управление на мпс, сумпс, шофьорска книжка | 
| Canada | dl\#, dl:, dlno\#, driver licence, driver licences, driver license, driver licenses, driver permit, drivers lic., drivers licence, driver's licence, drivers licences, driver's licences, drivers license, driver's license, drivers licenses, driver's licenses, drivers permit, driver's permit, drivers permit number, driving licence, driving license, driving permit, permis de conduire | 
| Croatia | vozačka dozvola | 
| Cyprus | άδεια οδήγησης | 
| Czech Republic | číslo licence, císlo licence řidiče, číslo řidičského průkazu, ovladače lic., povolení k jízdě, povolení řidiče, řidiči povolení, řidičský prúkaz, řidičský průkaz | 
| Denmark | kørekort, kørekortnummer | 
| Estonia | juhi litsentsi number, juhiloa number, juhiluba, juhiluba number | 
| Finland | ajokortin numero, ajokortti, förare lic., körkort, körkort nummer, kuljettaja lic., permis de conduire | 
| France | permis de conduire | 
| Germany | fuehrerschein, fuehrerschein- nr, fuehrerscheinnummer, fuhrerschein, führerschein, fuhrerschein- nr, führerschein- nr, fuhrerscheinnummer, führerscheinnummer | 
| Greece | δεια οδήγησης, adeia odigisis | 
| Hungary | illesztőprogramok lic, jogosítvány, jogsi, licencszám, vezető engedély, vezetői engedély | 
| India | driver licence, driver licences, driver license, driver licenses, drivers lic., drivers licence, driver's licence, drivers licences, driver's licences, drivers license, driver's license, drivers licenses, driver's licenses, driving licence, driving license | 
| Ireland | ceadúnas tiomána | 
| Italy | patente di guida, patente di guida numero, patente guida, patente guida numero | 
| Latvia | autovadītāja apliecība, licences numurs, vadītāja apliecība, vadītāja apliecības numurs, vadītāja atļauja, vadītāja licences numurs, vadītāji lic. | 
| Lithuania | vairuotojo pažymėjimas | 
| Luxembourg | fahrerlaubnis, führerschäin | 
| Malta | liċenzja tas-sewqan | 
| Netherlands | permis de conduire, rijbewijs, rijbewijsnummer | 
| Poland | numer licencyjny, prawo jazdy, zezwolenie na prowadzenie | 
| Portugal | carta de condução, carteira de habilitação, carteira de motorist, carteira habilitação, carteira motorist, licença condução, licença de condução, número de licença, número licença, permissão condução, permissão de condução | 
| Romania | numărul permisului de conducere, permis de conducere | 
| Slovakia | číslo licencie, číslo vodičského preukazu, ovládače lic., povolenia vodičov, povolenie jazdu, povolenie na jazdu, povolenie vodiča, vodičský preukaz | 
| Slovenia | vozniško dovoljenje | 
| Spain | carnet conducer, el carnet de conducer, licencia conducer, licencia de manejo, número carnet conducer, número de carnet de conducer, número de permiso conducer, número de permiso de conducer, número licencia conducer, número permiso conducer, permiso conducción, permiso conducer, permiso de conducción | 
| Sweden | ajokortin numero, dlno\# ajokortti, drivere lic., förare lic., körkort, körkort nummer, körkortsnummer, kuljettajat lic.  | 
| UK | dl\#, dl:, dlno\#, driver licence, driver licences, driver license, driver licenses, driver permit, drivers lic., drivers licence, driver's licence, drivers licences, driver's licences, drivers license, driver's license, drivers licenses, driver's licenses, drivers permit, driver's permit, drivers permit number, driving licence, driving license, driving permit | 
| US | dl\#, dl:, dlno\#, driver licence, driver licences, driver license, driver licenses, driver permit, drivers lic., drivers licence, driver's licence, drivers licences, driver's licences, drivers license, driver's license, drivers licenses, driver's licenses, drivers permit, driver's permit, drivers permit number, driving licence, driving license, driving permit | 

**Comments:** None

## Electoral roll number
<a name="mdis-reference-electoral-roll-num"></a>

**Managed data identifier ID:** UK\_ELECTORAL\_ROLL\_NUMBER

**Supported countries and regions:** UK

**Keyword required:** Yes. Keywords include: *electoral \#, electoral number, electoral roll \#, electoral roll no., electoral roll number, electoralrollno*

**Comments:** None

## Full name
<a name="mdis-reference-full-name"></a>

**Managed data identifier ID:** NAME

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** Macie can detect full names only. Support is limited to Latin character sets.

## Global Positioning System (GPS) coordinates
<a name="mdis-reference-GPS"></a>

**Managed data identifier ID:** LATITUDE\_LONGITUDE

**Supported countries and regions:** Any, if the coordinates are in proximity of an English keyword.

**Keyword required:** Yes. Keywords include: *coordinate, coordinates, lat long, latitude longitude, position*

**Comments:** Macie can detect GPS coordinates if the latitude and longitude coordinates are stored as a pair and they're in Decimal Degrees (DD) format, for example `41.948614,-87.655311`. Support doesn't include detection of coordinates in: Degrees Decimal Minutes (DDM) format, for example `41°56.9168'N 87°39.3187'W`; or Degrees, Minutes, Seconds (DMS) format, for example `41°56'55.0104"N 87°39'19.1196"W`.

## HTTP cookie
<a name="mdis-reference-HTTP_COOKIE"></a>

**Managed data identifier ID:** HTTP\_COOKIE

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** Detection requires a complete `Cookie` or `Set-Cookie` header. The header can include one or more name-value pairs, for example: `Set-Cookie: id=TWlrZQ` and `Cookie: session=3948; lang=en`.

## Mailing address
<a name="mdis-reference-mailing-address"></a>

**Managed data identifier ID:** ADDRESS (for Australia, Canada, France, Germany, Italy, Spain, UK, and the US), BRAZIL\_CEP\_CODE (for Brazil's Código de Endereçamento Postal)

**Supported countries and regions:** Australia, Brazil, Canada, France, Germany, Italy, Spain, UK, US

**Keyword required:** Varies. Keywords aren't required by the ADDRESS managed data identifier. Keywords are required by the BRAZIL\_CEP\_CODE managed data identifier. Keywords include: *cep, código de endereçamento postal, codigo de endereçamento postal, código postal, codigo postal*

**Comments:** Although a keyword isn't required by the ADDRESS managed data identifier, detection requires an address to include the name of a city or place and a corresponding ZIP or Postal Code in a supported country or region. The BRAZIL\_CEP\_CODE managed data identifier can detect only the Código de Endereçamento Postal (CEP) portion of an address.

## National identification number
<a name="mdis-reference-national-id"></a>

Support includes: Aadhaar numbers for India; Cédula de Ciudadanía numbers for Colombia; Clave Única de Registro de Población (CURP) numbers for Mexico; Codice Fiscale numbers for Italy; Documento Nacional de Identidad (DNI) numbers for Argentina and Spain; French National Institute for Statistics and Economic Studies (INSEE) codes; German National Identity Card numbers; Registro Geral (RG) numbers for Brazil; and, Rol Único Nacional (RUN) numbers for Chile.

**Managed data identifier ID:** Depending on country or region, ARGENTINA\_DNI\_NUMBER, BRAZIL\_RG\_NUMBER, CHILE\_RUT\_NUMBER, COLOMBIA\_CITIZENSHIP\_CARD\_NUMBER, FRANCE\_NATIONAL\_IDENTIFICATION\_NUMBER, GERMANY\_NATIONAL\_IDENTIFICATION\_NUMBER, INDIA\_AADHAAR\_NUMBER, ITALY\_NATIONAL\_IDENTIFICATION\_NUMBER, MEXICO\_CURP\_NUMBER, SPAIN\_DNI\_NUMBER

**Supported countries and regions:** Argentina, Brazil, Chile, Colombia, France, Germany, India, Italy, Mexico, Spain

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes for specific countries and regions.


| Country or region | Keywords | 
| --- | --- | 
| Argentina | dni, dni\#, d.n.i., documento nacional de identidad | 
| Brazil | registro geral, rg | 
| Chile | identidad número, nacional identidad, national unique role, nationaluniqueroleID\#, número identificación, rol único nacional, rol único tributario, run, run\#, r.u.n., rut, rut\#, r.u.t., unique national number, unique national role, unique tax registry, unique tax role, unique tributary number, unique tributary role | 
| Colombia | cédula de ciudadanía, documento de identificación | 
| France | assurance sociale, carte nationale d’identité, cni, code sécurité sociale, French social security number, fssn\#, insee, insurance number, national id number, nationalid\#, numéro d'assurance, sécurité sociale, sécurité sociale non., sécurité sociale numéro, social, social security, social security number, socialsecuritynumber, ss\#, ssn, ssn\# | 
| Germany | ausweisnummer, id number, identification number, identity number, insurance number, personal id, personalausweis | 
| India | aadhaar, aadhar, adhaar, uidai | 
| Italy | codice fiscal, dati anagrafici, ehic, health card, health insurance card, p. iva, partita i.v.a., personal data, tax code, tessera sanitaria | 
| Mexico | clave personal identidad, clave única, clave única de registro de población, clavepersonalIdentidad, curp, registration code, registry code, personal identidad clave, population code | 
| Spain | dni, dni\#, dninúmero\#, documento nacional de identidad, identidad único, identidadúnico\#, insurance number, national identification number, national identity, nationalid\#, nationalidno\#, número nacional identidad, personal identification number, personal identity no, unique identity number, uniqueid\# | 

**Comments:** The managed data identifier for Chile (CHILE\_RUT\_NUMBER) is designed to detect both Rol Único Nacional (RUN) numbers and Rol Único Tributario (RUT) numbers. For either type of number, Macie doesn't report occurrences where all the digits are zeroes, such as `00000000-K`, because they're commonly used as examples.

Although DNI numbers for Argentina and Spain have different syntaxes, there are similarities between them. Therefore, Macie might report a DNI number for Argentina as a DNI number for Spain, or the other way around. In addition, Macie doesn't report occurrences of the following character sequences, which are commonly used as example DNI numbers: `99999999` and `99.999.999`. Macie also doesn't report occurrences that consist of only zeroes—for example, `000000000` and `00.000.000`.

## National Insurance Number (NINO)
<a name="mdis-reference-NINO"></a>

**Managed data identifier ID:** UK\_NATIONAL\_INSURANCE\_NUMBER

**Supported countries and regions:** UK

**Keyword required:** Yes. Keywords include: *insurance no., insurance number, insurance\#, national insurance number, nationalinsurance\#, nationalinsurancenumber, nin, nino*

**Comments:** None

## Passport number
<a name="mdis-reference-passport-num"></a>

**Managed data identifier ID:** Depending on country or region, CANADA\_PASSPORT\_NUMBER, FRANCE\_PASSPORT\_NUMBER, GERMANY\_PASSPORT\_NUMBER, ITALY\_PASSPORT\_NUMBER, SPAIN\_PASSPORT\_NUMBER, UK\_PASSPORT\_NUMBER, USA\_PASSPORT\_NUMBER

**Supported countries and regions:** Canada, France, Germany, Italy, Spain, UK, US

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes for specific countries and regions.


| Country or region | Keywords | 
| --- | --- | 
| Canada | passeport, passeport\#, passport, passport\#, passportno, passportno\# | 
| France | numéro de passeport, passeport, passeport \#, passeport n °, passeport non | 
| Germany | ausstellungsdatum, ausstellungsort, geburtsdatum, passport, passports, reisepass, reisepass–nr, reisepassnummer | 
| Italy | italian passport number, numéro passeport, numéro passeport italien, passaporto, passaporto italiana, passaporto numero, passport number, repubblica italiana passaporto | 
| Spain | españa pasaporte, libreta pasaporte, número pasaporte, pasaporte, passport, passport book, passport no, passport number, spain passport | 
| UK | passeport \#, passeport n °, passeport non, passeportn °, passport \#, passport no, passport number, passport\#, passportid | 
| US | passport, travel document | 

**Comments:** None

## Permanent residence number
<a name="mdis-reference-permanent-residence-num"></a>

**Managed data identifier ID:** CANADA\_NATIONAL\_IDENTIFICATION\_NUMBER

**Supported countries and regions:** Canada

**Keyword required:** Yes. Keywords include: *carte résident permanent, numéro carte résident permanent, numéro résident permanent, permanent resident card, permanent resident card number, permanent resident no, permanent resident no., permanent resident number, pr no, pr no., pr non, pr number, résident permanent no., résident permanent non*

**Comments:** None

## Phone number
<a name="mdis-reference-phone-num"></a>

**Managed data identifier ID:** Depending on country or region, BRAZIL\_PHONE\_NUMBER, FRANCE\_PHONE\_NUMBER, GERMANY\_PHONE\_NUMBER, ITALY\_PHONE\_NUMBER, PHONE\_NUMBER (for Canada and the US), SPAIN\_PHONE\_NUMBER, UK\_PHONE\_NUMBER

**Supported countries and regions:** Brazil, Canada, France, Germany, Italy, Spain, UK, US

**Keyword required:** Varies. If a keyword is in proximity of the data, the number doesn’t have to include a country code. Keywords include: *cell, contact, fax, fax number, mobile, phone, phone number, tel, telephone, telephone number*. For Brazil, keywords also include: *cel, celular, fone, móvel, número residencial, numero residencial, telefone*. If a keyword isn’t in proximity of the data, the number has to include a country code.

**Comments:** For the US, support includes toll-free numbers.

## Public transportation card number
<a name="mdis-reference-public-transport-num"></a>

**Managed data identifier ID:** ARGENTINA\_TARJETA\_SUBE

**Supported countries and regions:** Argentina

**Keyword required:** Yes. Keywords include: *sistema único de boleto electrónico, sube*

**Comments:** Macie can detect 16‐digit Sistema Único de Boleto Electrónico (SUBE) card numbers that begin with `6061` and adhere to the Luhn check formula. Card number components can be separated by spaces or hyphens (‐), or not use a separator—for example, `6061 1234 1234 1234`, `6061‐1234‐1234‐1234`, and `6061123412341234`.

## Social Insurance Number (SIN)
<a name="mdis-reference-social-insurance-num"></a>

**Managed data identifier ID:** CANADA\_SOCIAL\_INSURANCE\_NUMBER

**Supported countries and regions:** Canada

**Keyword required:** Yes. Keywords include: *canadian id, numéro d'assurance sociale, sin, social insurance number*

**Comments:** None

## Social Security number (SSN)
<a name="mdis-reference-social-security-num"></a>

**Managed data identifier ID:** Depending on country or region, SPAIN\_SOCIAL\_SECURITY\_NUMBER, USA\_SOCIAL\_SECURITY\_NUMBER

**Supported countries and regions:** Spain, US

**Keyword required:** Yes. For Spain, keywords include: *número de la seguridad social, social security no., social security number, socialsecurityno\#, ssn, ssn\#*. For the US, keywords include: *social security, ss\#, ssn*.

**Comments:** None

## Taxpayer identification or reference number
<a name="mdis-reference-taxpayer-num"></a>

Support includes: CUIL and CUIT codes for Argentina; CIF, NIE, and NIF numbers for Spain; CNPJ and CPF numbers for Brazil; Codice Fiscale numbers for Italy; ITINs for the US; NIT numbers for Colombia; PANs for India; RFC numbers for Mexico; RUN and RUT numbers for Chile; Steueridentifikationsnummer numbers for Germany; TFNs for Australia; TINs for France; and, TRN and UTR numbers for the UK.

**Managed data identifier ID:** Depending on country or region, ARGENTINA\_INDIVIDUAL\_TAX\_IDENTIFICATION\_NUMBER, ARGENTINA\_ORGANIZATION\_TAX\_IDENTIFICATION\_NUMBER, AUSTRALIA\_TAX\_FILE\_NUMBER, BRAZIL\_CNPJ\_NUMBER, BRAZIL\_CPF\_NUMBER, CHILE\_RUT\_NUMBER, COLOMBIA\_INDIVIDUAL\_NIT\_NUMBER, COLOMBIA\_ORGANIZATION\_NIT\_NUMBER, FRANCE\_TAX\_IDENTIFICATION\_NUMBER, GERMANY\_TAX\_IDENTIFICATION\_NUMBER, INDIA\_PERMANENT\_ACCOUNT\_NUMBER, ITALY\_NATIONAL\_IDENTIFICATION\_NUMBER, MEXICO\_INDIVIDUAL\_RFC\_NUMBER, MEXICO\_ORGANIZATION\_RFC\_NUMBER, SPAIN\_NIE\_NUMBER, SPAIN\_NIF\_NUMBER, SPAIN\_TAX\_IDENTIFICATION\_NUMBER, UK\_TAX\_IDENTIFICATION\_NUMBER, USA\_INDIVIDUAL\_TAX\_IDENTIFICATION\_NUMBER

**Supported countries and regions:** Argentina, Australia, Brazil, Chile, Colombia, France, Germany, India, Italy, Mexico, Spain, UK, US

**Keyword required:** Yes. The following table lists the keywords that Macie recognizes for specific countries and regions.


| Country or region | Keywords | 
| --- | --- | 
| Argentina | argentina taxpayer id, clave única de identificación tributaria, cuil, c.u.i.l, cuit, c.u.i.t, número de identificación fiscal, número de contribuyente, unified labor identification code | 
| Australia | tax file number, tfn | 
| Brazil | cadastro de pessoa física, cadastro de pessoa fisica, cadastro de pessoas físicas, cadastro de pessoas fisicas, cadastro nacional da pessoa jurídica, cadastro nacional da pessoa juridica, cnpj, cpf | 
| Chile | identidad número, nacional identidad, national unique role, nationaluniqueroleID\#, número identificación, rol único nacional, rol único tributario, run, run\#, r.u.n., rut, rut\#, r.u.t., unique national number, unique national role, unique tax registry, unique tax role, unique tributary number, unique tributary role | 
| Colombia | nit, nit., nit\#, n.i.t. | 
| France | numéro d'identification fiscal, tax id, tax identification number, tax number, tin, tin\# | 
| Germany | identifikationsnummer, steuer id, steueridentifikationsnummer, steuernummer, tax id, tax identification number, tax number | 
| India | e-pan, pan card, pan number, permanent account number | 
| Italy | codice fiscal, dati anagrafici, ehic, health card, health insurance card, p. iva, partita i.v.a., personal data, tax code, tessera sanitaria | 
| Mexico | código del registro federal de contribuyentes, identificación de impuestos, identificacion de impuestos, impuesto al valor agregado, iva, iva\#, i.v.a., registro federal de contribuyentes, rfc, rfc\#, r.f.c. | 
| Spain | cif, cif número, cifnúmero\#, nie, nif, número de contribuyente, número de identidad de extranjero, número de identificación fiscal, número de impuesto corporativo, personal tax number, tax id, tax identification number, tax number, tin, tin\# | 
| UK | paye, tax id, tax id no., tax id number, tax identification, tax identification\#, tax no., tax number, tax reference, tax\#, taxid\#, temporary reference number, tin, trn, unique tax reference, unique taxpayer reference, utr | 
| US | i.t.i.n., individual taxpayer identification number, itin | 

**Comments:** The managed data identifier for Chile (CHILE\_RUT\_NUMBER) is designed to detect both Rol Único Nacional (RUN) numbers and Rol Único Tributario (RUT) numbers. For Registro Federal de Contribuyentes (RFC) numbers for Mexico, Macie doesn't report occurrences of the following character sequences, which are commonly used as example RFC numbers: `XAXX010101000` and `XEXX010101000`.

For several types of taxpayer identification and reference numbers, Macie doesn't report occurrences where all the digits are zeroes—for example, `00000000-K`, `000000000`, and `00.000.000`. This is because the use of only zeroes is common in examples of certain types of taxpayer identification and reference numbers.

## Vehicle identification number (VIN)
<a name="mdis-reference-vin"></a>

**Managed data identifier ID:** VEHICLE\_IDENTIFICATION\_NUMBER

**Supported countries and regions:** Any, if the VIN is in proximity of a keyword in one of the following languages: English, French, German, Lithuanian, Polish, Portuguese, Romanian, or Spanish.

**Keyword required:** Yes. Keywords include: *Fahrgestellnummer, niv, numarul de identificare, numarul seriei de sasiu, numer VIN, Número de Identificação do Veículo, Número de Identificación de Automóviles, numéro d'identification du véhicule, vehicle identification number, vin, VIN numeris*

**Comments:** Macie can detect VINs that consist of a 17-character sequence and adhere to the ISO 3779 and 3780 standards. These standards were designed for worldwide use.