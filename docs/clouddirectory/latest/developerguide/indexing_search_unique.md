Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# Unique vs Nonunique Indexes

Unique indexes differ from nonunique indexes in enforcing uniqueness of the indexed
attribute values for objects that are attached to the index. For example, you might want to
populate Person objects into two indexes, a unique one on an “email” attribute, and a nonunique
one on a “lastname” attribute. The lastname index allows many Person objects with the same last
name to be attached. On the other hand, the `AttachToIndex` call that targets the
email index returns a `LinkNameAlreadyInUseException` error if a Person with the same
email attribute is already attached. Note that the error does not remove the Person object
itself. Consequently, an application might create the Person, attach it to the hierarchy, and
attach it to indexes, all in a single batch request. This ensures that if uniqueness is violated
on any of the indexes, the object and all of its attachments are rolled back
automatically.
