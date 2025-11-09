# Troubleshooting

If you run into an error, use the following list to try to troubleshoot the issue. If
you need further support, reach out to the SageMaker AI team at
`<sm-smart-sifting-feedback@amazon.com>`.

**Exceptions from the SageMaker smart sifting library**

Use the following reference of exceptions raised by the SageMaker smart sifting library to
troubleshoot errors and identify causes.

| Exception Name                         | Description                                                                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| SiftConfigValidationException          | Thrown from the SageMaker smart sifting library in case of any missing Config key<br>or unsupported value type for Sift Key |
| UnsupportedDataFormatException         | Thrown from the SageMaker smart sifting library in case of any unsupported<br>DataFormat for Sifting logic                  |
| LossImplementationNotProvidedException | Thrown in case of missing or not implementing Loss interface                                                                |
