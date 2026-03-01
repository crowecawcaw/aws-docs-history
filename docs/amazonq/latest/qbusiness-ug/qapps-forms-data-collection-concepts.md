# Data collection concepts

This topic outlines specific concepts and features of Data collection forms in
Amazon Q Apps. These concepts are key to understanding how to collect data from users with
Amazon Q Apps.

###### Topics

- [Data collection](#qapps-forms-data-collection "#qapps-forms-data-collection")
- [Data collection form](#qapps-forms-data-collection-form "#qapps-forms-data-collection-form")
- [Creator](#qapps-forms-creator "#qapps-forms-creator")
- [Data collection owner](#qapps-forms-owner "#qapps-forms-owner")
- [User](#qapps-forms-user "#qapps-forms-user")
- [Shareable link](#qapps-forms-shareable-link "#qapps-forms-shareable-link")
- [Access control and security](#qapps-forms-access-control-and-security "#qapps-forms-access-control-and-security")

## Data collection

A _data collection_ is a pool of data that contains all
participant responses submitted through the data collection form, as well as the
configuration settings for how participants can access and submit data. Key aspects
of data collections include the following:

- Instantiation – After you publish your data collection app to the
  library, other users can open it and create a data collection. When a user
  creates a data collection, they become the data collection owner. Each owner
  has a unique shareable link they use control over which users participate.
  There can be multiple data collections for a single app.
- Data isolation – Each data collection maintains its own separate
  pool of data. This ensures that each owner's data collection stays
  completely separate from any other owners' using the app.
- Access control – The data collection owner creates and shares
  unique access links with participants.
- Flexibility – Multiple owners can create data collections from the
  same data collection app. For example, you might have a Project
  Retrospective data collection app. Different owners can create new data
  collections for different projects from this same app.
- Owner control – The owner manages access and data collection
  configuration.

## Data collection form

A _data collection form_ is a unique Amazon Q Apps card type that
allows you to collect multiple pieces of information from participating users. You
can add up to 20 data collection form cards per app.

## Creator

A _creator_ is the user who designs and builds the Q App with
the data collection form. Creators have the ability to do the following:

- Add data collection form cards.
- Define the form's fields.
- Set up and make changes to the overall structure of the Q App.
- Initiate data collections (i.e., operate as the 'owner' of the data
  collection app) of the Q App tow collect data from different groups of
  users.
- Can share, re-share, and unshare the Q App to and from the
  library.
- Creators can be owners of a data collection associated with their own
  app.

## Data collection owner

An owner is a user who opens a data collection app and configures a new data
collection with a shareable link. Owners control the data collection, including
access and submission settings. They can own only one active data collection per
app.

Key aspects of the Owner role include:

- Data collection management – Owners control the data collection,
  including when to start and stop accepting responses.
- Access control – Owners manage who can by access the data
  collection by sharing the link located in the data collection
  settings.
- Advanced settings – Owners can use the data collection's advanced
  settings to allow users to submit data or see all collected data. This is
  important when the data collection is being used for sensitive information
  (e.g., personal identifying information (PII)). For more information, see
  [Access control and security](#qapps-forms-access-control-and-security "#qapps-forms-access-control-and-security").
- Limited app editing capabilities – They can't make structural
  changes to the core data collection app (i.e., add, edit, and remove
  cards).

## User

A user accesses a shared data collection app via the unique data collection link
provided by the owner to submit data. Key aspects of the user role include
–

- Response submission – users can fill out and submit data using a
  form within the data collection.
- Limited access – users cannot modify the form structure or manage
  data collection data collection settings.
- Viewing data – Depending on controlled data collection settings,
  users may or may not be able to view other users' submissions.
- Multiple submissions – users may be able to submit multiple inputs,
  based on the form's configuration.

## Shareable link

A shareable link is a unique URL that provides access to a specific data
collection app. Owners share this link with intended participants over a channel of
their preference, such as email or slack. Key features of shareable links
include:

- Access control – Links are private and can only be accessed by
  users within the organization's Q Instance.
- Data collection-specific – Each link corresponds to a particular
  data collection of the Q App.
- Security – Links may have additional security measures, such as
  expiration dates or user authentication requirements.

## Access control and security

The Data collection owner controls who can submit data and who can view the
collected data.

###### Topics

- [Data access](#qapps-forms-data-access "#qapps-forms-data-access")
- [Data visibility](#qapps-forms-data-visibility "#qapps-forms-data-visibility")
- [Multiple submissions](#qapps-forms-multiple-submissions "#qapps-forms-multiple-submissions")
- [Limitations](#qapps-forms-limitations "#qapps-forms-limitations")
- [Security](#qapps-forms-security "#qapps-forms-security")

### Data access

By default, the shareable data collection link allows anyone within your
organization to submit data. As the owner, you can choose to:

- Leave the data collection open for unlimited submissions.
- Disable submissions at any time.

### Data visibility

The visibility of submitted data is also controlled by the owner. By default,
all users can view the collected data. You can choose to hide results and only
reveal them when you're ready to review the data.

This flexibility allows you to control the data collection form process
– whether you want it to be an open, transparent exercise or a more
controlled, private exercise. The owner maintains full control over the data
collection settings and data access. Users can only submit data through the
shared data collection link and view data based on the owner's
permissions.

### Multiple submissions

By default, data collection forms limit users to one response. When you add a
data collection form, you can clear the **Limit users to one
response** check box to allow for multiple submissions from each
user within a data collection. If a user submits a form multiple times in the
same data collection, all of their submissions are be saved. If you use a single
submission form, only the recent submission is saved.

### Limitations

The following are limitations for data collection apps

1. Isolated data usage – The collected data is confined to the
   Q App where they're created. You cannot combine them with other data
   sources or use different card output types within the same app.
2. Optional form fields – By default, form fields aren't required.
   Users can submit forms without completing all fields, potentially
   resulting in incomplete data.
3. Number of data collection cards:Creators can add up to 20 data
   collection form cards to a single Q App.

### Security

All data collected through Amazon Q Apps data collection form are stored
securely within your organization's Q Instance and are not accessible to anyone
outside your organization.
