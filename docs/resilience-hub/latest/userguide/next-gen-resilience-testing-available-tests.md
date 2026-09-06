

# Available tests
<a name="next-gen-resilience-testing-available-tests"></a>

Next generation Resilience Hub provides the following pre-configured test templates:
+ **Availability Zone: recovery** – Validate your service can detect and recover from an Availability Zone impairment.
+ **Dependency validation** – Validate how your service responds when its dependencies within the Region are impaired.
+ **Multi-Region: isolation** – Validate your service can operate independently from a Region when connectivity to another Region is unavailable.
+ **Multi-Region: recovery** – Validate your service can recover and serve clients from another Region within your recovery objectives when a Region is impaired.

Each test template declares the parameters it accepts, including whether each parameter is required and any default values.

```
aws resiliencehubv2 list-test-templates --region {{region}}
```

Use `get-test-template` to view the full definition of a test template. The response includes:
+ **actions** – The operations the test performs, each targeting a specific resource type.
+ **parameters** – The inputs you provide when you create a test from the template.

Each action includes the following:
+ **actionId** – A unique identifier for the action.
+ **description** – A description of what the action does.
+ **resourceType** – The type of resource the action targets.

Each parameter declares the following:
+ **name** – The parameter name you supply when you create a test.
+ **description** – A description of what the parameter controls.
+ **type** – The value type: `STRING`, `STRING_LIST`, or `INTEGER`.
+ **required** – Whether you must provide a value for the parameter.
+ **defaultValue** – The value used when you don't provide one. Applies to optional parameters.
+ **maxValues** – The maximum number of values you can provide for the parameter.

```
aws resiliencehubv2 get-test-template \
  --test-template-arn "arn:aws:resiliencehub:{{region}}:aws:test-template/aws-az-recovery:rtaz001" \
  --region {{region}}
```

Provide values for these parameters with the `--parameters` option when you create a test. For an example of creating a test, see [Getting started with Next generation Resilience Hub](next-gen-getting-started.md).

**Topics**
+ [Availability Zone: recovery](next-gen-resilience-testing-az-recovery.md)
+ [Dependency validation](next-gen-resilience-testing-dependency-validation.md)
+ [Multi-Region: isolation](next-gen-resilience-testing-multi-region-isolation.md)
+ [Multi-Region: recovery](next-gen-resilience-testing-multi-region-recovery.md)