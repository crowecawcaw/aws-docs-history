# Nova Act model version selection

The Nova Act service relies on a custom foundation model, specially trained for UI-forward applications such as browser automation, tool use, and Human-in-the-Loop.

We release models under two support levels:

- **General Availability (GA)** - Stable releases for production applications, supported for at least 1 year.
- **Preview** - Preview releases that give you an opportunity to try out new functionality and model performance.
  There are two approaches for selecting the model version for your workflow:

- **Automatically track to the latest version**
  - Select the `nova-act-latest` alias to automatically use the latest GA model version.
  - Select the `nova-act-preview` alias to automatically use the latest preview model.

- **Pin to a specific model version** - Select a specific model version that will be supported for at least 1 year.

###### Note

`nova-act-latest` only tracks GA models and will never automatically update to a preview model.

## Available model selection IDs

| Model-Id           | Description                                                                                                                                                                                                                                                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nova-act-latest`  | Alias to the latest GA model. Your workflows automatically track the latest GA model that your Nova Act SDK version supports.                                                                                                                                                                                           |
| `nova-act-preview` | Alias to the latest preview model. Your workflow automatically tracks the latest preview model that your Nova Act SDK supports.<br>\*_Note:_<br>• If the latest preview model requires a newer SDK version than you’re using, you’ll get the most recent GA model that your SDK supports, along with a warning message. |
| `nova-act-v1.0`    | The GA model released on December 2, 2025. This is the first example of a pinable model selection ID.                                                                                                                                                                                                                   |

###### Note

At launch (December 2, 2025), all three model IDs point to the same v1.0 model. The aliases automatically track newer versions as they become available.

## Model Selection Options

Specify the model version using the **`model_id`** parameter in your workflow definition. The following example uses **`model_id="nova-act-latest"`**:

```
 from nova_act import NovaAct, workflow

@workflow(workflow_definition_name="<your-workflow-name-here>", model_id="nova-act-latest")
def explore_travel_destinations():
    """Explore travel destinations."""
    with NovaAct(starting_page="https://nova.amazon.com/act/gym") as nova:
        nova.act("Click on NextDot, then explore possible destinations.")
```
