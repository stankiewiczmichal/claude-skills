# claude-skills

Agent skills packaged as plugins. Every skill is a folder with a `SKILL.md`
in the open [Agent Skills](https://agentskills.io) format, so it works in Claude
and in other tools that support that format.

## Install

### Claude Code

```
/plugin marketplace add stankiewiczmichal/claude-skills
/plugin install agent-orchestrator@claude-skills
```

### Claude (claude.ai, desktop, mobile)

Download a skill's `.zip` from [Releases](../../releases) and upload it under
**Settings → Capabilities → Skills**.

### Codex (CLI, IDE extension, app)

As a plugin: Codex reads Claude-compatible marketplaces
(`.claude-plugin/marketplace.json`). Register the repo, then install the plugin
from the Plugins Directory in the ChatGPT desktop app:

```
codex plugin marketplace add stankiewiczmichal/claude-skills
```

As a single skill: ask Codex
`$skill-installer install https://github.com/stankiewiczmichal/claude-skills/tree/main/plugins/agent-orchestrator/skills/agent-orchestrator`,
or copy the skill folder yourself:

```
mkdir -p ~/.agents/skills
cp -R plugins/agent-orchestrator/skills/agent-orchestrator ~/.agents/skills/
```

Use `<project>/.agents/skills/` instead to make a skill available in one project only.
Restart Codex if the skill does not appear.

### ChatGPT

Plugins added with `codex plugin marketplace add` (see above) appear in the
Plugins Directory of the ChatGPT desktop app, and their skills are then also
available in ChatGPT. On Business/Enterprise/Edu workspaces where an admin allows
it, a skill's `.zip` from [Releases](../../releases) can be uploaded directly.

### Other tools

Any agent that supports Agent Skills (see the list on
[agentskills.io](https://agentskills.io)) can use a skill folder copied into its
skills directory, for example `~/.claude/skills/` for Claude Code without the plugin.

## Layout

```
.claude-plugin/marketplace.json      # list of plugins in this repo
plugins/<plugin>/
  .claude-plugin/plugin.json         # plugin manifest (name, version, ...)
  skills/<skill>/SKILL.md            # one folder per skill
  skills/<skill>/...                 # optional scripts, references, assets
scripts/validate.py                  # checks manifests and SKILL.md frontmatter
scripts/package.py                   # builds dist/<skill>.zip for claude.ai
```

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/): you may
share and adapt the skills for non-commercial purposes, with attribution and under
the same license. Code and other output generated with the skills is not covered
by this license and may be used for any purpose. See [LICENSE](LICENSE).

The tooling in `scripts/` and `.github/workflows/` is open source under the
[MIT License](LICENSE-MIT).
