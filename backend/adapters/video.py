"""Video generation adapters for different AI models."""

from schema import VideoPrompt


class RunwayAdapter:
    """Runway Gen-3 adapter - cinematic scene descriptions."""

    model_name = "runway-gen3"

    def compile(self, p: VideoPrompt) -> str:
        parts = [f"A {p.duration_seconds}-second cinematic scene of {p.scene}"]

        if p.action:
            parts.append(f"Action: {p.action}")

        if p.camera_motion:
            parts.append(f"Camera: {p.camera_motion}")

        if p.lighting:
            parts.append(f"Lighting: {p.lighting}")

        parts.append("Realistic motion")

        return ". ".join(parts) + "."


class PikaAdapter:
    """Pika adapter - structured format with labeled sections."""

    model_name = "pika"

    def compile(self, p: VideoPrompt) -> str:
        lines = [f"Scene: {p.scene}"]

        if p.action:
            lines.append(f"Action: {p.action}")

        if p.camera_motion:
            lines.append(f"Camera movement: {p.camera_motion}")

        if p.style:
            lines.append(f"Style: {p.style}")

        lines.append(f"Duration: {p.duration_seconds}s")

        return "\n".join(lines)


class SoraAdapter:
    """OpenAI Sora adapter - coherent narrative descriptions."""

    model_name = "sora"

    def compile(self, p: VideoPrompt) -> str:
        parts = [f"A coherent {p.duration_seconds}-second cinematic video of {p.scene}"]

        if p.action:
            parts.append(f"The subject is {p.action}")

        if p.camera_motion:
            parts.append(f"The camera {p.camera_motion}")

        if p.lighting:
            parts.append(f"Lighting is {p.lighting}")

        if p.style:
            parts.append(f"Style: {p.style}")

        return ". ".join(parts) + "."
