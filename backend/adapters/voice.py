"""Voice synthesis adapters for different AI models."""

from schema import VoicePrompt


class OpenAIVoiceAdapter:
    """OpenAI Voice adapter - natural language descriptions."""

    model_name = "openai-voice"

    def compile(self, p: VoicePrompt) -> str:
        parts = []

        if p.emotion:
            if p.voice_gender:
                parts.append(f"Use a {p.emotion} {p.voice_gender} voice")
            else:
                parts.append(f"Use a {p.emotion} voice")
        elif p.voice_gender:
            parts.append(f"Use a {p.voice_gender} voice")

        if p.accent:
            parts.append(f"with a {p.accent} accent")

        if p.pace:
            parts.append(f"Pace: {p.pace}")

        if p.use_case:
            parts.append(f"Purpose: {p.use_case}")

        if p.age_range:
            parts.append(f"Age range: {p.age_range}")

        return ". ".join(parts) + "." if parts else "Generate natural voice."


class ElevenLabsAdapter:
    """ElevenLabs adapter - structured parameter format."""

    model_name = "elevenlabs"

    def compile(self, p: VoicePrompt) -> str:
        lines = []

        if p.voice_gender:
            lines.append(f"Voice: {p.voice_gender}")

        if p.accent:
            lines.append(f"Accent: {p.accent}")

        if p.emotion:
            lines.append(f"Emotion: {p.emotion}")

        if p.pace:
            lines.append(f"Pace: {p.pace}")

        if p.age_range:
            lines.append(f"Age: {p.age_range}")

        # ElevenLabs-specific parameters
        lines.append("Stability: 70%")
        lines.append("Clarity: High")

        return "\n".join(lines)
