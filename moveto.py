https://www.drissionpage.cn/ChromiumPage/actions/#-move_to

from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')
page.actions.move_to('#kw').click().type('DrissionPage')
page.actions.move_to('#su').click()
