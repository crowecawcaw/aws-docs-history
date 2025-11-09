# Events

Use _event detection_ to analyze text documents for speciﬁc types of events
and their related entities. Amazon Comprehend supports event detection across large collections of documents using
asynchronous analysis jobs. For more information about events, including example event analysis jobs, see [Announcing the launch of
Amazon Comprehend Events](https://aws.amazon.com/blogs/machine-learning/announcing-the-launch-of-amazon-comprehend-events/ "https://aws.amazon.com/blogs/machine-learning/announcing-the-launch-of-amazon-comprehend-events/")

### Entities

From the input text, Amazon Comprehend extracts a list of entities that are related to the detected event. An
_entity_ can be a real-world object, such as a person, place, or location; an entity can
also be a concept, such as a measurement, date, or quantity. Each occurrence of an entity is identified by a
_mention_, which is a textual reference to the entity in the input text. For each unique
entity, all mentions are grouped into a list. This list provides details for each location in the input text
where the entity occurs. Amazon Comprehend detects only the entities associated with supported event types.

Each entity associated with a supported event type returns with the following related
details:

- **Mentions**: Details for each occurrence of the
  same entity in the input text.
  - **BeginOffset**: A character offset in the
    input text that shows where the mention begins (the first character is at
    position 0).
  - **EndOffset**: A character offset in the
    input text that shows where the mention ends.
  - **Score**: The level of confidence that Amazon Comprehend
    has in the accuracy of the entity's type.
  - **GroupScore**: The level of confidence from
    Amazon Comprehend that the mention is correctly grouped with other mentions of the same
    entity.
  - **Text**: The text of the entity.
  - **Type**: The entity's type. For all
    supported entity types, see [Entity types](#events-entity-types "#events-entity-types").

### Events

Amazon Comprehend returns the list of events (of supported event types) that it detects in the input text. Each event
returns with the following related details:

- **Type**: The event's type. For all supported
  event types, see [Event types](#events-types "#events-types").
- **Arguments**: A list of arguments that are
  related to the detected event. An _argument_ consists of an
  entity that is related to the detected event. The argument's role describes the
  relationship, such as _who_ did _what_,
  _where_ and _when_.
  - **EntityIndex**: An index value that
    identifies an entity from the list of entities that Amazon Comprehend returned for this
    analysis.
  - **Role**: The argument type, which describes
    how the entity for this argument is related to the event. For all supported
    argument types, see [Argument types](#events-argument-types "#events-argument-types").
  - **Score**: The level of confidence that Amazon Comprehend
    has in the accuracy of the role detection.

- **Triggers**: A list of triggers for the detected
  event. A _trigger_ is a single word or phrase that indicates
  the occurrence of the event.
  - **BeginOffset**: A character offset in the
    input text that shows where the trigger begins (the first character is at
    position 0).
  - **EndOffset**: A character offset in the
    input text that shows where the trigger ends.
  - **Score**: The level of confidence that Amazon Comprehend
    has in the accuracy of the detection.
  - **Text**: The text of the trigger.
  - **GroupScore**: The level of confidence from
    Amazon Comprehend that the trigger is correctly grouped with other triggers for the same
    event.
  - **Type**: The type of event that this trigger
    indicates.

## Detect events results format

When your event detection job completes, Amazon Comprehend writes the analysis results to the Amazon S3 output location that
you specified when you started the job.

For each detected event, the output provides details in the following format:

```
{
   "Entities": [
     {
       "Mentions": [
         {
           "BeginOffset": number,
           "EndOffset": number,
           "Score": number,
           "GroupScore": number,
           "Text": "string",
           "Type": "string"
         }, ...
       ]
     }, ...
   ],
   "Events": [
     {
       "Type": "string",
       "Arguments": [
         {
           "EntityIndex": number,
           "Role": "string",
           "Score": number
         }, ...
       ],
       "Triggers": [
         {
           "BeginOffset": number,
           "EndOffset": number,
           "Score": number,
           "Text": "string",
           "GroupScore": number,
           "Type": "string"
         }, ...
       ]
     }, ...
   ]
 }
```

## Supported types for entities, events, and

arguments

### Entity types

| Type           | Description                                                                                                                                                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DATE           | Any reference to a date or time, whether specific or general.                                                                                                                                                          |
| FACILITY       | Buildings, airports, highways, bridges, and other permanent man-made structures<br>and real estate improvements.                                                                                                       |
| LOCATION       | Physical locations such as streets, cities, states, countries, bodies of water,<br>or geographic coordinates.                                                                                                          |
| MONETARY_VALUE | The value of something in US or other currency. The value can be specific or<br>approximate.                                                                                                                           |
| ORGANIZATION   | Companies and other groups of people defined by an established organizational<br>structure.                                                                                                                            |
| PERSON         | The names or nicknames of individuals or fictional characters.                                                                                                                                                         |
| PERSON_TITLE   | Any title which describes a person, which is usually an employment category<br>(such as CEO) or honorific (such as Mr.).                                                                                               |
| QUANTITY       | A number or value and the unit of measurement.                                                                                                                                                                         |
| STOCK_CODE     | A stock ticker symbol, such as AMZN, an International Securities Identification<br>Number (ISIN), Committee on Uniform Securities Identification Procedures (CUSIP), or<br>Stock Exchange Daily Official List (SEDOL). |

### Event types

| Type                 | Description                                                                                                                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BANKRUPTCY           | A legal proceeding involving a person or company unable to repay outstanding<br>debts.                                                                                                                                                                                       |
| EMPLOYMENT           | Occurs when an employee is hired, fired, retired, or otherwise changes<br>employment state.                                                                                                                                                                                  |
| CORPORATE_ACQUISTION | Occurs when a company obtains the possession of most or all of another<br>company's shares or physical assets to gain control of that company.                                                                                                                               |
| INVESTMENT_GENERAL   | Occurs when a person or company purchases an asset with the prospect of<br>generating future income or appreciation.                                                                                                                                                         |
| CORPORATE_MERGER     | Occurs when two or more companies unite to create a new legal entity.                                                                                                                                                                                                        |
| IPO                  | An initial public offering (IPO) of shares of a private corporation to the<br>public in a new stock issuance.                                                                                                                                                                |
| RIGHTS_ISSUE         | A group of rights offered to existing shareholders to purchase additional stock<br>shares, known as subscription warrants, in proportion to their existing<br>holdings.                                                                                                      |
| SECONDARY_OFFERING   | An offer of securities by a shareholder of a company.                                                                                                                                                                                                                        |
| SHELF_OFFERING       | A Securities and Exchange Commission (SEC) provision that allows an issuer to<br>register a new issue of security and sell portions of the issue over a period of<br>time without re-registering the security or incurring penalties. Also known as a<br>shelf registration. |
| TENDER_OFFERING      | An offer to purchase some or all of shareholders' shares in a company.                                                                                                                                                                                                       |
| STOCK_SPLIT          | Occurs when a company's board of directors increases the number of shares that<br>are outstanding by issuing more shares to current shareholders. This event also<br>applies to reverse stock splits.                                                                        |

### Argument types

| Argument types for BANKRUPTCY | Argument type                                                                  | Description |
| ----------------------------- | ------------------------------------------------------------------------------ | ----------- |
| FILER                         | The person or company filing the bankruptcy.                                   |
| DATE                          | The date or time of bankruptcy.                                                |
| PLACE                         | Location or facility where (or nearest to where) the bankruptcy took<br>place. |

| Argument types for EMPLOYMENT | Type                                          | Description |
| ----------------------------- | --------------------------------------------- | ----------- |
| EMPLOYEE                      | The person employed by a company.             |
| EMPLOYEE_TITLE                | The title of the employee.                    |
| EMPLOYER                      | The person or company employing the employee. |
| START_DATE                    | The start date or time of the employment.     |
| END_DATE                      | The end date or time of the employment.       |

| Argument types for CORPORATE_ACQUISTION, INVESTMENT_GENERAL | Type                                                                              | Description |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------- |
| AMOUNT                                                      | The monetary value associated with the transaction.                               |
| INVESTEE                                                    | The person or company associated with the investment.                             |
| INVESTOR                                                    | The person or company investing in the asset.                                     |
| DATE                                                        | The date or time of the acquisition or investment.                                |
| PLACE                                                       | Location where (or nearest to where) the acquisition or investment took<br>place. |

| Argument types for CORPORATE_MERGER | Type                                            | Description |
| ----------------------------------- | ----------------------------------------------- | ----------- |
| DATE                                | The date or time of the merger.                 |
| NEW_COMPANY                         | The new legal entity resulting from the merger. |
| PARTICIPANT                         | The company involved in the merger.             |

Argument types for IPO, RIGHTS_ISSUE, SECONDARY_OFFERING, SHELF_OFFERING,
TENDER_OFFERING| Type | Description |
| --- | --- |
| EXPIRE_DATE | The expiration date or time of the offering. |
| INVESTOR | The person or company investing in the asset. |
| OFFEREE | The person or company receiving the offering. |
| OFFERING_AMOUNT | The monetary value associated with the offering. |
| OFFERING_DATE | The date or time of the offering. |
| OFFEROR | The person or company initiating the offering. |
| OFFEROR_TOTAL_VALUE | The total monetary value associated with the offering. |
| RECORD_DATE | The record date or time of the offering. |
| SELLING_AGENT | The person or company facilitating the sale of the offering. |
| SHARE_PRICE | The monetary value associated with the share price. |
| SHARE_QUANTITY | The number of shares associated with the offering. |
| UNDERWRITERS | The company associated with the underwriting of the offering. |

| Argument types for STOCK_SPLIT | Type                                                                                                                   | Description |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| COMPANY                        | The company issuing shares of the stock split.                                                                         |
| DATE                           | The date or time of the stock split.                                                                                   |
| SPLIT_RATIO                    | The ratio of the increased new number of shares outstanding to the current<br>number of shares before the stock split. |
