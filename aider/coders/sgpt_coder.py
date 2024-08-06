from .sgpt_prompts import SgptPrompts
from .base_coder import Coder


class SgptCoder(Coder):
    """Get shell commands the same way as Shell-GPT."""

    edit_format = "sgpt"
    gpt_prompts = SgptPrompts()