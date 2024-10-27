# Image To Text

## 실행

아래를 참고해서 모델을 다운 받은 후 아래 명령어를 입력한다.

```
docker-compose -f ./image-to-text/docker-compose.yml up --build
```

dog.jpg에 대한 text를 생성해서 print한다.

## 작동 모델

아래 모델에서 작동을 확인했다.

https://huggingface.co/Salesforce/blip-image-captioning-large

## 모델 폴더 구조

모델을 다운 받은 후 .env의 MODEL_PATH를 수정한다.\
MODEL_PATH 폴더 내 파일들은 아래와 같은 형태여야 한다.

```
config.json
model.safetensors
preprocessor_config.json
pytorch_model.bin
README.md
special_tokens_map.json
tf_model.h5
tokenizer_config.json
tokenizer.json
vocab.txt
```
