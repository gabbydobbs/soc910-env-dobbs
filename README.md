# SOC 910 environment — Dobbs

A packaged snapshot of my Claude Code + VS Code development environment, for
rebuilding on another computer. Captured 2026-09-28 from a MacBook Pro
(Intel, macOS 13.7.8 Ventura). Built for SOC 910: How to Use AI for
Sociological Research (Fall 2026), Assignment 1.

## Contents

- `claude/` — user-level and project-level `CLAUDE.md`, `settings.json`,
  two skills, one slash command, and one hook (see `claude/README.md` for
  what each does and where it installs)
- `mcp/` — the `stata-mcp` server configuration and the command that
  registers it on a new machine
- `project/` — `.gitignore`, two-level folder structure, and commit
  history for the SOC 910 seminar materials folder
- `setup/versions.txt` — tool versions on the source machine
- `setup/install.md` — ordered install steps, ending in a verification
  checklist, plus what can't be reproduced (accounts, licenses, paths)
- `setup/daily-sync.sh` — the script behind an optional automated daily
  git sync (not required by the assignment; included for completeness)
- `screenshots/` — see `screenshots/README.md`

## Install summary

Install Node/Python/git/gh via Homebrew → install VS Code → install Claude
Code (`npm install -g @anthropic-ai/claude-code`) → copy the `claude/`
files into `~/.claude/` and the project folder → recreate the project
folder from `project/` → (optional) install Stata + the Stata MCP VS Code
extension and register it with `claude mcp add`. Full detail in
`setup/install.md`.

## Build Report

### 1. What machine is this, and was anything unusual about it?

I am running VSCode and Claude Code on a 2017 Macbook with a 3.5 GHz Dual-Core Intel Core i7 processor; 
As it is an old machine I have been using throughout my entire undergraduate and graduate career, it 
often has difficulty maintaining a stable, cool temperature. Additionally, the battery life of this computer is substantially deminished when running claude code, especially with multiple connectors and extensions installed. When the machine overheats, Claude Code and VScode often crash or run very slowly.I could use my partner's newer MacBook, but I am not sure how much better it would run these applications. 

### 2. What did you install, and what is each piece for?

I installed VSCode as a terminal and conneted claude, so that claude code would be linked in VSCode. 
I connected my google drive and google slides; claude was able to access my slide content to save style settings in it's directory for constructing future presentations. Additionally, I linked google drive, so that it would have access to my writings to log my prose style / academic style of writing in its instructions. I downloaded the STATA MCP, as well as a few programs for converting PDFs into MD files. 

### 3. What broke, what did the error actually say, and how did you fix it?

At first, the connectors for google workspace did not work; there was an issue with authorization. However, after I uninstalled the connectors and re-installed them, everything worked fine. After I installed these connectors, my VSCode and Claude app kept crashing and I kept having to restart my machine. It eventually worked. I attached a screenshot of the error code in the suppository files labeled /screenshots. After I installed these, my apps were crashing and my machine was overheating. I had to researt my machine several times to get everything working again. 

Additionally, my stata lisence recently expired & since I do not use it in my research regularly, I did not renew it. I got an error message "stata is not available. please check if it is installed and configured correctly." KU's mobile/virtual desktop STATA version can't fix this because the Stata MCP assumes Stata is running on the same machine you are using. Since KU's virtual desktop is a separate remote machine, there is no nerwork path from my Mac's local host to Stata. 

### 4. Which MCP server did you choose, why does it fit your research, and what did you ask the agent that it could answer only through that server?

I chose the STATA MCP server, but as a qualitative researcher I probably wont use it in my own research too often. I searched for an NVivo 15 MCP and a Dedoose MCP, but so far, nothing exists for either of those two qualitative programs. I haven't used Atlas, so I did not search for that MCP. Downloading data sets with claude code and analyzing them would be super helpful if I conducted that sort of analysis. In the future, I hope there are some qualitative coding connectors or MCP servers that come out soon (particularly for NVivo qualitative coding software). As of now, there is no qualitative coding MCP / connector for software that I have my projects coded in (i.e., NVivo). Because NVivo relies on a localized, closed database structure (.nvp or .nvpx project files), apparently you can't plug Claude directly into an open NVivo project database using an official plugin. I did some research and found that there are a few MCPs for qualitative coding, but I have not attempted to use them yet, since each one I have download so far has significantly slowed my app down. 

### 5. How is your project folder organized, what does your CLAUDE.md tell the agent, and what did you keep out of git?

My project folder, ~/Desktop/SOC 910, is a git repository pushed to a public GitHub repo (soc-910-coursework), organized into three subfolders: my downloaded articles/ for source PDFs as downloaded, reading articles for seminar/ for those same papers plus Markdown conversions, and presentations/ for slide decks. It also holds a project-level CLAUDE.md and a SESSION_LOG.md that accumulates entries whenever I run my /wrapup command. My CLAUDE.md setup works in two layers: a user-level file that applies to everything I do, setting communication style, a rule for when output should be saved as a file versus kept in chat, an instruction to always read PDFs in full, and also hard exclusions for sensitive data; and a project-level file inside SOC 910 describing that folder's specific layout and conventions. What I keep out of git goes beyond .gitignore excluding OS junk and Word lock files: my actual thesis interview data (26 participant interviews) never enters this folder at all, as it lives in Apple Notes and in a separate Thesis folder, both permanently off-limits per CLAUDE.md. Partway through this project I also realized that some of my other course papers, filed elsewhere, quote that same interview data verbatim, which showed me a folder-based exclusion wasn't enough, so the rule is now written to catch the pattern itself (i.e., quotes from pseudonymous "Dr. [Name]" ) rather than just one location.

### 6. When you clone this repository onto another of your machines and follow your install.md, what do you get, and what still has to be done by hand?

The original install.md told you to run gh repo create for the project folder, which would fail with "repository already exists" on a second machine tied to the same GitHub account — fixed to git clone instead. And settings.json had my username's absolute path hardcoded for the hook, which would silently fail (not error, just never fire) on a different account — Claude code fixed this with a sed rewrite at copy time, and it actually tested that it produces valid JSON before committing it and asked me to verify.

### 7. What did you customize, and what problem does it solve?

The customization I built was the citation-filename skill, which automatically renames any paper I download into my SOC 910 citation format — lastname_etal_year_short title_journal name (e.g., Niranjan-Azadi_etal_2026_Well-being Assessment Instruments_J Gen Intern Med.pdf). Before this, every time I downloaded a new article I had to manually retype that four-part filename myself — get the year right, shorten the title consistently, abbreviate the journal correctly — and across a semester of readings that adds up to a lot of repetitive, easy-to-get-wrong busywork. It also meant my filenames drifted out of consistency over time (different abbreviation styles, forgetting the "et al" ), which made my reading list harder to sort and cite from later. Now the skill applies the convention automatically the moment I download or rename a paper, so I don't have to hold the format in my head or manually enforce it every single time.

Also, I was quite tired of generic AI-drafted slides and the robitic prose that didn't match my personal academic style or prose. So, I also asked claude code to help develop a skill at ~/.claude/skills/match-my-style/SKILL.md, that triggers automatically whenever I draft slides. It reads style-notes.md and applies my real color/font/layout system and writing patterns instead of generic AI defaults. Now, CLAUDE.md just points to the skill instead of carrying the rule inline. Pushed to soc910-env-dobbs.
