evaluator_tools = [
    {
        "name": "output_message",
        "description": "A tool that outputs a message to the user.",
        "input_schema": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "The message to output to the user.",
                },
            },
            "required": ["message"],
        },
    }
]
