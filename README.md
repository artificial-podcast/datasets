## Datasets
Texts generated from a GPT-2 model trained on Fanfiction in different fandoms.

### Disclaimer

All publicly recognizable characters, settings, etc. are the property of their respective owners. The original characters and plot are the property of the author.


#### Text generation

Example:

```yaml
namespace: test1  # a sub-folder or namespace for the generated texts
model:
  name: "test_model"  # the pre-trained model used to generate the texts with
  version: 1          # the version to generate from

generate:
  texts: 1          # number of texts to generate per prompt
  words: 500        # number of words per text to generate
  temperature: 0.75 # the 'model temperature', controlls how eratic the text will be.

metadata:
  labels: 'label1 label2 label3' # some tags describing the content

# prompts that start the text generation
prompts: |
  This is the first prompt

  And this is the second prompt

  RANDOM
```

##### RANDOM

A prompt line `RANDOM` triggers, as the name suggest, the creation of a random text without supplying a prompt.


#### Structure of the generated texts

Example:

```yaml
---
prompt: 'The prompt used to create the text'
generate:
	labels: 'label label label'
	model: test_model
	words: 501
	temperature: 0.75
---

Without a wand, without a family he can reliably count on not being recognized, and without his own parents helping him, which isn’t a stretch."I’m sorry, I can’t even help you," he murmurs, brushing his hair back from his forehead."You’re a boy, Harry."
```
