from pathlib import Path
from typing import Optional

from pyfedappwrap.learning.app_types import BaseSelfLearnedApp
from typing_extensions import override

from config import BiconAppConfig, BiconAppInputConfig, BiconAppOutputConfig
from model import bicon_patient_stratification


class BiconApp(BaseSelfLearnedApp[BiconAppConfig, BiconAppInputConfig, BiconAppOutputConfig]):

    def __init__(self):
        super().__init__()

    def run_algorithm(self, data: BiconAppInputConfig) -> BiconAppOutputConfig:
        self.logger.info("Starting BiCoN prediction...")

        data.expr.to_csv("out.csv", index=False)
        data.net.to_csv("net.tsv", index=False, sep="\t")

        output_dir = Path("./output")
        output_dir.mkdir(exist_ok=True, parents=True)

        results = bicon_patient_stratification(
            path_expr=Path("out.csv"),
            path_net=Path("net.tsv"),
            output_dir=output_dir,
            L_g_min=self.config.l_g_min,
            L_g_max=self.config.l_g_max,
            max_iter=self.config.max_iter,
        )

        self.logger.info(f"BiCoN prediction completed")

        return results

    @override
    def get_test_data(self) -> Optional[dict[str, Path]]:
        return {
            "expr": Path("data/expr.csv"),
            "net": Path("data/net.tsv"),
        }
