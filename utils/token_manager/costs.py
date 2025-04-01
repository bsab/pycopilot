#
# https://github.com/AgentOps-AI/tokencost
# Prices last updated Jan 30, 2024 from LiteLLM's cost dictionary
#
cost_map = {
    "gpt-4": {
        "prompt": 0.03,
        "completion": 0.06,
        "max_prompt_tokens": 8192,
        "max_output_tokens": 4096
    },
    "gpt-4o": {
        "prompt": 0.0025,
        "completion": 0.01,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "gpt-4o-audio-preview": {
        "prompt": 0.0025,
        "completion": 0.01,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "gpt-4o-audio-preview-2024-10-01": {
        "prompt": 0.0025,
        "completion": 0.01,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "gpt-4o-mini": {
        "prompt": 0.00015,
        "completion": 0.0006,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "gpt-4o-mini-2024-07-18": {
        "prompt": 0.00015,
        "completion": 0.0006,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "o1-mini": {
        "prompt": 0.0011,
        "completion": 0.0044,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 65536
    },
    "o1-mini-2024-09-12": {
        "prompt": 0.003,
        "completion": 0.012,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 65536
    },
    "o1-preview": {
        "prompt": 0.015,
        "completion": 0.06,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 32768
    },
    "o1-preview-2024-09-12": {
        "prompt": 0.015,
        "completion": 0.06,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 32768
    },
    "chatgpt-4o-latest": {
        "prompt": 0.005,
        "completion": 0.015,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "gpt-4o-2024-05-13": {
        "prompt": 0.005,
        "completion": 0.015,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "gpt-4o-2024-08-06": {
        "prompt": 0.0025,
        "completion": 0.01,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "gpt-4-turbo-preview": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "gpt-4-0314": {
        "prompt": 0.03,
        "completion": 0.06,
        "max_prompt_tokens": 8192,
        "max_output_tokens": 4096
    },
    "gpt-4-0613": {
        "prompt": 0.03,
        "completion": 0.06,
        "max_prompt_tokens": 8192,
        "max_output_tokens": 4096
    },
    "gpt-4-32k": {
        "prompt": 0.06,
        "completion": 0.12,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 4096
    },
    "gpt-4-32k-0314": {
        "prompt": 0.06,
        "completion": 0.12,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 4096
    },
    "gpt-4-32k-0613": {
        "prompt": 0.06,
        "completion": 0.12,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 4096
    },
    "gpt-4-turbo": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "gpt-4-turbo-2024-04-09": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "gpt-4-1106-preview": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "gpt-4-0125-preview": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "gpt-4-vision-preview": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "gpt-4-1106-vision-preview": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "gpt-3.5-turbo": {
        "prompt": 0.0015,
        "completion": 0.002,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "gpt-3.5-turbo-0301": {
        "prompt": 0.0015,
        "completion": 0.002,
        "max_prompt_tokens": 4097,
        "max_output_tokens": 4096
    },
    "gpt-3.5-turbo-0613": {
        "prompt": 0.0015,
        "completion": 0.002,
        "max_prompt_tokens": 4097,
        "max_output_tokens": 4096
    },
    "gpt-3.5-turbo-1106": {
        "prompt": 0.001,
        "completion": 0.002,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "gpt-3.5-turbo-0125": {
        "prompt": 0.0005,
        "completion": 0.0015,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "gpt-3.5-turbo-16k": {
        "prompt": 0.003,
        "completion": 0.004,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "gpt-3.5-turbo-16k-0613": {
        "prompt": 0.003,
        "completion": 0.004,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "ft:gpt-3.5-turbo": {
        "prompt": 0.003,
        "completion": 0.006,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "ft:gpt-3.5-turbo-0125": {
        "prompt": 0.003,
        "completion": 0.006,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "ft:gpt-3.5-turbo-1106": {
        "prompt": 0.003,
        "completion": 0.006,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "ft:gpt-3.5-turbo-0613": {
        "prompt": 0.003,
        "completion": 0.006,
        "max_prompt_tokens": 4096,
        "max_output_tokens": 4096
    },
    "ft:gpt-4-0613": {
        "prompt": 0.03,
        "completion": 0.06,
        "max_prompt_tokens": 8192,
        "max_output_tokens": 4096
    },
    "ft:gpt-4o-2024-08-06": {
        "prompt": 0.00375,
        "completion": 0.015,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "ft:gpt-4o-mini-2024-07-18": {
        "prompt": 0.0003,
        "completion": 0.0012,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "ft:davinci-002": {
        "prompt": 0.002,
        "completion": 0.002,
        "max_prompt_tokens": 16384,
        "max_output_tokens": 4096
    },
    "ft:babbage-002": {
        "prompt": 0.0004,
        "completion": 0.0004,
        "max_prompt_tokens": 16384,
        "max_output_tokens": 4096
    },
    "text-embedding-3-large": {
        "prompt": 0.00013,
        "completion": 0.0,
        "max_prompt_tokens": 8191,
        "max_output_tokens": float('nan')
    },
    "text-embedding-3-small": {
        "prompt": 0.00002,
        "completion": 0.0,
        "max_prompt_tokens": 8191,
        "max_output_tokens": float('nan')
    },
    "text-embedding-ada-002": {
        "prompt": 0.0001,
        "completion": 0.0,
        "max_prompt_tokens": 8191,
        "max_output_tokens": float('nan')
    },
    "text-embedding-ada-002-v2": {
        "prompt": 0.0001,
        "completion": 0.0,
        "max_prompt_tokens": 8191,
        "max_output_tokens": float('nan')
    },
    "text-moderation-stable": {
        "prompt": 0.0,
        "completion": 0.0,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 0
    },
    "text-moderation-007": {
        "prompt": 0.0,
        "completion": 0.0,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 0
    },
    "text-moderation-latest": {
        "prompt": 0.0,
        "completion": 0.0,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 0
    },
    "256-x-256/dall-e-2": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "512-x-512/dall-e-2": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "1024-x-1024/dall-e-2": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "hd/1024-x-1792/dall-e-3": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "hd/1792-x-1024/dall-e-3": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "hd/1024-x-1024/dall-e-3": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "standard/1024-x-1792/dall-e-3": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "standard/1792-x-1024/dall-e-3": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "standard/1024-x-1024/dall-e-3": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "whisper-1": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "tts-1": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "tts-1-hd": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "azure/tts-1": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "azure/tts-1-hd": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "azure/whisper-1": {
        "prompt": float('nan'),
        "completion": float('nan'),
        "max_prompt_tokens": float('nan'),
        "max_output_tokens": float('nan')
    },
    "azure/o1-mini": {
        "prompt": 0.00121,
        "completion": 0.00484,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 65536
    },
    "azure/o1-mini-2024-09-12": {
        "prompt": 0.00121,
        "completion": 0.00484,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 65536
    },
    "azure/o1-preview": {
        "prompt": 0.015,
        "completion": 0.06,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 32768
    },
    "azure/o1-preview-2024-09-12": {
        "prompt": 0.015,
        "completion": 0.06,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 32768
    },
    "azure/gpt-4o": {
        "prompt": 0.0025,
        "completion": 0.01,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "azure/gpt-4o-2024-08-06": {
        "prompt": 0.0025,
        "completion": 0.01,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "azure/gpt-4o-2024-05-13": {
        "prompt": 0.005,
        "completion": 0.015,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "azure/global-standard/gpt-4o-2024-08-06": {
        "prompt": 0.0025,
        "completion": 0.01,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "azure/global-standard/gpt-4o-mini": {
        "prompt": 0.00015,
        "completion": 0.0006,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "azure/gpt-4o-mini": {
        "prompt": 0.000165,
        "completion": 0.00066,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 16384
    },
    "azure/gpt-4-turbo-2024-04-09": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "azure/gpt-4-0125-preview": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "azure/gpt-4-1106-preview": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "azure/gpt-4-0613": {
        "prompt": 0.03,
        "completion": 0.06,
        "max_prompt_tokens": 8192,
        "max_output_tokens": 4096
    },
    "azure/gpt-4-32k-0613": {
        "prompt": 0.06,
        "completion": 0.12,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 4096
    },
    "azure/gpt-4-32k": {
        "prompt": 0.06,
        "completion": 0.12,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 4096
    },
    "azure/gpt-4": {
        "prompt": 0.03,
        "completion": 0.06,
        "max_prompt_tokens": 8192,
        "max_output_tokens": 4096
    },
    "azure/gpt-4-turbo": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "azure/gpt-4-turbo-vision-preview": {
        "prompt": 0.01,
        "completion": 0.03,
        "max_prompt_tokens": 128000,
        "max_output_tokens": 4096
    },
    "azure/gpt-35-turbo-16k-0613": {
        "prompt": 0.003,
        "completion": 0.004,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "azure/gpt-35-turbo-1106": {
        "prompt": 0.001,
        "completion": 0.002,
        "max_prompt_tokens": 16384,
        "max_output_tokens": 4096
    },
    "azure/gpt-35-turbo-0613": {
        "prompt": 0.0015,
        "completion": 0.002,
        "max_prompt_tokens": 4097,
        "max_output_tokens": 4096
    },
    "azure/gpt-35-turbo-0301": {
        "prompt": 0.0002,
        "completion": 0.002,
        "max_prompt_tokens": 4097,
        "max_output_tokens": 4096
    },
    "azure/gpt-35-turbo-0125": {
        "prompt": 0.0005,
        "completion": 0.0015,
        "max_prompt_tokens": 16384,
        "max_output_tokens": 4096
    },
    "azure/gpt-35-turbo-16k": {
        "prompt": 0.003,
        "completion": 0.004,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "azure/gpt-35-turbo": {
        "prompt": 0.0015,
        "completion": 0.002,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "azure/ft:gpt-3.5-turbo": {
        "prompt": 0.003,
        "completion": 0.006,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "azure/ft:gpt-3.5-turbo-0613": {
        "prompt": 0.003,
        "completion": 0.006,
        "max_prompt_tokens": 4096,
        "max_output_tokens": 4096
    },
    "azure/ft:gpt-3.5-turbo-1106": {
        "prompt": 0.003,
        "completion": 0.006,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "azure/ft:gpt-3.5-turbo-0125": {
        "prompt": 0.003,
        "completion": 0.006,
        "max_prompt_tokens": 16385,
        "max_output_tokens": 4096
    },
    "azure/ft:gpt-4-0613": {
        "prompt": 0.03,
        "completion": 0.06,
        "max_prompt_tokens": 8192,
        "max_output_tokens": 4096
    },
    "azure/text-embedding-3-small": {
        "prompt": 0.00002,
        "completion": 0.0,
        "max_prompt_tokens": 8191,
        "max_output_tokens": float('nan')
    },
    "azure/text-embedding-3-large": {
        "prompt": 0.00013,
        "completion": 0.0,
        "max_prompt_tokens": 8191,
        "max_output_tokens": float('nan')
    },
    "azure/text-embedding-ada-002-v2": {
        "prompt": 0.0001,
        "completion": 0.0,
        "max_prompt_tokens": 8191,
        "max_output_tokens": float('nan')
    },
    "azure/text-embedding-ada-002": {
        "prompt": 0.0001,
        "completion": 0.0,
        "max_prompt_tokens": 8191,
        "max_output_tokens": float('nan')
    },
    "azure/text-moderation-stable": {
        "prompt": 0.0,
        "completion": 0.0,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 0
    },
    "azure/text-moderation-007": {
        "prompt": 0.0,
        "completion": 0.0,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 0
    },
    "azure/text-moderation-latest": {
        "prompt": 0.0,
        "completion": 0.0,
        "max_prompt_tokens": 32768,
        "max_output_tokens": 0
    }
}
