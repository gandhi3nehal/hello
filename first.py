import anthropic
client = anthropic.Anthropic(
    base_url='http://localhost:11434',
    api_key='ollama',  # required but ignored
)
message = client.messages.create(model='qwen3-coder:480b-cloud', 
                                 max_tokens=1024, 
                                 messages=[{'role': 'user', 'content': 'Write a function to check if a number is odd or even'}])
print(message.content[0].text)