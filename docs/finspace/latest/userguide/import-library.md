After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Importing library in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

You can install notebook-scoped libraries on a running Amazon FinSpace cluster directly via a FinSpace notebook. This capability is useful in scenarios in which you do
not have access to a PyPI repository but need to analyze and visualize a dataset.

Notebook-scoped libraries provide you the following benefits:

- **Runtime installation** – You can import Python libraries from PyPI repositories and install them on your remote cluster on the fly when you need them.
  These libraries are instantly available to your Spark runtime environment. There is no need to restart the notebook session or recreate your cluster.
- **Dependency isolation** – The libraries you install using FinSpace notebooks are isolated to your notebook session and don't interfere with bootstrapped cluster
  libraries or libraries installed from other notebook sessions. These notebook-scoped libraries take precedence over bootstrapped libraries. Multiple notebook
  users can import their preferred version of the library and use it without dependency clashes on the same cluster.
- **Portable library environment** – The library package installation happens from your notebook file. This allows you to recreate the library environment
  when you switch the notebook to a different cluster by re-executing the notebook code. At the end of the notebook session, the libraries you install through
  FinSpace notebooks are automatically removed from the hosting cluster.
  The following example code shows how to install pandas and matplotlib from the PiPY repository.

```
sc.install_pypi_package("pandas==0.25.1") #Install pandas version 0.25.1
sc.install_pypi_package("matplotlib", "https://pypi.org/simple") #Install matplotlib from given PyPI repository
```

You can uninstall packages using the `uninstall_package` PySpark API.

```
sc.uninstall_package('pandas')
```
