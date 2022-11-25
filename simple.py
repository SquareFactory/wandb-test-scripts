import wandb
import time


wandb.login()


wandb.init(project="jupyter-projo")
for ii in range(30):
  wandb.log({"acc": 1 - 2 ** -ii, "loss": 2 ** -ii})
  time.sleep(0.5)

art = wandb.Artifact("my-object-detector", type="model")
art.add_file("dump_model.pt")
wandb.log_artifact(art)
 