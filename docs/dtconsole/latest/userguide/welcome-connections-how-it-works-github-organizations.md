# How connections in

AWS CodeConnections work with organizations

For organizations with a provider, such as GitHub Organizations, you cannot install a
GitHub app into multiple GitHub Organizations. A connection has a 1:1 mapping with an
organization through the use of the Github connector app. The connector app should be
separate for every organization in GitHub or GitHub Enterprise Server and should have a
connection associated with it.

For example, to work with multiple organizations on the same GitHub server, you must
create separate connections for each organization and install separate GitHub apps for these
organizations. The target account on the Github side, however, can be the same.
