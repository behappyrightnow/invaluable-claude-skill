# Invaluable: A Claude Code Skill for Values Clarity

A Claude Code skill derived from **Somik Raha's book *Invaluable: Achieving Clarity on Value***.

This skill makes the book's framework accessible as an interactive conversation inside Claude Code. If you have the book, the skill points you to specific chapters and pages for deeper reading. If you don't have the book yet, the skill can still help you begin the inquiry — and may give you a reason to seek it out.

---

## What This Skill Does

The skill embeds the full intellectual framework of *Invaluable* — its distinctions, tests, stories, aphorisms, and philosophical foundations — into a values coaching conversation. It can help you:

- **Understand value clearly**: Hartman's three dimensions of value, the difference between intrinsic, extrinsic, and systemic valuation, and the valuation mistakes we make without realizing it
- **Rethink the metrics on your project**: Whether you're running a startup, a non-profit, a research initiative, or a team inside a large organization, the skill can help you distinguish input metrics (which drive the behavior you want) from output metrics (which only account for what already happened) — and identify whether a numinous metric is possible for your work. This often unlocks entirely new ways of measuring what matters.
- **Map your, your team's, or your company's unique values**: Discover the Heart (why), Habit (how), and Head (what) — the three values that, braided together, define a unique capacity for meaningful action
- **Make values-based decisions**: Think through the quality of your decision from the perspective of your values map
- **Connect to neuroscience**: Understand why feelings are not noise in the decision-making system — they *are* the system
- **Receive aphorisms from the book** injected at the right moments — not as lessons, but as gifts

---

## Who This Is For

**Readers of *Invaluable: Achieving Clarity on Value*** will get the most from this skill. Throughout the conversation, the skill will reference specific chapters and page numbers so you can return to the source text to deepen what the conversation opens up.

Others curious about values clarity, decision-making, and meaning are also welcome to engage — but please know that the framework here belongs to the book, and the book has more depth, story, and nuance than any skill can carry.

---

## Installation

This skill works with [Claude Code](https://claude.ai/code) (the CLI or desktop app).

### Step 1: Copy the skill into your Claude skills directory

```bash
mkdir -p ~/.claude/skills/invaluable/references
cp skills/invaluable/SKILL.md ~/.claude/skills/invaluable/SKILL.md
cp skills/invaluable/references/quick-reference.md ~/.claude/skills/invaluable/references/quick-reference.md
```

Or clone this repository directly into the right place:

```bash
git clone https://github.com/somikraha/invaluable-claude-skill /tmp/invaluable-skill
cp -r /tmp/invaluable-skill/skills/invaluable ~/.claude/skills/invaluable
```

### Step 2: Start Claude Code

```bash
claude
```

The skill activates automatically when the conversation touches values, meaning, decision-making, or the Three-Goddess Braid. No slash command needed — just start talking.

---

## Example Conversations

Here are real things you can ask. The skill will respond as a Socratic partner — drawing out, not imposing.

### Starting a values mapping session

```
Help me map my values.
```

```
I'm at a career crossroads and I don't know what I actually value.
Can you help me figure that out?
```

```
I keep making decisions that feel right in the moment but wrong
in retrospect. I think something is off with my values. Can we explore?
```

### Exploring specific concepts from the book

```
What's the difference between an input metric and an output metric?
```

```
Can you explain Hartman's three dimensions of value?
```

```
What is a numinous value? Do I have one?
```

```
Why does the book say feelings are rational, not irrational?
```

### Rethinking metrics on a project

```
We're measuring user engagement by time-on-site, but growth
has stalled. Help me think about whether we're using the
right metrics.
```

```
I'm running a non-profit focused on community resilience.
What would an input metric look like for our work?
Is a numinous metric possible here?
```

```
Our team hits all its OKRs but people feel burned out and
disconnected. What's happening at the level of metrics?
```

```
I'm building a product. Help me find a metric that actually
drives the behavior I care about, not just measures what
happened after the fact.
```

### Using the framework for a real decision

```
I have to decide whether to take a job offer that pays more
but feels wrong. Help me think through the quality of this
decision from the perspective of my values.
```

```
My team keeps hitting metrics but something feels hollow.
What might be happening here?
```

### Going deeper with the book

```
Help me understand the story in Chapter ..., Page ..
```

```
I am struggling with this decision: xyz, what part of the book
would be relevant for me? Can you guide me in a conversation
and suggest specific pages to deepen my thinking?
```

---

## Caveats and Responsible Use

*The book devotes pages 231–237 to what the book calls "the shadows" — the ways this framework can cause harm when used without care. These caveats are embedded directly in the skill, and they deserve to be named plainly here.*

### This work is for your own inquiry first

The most generative use of this skill is solitary: sitting with your own values, your own life, your own decisions. Before you bring this framework to anyone else, do the work yourself. The book is explicit: if you haven't inquired into your own meaningful purpose, you are not ready to facilitate this for others.

### Power imbalances are real

If you use what you learn here to facilitate a values conversation with another person — a friend, a colleague, a report — be aware that the listener holds power over the person being mapped. The person being mapped is sharing from a vulnerable place. This is not casual conversation. It is closer to therapeutic territory.

The invitation must come from them, not from your enthusiasm about what you discovered. And when you hold that space, hold it without judgment.

### "Voluntary" is not always truly voluntary

In any context where one person has power over another — employer and employee, funder and founder — an invitation to do values mapping is not neutral. People will participate to protect themselves, not from genuine desire. In those conditions, the conversation produces performance, not truth. The skill itself has no power over you. But if you take what you learn here into the world, this warning travels with you.

### No judgment — ever

The vow the book asks readers to take: *"I won't judge."* Not during a mapping conversation. Not after it. Not even silently. When someone names their Heart value, they are giving you something sacred. Respond accordingly.

### Do not use this to extract performance from people

The most pernicious misuse of this framework: *"Use values with your team — it motivates people and gets better results."* This is exploitative. It treats sacred inquiry as a management technique. The goal of this work is human flourishing, not productivity optimization. If you find yourself reaching for this framework as a lever for output, stop and do the inquiry on yourself first.

### This is an AI, not a therapist

This skill will not judge you, exploit you, or have power over you. But it is not a therapist, a coach, or a human being who truly knows you. For significant life decisions, values mapping conversations with trusted humans who know you remain more powerful than any AI-mediated conversation. Use this as a starting point, not an endpoint.

---

## Structure of This Repository

```
invaluable-claude-skill/
├── README.md                                    # This file
└── skills/
    └── invaluable/
        ├── SKILL.md                             # The full skill (install this)
        └── references/
            └── quick-reference.md               # Compact mapping summary
```

---

## About the Book

**Invaluable: Achieving Clarity on Value** by Somik Raha

The book draws on Robert Hartman's formal axiology, Antonio Damasio's neuroscience of decision-making, Ron Howard's decision analysis framework, ancient philosophical frameworks, and decades of the author's own practice helping individuals and organizations achieve clarity on what they truly value.

Its central tool — the Three-Goddess Braid — maps three intertwined values (Heart, Habit, Head) that together define a person's unique capacity for meaningful action.

---

## License

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

Copyright © Somik Raha

You are free to:
- **Share** — copy and redistribute this skill in any medium or format
- **Adapt** — remix, transform, and build upon it
- **Use commercially or non-commercially** — for any purpose

Under the following terms:
- **Attribution** — Attribution is only required if you are redistributing a copy of this skill outside of this repository (for example, publishing it to another platform, packaging it in a product, or sharing a modified version elsewhere). Simply installing and using this skill for yourself — commercially or non-commercially — requires no attribution. If you do redistribute, give credit to Somik Raha and the book *Invaluable: Achieving Clarity on Value*, link to this repository, and note any changes you made.

**No warranties are given.** This skill is provided as-is, without guarantee of accuracy, completeness, or fitness for any purpose. The author and contributors accept no liability for any harm arising from use or misuse of this material.

Full license text: https://creativecommons.org/licenses/by/4.0/

---

*Please use this thoughtfully. The framework it encodes was built in service of human flourishing — not productivity, not performance, not optimization. The goal is to help you come alive. Use it accordingly.*
