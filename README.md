# OpenAI Extension for TheFuck

TheFuck is a magnificent tool that corrects your previous console command. It is a life saver for those who are not very good at typing or remembering commands. However, as amazing as it is, it does not have built-in support for Generational AI. This extension adds a new rule to TheFuck that uses OpenAI to generate a new command based on the previous one.

**Note:** This extension requires an OpenAI API key. You can get one by signing up at [OpenAI](https://platform.openai.com/signup). Although the API key is free, the usage is not. Make sure to read the pricing details on the OpenAI website.

## Installation

*NOTE:* Although this code should work in newer versions, thefuck doesn't support Python versions >= 3.10. Make sure you are using a python 3.8 or 3.9 environment.

1. Install TheFuck by following the instructions on the [TheFuck GitHub page](https://github.com/nvbn/thefuck/tree/master).

2. Install this extension using pip:

    ```bash
    pip install thefuck-contrib-openai
    ```

3. Set the OpenAI API key:

    ```bash
    export OPENAI_API_KEY'='your-api-key'
    ```

4. Optionally, add the following rule to your TheFuck configuration file (usually located at `~/.config/thefuck/settings.py`) to set which rules to use. For example, to only use the OpenAI rule:

    ```python
    rules = [ 'openai' ]
    ```

## Usage

After installing the extension, you can use TheFuck as you normally would. If the OpenAI rule is enabled, it will generate a new command based on the previous one. The generated command will be displayed in the console, and you can choose to run it by pressing `y`.

To use a different OpenAI model, you can set the `OPENAI_MODEL` environment variable. The default model is `openai-4o-mini`. For example, to use the `openai-4o` model:

```bash
export OPENAI_MODEL='openai-4o'
```

## License

This extension is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
