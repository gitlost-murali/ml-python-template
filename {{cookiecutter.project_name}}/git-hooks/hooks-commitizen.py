from typing import Any, Dict, List

import questionary

questions: List[Dict[str, Any]] = [
    {
        "type": "list",
        "name": "prefix",
        "message": "Select the type of change you are committing",
        "choices": [
            {
                "value": "fix",
                "name": "fix: A bug fix. Correlates with PATCH in SemVer",
            },
            {
                "value": "feat",
                "name": "feat: A new feature. Correlates with MINOR in SemVer",
            },
            {"value": "docs", "name": "docs: Documentation only changes"},
            {
                "value": "style",
                "name": (
                    "style: Changes that do not affect the "
                    "meaning of the code (white-space, formatting,"
                    " missing semi-colons, etc)"
                ),
            },
            {
                "value": "refactor",
                "name": (
                    "refactor: A code change that neither fixes "
                    "a bug nor adds a feature"
                ),
            },
            {
                "value": "perf",
                "name": "perf: A code change that improves performance",
            },
            {
                "value": "test",
                "name": ("test: Adding missing or correcting " "existing tests"),
            },
            {
                "value": "build",
                "name": (
                    "build: Changes that affect the build system or "
                    "external dependencies (example scopes: pip, docker, npm)"
                ),
            },
            {
                "value": "ci",
                "name": (
                    "ci: Changes to our CI configuration files and "
                    "scripts (example scopes: GitLabCI)"
                ),
            },
        ],
    },
    {
        "type": "input",
        "name": "scope",
        "message": (
            "What is the scope of this change (e.g. component or file name): "
            "(press enter to skip)"
        ),
    },
    {
        "type": "input",
        "name": "jira",
        "message": (
            "JIRA issue number (multiple issue numbers can be separated by comma):"
        ),
    },
    {
        "type": "input",
        "name": "subject",
        "message": (
            "Write a short and imperative summary of the code changes: "
            "(lower case and no period)\n"
        ),
    },
    {
        "type": "input",
        "name": "body",
        "message": (
            "Provide additional contextual information about the code changes: "
            "(press [enter] to skip)\n"
        ),
    },
    {
        "type": "confirm",
        "message": "Are there any breaking changes?",
        "name": "is_breaking_change",
        "default": False,
    },
    {
        "type": "input",
        "name": "footer",
        "message": (
            "A BREAKING CHANGE commit requires a body. "
            "Please enter a longer description of the commit itself:\n"
        ),
    },
]

has_message = False
with open(".git/COMMIT_EDITMSG", "r") as file:
    for line in file:
        if not line.startswith("\n") and not line.startswith("#"):
            has_message = True
            break

if not has_message:
    answers = questionary.prompt(questions)

    with open(".git/COMMIT_EDITMSG", "w") as file:
        commit_str = ""
        if answers["prefix"]:
            commit_str += answers["prefix"].strip()
        if answers["scope"] and len(answers["scope"]) >= 0:
            commit_str += f"({answers['scope'].strip()})"
        commit_str += ": "
        if answers["jira"] and len(answers["jira"]) > 0:
            commit_str += "("
            jira_ids = answers["jira"].split(",")
            for jira_id in jira_ids[:-1]:
                commit_str += f"{jira_ids[-1].strip()}, "
            commit_str += f"{jira_ids[-1].strip()}) "
        if answers["subject"]:
            commit_str += answers["subject"].strip()
        if answers["body"]:
            commit_str += f"\n\n{answers['body'].strip()}"
        if answers["is_breaking_change"]:
            commit_str += f"\n\nBREAKING CHANGE: {answers['footer']}"

        commit_str += "\n"
        file.write(commit_str)
