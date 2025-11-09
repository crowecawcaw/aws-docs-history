# Interacting with flows in Runtime Mode

Runtime execution is how you interact with and run Amazon Quick Flows after they've been created and shared. When you open a flow from the library, you enter the runtime environment where you can provide inputs, run steps, and get results from the flow. Think of runtime as the "using" phase of flows - where the actual work gets done.

Runtime execution provides flexible ways to interact with flows, from structured step-by-step running to conversational chat-based interaction, giving you the control and experience that works best for your workflow.

## Runtime modes

Amazon Quick Flows offers three different runtime modes to match your preferred way of working and the complexity of your flow.

### Dual mode runtime

Dual mode gives you the best of both worlds by combining structured and chat interfaces in a single view. This is the default mode when you open most flows from the library.

**What you see:** The interface shows both a structured view on the left displaying all flow steps, inputs, and outputs, alongside a chat interface on the right where you can have conversations with the flow's AI agent.

**How it works:** You can interact with your flow in either interface - provide inputs through the structured forms or by chatting with the agent. The agent understands your flow's structure and can guide you through the process, request inputs, and run steps based on your conversational requests.

**Best for:** Most users and most flows, especially when you want flexibility to switch between structured interaction and natural conversation. This mode is particularly useful when you're learning a new flow or when the flow has complex logic.

**Key features:**

- Progress tracking visible in structured view
- Conversational guidance from the AI agent
- Ability to jump to any step or run steps out of order
- Real-time synchronization between chat and structured interfaces

### Full structured mode

Full structured mode provides a traditional form-based interface where you can see and interact with all Flow components in an organized, step-by-step layout.

**What you see:** A clean, organized view showing all flow steps, input fields, output areas, and action buttons. Each step is clearly labeled and shows its current status (pending, running, completed).

**How it works:** You work through the flow by filling in input fields, clicking run buttons, and reviewing outputs in a structured sequence. You can see the entire flow layout and jump to any step you need to work on.

**Best for:** Users who prefer traditional form interfaces, complex flows with many steps, or situations where you need to see the complete flow structure at once. Also ideal for flows that require precise input formatting or when working with multiple related inputs.

**Key features:**

- Clear visual progress through flow steps
- Direct input into form fields
- Immediate visibility of all Flow components
- Easy navigation between steps

### Full chat mode

Full chat mode provides a purely conversational interface where you interact with your flow entirely through natural language conversation with an AI agent.

**What you see:** A chat interface similar to messaging applications, where you have conversations with an AI agent that understands your flow and can run it based on your requests.

**How it works:** The AI agent guides you through the flow by asking for inputs, explaining what the flow can do, and running steps based on your conversational requests. You can ask the agent to run specific parts of the flow, regenerate outputs, or modify results through natural language.

**Best for:** Users who prefer conversational interfaces, simple flows with straightforward inputs, or when you want to focus on the task rather than the flow structure. Particularly useful for flows you use frequently.

**Key features:**

- Natural language interaction
- AI agent guidance and explanations
- Ability to request specific actions conversationally
- Simplified interface focused on conversation

## What is a progress tracker?

The progress tracker is a visual indicator that shows you the current status and progress of your flow execution. It helps you understand where you are in the flow, what steps have been completed, and what's currently running or waiting for input.

### How the progress tracker works

**Step status indicators:** Each step in your flow shows its current state - pending (not yet started), running (currently running), completed (finished successfully), or requiring input (waiting for you to provide information).

**Active step highlighting:** The step you're currently working on or that's currently running is highlighted and brought into view automatically. If multiple steps are running in parallel, all active steps are highlighted.

**Progressive disclosure:** Steps open and close automatically based on the flow's execution. When you start a flow, only the first step is open. As you progress, subsequent steps open when they become active, keeping your focus on the current work.

**Visual progress indicators:** Running steps show progress indicators (like spinning icons) to let you know something is happening, especially for steps that take time to complete.

### Understanding step states

**Closed steps:** Steps that haven't been reached yet or aren't currently relevant remain closed to reduce visual clutter.

**Open steps:** Steps that are active, or require your input are automatically opened and visible.

**Completed steps:** Steps that have finished successfully show their results and cannot be closed.

**Error states:** If a step encounters an error, it's clearly marked and provides information about what went wrong and how to resolve it.

## How can I start a new flow run?

Starting a new flow run gives you a fresh execution environment to work with your flow. There are several ways to begin a new run depending on your current context.

### Starting from the library

When you open a flow from the Amazon Quick Flows library, you automatically start a new run. The flow opens in dual mode by default, with the AI agent providing a greeting message and overview of what the flow can accomplish.

**What happens:** The flow initializes with empty inputs and a clean state. The AI agent introduces the flow and asks for any initial inputs needed to get started. All previous execution history is separate from this new run.

### Starting a new run from within a flow

If you're already working with a flow and want to start fresh, you can create a new run without leaving the current flow.

**Using the **New run** button:** Click the **New run** button in the chat interface or in the structured mode to start a completely new flow run. This creates a new conversation and execution context while preserving your previous run in the history.

**Confirmation process:** When you start a new run, you'll see a confirmation dialog to make sure you want to leave your current progress and begin fresh. This prevents accidental loss of work.

### What gets reset vs. preserved

**New run button:**

- Creates entirely new execution context
- Clears all inputs and outputs
- Starts fresh chat conversation
- Previous run is saved to history

## Ability to resume runs from flow history

Flow history allows you to return to previous executions of your flows, continuing where you left off or reviewing past results. This feature is essential for ongoing work and maintaining context across multiple sessions.

### Accessing flow history

**History icon:** Each flow has a history icon in the chat interface that shows all your previous runs of that specific flow. Click this icon to see a chronological list of your past executions.

**Recent runs first:** Your flow history is organized with the most recent runs at the top, along with timestamps showing when each run was created or last modified.

**Flow-specific history:** Each flow maintains its own separate history. When you view history for a Customer Issue Resolver flow, you only see runs for that specific flow, not other flows you've used.

### Resuming previous runs

**Continuing where you left off:** When you select a previous run from history, both the chat conversation and structured mode are restored to their last state. If you were in the middle of providing input for a specific step, that step will be highlighted and ready for you to continue.

**Preserved context:** All your previous inputs, generated outputs, and conversation history are maintained exactly as they were when you last worked on that run.

**Seamless continuation:** You can immediately continue working - provide additional inputs, run next steps, or modify previous results without having to start over.

### Managing your run history

**Automatic saving:** Every interaction with a flow is automatically saved to your run history. You don't need to manually save your progress.

**History persistence:** flow runs are preserved in your history for an extended period of 30 days, allowing you to return to work even after days or weeks.

**Run identification:** Each run in your history is identified by either your first message to the agent or a smart summary of what you accomplished in that session, making it easy to find the run you're looking for.

**Updating existing runs:** When you resume and continue working on a previous run, it's updated in place and moved to the top of your history list as the most recent activity.

## Working with runtime

Understanding how to effectively use the different runtime modes and features will help you get the most out of your flows.

### Switching between modes

You can easily switch between runtime modes while working with a flow:

**Dual to structured:** Click the "X" button in the chat interface to close the chat and work in full structured mode.

**Structured to dual:** Click the sparkle icon to reopen the chat interface and return to dual mode.

**Dual to chat:** Expand the chat interface to focus entirely on conversational interaction.

### Best practices for runtime

**Choose the right mode:** Use dual mode for learning new flows, structured mode for complex multi-step processes, and chat mode for familiar flows or quick tasks.

**Leverage the AI agent:** In chat and dual modes, the AI agent can explain flow capabilities, suggest next steps, and help troubleshoot issues. You can also ask the agent to customize output responses by specifying length requirements or adjusting tone. Request modifications like "summarize meeting notes in 200 words" or "make email draft more professional". Don't hesitate to ask questions about what the flow can do.

**Use history effectively:** Regularly check your flow history to resume important work or reference previous results. This is especially valuable for flows you use repeatedly with different inputs.

**Monitor progress:** Pay attention to the progress tracker to understand what's happening, especially for flows with long-running steps or complex logic.

### Handling errors and interruptions

**Error recovery:** When errors occur, the flow provides clear information about what went wrong and suggested next steps for resolution or gives you an option to retry.

**Input validation:** The system validates your inputs based on the flow's requirements and provides helpful feedback if something needs to be corrected.

## Amazon Quick Suite reference

Use this table to understand the different execution modes:

| Runtime Modes | #               | Runtime Mode      | Interface                      | Best For                          | Key Features |
| ------------- | --------------- | ----------------- | ------------------------------ | --------------------------------- | ------------ |
| 1             | Dual Mode       | Chat + Structured | Most users, learning flows     | Flexible interaction, AI guidance |
| 2             | Full Structured | Forms and buttons | Complex flows, precise control | Clear progress, direct input      |
| 3             | Full Chat       | Conversation only | Simple flows, mobile use       | Natural language, AI assistance   |

| Common Actions | #                    | Action                      | How To                             | Result |
| -------------- | -------------------- | --------------------------- | ---------------------------------- | ------ |
| 1              | Start new run        | Click \*New run<br>• button | Fresh execution, new history entry |
| 2              | Resume previous run  | History → Select run        | Continue where you left off        |
| 3              | Switch to structured | Click X in chat             | Full structured mode               |
| 4              | Switch to dual       | Click sparkle icon          | Chat + structured mode             |
