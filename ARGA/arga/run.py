import settings

from clustering import Clustering_Runner
from link_prediction import Link_pred_Runner


dataname = 'hsa'                     # 'cora' or 'citeseer' or 'pubmed' or 'hsa' or 'mmu' or 'rno'
model = 'arga_ae'                     # 'arga_ae' or 'arga_vae'
task = 'link_prediction'              # 'clustering' or 'link_prediction'
n_hop_enable = True                  # True or False                                                                                             # Author: Tonni
hop_count = 1                         # Degree of neighbours. For example, hop_count = 1 means info till friends of neighbouring nodes            # Author: Tonni
pred_column = None                    # None or column number  (we dont need that for kegg link prediction)                                                                                  # Author: Tonni


settings = settings.get_settings(dataname, model, task, n_hop_enable, hop_count, pred_column)
print("settings:", settings)

if task == 'clustering':
    runner = Clustering_Runner(settings)
else: # task == 'link_prediction'
    runner = Link_pred_Runner(settings)

runner.erun()

