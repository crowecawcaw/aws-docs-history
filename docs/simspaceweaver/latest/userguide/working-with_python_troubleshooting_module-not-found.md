End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# A Python simulation or view client throws a ModuleNotFound error

Python throws a `ModuleNotFound` error when it can't locate
a required Python package.

If your simulation is in the AWS Cloud, make sure that your custom container has all
of the required dependencies listed in your `requirements.txt`.
Remember to run `quick-start.py` again if you
edit `requirements.txt`.

If you get the error for the `PythonBubblesSample` client,
use `pip` to install the indicated package:

```
pip install `package-name`==`version-number`
```
