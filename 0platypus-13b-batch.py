from llama_cpp import Llama #import for GGML models
from rich import console
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import datetime
console = Console() #initialize RICH console 
console.clear()  #clear screen
lista = [
"How was Anne Frank’s diary discovered?",
"Tell me about the Industrial Revolution in detail",
"Write a short story about a dragon who was evil and then saw error in it’s way",
"Write dialogue between a detective and a suspect",
"Suggest a plot twist for my crime novel",
"I sit in front of the computer all day. How  do I manage and mitigate eye strain?",
"How can  I deal with interruptions at work?",
"Suggest a daily schedule for a busy professional",
"Summarize the key points  of this paper: How to write articles that people want to read | by Sunil Sandhu | JavaScript in Plain English. How to write articles that people want to read. Here are a bunch of recommendations that the In Plain English team consider to be best practices when writing articles that your readers will find engaging and easy-to-read. Written  by Sunil Sandhu. Take a moment to give your article a good title and subtitle. Try to make them concise, yet compelling. If in doubt, ask yourself: “Would I find this title interesting enough that I would want to continue to read the article?” Don’t create weird formats for your headings and subheadings. Just keep them simple and make sure that the formatting for each heading/subheading in your article is consistent with one another. If you are planning on numbering your headings, here are some examples for you to refer to… Half-baked articles look bad. If you cannot be bothered to take the time to write your article in a way that has good structure, good punctuation, good spelling, and good formatting, what makes you think that somebody else is going to spend good time reading it?Take pride in your work. Your writing is an extension of who you are as a person, especially in a professional context. If you are writing about code, it is likely that you have aspirations to work with software, or already do. The words you write represent that, so make sure you do a good job of representing yourself! Capitalise the start of every sentence. Regarding articles that have a 2–3min read time - have you definitely covered everything that your article needs and your readers expect?  Following on from the previous point, research has shown that articles of 7–8mins appear to perform best. If you are not confident that your level of English is perfect/near-perfect, try running your article through some writing software that has the language set to English (UK) or English (US). Try writing your article in Google Docs. Some people swear by Grammarly. While Grammarly is a nice tool for improving the quality of your content, we have still come across far too many writers who swear they have used Grammarly to check their work, yet it still contains simple errors. Even if you're confident in your English, I would still recommend using these tools. If in doubt about those any of those three previous points, go ahead and read your own article back. Consider whether you still think your article is good enough for other people to spend time reading. Hopefully it is! 🙂 Don’t overuse emojis! Don’t overuse GIFs and memes.",
"Extract the main points of this text: How to write articles that people want to read | by Sunil Sandhu | JavaScript in Plain English. How to write articles that people want to read. Here are a bunch of recommendations that the In Plain English team consider to be best practices when writing articles that your readers will find engaging and easy-to-read. Written  by Sunil Sandhu. Take a moment to give your article a good title and subtitle. Try to make them concise, yet compelling. If in doubt, ask yourself: “Would I find this title interesting enough that I would want to continue to read the article?” Don’t create weird formats for your headings and subheadings. Just keep them simple and make sure that the formatting for each heading/subheading in your article is consistent with one another. If you are planning on numbering your headings, here are some examples for you to refer to… Half-baked articles look bad. If you cannot be bothered to take the time to write your article in a way that has good structure, good punctuation, good spelling, and good formatting, what makes you think that somebody else is going to spend good time reading it? Take pride in your work. Your writing is an extension of who you are as a person, especially in a professional context. If you are writing about code, it is likely that you have aspirations to work with software, or already do. The words you write represent that, so make sure you do a good job of representing yourself! Capitalise the start of every sentence. Regarding articles that have a 2–3min read time - have you definitely covered everything that your article needs and your readers expect?  Following on from the previous point, research has shown that articles of 7–8mins appear to perform best. If you are not confident that your level of English is perfect/near-perfect, try running your article through some writing software that has the language set to English (UK) or English (US). Try writing your article in Google Docs. Some people swear by Grammarly. While Grammarly is a nice tool for improving the quality of your content, we have still come across far too many writers who swear they have used Grammarly to check their work, yet it still contains simple errors. Even if you're confident in your English, I would still recommend using these tools. If in doubt about those any of those three previous points, go ahead and read your own article back. Consider whether you still think your article is good enough for other people to spend time reading. Hopefully it is! 🙂 Don’t overuse emojis! Don’t overuse GIFs and memes.",
"Suggest ways to improve my public speaking skills",
"How can I improve my romance life?",
"Predict the best crops to plant in a summer garden in Italy",
"Predict the impact of artificial intelligence on human learning"
]
# Load in memory the quantized model
llm = Llama(model_path="./models/platypus2-13b.ggmlv3.q2_K.bin", 
            n_ctx=1024, n_batch=128, verbose=False)

# FUNCTION TO LOG ALL CHAT MESSAGES INTO chathistory.txt
def writehistory(text):
    with open('experiments.txt', 'a') as f:
        f.write(text)
        f.write('\n')
    f.close()
# TITLE section
console.print(Panel("Your AI generation with :snail: [yellow]Ptatypus-13b GGML"))
mainstart = datetime.datetime.now()
# Accept input until you  prompt 'quit'
for item in lista:
        instruction = item
        usertext = f"user: {instruction}"
        console.print(f"[green_yellow][i]User[/i] :speaking_head: :  {instruction}")
        writehistory(usertext)
        start = datetime.datetime.now()
        # put together the instruction in the prompt template for Platypus models
        prompt = f"Below is an instruction that describes a task. Write a response that appropriately completes the request.\n### Instruction:\n{instruction}\n### Response:"
        output = llm(prompt,temperature  = 0.7, max_tokens=1024, top_k=20, top_p=0.9,
                repeat_penalty=1.15)
        stop = datetime.datetime.now()
        gen_time = stop-start
        res = output['choices'][0]['text'].strip()
        bottext = f"Platypus2-13b : {res}\ntext generated in {gen_time}\n---\n"
        writehistory(bottext)
        console.print(f"[yellow1]Platypus2-13b :snail: : {res}")
        console.print(f"[grey53][i]:two_o’clock: text generated in {gen_time}[/i] ")
mainstop = datetime.datetime.now()
totalloop =  mainstop - mainstart
console.print(f"[red1][i]:two_o’clock: Entire Loop duration: {totalloop}[/i] ")