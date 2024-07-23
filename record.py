# https://www.drissionpage.cn/ChromiumPage/actions/#-move_to

from DrissionPage import ChromiumPage,ChromiumOptions
# https://rapidai.github.io/RapidOCRDocs/install_usage/api/RapidOCR/#_5

from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()


browser_path=r"C:\Users\Administrator\AppData\Local\ms-playwright\chromium-1124\chrome-win\chrome.exe"
options = ChromiumOptions()

options.set_paths(browser_path=browser_path)

page = ChromiumPage(addr_or_opts=options)
page.get('https://www.baidu.com')
# 对整页截图并保存
page.get_screenshot(path='tmp', name='pic.jpg', full_page=True)
page.rect.size
img_path = 'tmp/pic.jpg'

result, elapse = engine(img_path, use_det=True, use_cls=True, use_rec=True)
print(result)
print(elapse)

# 默认都为True

page.actions.move_to('#kw').click().type('DrissionPage')
page.actions.move_to('#su').click()
