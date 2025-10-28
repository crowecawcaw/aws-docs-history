# Controlling Access

a AWS Service Catalog portfolio gives your administrators a level of access
control for your groups of end users. When you add users to a portfolio, they can browse
and launch any of the products in the portfolio. For more information, see [Managing Portfolios](catalogs_portfolios.md "catalogs_portfolios.md").

## Constraints

Constraints control which rules are applied to your end users
when launching a product from a specific portfolio. You use them to apply limits to
products for governance or cost control. For more information about constraints, see
[Using AWS Service Catalog Constraints](constraints.md "constraints.md").

AWS Service Catalog launch constraints give you more control
over permissions needed by an end user. When your administrator creates a launch
constraint for a product in a portfolio, the launch constraint associates a role ARN
that is used when your end users launch the product from that portfolio. Using this
pattern, you can control access to AWS resource creation. For more information, see
[AWS Service Catalog Launch Constraints](constraints-launch.md "constraints-launch.md").
