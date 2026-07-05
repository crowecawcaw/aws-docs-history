End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Patch baselines

By default, all operating system (OS) vendor-provided patches are installed
using the AMS-default patch baseline. If you want to restrict which patches
are installed, you can optionally create a patch baseline using the RFC change
type Deployment | Patching | SSM patch baseline | Create `OS` (CT ID varies per operating system).

For information about using these change types, see
[Patching subcategory](../ctref/deployment-patching-section.md "../ctref/deployment-patching-section.md").
