We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Names and IDs for all Objects

Every object in Amazon ML must have an identifier, or ID. The
Amazon ML console generates ID values for you, but if you use the
API you must generate your own. Each ID must be unique among all
Amazon ML objects of the same type in your AWS account. That is,
you cannot have two evaluations with the same ID. It is possible
to have an evaluation and a datasource with the same ID, although
it is not recommended.

We recommend that you use randomly generated identifiers for your
objects, prefixed with a short string to identify their type. For
example, when the Amazon ML console generates a datasource, it
assigns the datasource a random, unique ID like
"ds-zScWIuWiOxF". This ID is sufficiently random to
avoid collisions for any single user, and it's also compact and
readable. The "ds-" prefix is for convenience and
clarity, but is not required. If you're not sure what to use for
your ID strings, we recommend using hexadecimal UUID values (like
28b1e915-57e5-4e6c-a7bd-6fb4e729cb23), which are readily available
in any modern programming environment.

ID strings can contain ASCII letters, numbers, hyphens and
underscores, and can be up to 64 characters long. It is possible
and perhaps convenient to encode metadata into an ID string. But
it is not recommended because once an object has been created, its
ID cannot be changed.

Object names provide an easy way for you to associate
user-friendly metadata with each object. You can update names
after an object has been created. This makes it possible for the
object's name to reflect some aspect of your ML workflow. For
example, you might initially name an ML model "experiment
#3", and then later rename the model "final production
model". Names can be any string you want, up to 1,024
characters.
