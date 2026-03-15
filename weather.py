import anthropic
client = anthropic.Anthropic(
    base_url='http://localhost:11434',
    api_key='ollama',  # required but ignored
)

message = client.messages.create(
    model='qwen3-coder:480b-cloud',
    max_tokens=1024,     
    tools=[{
        'name': 'get_weather',
        'description': 'Get the current weather in a location',
        'input_schema': {
            'type': 'object',
            'properties': {'location': {'type': 'string', 'description': 'City, State'}},
            'required': ['location']
        }
    }],
    messages=[{'role': 'user', 'content': "What's the weather in Los Angeles?"}]
)

for block in message.content:
    if block.type == 'tool_use':
        print(f'Tool: {block.name}')
        print(f'Input: {block.input}')