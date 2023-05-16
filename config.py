# config
repo = "AK391/animegan2-pytorch:main"
model = "generator"
repo_description = repo.split("/")[-1].capitalize()
intro = "Gradio Demo for AnimeGanv2 Face Portrait. To use it, simply upload your image, or click one of the examples to load them. Read more at the links below. Please use a cropped portrait picture for best results similar to the examples below."
description = f'''# {repo_description}!🚀\n{intro}'''
device = "cpu"
version_list = ['version 1 (🔺 stylization, 🔻 robustness)', 'version 2 (🔺 robustness,🔻 stylization)']
