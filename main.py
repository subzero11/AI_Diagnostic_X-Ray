import io

import requests
import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig

# step 1: Setup constant
device = "cuda"
dtype = torch.float16

# step 2: Load Processor and Model
processor = AutoProcessor.from_pretrained("StanfordAIMI/CheXagent-8b", trust_remote_code=True)
generation_config = GenerationConfig.from_pretrained("StanfordAIMI/CheXagent-8b")
model = AutoModelForCausalLM.from_pretrained("StanfordAIMI/CheXagent-8b", torch_dtype=dtype, trust_remote_code=True)

# step 3: Fetch the images
image_path = "https://upload.wikimedia.org/wikipedia/commons/0/0c/X-ray_of_rib_fractures_and_pneumothorax.jpg"
images = [Image.open(io.BytesIO(requests.get(image_path).content)).convert("RGB")]

# step 4: Generate the Findings section
prompt = f'Describe "Thorax"'
inputs = processor(images=images, text=f" USER: <s>{prompt} ASSISTANT: <s>", return_tensors="pt").to(device=device, dtype=dtype)
output = model.generate(**inputs, generation_config=generation_config)[0]
response = processor.tokenizer.decode(output, skip_special_tokens=True)
