# thePromptBattle
Repo of the code and results from the Medium article Battle of the Prompts: Unveiling the True Capabilities of Open Source Language Models
<br>
Putting LLMs to the Test: Analyzing Performance of Orca-3b, Llama2–7b and Platypus-13b Across Varied Prompts<br>
- The 3 python files contains the code for the loop over the questions.
- Every model will generate a dedicated txt file to log the questions and answers
<br>

### Requirements


```python
pip  install mkl mkl-include 
pip install torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0
pip install llama-cpp-python==0.1.78
pip install accelerate
pip install rich
pip install bitsandbytes
```

<br>
<img src="https://github.com/fabiomatricardi/thePromptBattle/blob/main/logo-article.png" width=700>


## Final evaluation
<img src="https://github.com/fabiomatricardi/thePromptBattle/raw/main/finalTable.png" width=600>

For detailed explanations and reasoning read the Medium article.
