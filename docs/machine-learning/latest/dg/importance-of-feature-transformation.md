We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Importance of Feature Transformation

Consider a machine learning model whose task is to decide whether
a credit card transaction is fraudulent or not. Based on your
application background knowledge and data analysis, you might
decide which data fields (or features) are important to include in
the input data. For example, transaction amount, merchant name,
address, and credit card owner's address are important to provide
to the learning process. On the other hand, a randomly generated
transaction ID carries no information (if we know that it really
is random), and is not useful.

Once you have decided on which fields to include, you transform
these features to help the learning process. Transformations add
background experience to the input data, enabling the machine
learning model to benefit from this experience. For example, the
following merchant address is represented as a string:

"123 Main Street, Seattle, WA 98101"

By itself, the address has limited expressive power – it is useful
only for learning patterns associated with that exact address.
Breaking it up into constituent parts, however, can create
additional features like "Address" (123 Main Street),
"City" (Seattle), "State" (WA) and
"Zip" (98101). Now, the learning algorithm can group
more disparate transactions together, and discover broader
patterns – perhaps some merchant zip codes experience more
fraudulent activity than others.

For more information about the feature transformation approach and
process, see
[Machine
Learning Concepts](machine-learning-concepts.md "machine-learning-concepts.md").
