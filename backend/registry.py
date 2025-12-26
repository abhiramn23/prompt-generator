"""
Central registry for all prompt adapters.
Maps model names to their corresponding adapter instances.
"""

from adapters.image import (
    DalleAdapter,
    MidjourneyAdapter,
    StableDiffusionAdapter,
    ImagenAdapter,
    FireflyAdapter,
)
from adapters.video import RunwayAdapter, PikaAdapter, SoraAdapter
from adapters.voice import OpenAIVoiceAdapter, ElevenLabsAdapter

# Registry mapping model names to adapter instances
ADAPTER_REGISTRY = {
    # Image models
    "dalle-3": DalleAdapter(),
    "midjourney-v6": MidjourneyAdapter(),
    "sdxl": StableDiffusionAdapter(),
    "imagen": ImagenAdapter(),
    "firefly": FireflyAdapter(),
    # Video models
    "runway-gen3": RunwayAdapter(),
    "pika": PikaAdapter(),
    "sora": SoraAdapter(),
    # Voice models
    "openai-voice": OpenAIVoiceAdapter(),
    "elevenlabs": ElevenLabsAdapter(),
}


def get_available_models_by_modality():
    """Return available models grouped by modality."""
    return {
        "image": ["dalle-3", "midjourney-v6", "sdxl", "imagen", "firefly"],
        "video": ["runway-gen3", "pika", "sora"],
        "voice": ["openai-voice", "elevenlabs"],
    }
