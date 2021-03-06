# https://note.com/npaka/n/n96dde45fdf8d

# Huggingface Transformersのインストール
!pip install transformers==4.4.2

# Sentencepieceのインストール
!pip install sentencepiece==0.1.91


from transformers import T5Tokenizer, AutoModelForCausalLM

# トークナイザーとモデルの準備
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")

# 推論
input = tokenizer.encode("昔々あるところに", return_tensors="pt")
output = model.generate(input, do_sample=True, max_length=30, num_return_sequences=3)
print(tokenizer.batch_decode(output))
