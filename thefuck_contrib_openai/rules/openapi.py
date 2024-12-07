"""OpenAI rule for thefuck. This rule uses the OpenAI API to correct command-line mistakes."""
import os
import sys
import platform
from os import environ
import openai


def match(_):
    """Match the command to see if it should be corrected by OpenAI. Currently, this rule is
    always matched.

    Args:
        command (command): The command that needs to be corrected, called from thefuck.

    Returns:
        boolean: True if the command should be corrected by OpenAI, False otherwise.
    """
    return True


def get_new_command(command):
    """Get the corrected command from OpenAI.

    Args:
        command (command): The command that needs to be corrected, called from thefuck.

    Returns:
        string: The (hopefully) corrected command.
    """
    system_type = platform.system()
    if system_type == 'Darwin':
        system_type = 'MacOS (Darwin)'
    client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    messages = [
        {
            "role": "system",
            "content": "You are a command-line assistant, an expert in bash, zsh, and " +
            "similar shells. You are also familiar with many of the most popular commands, " +
            "such as git, npm, vim, and others. You are here to help the user fix their " +
            "command-line mistakes."
        },
        {
            "role": "user",
            "content": f"I am using the shell: {environ['SHELL']} on {system_type}\n" +
            "Please provide the corrected command only, without explanation." +
            f"The following command resulted in an error:\n\n{command.script}\n\n" +
            f"The attempt to run the command resulted in the output:\n\n{command.output}"
        }
    ]

    model = environ.get('OPENAI_MODEL', 'gpt-4o-mini')
    max_tokens = environ.get('OPENAI_MAX_TOKENS', '100')
    
    try:
        max_tokens = int(max_tokens)
    except ValueError:
        print(f"Invalid value for OPENAI_MAX_TOKENS: {max_tokens}. Using default value of 100.", file=sys.stderr)
        max_tokens = 100
        
    temperature = environ.get('OPENAI_TEMPERATURE', '0')
    try:
        temperature = float(temperature)
    except ValueError:
        print(f"Invalid value for OPENAPI_TEMPERATURE: {temperature}. Using default value of 0.", file=sys.stderr)
        temperature = 0.0
        
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature
    )
    suggestion = response.choices[0].message.content.strip()
    suggestion_lines = suggestion.split('\n')
    # If the suggestion is more than one line, return the second line as the suggestion
    # (OpenAI often surrounts the suggestion in a markdown block)
    if len(suggestion_lines) > 1:
        return suggestion_lines[1]
    else:
        return suggestion
