# Configuring Reusable Expressions for a

Search Domain in Amazon CloudSearch

When you define an expression in a domain's configuration, you can reference the
expression in any search request. Adding an expression to the domain configuration
reduces the overhead of specifying it in every request, and helps maximize response
times and minimize costs.

When you add an expression to your domain configuration, it takes some time for the
change to be processed and the new expression to become active. To quickly test changes
to an expression, you can define and use the expression directly in a search request, as
described in [query time expressions](defining-expressions-in-requests.md "defining-expressions-in-requests.md"). After you have finished testing
and tuning an expression, you should add it to your domain configuration.

###### Topics

- [Configuring Expressions Using the Amazon CloudSearch Console](#configuring-expressions-console "#configuring-expressions-console")
- [Configuring Amazon CloudSearch Expressions Using the AWS CLI](#configuring-expressions-clt "#configuring-expressions-clt")
- [Configuring Expressions Using the Amazon CloudSearch Configuration API](#configuring-expressions-sdk "#configuring-expressions-sdk")

## Configuring Expressions Using the Amazon CloudSearch Console

###### To configure an expression

1. Open the Amazon CloudSearch console at [https://console.aws.amazon.com/cloudsearch/home](https://console.aws.amazon.com/cloudsearch/home "https://console.aws.amazon.com/cloudsearch/home").
2. From the left navigation pane, choose **Domains**.
3. Choose the name of the domain to open its configuration.
4. Go to the **Advanced search options** tab.
5. In the **Expressions** pane, choose **Add
   expression**.
6. Enter a name for the new expression.
7. For **Value**, enter the numerical expression that you
   want to evaluate at search time. You can select **Insert**
   to add special values and mathematical and trigonometric functions.
8. Choose **Save**.

## Configuring Amazon CloudSearch Expressions Using the AWS CLI

You use the `aws cloudsearch define-expression` command to define
computed expressions for a domain.

###### To configure an expression

- Run the `aws cloudsearch define-expression` command to define a new
  expression. You specify a name for the expression with the
  `--name` option, and the numeric expression that you want to
  evaluate with the `--expression` option. For example, the following request creates an expression
  called `popularhits` that takes into account a document's `popularity` and relevance `_score`.

```
aws cloudsearch define-expression --domain-name movies --name popularhits --expression '((0.3*popularity)/10.0)+(0.7* _score)'

{
    "Expression": {
        "Status": {
            "PendingDeletion": false,
            "State": "Processing",
            "CreationDate": "2014-05-01T01:15:18Z",
            "UpdateVersion": 52,
            "UpdateDate": "2014-05-01T01:15:18Z"
        },
        "Options": {
            "ExpressionName": "popularhits",
            "ExpressionValue": "((0.3*popularity)/10.0)+(0.7* _score)"
        }
    }
}
```

## Configuring Expressions Using the Amazon CloudSearch Configuration API

The AWS SDKs (except the Android and iOS SDKs) support all of the Amazon CloudSearch actions defined in the Amazon CloudSearch Configuration API, including `DefineExpression`. For more information about installing and using the AWS SDKs, see [AWS Software Development Kits](http://aws.amazon.com/code "http://aws.amazon.com/code").
