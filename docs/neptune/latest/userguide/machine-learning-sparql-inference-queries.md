# SPARQL inference queries in Neptune ML

Neptune ML maps the RDF graph into a property graph to model the ML Task.
Currently, it supports the following use-cases:

- **Object classification**   –  
  Predicts the categorical feature of an object.
- **Object regression**   –  
  Predicts a numerical property of an object.
- **Object prediction**   –  
  Predicts an object given a subject and a relationship.
- **Subject prediction**   –  
  Predicts a subject given an object and a relationship.

###### Note

Neptune ML does not support subject classification and regression use cases
with SPARQL.
