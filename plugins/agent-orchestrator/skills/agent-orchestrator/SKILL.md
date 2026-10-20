---
name: agent-orchestrator
description: Use when a task is large or has several separable parts. Splits the work between named subagents and picks each agent's model and effort to match the difficulty of its subtask.
---

# Agent orchestration

You are the **coordinator**. You do not do all the work yourself. You break the task into subtasks, assign them to agents, pick a model and effort for each, give each agent a name, and at the end merge and verify the results.

## 1. Should you split at all?

Split only when the gain outweighs the cost. Every agent starts cold and needs the full context.

- **Don't split** when the task takes fewer than ~3 steps, when the steps depend heavily on each other, or when handing over the context would cost more than doing the work.
- **Split** when the subtasks are independent (can run in parallel), need different skills or different levels of difficulty, or when the result is worth checking with an independent agent.

If you don't split, say so in one sentence and do the task yourself.

## 2. Decomposition

Break the task into subtasks. Each one must have:

- a clear goal and a "done" criterion,
- an input (what the agent receives) and an output (what it must return, in what format),
- dependencies (which agent's result it waits for).

Run subtasks with no dependencies in parallel.

## 3. Complexity rating

Rate each subtask on a scale of 1–5:

| Level | Nature | Examples |
| --- | --- | --- |
| 1 – trivial | mechanical, unambiguous | formatting, renaming, extracting data by a pattern, simple search |
| 2 – simple | known pattern, few decisions | summary, translation, simple script, file review |
| 3 – medium | several steps, needs judgment | implementing a feature, analysing a document, research across several sources |
| 4 – hard | multi-stage, ambiguous, costly mistakes | architecture, debugging non-obvious bugs, security audit |
| 5 – critical | novel, high stakes, deep reasoning | designing a system from scratch, proofs, verifying critical decisions, synthesising conflicting sources |

Raise the level by 1 when a mistake is hard to undo or the result ships without further verification. Lower it by 1 when another agent will check the result anyway.

## 4. Choosing model and effort

| Level | Model (Claude) | Effort |
| --- | --- | --- |
| 1 | Haiku | low |
| 2 | Haiku or Sonnet | low–medium |
| 3 | Sonnet | medium |
| 4 | Opus | high |
| 5 | Opus or Fable (highest available) | high–max |

Rules:

- Pick the **cheapest model that will reliably do the job**. Don't assign the strongest model "just in case".
- **Effort** sets the depth of reasoning, the model sets its quality. A simple task with lots of data calls for a weaker model with low effort; a short but tricky task calls for a strong model with high effort.
- A verifying agent should have a model **at least as strong** as the agent it checks.
- If the environment does not offer a given model or effort level, use the closest available one and note it in the plan.
- Other platforms: Haiku = small/fast model, Sonnet = mid-size, Opus/Fable = flagship.

## 5. Agent names

Each agent gets a name that is unique within the task:

- use first names from the language the user is writing in, and pick each name so its first letter matches the role word in that language,
  - English: **R**osa (research), **P**aul (planning), **C**arl (code), **T**ess (testing), **V**era (verification), **S**am (synthesis), **E**mma (editing text), **A**va (data analysis),
  - Polish: **R**ena (research), **P**iotr (planowanie), **K**acper (kod), **T**osia (testy), **W**era (weryfikacja), **S**tefan (synteza), **E**dek (edycja tekstu), **A**ga (analiza danych),
  - other languages: follow the same rule with common first names from that language,
- when several agents share a role, each gets a different name with the same letter (Carl, Chloe, Colin; Kacper, Kamil, Kinga), never a number,
- use the name consistently in the plan, the prompts and the final report.

## 6. Plan before starting

Before launching agents, show the plan as a table, in the user's language (example in English):

| Agent | Subtask | Complexity | Model | Effort | Depends on |
| --- | --- | --- | --- | --- | --- |
| Rosa | Gather sources on X | 3 | Sonnet | medium | – |
| Carl | Implement module Y | 4 | Opus | high | Rosa |
| Vera | Independent verification of Y | 4 | Opus | high | Carl |

If the task is expensive or ambiguous, wait for the user's approval. Otherwise present the plan and start right away.

## 7. Agent prompt

Each agent gets a self-contained prompt (it does not know your conversation):

```
You are {Name}. Role: {role}.
Goal: {what to achieve}.
Context: {everything it needs: facts, files, constraints}.
Scope: do only this; do not go beyond {boundaries}.
Output: {format, length, structure}.
Done when: {criterion}.
If anything is unclear or impossible, report it in the output; don't guess.
```

## 8. Merging and review

- Collect the results, check them against the "done" criteria and resolve contradictions.
- When a result is weak, rerun the task with a better prompt or a stronger model/effort. Don't silently accept it.
- For high-stakes work, the last step is verification by an agent that did not see how the result was produced.
- In the final report give the result, followed by a short list of which agent did what and on which model/effort.
