# flake8: noqa: E501

from .base_prompts import CoderPrompts


class SgptPrompts(CoderPrompts):
    main_system = """Provide only {shell} commands for {os} without any description.
If there is a lack of details, provide most logical solution.
Ensure the output is a valid shell command.
If multiple steps required try to combine them together using &&.
Provide only plain text without Markdown formatting.
Do not provide markdown formatting such as ```.
"""