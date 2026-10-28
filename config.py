from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pyfedappwrap.learning.run_runfig import AppConfig, AppInputConfig, AppOutputConfig


@dataclass
class BiconAppConfig(AppConfig):
    l_g_min: int = 10
    l_g_max: int = 15
    max_iter: int = 15


@dataclass
class BiconAppInputConfig(AppInputConfig):
    net: Any | None = None
    expr: Any | None = None


@dataclass
class BiconAppOutputConfig(AppOutputConfig):
    cluster_map: Path | None = None
    network: Path | None = None
    result: Path | None = None
