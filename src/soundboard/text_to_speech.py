import torch

def apply_tts(repo_name, model, language, model_id, sample_rate, speaker, put_accent, put_yo, device_name, text):
    device = torch.device(device_name)
    model, _ = torch.hub.load(repo_or_dir=repo_name,
            model=model,
            language=language,
            speaker=model_id)
    model.to(device)
    audio = model.apply_tts(text=text,
            speaker=speaker,
            put_accent=put_accent,
            put_yo=put_yo)
    return audio
