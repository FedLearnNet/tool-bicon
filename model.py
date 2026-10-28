import os
from pathlib import Path

from config import BiconAppOutputConfig

os.environ["SCIPY_ARRAY_API"] = "1"

from bicon import data_preprocessing, BiCoN, results_analysis

def bicon_patient_stratification(
        path_expr: Path, path_net: Path, output_dir: Path, L_g_min=10, L_g_max=15, max_iter=15
) -> BiconAppOutputConfig:
    """BiCoN: network-constrained biclustering of patients and multi-omics data

    See:
     https://github.com/daisybio/BiCoN
     https://pubmed.ncbi.nlm.nih.gov/33367514/

    :param path_expr:
    :param path_net:
    :param output_dir:
    :param L_g_min: Min size of subnetwork
    :param L_g_max: Max size of subnetwork
    :return:
    """

    # Preprocess data
    GE, G, labels, _ = data_preprocessing(str(path_expr), str(path_net))

    # Set the model and run the search:
    model = BiCoN(GE, G, L_g_min, L_g_max)
    solution, scores = model.run_search(max_iter=max_iter)

    # save results
    results = results_analysis(solution, labels)
    output_dir.mkdir(exist_ok=True, parents=True)

    # Create output configuration with actual file paths
    output_config = BiconAppOutputConfig(
        cluster_map=output_dir / "clustermap.png",
        network=output_dir / "network.png",
        result=output_dir / "results.csv"
    )

    results.save(output=output_config.result)
    results.show_networks(GE, G, output=output_config.network)
    results.show_clustermap(GE, G, output=output_config.cluster_map)

    """
    If you have a patient's phenotype you would like to use for comparison,
    please make sure that patients IDs are exactly (!)
    matching the IDs that were used as an input. The IDs should be represented as a list of two lists
    """
    # true_classes = [['GSM748056', 'GSM748059',..], ['GSM748278', 'GSM748279', 'GSM1465989']]
    # results.show_clustermap(GE, G, output = "results/clustermap.png", true_labels = true_classes)
    return output_config
