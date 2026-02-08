# Sample data models in NoSQL Workbench

The home page for the modeler and visualizer displays a number of sample models that ship
with NoSQL Workbench. This section describes these models and their potential uses.

###### Topics

- [Employee data model](#workbench.SampleModels.EmployeeDataModel "#workbench.SampleModels.EmployeeDataModel")
- [Credit card
  transactions data model](#workbench.SampleModels.CreditCardTransactionsDataModel "#workbench.SampleModels.CreditCardTransactionsDataModel")
- [Airline operations data
  model](#workbench.SampleModels.AirlineOperations "#workbench.SampleModels.AirlineOperations")

## Employee data model

This data model represents an Amazon Keyspaces schema for an employee database
application.

Applications that access employee information for a given company can use this data
model.

The access patterns supported by this data model are:

- Retrieval of an employee record with a given ID.
- Retrieval of an employee record with a given ID and division.
- Retrieval of an employee record with a given ID and name.

## Credit card

transactions data model

This data model represents an Amazon Keyspaces schema for credit card transactions at retail
stores.

The storage of credit card transactions not only helps stores with bookkeeping, but
also helps store managers analyze purchase trends, which can help them with forecasting
and planning.

The access patterns supported by this data model are:

- Retrieval of transactions by credit card number, month and year, and
  date.
- Retrieval of transactions by credit card number, category, and date.
- Retrieval of transactions by category, location, and credit card
  number.
- Retrieval of transactions by credit card number and dispute status.

## Airline operations data

model

This data model shows data about plane flights, including airports, airlines, and
flight routes.

Key components of Amazon Keyspaces modeling that are demonstrated are key-value pairs,
wide-column data stores, composite keys, and complex data types such as maps to
demonstrate common NoSQL data-access patterns.

The access patterns supported by this data model are:

- Retrieval of routes originating from a given airline at a given
  airport.
- Retrieval of routes with a given destination airport.
- Retrieval of airports with direct flights.
- Retrieval of airport details and airline details.
