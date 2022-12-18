import requests

from fake_user_agent import user_agent

ua = user_agent()

admin_page = 'https://securepayments.sberbank.ru/mportal3/admin'

login_page = 'https://securepayments.sberbank.ru/mportal3/auth/login'
auth_data = {"login": "P2536017137_3981-operator", "password": "995F703B6E5550970B70E200E28039B3", "language": "ru"}


def main():
    headers = {'user-agent': ua}
    # requests.post(login_page, data=auth_data, headers=headers)
    r = requests.get(admin_page, headers=headers)
    with open('index.html', 'w', encoding="utf-8") as f:
        f.write(r.text)
    print(r.status_code)


if __name__ == '__main__':
    main()
