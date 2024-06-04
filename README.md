# AI_Diagnostic_X-Ray


## Using Stanford-AIMI 8b model to Read X-ray and interpret findings.  

Note: Prompt is generalized ("thorax"), to keep low latency and demonstrate code functionality.  Additionally cuda and torch.float16 are used for the same purpose.  Prompt and datatype can be modified by medical or technically inclined individuals to improve accuracy, produce more succinct and elaborate output.  Example: [thorax, trachea...etc]  Image is shown below and the code is available in repo.

-Khan









![10-04-Pneumothorax_Drainage](https://github.com/subzero11/AI_Diagnostic_X-Ray/assets/16353348/b839187f-25bc-4bae-bcc8-44b38496d9e7)




@article{chexagent-2024,
  title={CheXagent: Towards a Foundation Model for Chest X-Ray Interpretation},
  author={Chen, Zhihong and Varma, Maya and Delbrouck, Jean-Benoit and Paschali, Magdalini and Blankemeier, Louis and Veen, Dave Van and Valanarasu, Jeya Maria Jose and Youssef, Alaa and Cohen, Joseph Paul and Reis, Eduardo Pontes and Tsai, Emily B. and Johnston, Andrew and Olsen, Cameron and Abraham, Tanishq Mathew and Gatidis, Sergios and Chaudhari, Akshay S and Langlotz, Curtis},
  journal={arXiv preprint arXiv:2401.12208},
  url={https://arxiv.org/abs/2401.12208},
  year={2024}
