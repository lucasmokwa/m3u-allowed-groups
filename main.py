import os


def _load_m3u(path: str) -> str:
    with open(path) as file:
        string = file.read()
    return string


def _filter_channels(channels: list[str], allowed_groups: set[str]) -> list[str]:
    return [
        channel
        for channel in channels
        if any(group in channel for group in allowed_groups)
    ]


def _process_channels(file: str) -> str:
    separator = "#EXTINF"
    file = file.split(separator)
    allowed_groups = {
        "Canais | 4K",
        "Canais | ESPN",
        "Canais | Esportes",
        "Canais | Globo",
        "Canais | Notícias",
        "Canais | Premiere",
        "Canais | SporTV",
        "Canais | Variedades",
    }
    channels = _filter_channels(file, allowed_groups)
    channels.insert(0, "#EXTM3U\n")
    return separator.join(channels)


def _write_m3u(text: str):
    with open("processed_playlist.m3u", "w") as file:
        file.write(text)


if __name__ == "__main__":
    cwd = os.getcwd()
    file = _load_m3u(f"{cwd}/lista_xPDQ4enzyaKF_plus.m3u")
    new_string = _process_channels(file)
    _write_m3u(new_string)
