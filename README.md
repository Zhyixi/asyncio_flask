## run server
# 使用開發環境模式啟動server 於 http://localhost:5000/
flask --app [app module or .py file] run --debug
# 使用其他port
flask --app [app module or .py file] run --debug --port 5001
# 開放同網域使用
python -m flask --app flaskr run --debug --port 5000 --host 0.0.0.0

#### 注意事項
# 儲存套件
pip freeze > requirements.txt
# 安裝套件
pip install -r requirements.txt

#### 使用cmd terminal
## 建立檔案
# 說明檔案
touch README.md
# git 省略設定檔案
touch .gitignore

#### Flask 概念
# 應用物件代表整个 Web 應用程序
# 應用工廠模式(Application Factory Pattern)
是一種程式的設計模式，將應用的建立與配置過程分開，使應用物件在需要的時候才建立。
通常會建立一個工廠函数（Factory Function），用於建立對象。
该工厂函数负责创建应用对象并进行必要的配置，例如注册蓝图、设置数据库连接等。
在需要使用应用对象的地方，可以通过调用工厂函数来获取应用对象，从而实现灵活的应用对象创建和配置。
应用工厂模式的优点包括：
分离应用的创建和配置，使代码更易于维护和测试。
可以灵活地创建多个应用对象，实现多个应用的组合。
支持在不同的环境中使用不同的配置，例如开发环境、生产环境等。
总结来说，应用对象是表示整个 Flask Web 应用程序的对象，负责处理请求和返回响应。而应用工厂模式是一种用于创建和配置应用对象的设计模式，通过工厂函数将应用的创建和配置过程分离，提高代码的可维护性和灵活性。
可以在view.py中調用與建立應用

# 套件管理工具poetry
poetry export --without-hashes --output requirements.txt
poetry add 
poetry install
If you want to update it to the latest compatible version, you can use `poetry update package`.
If you prefer to upgrade it to the latest available version, you can use `poetry add package@latest`.

# curl 在命令列提出request的方法，下面是quart 的app測試
curl --json "{\"hello\": \"world\"}" http://localhost:5000/echo
curl http://localhost:5000/example
