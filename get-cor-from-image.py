# https://rapidai.github.io/RapidOCRDocs/install_usage/api/RapidOCR/#_5

from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()

img_path = 'tests/test_files/ch_en_num.jpg'

# 默认都为True
result, elapse = engine(img_path, use_det=True, use_cls=True, use_rec=True)
print(result)
print(elapse)
