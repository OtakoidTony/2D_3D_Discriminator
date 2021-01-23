# 2D_3D_Discriminator
2D 일러스트와 3D modelling 일러스트 \[ex) MMD\] 을 판별하는 프로그램.

## 실행방법
```
python get_dataset_from_gelbooru.py
python dataset_initiation.py
python main.py
```
위를 순차적으로 실행하면 model폴더에 model이라는 텐서플로우 모델 폴더가 생기는데,  
이걸 사용하시면 됩니다!

예시)
```py
model = tf.keras.models.load_model('model/model')

def predict(image):
    return "2D" if model.predict(np.array([img_to_array(Image.open(image).resize((150, 150)).convert("RGB"))]))[0][0]>0.5 else "3d"
```

## 폴더 구조
```
├─dataset
│  ├─2d
│  ├─3d
│  └─pkl
└─model
```

에러가 나면 위와 같이 폴더를 만들어주세요!
