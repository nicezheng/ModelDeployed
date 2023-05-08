import torch

from config import *

# model
model1 = torch.hub.load(repo,
                        model,
                        pretrained="face_paint_512_v1",
                        device=device)
model2 = torch.hub.load(
    repo,
    model,
    pretrained=True,
    progress=False,
    device=device
)

face2paint = torch.hub.load(
    repo, 'face2paint', device=device,
    size=512, side_by_side=False
)


def run_inference(img, ver):
    if ver == 'version 2 (🔺 robustness,🔻 stylization)':
        out = face2paint(model2, img)
    else:
        out = face2paint(model1, img)
    return out
